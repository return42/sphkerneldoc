.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/smumgr/tonga_smc.c

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

@param    hwmgr      the address of the hardware manager
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

@param    hwmgr      the address of the hardware manager
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

@param    \*hwmgr The address of the hardware manager.
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

@param    \*hwmgr The address of the hardware manager.
\ ``param``\     \*table The SMC DPM table structure to be populated.
\ ``return``\    0

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

@param    hwmgr      the address of the hardware manager
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

@param    hwmgr      the address of the hardware manager
\ ``param``\     table     the SMC DPM table structure to be populated
\ ``return``\    always 0

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

@param    hwmgr      the address of the hardware manager
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

@param    hwmgr      the address of the hardware manager
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

@param    hwmgr      the address of the hardware manager

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

@param    hwmgr      the address of the hardware manager
\ ``param``\     memory_clock the memory clock to use to populate the structure
\ ``param``\     sclk        the SMC SCLK structure to be populated

.. _`tonga_program_memory_timing_parameters`:

tonga_program_memory_timing_parameters
======================================

.. c:function:: int tonga_program_memory_timing_parameters(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_program_memory_timing_parameters.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0
This function is to be called from the SetPowerState table.

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

@param    hwmgr      the address of the hardware manager
\ ``param``\     table     the SMC DPM table structure to be populated
\ ``return``\    always 0

.. _`tonga_init_arb_table_index`:

tonga_init_arb_table_index
==========================

.. c:function:: int tonga_init_arb_table_index(struct pp_smumgr *smumgr)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

.. _`tonga_init_arb_table_index.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_init_smc_table`:

tonga_init_smc_table
====================

.. c:function:: int tonga_init_smc_table(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_init_smc_table.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``param``\     pInput  the pointer to input data (PowerState)
\ ``return``\    always 0

.. _`tonga_thermal_setup_fan_table`:

tonga_thermal_setup_fan_table
=============================

.. c:function:: int tonga_thermal_setup_fan_table(struct pp_hwmgr *hwmgr)

    @param    hwmgr  the address of the powerplay hardware manager. \ ``param``\     pInput the pointer to input data \ ``param``\     pOutput the pointer to output data \ ``param``\     pStorage the pointer to temporary storage \ ``param``\     Result the last failure code \ ``return``\    result from set temperature range routine

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_process_firmware_header`:

tonga_process_firmware_header
=============================

.. c:function:: int tonga_process_firmware_header(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`tonga_process_firmware_header.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`tonga_set_mc_special_registers`:

tonga_set_mc_special_registers
==============================

.. c:function:: int tonga_set_mc_special_registers(struct pp_hwmgr *hwmgr, struct tonga_mc_reg_table *table)

    1.   when we see mmMC_SEQ_MISC1, bit[31:16] EMRS1, need to be write to mmMC_PMG_CMD_EMRS /_LP[15:0]. Bit[15:0] MRS, need to be update mmMC_PMG_CMD_MRS/_LP[15:0] 2.   when we see mmMC_SEQ_RESERVE_M, bit[15:0] EMRS2, need to be write to mmMC_PMG_CMD_MRS1/_LP[15:0]. 3.   need to set these data for each clock range \ ``param``\     hwmgr the address of the powerplay hardware manager. \ ``param``\     table the address of MCRegTable \ ``return``\    always 0

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param struct tonga_mc_reg_table \*table:
        *undescribed*

.. This file was automatic generated / don't edit.

