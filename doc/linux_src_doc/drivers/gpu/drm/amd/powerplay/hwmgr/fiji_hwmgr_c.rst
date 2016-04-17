.. -*- coding: utf-8; mode: rst -*-

============
fiji_hwmgr.c
============


.. _`fiji_get_evv_voltages`:

fiji_get_evv_voltages
=====================

.. c:function:: int fiji_get_evv_voltages (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_get_evv_voltages.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always 0



.. _`fiji_patch_with_vdd_leakage`:

fiji_patch_with_vdd_leakage
===========================

.. c:function:: void fiji_patch_with_vdd_leakage (struct pp_hwmgr *hwmgr, uint16_t *voltage, struct fiji_leakage_voltage *leakage_table)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param uint16_t \*voltage:

        *undescribed*

    :param struct fiji_leakage_voltage \*leakage_table:

        *undescribed*



.. _`fiji_patch_with_vdd_leakage.description`:

Description
-----------


``param``     hwmgr  the address of the powerplay hardware manager.
``param``     pointer to changing voltage
``param``     pointer to leakage table



.. _`fiji_patch_lookup_table_with_leakage`:

fiji_patch_lookup_table_with_leakage
====================================

.. c:function:: int fiji_patch_lookup_table_with_leakage (struct pp_hwmgr *hwmgr, phm_ppt_v1_voltage_lookup_table *lookup_table, struct fiji_leakage_voltage *leakage_table)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param phm_ppt_v1_voltage_lookup_table \*lookup_table:

        *undescribed*

    :param struct fiji_leakage_voltage \*leakage_table:

        *undescribed*



.. _`fiji_patch_lookup_table_with_leakage.description`:

Description
-----------


``param``     hwmgr  the address of the powerplay hardware manager.
``param``     pointer to voltage lookup table
``param``     pointer to leakage table
``return``     always 0



.. _`fiji_read_clock_registers`:

fiji_read_clock_registers
=========================

.. c:function:: int fiji_read_clock_registers (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_read_clock_registers.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always 0



.. _`fiji_get_memory_type`:

fiji_get_memory_type
====================

.. c:function:: int fiji_get_memory_type (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_get_memory_type.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always 0



.. _`fiji_enable_acpi_power_management`:

fiji_enable_acpi_power_management
=================================

.. c:function:: int fiji_enable_acpi_power_management (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_enable_acpi_power_management.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always 0



.. _`fiji_init_power_gate_state`:

fiji_init_power_gate_state
==========================

.. c:function:: int fiji_init_power_gate_state (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_init_power_gate_state.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always 0



.. _`fiji_voltage_control`:

fiji_voltage_control
====================

.. c:function:: bool fiji_voltage_control (const struct pp_hwmgr *hwmgr)

    :param const struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_voltage_control.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.



.. _`fiji_enable_voltage_control`:

fiji_enable_voltage_control
===========================

.. c:function:: int fiji_enable_voltage_control (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_enable_voltage_control.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always 0



.. _`fiji_trim_voltage_table`:

fiji_trim_voltage_table
=======================

.. c:function:: int fiji_trim_voltage_table (struct pp_hwmgr *hwmgr, struct pp_atomctrl_voltage_table *vol_table)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param struct pp_atomctrl_voltage_table \*vol_table:

        *undescribed*



.. _`fiji_trim_voltage_table.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``param``    vol_table  the pointer to changing voltage table
``return``    0 in success



.. _`fiji_construct_voltage_tables`:

fiji_construct_voltage_tables
=============================

.. c:function:: int fiji_construct_voltage_tables (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_construct_voltage_tables.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always 0



.. _`fiji_program_static_screen_threshold_parameters`:

fiji_program_static_screen_threshold_parameters
===============================================

.. c:function:: int fiji_program_static_screen_threshold_parameters (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_program_static_screen_threshold_parameters.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always 0



.. _`fiji_enable_display_gap`:

fiji_enable_display_gap
=======================

.. c:function:: int fiji_enable_display_gap (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_enable_display_gap.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always  0



.. _`fiji_program_voting_clients`:

fiji_program_voting_clients
===========================

.. c:function:: int fiji_program_voting_clients (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_program_voting_clients.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always  0



.. _`fiji_process_firmware_header`:

fiji_process_firmware_header
============================

.. c:function:: int fiji_process_firmware_header (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_process_firmware_header.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always  0



.. _`fiji_initial_switch_from_arbf0_to_f1`:

fiji_initial_switch_from_arbf0_to_f1
====================================

.. c:function:: int fiji_initial_switch_from_arbf0_to_f1 (struct pp_hwmgr *hwmgr)

    >F1

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_initial_switch_from_arbf0_to_f1.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always 0
This function is to be called from the SetPowerState table.



.. _`fiji_populate_cac_table`:

fiji_populate_cac_table
=======================

.. c:function:: int fiji_populate_cac_table (struct pp_hwmgr *hwmgr, struct SMU73_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param struct SMU73_Discrete_DpmTable \*table:

        *undescribed*



.. _`fiji_populate_cac_table.description`:

Description
-----------


``param``    hwmgr  the address of the hardware manager
``param``    table  the SMC DPM table structure to be populated
``return``   always 0



.. _`fiji_populate_smc_voltage_tables`:

fiji_populate_smc_voltage_tables
================================

.. c:function:: int fiji_populate_smc_voltage_tables (struct pp_hwmgr *hwmgr, struct SMU73_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param struct SMU73_Discrete_DpmTable \*table:

        *undescribed*



.. _`fiji_populate_smc_voltage_tables.description`:

Description
-----------


``param``    hwmgr   the address of the hardware manager
``param``    table   the SMC DPM table structure to be populated
``return``   always  0



.. _`fiji_calculate_sclk_params`:

fiji_calculate_sclk_params
==========================

.. c:function:: int fiji_calculate_sclk_params (struct pp_hwmgr *hwmgr, uint32_t clock, struct SMU73_Discrete_GraphicsLevel *sclk)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param uint32_t clock:

        *undescribed*

    :param struct SMU73_Discrete_GraphicsLevel \*sclk:

        *undescribed*



.. _`fiji_calculate_sclk_params.description`:

Description
-----------


``param``    hwmgr  the address of the hardware manager
``param``    clock  the engine clock to use to populate the structure
``param``    sclk   the SMC SCLK structure to be populated



.. _`fiji_populate_single_graphic_level`:

fiji_populate_single_graphic_level
==================================

.. c:function:: int fiji_populate_single_graphic_level (struct pp_hwmgr *hwmgr, uint32_t clock, uint16_t sclk_al_threshold, struct SMU73_Discrete_GraphicsLevel *level)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param uint32_t clock:

        *undescribed*

    :param uint16_t sclk_al_threshold:

        *undescribed*

    :param struct SMU73_Discrete_GraphicsLevel \*level:

        *undescribed*



.. _`fiji_populate_single_graphic_level.description`:

Description
-----------


``param``    hwmgr      the address of the hardware manager
``param``    clock the engine clock to use to populate the structure
``param``    sclk        the SMC SCLK structure to be populated



.. _`fiji_populate_all_graphic_levels`:

fiji_populate_all_graphic_levels
================================

.. c:function:: int fiji_populate_all_graphic_levels (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_populate_all_graphic_levels.description`:

Description
-----------


``param``    hwmgr      the address of the hardware manager



.. _`fiji_get_mclk_frequency_ratio`:

fiji_get_mclk_frequency_ratio
=============================

.. c:function:: uint8_t fiji_get_mclk_frequency_ratio (uint32_t mem_clock)

    :param uint32_t mem_clock:

        *undescribed*



.. _`fiji_get_mclk_frequency_ratio.description`:

Description
-----------

SEQ_CG_RESP  Bit[31:24] - 0x0
Bit[27:24] \96 DDR3 Frequency ratio
0x0 <= 100MHz,       450 < 0x8 <= 500MHz
100 < 0x1 <= 150MHz,       500 < 0x9 <= 550MHz
150 < 0x2 <= 200MHz,       550 < 0xA <= 600MHz
200 < 0x3 <= 250MHz,       600 < 0xB <= 650MHz
250 < 0x4 <= 300MHz,       650 < 0xC <= 700MHz
300 < 0x5 <= 350MHz,       700 < 0xD <= 750MHz
350 < 0x6 <= 400MHz,       750 < 0xE <= 800MHz
400 < 0x7 <= 450MHz,       800 < 0xF



.. _`fiji_calculate_mclk_params`:

fiji_calculate_mclk_params
==========================

.. c:function:: int fiji_calculate_mclk_params (struct pp_hwmgr *hwmgr, uint32_t clock, struct SMU73_Discrete_MemoryLevel *mclk)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param uint32_t clock:

        *undescribed*

    :param struct SMU73_Discrete_MemoryLevel \*mclk:

        *undescribed*



.. _`fiji_calculate_mclk_params.description`:

Description
-----------


``param``    hwmgr   the address of the hardware manager
``param``    clock   the memory clock to use to populate the structure
``param``    sclk    the SMC SCLK structure to be populated



.. _`fiji_populate_all_memory_levels`:

fiji_populate_all_memory_levels
===============================

.. c:function:: int fiji_populate_all_memory_levels (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_populate_all_memory_levels.description`:

Description
-----------


``param``    hwmgr      the address of the hardware manager



.. _`fiji_populate_mvdd_value`:

fiji_populate_mvdd_value
========================

.. c:function:: int fiji_populate_mvdd_value (struct pp_hwmgr *hwmgr, uint32_t mclk, SMIO_Pattern *smio_pat)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param uint32_t mclk:

        *undescribed*

    :param SMIO_Pattern \*smio_pat:

        *undescribed*



.. _`fiji_populate_mvdd_value.description`:

Description
-----------


``param``    hwmgr      the address of the hardware manager
``param``    mclk        the MCLK value to be used in the decision if MVDD should be high or low.
``param``    voltage     the SMC VOLTAGE structure to be populated



.. _`fiji_populate_vr_config`:

fiji_populate_vr_config
=======================

.. c:function:: int fiji_populate_vr_config (struct pp_hwmgr *hwmgr, struct SMU73_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param struct SMU73_Discrete_DpmTable \*table:

        *undescribed*



.. _`fiji_populate_vr_config.description`:

Description
-----------


``param``    hwmgr   the address of the hardware manager
``param``    table   the SMC DPM table structure to be populated
``return``   always 0



.. _`fiji_init_smc_table`:

fiji_init_smc_table
===================

.. c:function:: int fiji_init_smc_table (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_init_smc_table.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``param``    pInput  the pointer to input data (PowerState)
``return``   always 0



.. _`fiji_init_arb_table_index`:

fiji_init_arb_table_index
=========================

.. c:function:: int fiji_init_arb_table_index (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`fiji_init_arb_table_index.description`:

Description
-----------


``param``    hwmgr  the address of the powerplay hardware manager.
``return``   always 0

