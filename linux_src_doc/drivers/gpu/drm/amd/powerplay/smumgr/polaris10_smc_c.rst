.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/smumgr/polaris10_smc.c

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

@param    \*hwmgr The address of the hardware manager.
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

@param    hwmgr  the address of the hardware manager
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

@param    hwmgr   the address of the hardware manager
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

@param    hwmgr  the address of the hardware manager
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

@param    hwmgr      the address of the hardware manager
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

@param    hwmgr      the address of the hardware manager

.. _`polaris10_populate_all_memory_levels`:

polaris10_populate_all_memory_levels
====================================

.. c:function:: int polaris10_populate_all_memory_levels(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_populate_all_memory_levels.description`:

Description
-----------

@param    hwmgr      the address of the hardware manager

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

@param    hwmgr      the address of the hardware manager
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

@param    hwmgr   the address of the hardware manager
\ ``param``\     table   the SMC DPM table structure to be populated
\ ``return``\    always 0

.. _`polaris10_init_arb_table_index`:

polaris10_init_arb_table_index
==============================

.. c:function:: int polaris10_init_arb_table_index(struct pp_smumgr *smumgr)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

.. _`polaris10_init_arb_table_index.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
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

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`polaris10_thermal_setup_fan_table`:

polaris10_thermal_setup_fan_table
=================================

.. c:function:: int polaris10_thermal_setup_fan_table(struct pp_hwmgr *hwmgr)

    @param    hwmgr  the address of the powerplay hardware manager. \ ``param``\     pInput the pointer to input data \ ``param``\     pOutput the pointer to output data \ ``param``\     pStorage the pointer to temporary storage \ ``param``\     Result the last failure code \ ``return``\    result from set temperature range routine

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_process_firmware_header`:

polaris10_process_firmware_header
=================================

.. c:function:: int polaris10_process_firmware_header(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`polaris10_process_firmware_header.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always  0

.. This file was automatic generated / don't edit.

