.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/smumgr/iceland_smc.c

.. _`iceland_calculate_sclk_params`:

iceland_calculate_sclk_params
=============================

.. c:function:: int iceland_calculate_sclk_params(struct pp_hwmgr *hwmgr, uint32_t engine_clock, SMU71_Discrete_GraphicsLevel *sclk)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t engine_clock:
        *undescribed*

    :param SMU71_Discrete_GraphicsLevel \*sclk:
        *undescribed*

.. _`iceland_calculate_sclk_params.description`:

Description
-----------

@param    hwmgr      the address of the hardware manager
\ ``param``\     engine_clock the engine clock to use to populate the structure
\ ``param``\     sclk        the SMC SCLK structure to be populated

.. _`iceland_populate_single_graphic_level`:

iceland_populate_single_graphic_level
=====================================

.. c:function:: int iceland_populate_single_graphic_level(struct pp_hwmgr *hwmgr, uint32_t engine_clock, uint16_t sclk_activity_level_threshold, SMU71_Discrete_GraphicsLevel *graphic_level)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t engine_clock:
        *undescribed*

    :param uint16_t sclk_activity_level_threshold:
        *undescribed*

    :param SMU71_Discrete_GraphicsLevel \*graphic_level:
        *undescribed*

.. _`iceland_populate_single_graphic_level.description`:

Description
-----------

@param    hwmgr      the address of the hardware manager
\ ``param``\     engine_clock the engine clock to use to populate the structure
\ ``param``\     sclk        the SMC SCLK structure to be populated

.. _`iceland_populate_all_graphic_levels`:

iceland_populate_all_graphic_levels
===================================

.. c:function:: int iceland_populate_all_graphic_levels(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`iceland_populate_all_graphic_levels.description`:

Description
-----------

@param    hwmgr      the address of the hardware manager

.. _`iceland_calculate_mclk_params`:

iceland_calculate_mclk_params
=============================

.. c:function:: int iceland_calculate_mclk_params(struct pp_hwmgr *hwmgr, uint32_t memory_clock, SMU71_Discrete_MemoryLevel *mclk, bool strobe_mode, bool dllStateOn)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t memory_clock:
        *undescribed*

    :param SMU71_Discrete_MemoryLevel \*mclk:
        *undescribed*

    :param bool strobe_mode:
        *undescribed*

    :param bool dllStateOn:
        *undescribed*

.. _`iceland_calculate_mclk_params.description`:

Description
-----------

@param    hwmgr      the address of the hardware manager
\ ``param``\     memory_clock the memory clock to use to populate the structure
\ ``param``\     sclk        the SMC SCLK structure to be populated

.. _`iceland_populate_all_memory_levels`:

iceland_populate_all_memory_levels
==================================

.. c:function:: int iceland_populate_all_memory_levels(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`iceland_populate_all_memory_levels.description`:

Description
-----------

@param    hwmgr      the address of the hardware manager

.. _`iceland_program_memory_timing_parameters`:

iceland_program_memory_timing_parameters
========================================

.. c:function:: int iceland_program_memory_timing_parameters(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`iceland_program_memory_timing_parameters.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0
This function is to be called from the SetPowerState table.

.. _`iceland_init_smc_table`:

iceland_init_smc_table
======================

.. c:function:: int iceland_init_smc_table(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`iceland_init_smc_table.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``param``\     pInput  the pointer to input data (PowerState)
\ ``return``\    always 0

.. _`iceland_thermal_setup_fan_table`:

iceland_thermal_setup_fan_table
===============================

.. c:function:: int iceland_thermal_setup_fan_table(struct pp_hwmgr *hwmgr)

    @param    hwmgr  the address of the powerplay hardware manager. \ ``param``\     pInput the pointer to input data \ ``param``\     pOutput the pointer to output data \ ``param``\     pStorage the pointer to temporary storage \ ``param``\     Result the last failure code \ ``return``\    result from set temperature range routine

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`iceland_process_firmware_header`:

iceland_process_firmware_header
===============================

.. c:function:: int iceland_process_firmware_header(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`iceland_process_firmware_header.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`iceland_set_mc_special_registers`:

iceland_set_mc_special_registers
================================

.. c:function:: int iceland_set_mc_special_registers(struct pp_hwmgr *hwmgr, struct iceland_mc_reg_table *table)

    1.   when we see mmMC_SEQ_MISC1, bit[31:16] EMRS1, need to be write to  mmMC_PMG_CMD_EMRS /_LP[15:0]. Bit[15:0] MRS, need to be update mmMC_PMG_CMD_MRS/_LP[15:0] 2.   when we see mmMC_SEQ_RESERVE_M, bit[15:0] EMRS2, need to be write to mmMC_PMG_CMD_MRS1/_LP[15:0]. 3.   need to set these data for each clock range

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param struct iceland_mc_reg_table \*table:
        *undescribed*

.. _`iceland_set_mc_special_registers.description`:

Description
-----------

@param    hwmgr the address of the powerplay hardware manager.
\ ``param``\     table the address of MCRegTable
\ ``return``\    always 0

.. This file was automatic generated / don't edit.

