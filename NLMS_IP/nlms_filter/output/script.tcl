############################################################
## This file is generated automatically by Vitis HLS.
## Please DO NOT edit it.
## Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
############################################################
open_project nlms_filter
set_top nlms_top
add_files nlms_filter/top.hpp
add_files nlms_filter/top.cpp
add_files -tb nlms_filter/main.cpp -cflags "-Wno-unknown-pragmas" -csimflags "-Wno-unknown-pragmas"
open_solution "output" -flow_target vivado
set_part {xc7s50-ftgb196-1}
create_clock -period 10 -name default
source "./nlms_filter/output/directives.tcl"
csim_design -clean
csynth_design
cosim_design
export_design -format ip_catalog
