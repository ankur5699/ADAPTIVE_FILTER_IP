#include <iostream>
#include "top.hpp"

int main()
{

#ifndef FLOATING_APP
	fixed_point_t input[NUM_TAPS];
	fixed_point_t desired_signal[NUM_TAPS];
	fixed_point_t weights[NUM_TAPS];
#else
	float input[NUM_TAPS];
	float desired_signal[NUM_TAPS];
	float weights[NUM_TAPS];
#endif
	int i = 0;

	for (int i=0; i<NUM_TAPS; i++){
		input[i] = rand()%20 + 0.1;
		desired_signal[i] = rand()%20 + 0.1;
//		weights[i] = 0;
	}

	nlms_top(input,desired_signal,weights);

	std::cout<<"input signal"<<std::endl;
	for (int i=0; i<NUM_TAPS; i++){
		std::cout<<"\t"<<input[i];
	}
	std::cout<<std::endl;

	for (int i=0; i<NUM_TAPS; i++){
	std::cout<<"\t"<<weights[i];
	}
	std::cout<<std::endl;

	for (int i=0; i<NUM_TAPS; i++){
	std::cout<<"\t"<<weights[i] * input[i];
	}
	std::cout<<std::endl;

	for (int i=0; i<NUM_TAPS; i++){
	std::cout<<"\t"<<desired_signal[i];
	}
	std::cout<<std::endl;



	return 0;
}
