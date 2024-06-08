#include "top.hpp"


#ifndef FLOATING_APP
void nlms_top(
		fixed_point_t input_signal[NUM_TAPS],
		fixed_point_t desired_signal[NUM_TAPS],
		fixed_point_t weights[NUM_TAPS]
		)
{
#pragma HLS INTERFACE mode=ap_fifo port=input_signal
#pragma HLS INTERFACE mode=ap_fifo port=desired_signal
#pragma HLS INTERFACE mode=ap_fifo port=weights

	fixed_point_t estimation[NUM_TAPS];
	fixed_point_t error[NUM_TAPS];
	fixed_point_t acc[NUM_TAPS];
	int MSE;

	for (int i=0; i<NUM_TAPS; i++)
		acc[i] = 0;

	for(int j=0; j<NUM_ITERATIONS; j++){

		for (int i=0; i<NUM_TAPS; i++){
#pragma HLS LOOP_FLATTEN
			estimation[i] = acc[i] * input_signal[i];
			error[i] = desired_signal[i] - estimation[i];
		}

//		MSE = mse(error);
//		if (MSE < 5)
//			break;

		for (int i=0; i<NUM_TAPS; i++)
			acc[i] = acc[i] + ((fixed_point_t)LEARNING_RATE * input_signal[i] * error[i]);
	}

	for (int i=0; i<NUM_TAPS; i++)
		weights[i] = acc[i];


}
#else
void nlms_top(
		float input_signal[NUM_TAPS],
		float desired_signal[NUM_TAPS],
		float weights[NUM_TAPS]
		)
{
#pragma HLS TOP name=nlms_top
	float estimation[NUM_TAPS];
	float error[NUM_TAPS];
//	float acc[NUM_TAPS] = {0.0};
	int MSE;



	nlms_outer_loop:for(int j=0; j<NUM_ITERATIONS; j++){
#pragma HLS PIPELINE off
		nlms_inner_loop:for (int i=0; i<NUM_TAPS; i++){
#pragma HLS PIPELINE
			estimation[i] = weights[i] * input_signal[i];
			error[i] = desired_signal[i] - estimation[i];
			weights[i] = weights[i] + (LEARNING_RATE/(0.0001 + input_signal[i] * input_signal[i])) * input_signal[i] * error[i];
#ifndef __SYNTHESIS__
			printf("%f\t", error[i]);

#endif

		}
#ifndef __SYNTHESIS__
			printf("\n");
#endif

	}
//
//	for (int i=0; i<NUM_TAPS; i++)
//		weights[i] = acc[i];


}





#endif

