.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/tonga_hwmgr.c

.. _`tonga_get_dpm_level_enable_mask_value`:

tonga_get_dpm_level_enable_mask_value
=====================================

.. c:function:: uint32_t tonga_get_dpm_level_enable_mask_value(struct tonga_single_dpm_table *dpm_table)

    generate the DPM level mask value \ ``param``\     hwmgr      the address of the hardware manager

    :param struct tonga_single_dpm_table \*dpm_table:
        *undescribed*

.. _`tonga_initialize_dpm_defaults`:

tonga_initialize_dpm_defaults
=============================

.. c:function:: void tonga_initialize_dpm_defaults(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_initialize_dpm_defaults.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.

.. _`tonga_get_sclk_for_voltage_evv`:

tonga_get_sclk_for_voltage_evv
==============================

.. c:function:: int tonga_get_sclk_for_voltage_evv(struct pp_hwmgr *hwmgr, phm_ppt_v1_voltage_lookup_table *lookup_table, uint16_t virtual_voltage_id, uint32_t *sclk)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param phm_ppt_v1_voltage_lookup_table \*lookup_table:
        *undescribed*

    :param uint16_t virtual_voltage_id:
        *undescribed*

    :param uint32_t \*sclk:
        *undescribed*

.. _`tonga_get_sclk_for_voltage_evv.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``param``\     virtual_voltage_Id  voltageId to look for.
\ ``param``\     sclk output value .
\ ``return``\    always 0 if success and 2 if association not found

.. _`tonga_get_evv_voltage`:

tonga_get_evv_voltage
=====================

.. c:function:: int tonga_get_evv_voltage(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_get_evv_voltage.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    2 if vddgfx returned is greater than 2V or if BIOS

.. _`tonga_send_msg_to_smc_return_parameter`:

tonga_send_msg_to_smc_return_parameter
======================================

.. c:function:: PPSMC_Result tonga_send_msg_to_smc_return_parameter(struct pp_hwmgr *hwmgr, PPSMC_Msg msg, uint32_t *parameter)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param PPSMC_Msg msg:
        *undescribed*

    :param uint32_t \*parameter:
        *undescribed*

.. _`tonga_dpm_force_state`:

tonga_dpm_force_state
=====================

.. c:function:: int tonga_dpm_force_state(struct pp_hwmgr *hwmgr, uint32_t n)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t n:
        *undescribed*

.. _`tonga_dpm_force_state_mclk`:

tonga_dpm_force_state_mclk
==========================

.. c:function:: int tonga_dpm_force_state_mclk(struct pp_hwmgr *hwmgr, uint32_t n)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t n:
        *undescribed*

.. _`tonga_dpm_force_state_pcie`:

tonga_dpm_force_state_pcie
==========================

.. c:function:: int tonga_dpm_force_state_pcie(struct pp_hwmgr *hwmgr, uint32_t n)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t n:
        *undescribed*

.. _`tonga_set_boot_state`:

tonga_set_boot_state
====================

.. c:function:: int tonga_set_boot_state(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_set_boot_state.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_process_firmware_header`:

tonga_process_firmware_header
=============================

.. c:function:: int tonga_process_firmware_header(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_process_firmware_header.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_read_clock_registers`:

tonga_read_clock_registers
==========================

.. c:function:: int tonga_read_clock_registers(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_read_clock_registers.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_get_memory_type`:

tonga_get_memory_type
=====================

.. c:function:: int tonga_get_memory_type(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_get_memory_type.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_enable_acpi_power_management`:

tonga_enable_acpi_power_management
==================================

.. c:function:: int tonga_enable_acpi_power_management(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_enable_acpi_power_management.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_init_power_gate_state`:

tonga_init_power_gate_state
===========================

.. c:function:: int tonga_init_power_gate_state(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_init_power_gate_state.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_check_for_dpm_running`:

tonga_check_for_dpm_running
===========================

.. c:function:: int tonga_check_for_dpm_running(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_check_for_dpm_running.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_check_for_dpm_stopped`:

tonga_check_for_dpm_stopped
===========================

.. c:function:: int tonga_check_for_dpm_stopped(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_check_for_dpm_stopped.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_trim_voltage_table`:

tonga_trim_voltage_table
========================

.. c:function:: int tonga_trim_voltage_table(struct pp_hwmgr *hwmgr, pp_atomctrl_voltage_table *voltage_table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param pp_atomctrl_voltage_table \*voltage_table:
        *undescribed*

.. _`tonga_trim_voltage_table.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``param``\     voltage_table  the pointer to changing voltage table
\ ``return``\     1 in success

.. _`tonga_construct_voltage_tables`:

tonga_construct_voltage_tables
==============================

.. c:function:: int tonga_construct_voltage_tables(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_construct_voltage_tables.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_populate_smc_vddc_table`:

tonga_populate_smc_vddc_table
=============================

.. c:function:: int tonga_populate_smc_vddc_table(struct pp_hwmgr *hwmgr, SMU72_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param SMU72_Discrete_DpmTable \*table:
        *undescribed*

.. _`tonga_populate_smc_vddc_table.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     table     the SMC DPM table structure to be populated
\ ``return``\    always 0

.. _`tonga_populate_smc_vdd_gfx_table`:

tonga_populate_smc_vdd_gfx_table
================================

.. c:function:: int tonga_populate_smc_vdd_gfx_table(struct pp_hwmgr *hwmgr, SMU72_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param SMU72_Discrete_DpmTable \*table:
        *undescribed*

.. _`tonga_populate_smc_vdd_gfx_table.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     table     the SMC DPM table structure to be populated
\ ``return``\    always 0

.. _`tonga_populate_smc_vdd_ci_table`:

tonga_populate_smc_vdd_ci_table
===============================

.. c:function:: int tonga_populate_smc_vdd_ci_table(struct pp_hwmgr *hwmgr, SMU72_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param SMU72_Discrete_DpmTable \*table:
        *undescribed*

.. _`tonga_populate_smc_vdd_ci_table.description`:

Description
-----------

\ ``param``\     \*hwmgr The address of the hardware manager.
\ ``param``\     \*table The SMC DPM table structure to be populated.
\ ``return``\    0

.. _`tonga_populate_smc_mvdd_table`:

tonga_populate_smc_mvdd_table
=============================

.. c:function:: int tonga_populate_smc_mvdd_table(struct pp_hwmgr *hwmgr, SMU72_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param SMU72_Discrete_DpmTable \*table:
        *undescribed*

.. _`tonga_populate_smc_mvdd_table.description`:

Description
-----------

\ ``param``\     \*hwmgr The address of the hardware manager.
\ ``param``\     \*table The SMC DPM table structure to be populated.
\ ``return``\    0

.. _`convert_to_vid`:

convert_to_vid
==============

.. c:function:: uint8_t convert_to_vid(uint16_t vddc)

    :param uint16_t vddc:
        *undescribed*

.. _`tonga_populate_cac_tables`:

tonga_populate_cac_tables
=========================

.. c:function:: int tonga_populate_cac_tables(struct pp_hwmgr *hwmgr, SMU72_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param SMU72_Discrete_DpmTable \*table:
        *undescribed*

.. _`tonga_populate_cac_tables.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     table     the SMC DPM table structure to be populated
\ ``return``\    always 0

.. _`tonga_populate_smc_voltage_tables`:

tonga_populate_smc_voltage_tables
=================================

.. c:function:: int tonga_populate_smc_voltage_tables(struct pp_hwmgr *hwmgr, SMU72_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param SMU72_Discrete_DpmTable \*table:
        *undescribed*

.. _`tonga_populate_smc_voltage_tables.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     table     the SMC DPM table structure to be populated
\ ``return``\    always 0

.. _`tonga_populate_vr_config`:

tonga_populate_vr_config
========================

.. c:function:: int tonga_populate_vr_config(struct pp_hwmgr *hwmgr, SMU72_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param SMU72_Discrete_DpmTable \*table:
        *undescribed*

.. _`tonga_populate_vr_config.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     table     the SMC DPM table structure to be populated
\ ``return``\    always 0

.. _`tonga_reset_to_default`:

tonga_reset_to_default
======================

.. c:function:: int tonga_reset_to_default(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_reset_to_default.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_program_memory_timing_parameters`:

tonga_program_memory_timing_parameters
======================================

.. c:function:: int tonga_program_memory_timing_parameters(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_program_memory_timing_parameters.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0
This function is to be called from the SetPowerState table.

.. _`tonga_calculate_mclk_params`:

tonga_calculate_mclk_params
===========================

.. c:function:: int tonga_calculate_mclk_params(struct pp_hwmgr *hwmgr, uint32_t memory_clock, SMU72_Discrete_MemoryLevel *mclk, bool strobe_mode, bool dllStateOn)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t memory_clock:
        *undescribed*

    :param SMU72_Discrete_MemoryLevel \*mclk:
        *undescribed*

    :param bool strobe_mode:
        *undescribed*

    :param bool dllStateOn:
        *undescribed*

.. _`tonga_calculate_mclk_params.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     memory_clock the memory clock to use to populate the structure
\ ``param``\     sclk        the SMC SCLK structure to be populated

.. _`tonga_populate_mvdd_value`:

tonga_populate_mvdd_value
=========================

.. c:function:: int tonga_populate_mvdd_value(struct pp_hwmgr *hwmgr, uint32_t mclk, SMIO_Pattern *smio_pattern)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t mclk:
        *undescribed*

    :param SMIO_Pattern \*smio_pattern:
        *undescribed*

.. _`tonga_populate_mvdd_value.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     mclk        the MCLK value to be used in the decision if MVDD should be high or low.
\ ``param``\     voltage     the SMC VOLTAGE structure to be populated

.. _`tonga_calculate_sclk_params`:

tonga_calculate_sclk_params
===========================

.. c:function:: int tonga_calculate_sclk_params(struct pp_hwmgr *hwmgr, uint32_t engine_clock, SMU72_Discrete_GraphicsLevel *sclk)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t engine_clock:
        *undescribed*

    :param SMU72_Discrete_GraphicsLevel \*sclk:
        *undescribed*

.. _`tonga_calculate_sclk_params.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     engine_clock the engine clock to use to populate the structure
\ ``param``\     sclk        the SMC SCLK structure to be populated

.. _`tonga_populate_single_graphic_level`:

tonga_populate_single_graphic_level
===================================

.. c:function:: int tonga_populate_single_graphic_level(struct pp_hwmgr *hwmgr, uint32_t engine_clock, uint16_t sclk_activity_level_threshold, SMU72_Discrete_GraphicsLevel *graphic_level)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t engine_clock:
        *undescribed*

    :param uint16_t sclk_activity_level_threshold:
        *undescribed*

    :param SMU72_Discrete_GraphicsLevel \*graphic_level:
        *undescribed*

.. _`tonga_populate_single_graphic_level.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     engine_clock the engine clock to use to populate the structure
\ ``param``\     sclk        the SMC SCLK structure to be populated

.. _`tonga_populate_all_graphic_levels`:

tonga_populate_all_graphic_levels
=================================

.. c:function:: int tonga_populate_all_graphic_levels(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_populate_all_graphic_levels.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager

.. _`tonga_populate_all_memory_levels`:

tonga_populate_all_memory_levels
================================

.. c:function:: int tonga_populate_all_memory_levels(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_populate_all_memory_levels.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager

.. _`tonga_init_smc_table`:

tonga_init_smc_table
====================

.. c:function:: int tonga_init_smc_table(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_init_smc_table.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``param``\     pInput  the pointer to input data (PowerState)
\ ``return``\    always 0

.. _`tonga_get_mc_microcode_version`:

tonga_get_mc_microcode_version
==============================

.. c:function:: int tonga_get_mc_microcode_version(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_get_mc_microcode_version.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_initializa_dynamic_state_adjustment_rule_settings`:

tonga_initializa_dynamic_state_adjustment_rule_settings
=======================================================

.. c:function:: int tonga_initializa_dynamic_state_adjustment_rule_settings(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_initializa_dynamic_state_adjustment_rule_settings.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.

.. _`tonga_patch_with_vdd_leakage`:

tonga_patch_with_vdd_leakage
============================

.. c:function:: void tonga_patch_with_vdd_leakage(struct pp_hwmgr *hwmgr, uint16_t *voltage, phw_tonga_leakage_voltage *pLeakageTable)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint16_t \*voltage:
        *undescribed*

    :param phw_tonga_leakage_voltage \*pLeakageTable:
        *undescribed*

.. _`tonga_patch_with_vdd_leakage.description`:

Description
-----------

\ ``param``\      hwmgr  the address of the powerplay hardware manager.
\ ``param``\      pointer to changing voltage
\ ``param``\      pointer to leakage table

.. _`tonga_patch_lookup_table_with_leakage`:

tonga_patch_lookup_table_with_leakage
=====================================

.. c:function:: int tonga_patch_lookup_table_with_leakage(struct pp_hwmgr *hwmgr, phm_ppt_v1_voltage_lookup_table *lookup_table, phw_tonga_leakage_voltage *pLeakageTable)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param phm_ppt_v1_voltage_lookup_table \*lookup_table:
        *undescribed*

    :param phw_tonga_leakage_voltage \*pLeakageTable:
        *undescribed*

.. _`tonga_patch_lookup_table_with_leakage.description`:

Description
-----------

\ ``param``\      hwmgr  the address of the powerplay hardware manager.
\ ``param``\      pointer to voltage lookup table
\ ``param``\      pointer to leakage table
\ ``return``\      always 0

.. _`tonga_enable_voltage_control`:

tonga_enable_voltage_control
============================

.. c:function:: int tonga_enable_voltage_control(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_enable_voltage_control.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`cf_tonga_voltage_control`:

cf_tonga_voltage_control
========================

.. c:function:: bool cf_tonga_voltage_control(const struct pp_hwmgr *hwmgr)

    :param const struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`cf_tonga_voltage_control.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.

.. _`tonga_set_mc_special_registers`:

tonga_set_mc_special_registers
==============================

.. c:function:: int tonga_set_mc_special_registers(struct pp_hwmgr *hwmgr, phw_tonga_mc_reg_table *table)

    1.   when we see mmMC_SEQ_MISC1, bit[31:16] EMRS1, need to be write to  mmMC_PMG_CMD_EMRS /_LP[15:0]. Bit[15:0] MRS, need to be update mmMC_PMG_CMD_MRS/_LP[15:0] 2.   when we see mmMC_SEQ_RESERVE_M, bit[15:0] EMRS2, need to be write to mmMC_PMG_CMD_MRS1/_LP[15:0]. 3.   need to set these data for each clock range

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param phw_tonga_mc_reg_table \*table:
        *undescribed*

.. _`tonga_set_mc_special_registers.description`:

Description
-----------

\ ``param``\     hwmgr the address of the powerplay hardware manager.
\ ``param``\     table the address of MCRegTable
\ ``return``\    always 0

.. _`tonga_initial_switch_from_arb_f0_to_f1`:

tonga_initial_switch_from_arb_f0_to_f1
======================================

.. c:function:: int tonga_initial_switch_from_arb_f0_to_f1(struct pp_hwmgr *hwmgr)

    >F1

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_initial_switch_from_arb_f0_to_f1.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0
This function is to be called from the SetPowerState table.

.. _`tonga_init_arb_table_index`:

tonga_init_arb_table_index
==========================

.. c:function:: int tonga_init_arb_table_index(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_init_arb_table_index.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_program_static_screen_threshold_parameters`:

tonga_program_static_screen_threshold_parameters
================================================

.. c:function:: int tonga_program_static_screen_threshold_parameters(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_program_static_screen_threshold_parameters.description`:

Description
-----------

\ ``param``\    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_enable_display_gap`:

tonga_enable_display_gap
========================

.. c:function:: int tonga_enable_display_gap(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_enable_display_gap.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_program_voting_clients`:

tonga_program_voting_clients
============================

.. c:function:: int tonga_program_voting_clients(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_program_voting_clients.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_hwmgr_backend_init`:

tonga_hwmgr_backend_init
========================

.. c:function:: int tonga_hwmgr_backend_init(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_hwmgr_backend_init.description`:

Description
-----------

\ ``param``\    hwmgr the address of the powerplay hardware manager.
\ ``return``\    1 if success; otherwise appropriate error code.

.. _`tonga_set_max_fan_pwm_output`:

tonga_set_max_fan_pwm_output
============================

.. c:function:: int tonga_set_max_fan_pwm_output(struct pp_hwmgr *hwmgr, uint16_t us_max_fan_pwm)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint16_t us_max_fan_pwm:
        *undescribed*

.. _`tonga_program_display_gap`:

tonga_program_display_gap
=========================

.. c:function:: int tonga_program_display_gap(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_program_display_gap.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always OK

.. _`tonga_set_max_fan_rpm_output`:

tonga_set_max_fan_rpm_output
============================

.. c:function:: int tonga_set_max_fan_rpm_output(struct pp_hwmgr *hwmgr, uint16_t us_max_fan_pwm)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint16_t us_max_fan_pwm:
        *undescribed*

.. This file was automatic generated / don't edit.

