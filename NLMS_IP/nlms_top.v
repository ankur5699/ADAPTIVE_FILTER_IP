module nlms_top #(
parameter reg DATA_WIDTH = 16,
parameter reg NUM_TAPS = 128
)
  (
  //clk and rst
  input clk,
  input rst,
  //control signals
  input start,
  output idle,
  output ready,

  //signal
  input[15:0] input_signal,
  input[15:0] desired_signal_out
);

/*
What are we doing here?
NLMS algorithm that is already implemented in python algorithm
It will be ported to hardware

NUM_OF_TAPS = 128
desired signal
input signal
weights get updated after a few iterations
*/

  reg start_reg;
  reg idle_reg;
  reg ready_reg;


endmodule
