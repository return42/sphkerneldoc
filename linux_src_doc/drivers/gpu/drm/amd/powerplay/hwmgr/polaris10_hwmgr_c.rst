.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/polaris10_hwmgr.c

.. _`phm_get_mc_microcode_version`:

phm_get_mc_microcode_version
============================

.. c:function:: int phm_get_mc_microcode_version(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`phm_get_mc_microcode_version.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`polaris10_enable_smc_voltage_controller`:

polaris10_enable_smc_voltage_controller
=======================================

.. c:function:: int polaris10_enable_smc_voltage_controller(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_enable_smc_voltage_controller.description`:

Description
-----------

\ ``param``\     pHwMgr  the address of the powerplay hardware manager.
\ ``return``\    always PP_Result_OK

.. _`polaris10_voltage_control`:

polaris10_voltage_control
=========================

.. c:function:: bool polaris10_voltage_control(const struct pp_hwmgr *hwmgr)

    :param const struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_voltage_control.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.

.. _`polaris10_enable_voltage_control`:

polaris10_enable_voltage_control
================================

.. c:function:: int polaris10_enable_voltage_control(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_enable_voltage_control.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`polaris10_construct_voltage_tables`:

polaris10_construct_voltage_tables
==================================

.. c:function:: int polaris10_construct_voltage_tables(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_construct_voltage_tables.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`polaris10_program_static_screen_threshold_parameters`:

polaris10_program_static_screen_threshold_parameters
====================================================

.. c:function:: int polaris10_program_static_screen_threshold_parameters(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_program_static_screen_threshold_parameters.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`polaris10_enable_display_gap`:

polaris10_enable_display_gap
============================

.. c:function:: int polaris10_enable_display_gap(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_enable_display_gap.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always  0

.. _`polaris10_program_voting_clients`:

polaris10_program_voting_clients
================================

.. c:function:: int polaris10_program_voting_clients(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_program_voting_clients.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always  0

.. _`polaris10_process_firmware_header`:

polaris10_process_firmware_header
=================================

.. c:function:: int polaris10_process_firmware_header(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_process_firmware_header.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always  0

.. _`polaris10_initial_switch_from_arbf0_to_f1`:

polaris10_initial_switch_from_arbf0_to_f1
=========================================

.. c:function:: int polaris10_initial_switch_from_arbf0_to_f1(struct pp_hwmgr *hwmgr)

    >F1

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_initial_switch_from_arbf0_to_f1.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0
This function is to be called from the SetPowerState table.

.. _`polaris10_populate_smc_mvdd_table`:

polaris10_populate_smc_mvdd_table
=================================

.. c:function:: int polaris10_populate_smc_mvdd_table(struct pp_hwmgr *hwmgr, SMU74_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param SMU74_Discrete_DpmTable \*table:
        *undescribed*

.. _`polaris10_populate_smc_mvdd_table.description`:

Description
-----------

\ ``param``\     \*hwmgr The address of the hardware manager.
\ ``param``\     \*table The SMC DPM table structure to be populated.
\ ``return``\    0

.. _`polaris10_populate_cac_table`:

polaris10_populate_cac_table
============================

.. c:function:: int polaris10_populate_cac_table(struct pp_hwmgr *hwmgr, struct SMU74_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param struct SMU74_Discrete_DpmTable \*table:
        *undescribed*

.. _`polaris10_populate_cac_table.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the hardware manager
\ ``param``\     table  the SMC DPM table structure to be populated
\ ``return``\    always 0

.. _`polaris10_populate_smc_voltage_tables`:

polaris10_populate_smc_voltage_tables
=====================================

.. c:function:: int polaris10_populate_smc_voltage_tables(struct pp_hwmgr *hwmgr, struct SMU74_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param struct SMU74_Discrete_DpmTable \*table:
        *undescribed*

.. _`polaris10_populate_smc_voltage_tables.description`:

Description
-----------

\ ``param``\     hwmgr   the address of the hardware manager
\ ``param``\     table   the SMC DPM table structure to be populated
\ ``return``\    always  0

.. _`polaris10_calculate_sclk_params`:

polaris10_calculate_sclk_params
===============================

.. c:function:: int polaris10_calculate_sclk_params(struct pp_hwmgr *hwmgr, uint32_t clock, SMU_SclkSetting *sclk_setting)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t clock:
        *undescribed*

    :param SMU_SclkSetting \*sclk_setting:
        *undescribed*

.. _`polaris10_calculate_sclk_params.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the hardware manager
\ ``param``\     clock  the engine clock to use to populate the structure
\ ``param``\     sclk   the SMC SCLK structure to be populated

.. _`polaris10_populate_single_graphic_level`:

polaris10_populate_single_graphic_level
=======================================

.. c:function:: int polaris10_populate_single_graphic_level(struct pp_hwmgr *hwmgr, uint32_t clock, uint16_t sclk_al_threshold, struct SMU74_Discrete_GraphicsLevel *level)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t clock:
        *undescribed*

    :param uint16_t sclk_al_threshold:
        *undescribed*

    :param struct SMU74_Discrete_GraphicsLevel \*level:
        *undescribed*

.. _`polaris10_populate_single_graphic_level.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     clock the engine clock to use to populate the structure
\ ``param``\     sclk        the SMC SCLK structure to be populated

.. _`polaris10_populate_all_graphic_levels`:

polaris10_populate_all_graphic_levels
=====================================

.. c:function:: int polaris10_populate_all_graphic_levels(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_populate_all_graphic_levels.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager

.. _`polaris10_populate_all_memory_levels`:

polaris10_populate_all_memory_levels
====================================

.. c:function:: int polaris10_populate_all_memory_levels(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_populate_all_memory_levels.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager

.. _`polaris10_populate_mvdd_value`:

polaris10_populate_mvdd_value
=============================

.. c:function:: int polaris10_populate_mvdd_value(struct pp_hwmgr *hwmgr, uint32_t mclk, SMIO_Pattern *smio_pat)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t mclk:
        *undescribed*

    :param SMIO_Pattern \*smio_pat:
        *undescribed*

.. _`polaris10_populate_mvdd_value.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     mclk        the MCLK value to be used in the decision if MVDD should be high or low.
\ ``param``\     voltage     the SMC VOLTAGE structure to be populated

.. _`polaris10_populate_vr_config`:

polaris10_populate_vr_config
============================

.. c:function:: int polaris10_populate_vr_config(struct pp_hwmgr *hwmgr, struct SMU74_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param struct SMU74_Discrete_DpmTable \*table:
        *undescribed*

.. _`polaris10_populate_vr_config.description`:

Description
-----------

\ ``param``\     hwmgr   the address of the hardware manager
\ ``param``\     table   the SMC DPM table structure to be populated
\ ``return``\    always 0

.. _`polaris10_init_smc_table`:

polaris10_init_smc_table
========================

.. c:function:: int polaris10_init_smc_table(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_init_smc_table.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`polaris10_init_arb_table_index`:

polaris10_init_arb_table_index
==============================

.. c:function:: int polaris10_init_arb_table_index(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_init_arb_table_index.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`polaris10_get_evv_voltages`:

polaris10_get_evv_voltages
==========================

.. c:function:: int polaris10_get_evv_voltages(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_get_evv_voltages.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`polaris10_patch_with_vdd_leakage`:

polaris10_patch_with_vdd_leakage
================================

.. c:function:: void polaris10_patch_with_vdd_leakage(struct pp_hwmgr *hwmgr, uint16_t *voltage, struct polaris10_leakage_voltage *leakage_table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint16_t \*voltage:
        *undescribed*

    :param struct polaris10_leakage_voltage \*leakage_table:
        *undescribed*

.. _`polaris10_patch_with_vdd_leakage.description`:

Description
-----------

\ ``param``\      hwmgr  the address of the powerplay hardware manager.
\ ``param``\      pointer to changing voltage
\ ``param``\      pointer to leakage table

.. _`polaris10_patch_lookup_table_with_leakage`:

polaris10_patch_lookup_table_with_leakage
=========================================

.. c:function:: int polaris10_patch_lookup_table_with_leakage(struct pp_hwmgr *hwmgr, phm_ppt_v1_voltage_lookup_table *lookup_table, struct polaris10_leakage_voltage *leakage_table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param phm_ppt_v1_voltage_lookup_table \*lookup_table:
        *undescribed*

    :param struct polaris10_leakage_voltage \*leakage_table:
        *undescribed*

.. _`polaris10_patch_lookup_table_with_leakage.description`:

Description
-----------

\ ``param``\      hwmgr  the address of the powerplay hardware manager.
\ ``param``\      pointer to voltage lookup table
\ ``param``\      pointer to leakage table
\ ``return``\      always 0

.. _`polaris10_program_display_gap`:

polaris10_program_display_gap
=============================

.. c:function:: int polaris10_program_display_gap(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_program_display_gap.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always OK

.. _`polaris10_set_max_fan_rpm_output`:

polaris10_set_max_fan_rpm_output
================================

.. c:function:: int polaris10_set_max_fan_rpm_output(struct pp_hwmgr *hwmgr, uint16_t us_max_fan_rpm)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint16_t us_max_fan_rpm:
        *undescribed*

.. _`polaris10_read_clock_registers`:

polaris10_read_clock_registers
==============================

.. c:function:: int polaris10_read_clock_registers(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_read_clock_registers.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`polaris10_get_memory_type`:

polaris10_get_memory_type
=========================

.. c:function:: int polaris10_get_memory_type(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_get_memory_type.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`polaris10_enable_acpi_power_management`:

polaris10_enable_acpi_power_management
======================================

.. c:function:: int polaris10_enable_acpi_power_management(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_enable_acpi_power_management.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`polaris10_init_power_gate_state`:

polaris10_init_power_gate_state
===============================

.. c:function:: int polaris10_init_power_gate_state(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_init_power_gate_state.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. This file was automatic generated / don't edit.

