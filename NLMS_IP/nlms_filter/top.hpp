#ifndef TOP_NLMS
#define TOP_NLMS

#include "ap_fixed.h"

#ifndef __SYNTHESIS__
#include <stdio.h>
#endif

#define FLOATING_APP

#define DEC_COMP 8
#define INT_COMP 24


#ifndef FLOATING_APP
typedef ap_fixed<DEC_COMP, INT_COMP> fixed_point_t;
#endif


#define NUM_TAPS 128
#define LEARNING_RATE 1
#define NUM_ITERATIONS 10



#ifndef FLOATING_APP
void nlms_top(
		fixed_point_t input_signal[NUM_TAPS],
		fixed_point_t desired_signal[NUM_TAPS],
		fixed_point_t weights[NUM_TAPS]
		);
#else
void nlms_top(
		float input_signal[NUM_TAPS],
		float desired_signal[NUM_TAPS],
		float weights[NUM_TAPS]
		);
#endif

int mse(float error[NUM_TAPS]);


#endif
