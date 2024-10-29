import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from scipy.fft import fft, fftfreq
from playsound import playsound
import tempfile
import math

SNR = -20
# HELICOPTER_SOUND_FACTOR = 1.15
# Filter properties
N = 128 #Number of TAPS
u = 1.2
eps = 1

# Add noise according to some SNR value
def add_noise_with_snr(signal, snr_db):
    global noise_samples
    signal_power = np.mean(signal ** 2)
    print(f"Signal Power {10*math.log10(signal_power)}")
    snr_linear = 10 ** (snr_db / 10)  # Convert SNR from dB to linear
    noise_power = signal_power / snr_linear
    noise = np.random.normal(0, np.sqrt(noise_power), signal.shape)
    noise_samples = noise
    return signal + noise


def adapt(x, d, w, u, iterations, ALGO='LMS'):
    """
    Provide signal, desired signal
    learning rate, number of iterations and algorithm

    valid algorithms include LMS and NLMS for now
    """
    # w = np.zeros(len(x))
    for i in range(iterations):
        y = x * w
        error = d - y
        mse = sum(np.square(error))
        if (mse < 0.1):
            print(f"Stopped at iteration number :{i}")
            break
        if ALGO == "LMS":
            w = w + u * x * error
        if ALGO == "NLMS":
            w = w + (u/(0.0001+(x*x))) * x * error
        error[error < 0.0001] = 0
        # print(sum(np.square(error)))
    return w


# Load the audio file and extract the sample data
audio = AudioSegment.from_file("mic_test.mp4")
audio_samples = np.array(audio.get_array_of_samples()) >>2
sampling_rate = 44200  # Hz

# Load the Helicopter audio file and extract the sample data
heli_sound = AudioSegment.from_file("helicopter.mp3")
heli_sound_samples = np.array(heli_sound.get_array_of_samples())

heli_sound_samples = heli_sound_samples[:len(audio_samples)]
noisy_audio_samples =  add_noise_with_snr(audio_samples, SNR) + (heli_sound_samples)
 

# Step 1: Plot the original and noisy audio waveforms
plt.figure(figsize=(12, 8))

# Original waveform
plt.subplot(4, 1, 1)
plt.plot(audio_samples, color='blue', label="Original Audio")
# plt.plot(noisy_audio_samples, color='gray', alpha=0.5, label="Noisy Audio")
plt.title("Audio Waveform (Original and Noisy)")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude")
plt.legend()

# Step 2: Compute the frequency spectrum for both original and noisy audio
n = len(audio_samples)
xf = fftfreq(n, 1 / sampling_rate)

# FFT of original signal
yf = fft(audio_samples)
# FFT of noisy signal
yf_noisy = fft(noisy_audio_samples)

# Frequency spectrum
#plot this in dB
plt.subplot(4, 1, 2)
plt.plot(xf[:n // 2], 10*np.log10(np.abs(yf[:n // 2])), color='blue', label="Original Spectrum")
plt.plot(xf[:n // 2], 10*np.log10(np.abs(yf_noisy[:n // 2])), color='gray', alpha=0.5, label="Noisy Spectrum")
plt.title("Frequency Spectrum (Original and Noisy)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude dB")
plt.legend()

# Step 3: Plot the noisy waveform alone
plt.subplot(4, 1, 3)
plt.plot(noisy_audio_samples, color='gray')
plt.title("Noisy Audio Waveform")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude")



# Step 4: Convert back to pydub audio format and play the noisy audio
noisy_audio = audio._spawn(noisy_audio_samples.astype(audio_samples.dtype).tobytes())

# Save the noisy audio to a temporary file for playback
with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
    noisy_audio.export(tmp_file.name, format="wav")
    playsound(tmp_file.name)

######### We Have all the components to Demonstrate ANC ##########
'''
1) Let a 128 tap Transfer function represent outside to inside environment transfer function


2) mic on the outside will capture noise 
(helicopter noise + white noise)

3) mic on the inside will capture  
noise + audio

4) We will output the following at the speaker
-noise + audio

and at this mic we must subtract audio
'''

#1) High Pass Filter represents passive noise reduction
# Could've chosen any other environment, the environment will keep changing slightly

from Filter_values import High_pass_filter #Check Filter_values.py

#mic outside the headphones will capture this
out_mic = noise_samples + heli_sound_samples

filtered_input = np.convolve(out_mic, High_pass_filter, mode='same')

#Mic inside will capture
#No Noise cancellation yet
in_mic = filtered_input + audio_samples/4
yf_in_mic = fft(in_mic)


adapted_signal = np.zeros(len(audio_samples))
weights = np.zeros(N)


for i in range(0,len(audio_samples),N):
    weights                = adapt(out_mic[i:i+N], in_mic[i:i+N], weights, u, N, 'NLMS')
    adapted_signal[i:i+N]  = weights * out_mic[i:i+N] #dot product
    

noise_cancelled = (in_mic - adapted_signal) + audio_samples


##play in mic sound
# Step 4: Convert back to pydub audio format and play the noisy audio
noisy_audio = audio._spawn(noise_cancelled.astype(audio_samples.dtype).tobytes())

# Save the noisy audio to a temporary file for playback
with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
    noisy_audio.export(tmp_file.name, format="wav")
    playsound(tmp_file.name)



# Step 4: Plot the noisy waveform alone
plt.subplot(4, 1, 4)
plt.plot(noise_cancelled, color='gray', label="Original Noisy Output")
# plt.plot(noisy_audio_samples, alpha=0.5, color='red', label="Passive Noise Reduction Output")
plt.title("Inner Mic Audio Waveform")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

















