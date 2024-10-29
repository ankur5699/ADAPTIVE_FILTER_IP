import numpy as np
import matplotlib.pyplot as plt


def adapt(x, d, u, iterations, ALGO='LMS'):
    """
    Provide signal, desired signal
    learning rate, number of iterations and algorithm

    valid algorithms include LMS and NLMS for now
    """
    w = np.zeros(len(x))
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


NOISY_CHANNEL = True
IMPROVISE_ADAPT_OVERCOME = True

# Filter properties
N = 128
u = 1.2
eps = 1
sampling_freq = 44.1 * 1000

# noise added
SNR_dB = -50

# Signal properties
NUM_SAMPLES = 128
signal_freq = 1.5 * 1000
w = 2 * np.pi * signal_freq
t = np.linspace(0.0, NUM_SAMPLES/sampling_freq, NUM_SAMPLES)
s = np.sin(w*t)
# CHANNEL_PROPERTIES = np.random.normal(0, 1.0, NUM_SAMPLES)
from Filter_values import High_pass_filter

CHANNEL_PROPERTIES = High_pass_filter
# Convert SNR from dB to linear scale
SNR_linear = 10**(SNR_dB / 10)
SIGNAL_POWER = np.sum(s*s)/NUM_SAMPLES
NOISE_POWER = SIGNAL_POWER/SNR_linear

if NOISY_CHANNEL:
    ref_noise = np.random.normal(0, np.sqrt(NOISE_POWER), NUM_SAMPLES)
    noise = ref_noise * CHANNEL_PROPERTIES
    sig = s + noise

# let noise be reduced by 3dB when recieved in mic that is isolated from signal
    if IMPROVISE_ADAPT_OVERCOME:
        w = adapt(ref_noise, noise, u, N, 'NLMS')
        s_red = sig - w * ref_noise


# Create a subplot with two rows and one column
plt.subplot(3, 1, 1)  # First subplot (top)
plt.plot(t, s, label='Original')
plt.title('Original Signal')
plt.grid()


# Create a subplot with two rows and one column
plt.subplot(3, 1, 2)  # First subplot (top)
plt.plot(t, sig, label='NOISY SIGNAL')
plt.title('Noisy Signal')
plt.grid()

plt.subplot(3, 1, 3)  # Second subplot (bottom)
plt.plot(t, s_red, label='NOISE REDUCTION', color='orange')
plt.title('Noise Reduced Signal')
plt.grid()

plt.tight_layout()  # Adjust spacing between subplots

# plt.plot(t, s)
plt.show()
