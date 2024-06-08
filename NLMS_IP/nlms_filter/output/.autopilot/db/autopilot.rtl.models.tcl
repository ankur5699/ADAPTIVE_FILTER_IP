set SynModuleInfo {
  {SRCNAME nlms_top MODELNAME nlms_top RTLNAME nlms_top IS_TOP 1
    SUBMODULES {
      {MODELNAME nlms_top_fsub_32ns_32ns_32_7_full_dsp_1 RTLNAME nlms_top_fsub_32ns_32ns_32_7_full_dsp_1 BINDTYPE op TYPE fsub IMPL fulldsp LATENCY 6 ALLOW_PRAGMA 1}
      {MODELNAME nlms_top_fmul_32ns_32ns_32_4_max_dsp_1 RTLNAME nlms_top_fmul_32ns_32ns_32_4_max_dsp_1 BINDTYPE op TYPE fmul IMPL maxdsp LATENCY 3 ALLOW_PRAGMA 1}
      {MODELNAME nlms_top_fptrunc_64ns_32_2_no_dsp_1 RTLNAME nlms_top_fptrunc_64ns_32_2_no_dsp_1 BINDTYPE op TYPE fptrunc IMPL auto LATENCY 1 ALLOW_PRAGMA 1}
      {MODELNAME nlms_top_fpext_32ns_64_2_no_dsp_1 RTLNAME nlms_top_fpext_32ns_64_2_no_dsp_1 BINDTYPE op TYPE fpext IMPL auto LATENCY 1 ALLOW_PRAGMA 1}
      {MODELNAME nlms_top_dadd_64ns_64ns_64_8_full_dsp_1 RTLNAME nlms_top_dadd_64ns_64ns_64_8_full_dsp_1 BINDTYPE op TYPE dadd IMPL fulldsp LATENCY 7 ALLOW_PRAGMA 1}
      {MODELNAME nlms_top_dmul_64ns_64ns_64_7_max_dsp_1 RTLNAME nlms_top_dmul_64ns_64ns_64_7_max_dsp_1 BINDTYPE op TYPE dmul IMPL maxdsp LATENCY 6 ALLOW_PRAGMA 1}
      {MODELNAME nlms_top_ddiv_64ns_64ns_64_59_no_dsp_1 RTLNAME nlms_top_ddiv_64ns_64ns_64_59_no_dsp_1 BINDTYPE op TYPE ddiv IMPL fabric LATENCY 58 ALLOW_PRAGMA 1}
      {MODELNAME nlms_top_flow_control_loop_pipe RTLNAME nlms_top_flow_control_loop_pipe BINDTYPE interface TYPE internal_upc_flow_control INSTNAME nlms_top_flow_control_loop_pipe_U}
    }
  }
}
