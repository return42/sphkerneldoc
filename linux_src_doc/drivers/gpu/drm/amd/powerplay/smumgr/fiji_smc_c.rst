.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/smumgr/fiji_smc.c

.. _`fiji_populate_cac_table`:

fiji_populate_cac_table
=======================

.. c:function:: int fiji_populate_cac_table(struct pp_hwmgr *hwmgr, struct SMU73_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param struct SMU73_Discrete_DpmTable \*table:
        *undescribed*

.. _`fiji_populate_cac_table.description`:

Description
-----------

@param    hwmgr  the address of the hardware manager
\ ``param``\     table  the SMC DPM table structure to be populated
\ ``return``\    always 0

.. _`fiji_populate_smc_voltage_tables`:

fiji_populate_smc_voltage_tables
================================

.. c:function:: int fiji_populate_smc_voltage_tables(struct pp_hwmgr *hwmgr, struct SMU73_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param struct SMU73_Discrete_DpmTable \*table:
        *undescribed*

.. _`fiji_populate_smc_voltage_tables.description`:

Description
-----------

@param    hwmgr   the address of the hardware manager
\ ``param``\     table   the SMC DPM table structure to be populated
\ ``return``\    always  0

.. _`fiji_calculate_sclk_params`:

fiji_calculate_sclk_params
==========================

.. c:function:: int fiji_calculate_sclk_params(struct pp_hwmgr *hwmgr, uint32_t clock, struct SMU73_Discrete_GraphicsLevel *sclk)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t clock:
        *undescribed*

    :param struct SMU73_Discrete_GraphicsLevel \*sclk:
        *undescribed*

.. _`fiji_calculate_sclk_params.description`:

Description
-----------

@param    hwmgr  the address of the hardware manager
\ ``param``\     clock  the engine clock to use to populate the structure
\ ``param``\     sclk   the SMC SCLK structure to be populated

.. _`fiji_populate_single_graphic_level`:

fiji_populate_single_graphic_level
==================================

.. c:function:: int fiji_populate_single_graphic_level(struct pp_hwmgr *hwmgr, uint32_t clock, uint16_t sclk_al_threshold, struct SMU73_Discrete_GraphicsLevel *level)

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

@param    hwmgr      the address of the hardware manager
\ ``param``\     clock the engine clock to use to populate the structure
\ ``param``\     sclk        the SMC SCLK structure to be populated

.. _`fiji_populate_all_graphic_levels`:

fiji_populate_all_graphic_levels
================================

.. c:function:: int fiji_populate_all_graphic_levels(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`fiji_populate_all_graphic_levels.description`:

Description
-----------

@param    hwmgr      the address of the hardware manager

.. _`fiji_get_mclk_frequency_ratio`:

fiji_get_mclk_frequency_ratio
=============================

.. c:function:: uint8_t fiji_get_mclk_frequency_ratio(uint32_t mem_clock)

    SEQ_CG_RESP  Bit[31:24] - 0x0 Bit[27:24] \96 DDR3 Frequency ratio 0x0 <= 100MHz,       450 < 0x8 <= 500MHz 100 < 0x1 <= 150MHz,       500 < 0x9 <= 550MHz 150 < 0x2 <= 200MHz,       550 < 0xA <= 600MHz 200 < 0x3 <= 250MHz,       600 < 0xB <= 650MHz 250 < 0x4 <= 300MHz,       650 < 0xC <= 700MHz 300 < 0x5 <= 350MHz,       700 < 0xD <= 750MHz 350 < 0x6 <= 400MHz,       750 < 0xE <= 800MHz 400 < 0x7 <= 450MHz,       800 < 0xF

    :param uint32_t mem_clock:
        *undescribed*

.. _`fiji_calculate_mclk_params`:

fiji_calculate_mclk_params
==========================

.. c:function:: int fiji_calculate_mclk_params(struct pp_hwmgr *hwmgr, uint32_t clock, struct SMU73_Discrete_MemoryLevel *mclk)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t clock:
        *undescribed*

    :param struct SMU73_Discrete_MemoryLevel \*mclk:
        *undescribed*

.. _`fiji_calculate_mclk_params.description`:

Description
-----------

@param    hwmgr   the address of the hardware manager
\ ``param``\     clock   the memory clock to use to populate the structure
\ ``param``\     sclk    the SMC SCLK structure to be populated

.. _`fiji_populate_all_memory_levels`:

fiji_populate_all_memory_levels
===============================

.. c:function:: int fiji_populate_all_memory_levels(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`fiji_populate_all_memory_levels.description`:

Description
-----------

@param    hwmgr      the address of the hardware manager

.. _`fiji_populate_mvdd_value`:

fiji_populate_mvdd_value
========================

.. c:function:: int fiji_populate_mvdd_value(struct pp_hwmgr *hwmgr, uint32_t mclk, SMIO_Pattern *smio_pat)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t mclk:
        *undescribed*

    :param SMIO_Pattern \*smio_pat:
        *undescribed*

.. _`fiji_populate_mvdd_value.description`:

Description
-----------

@param    hwmgr      the address of the hardware manager
\ ``param``\     mclk        the MCLK value to be used in the decision if MVDD should be high or low.
\ ``param``\     voltage     the SMC VOLTAGE structure to be populated

.. _`fiji_populate_vr_config`:

fiji_populate_vr_config
=======================

.. c:function:: int fiji_populate_vr_config(struct pp_hwmgr *hwmgr, struct SMU73_Discrete_DpmTable *table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param struct SMU73_Discrete_DpmTable \*table:
        *undescribed*

.. _`fiji_populate_vr_config.description`:

Description
-----------

@param    hwmgr   the address of the hardware manager
\ ``param``\     table   the SMC DPM table structure to be populated
\ ``return``\    always 0

.. _`fiji_init_smc_table`:

fiji_init_smc_table
===================

.. c:function:: int fiji_init_smc_table(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`fiji_init_smc_table.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``param``\     pInput  the pointer to input data (PowerState)
\ ``return``\    always 0

.. _`fiji_thermal_setup_fan_table`:

fiji_thermal_setup_fan_table
============================

.. c:function:: int fiji_thermal_setup_fan_table(struct pp_hwmgr *hwmgr)

    @param    hwmgr  the address of the powerplay hardware manager. \ ``param``\     pInput the pointer to input data \ ``param``\     pOutput the pointer to output data \ ``param``\     pStorage the pointer to temporary storage \ ``param``\     Result the last failure code \ ``return``\    result from set temperature range routine

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`fiji_process_firmware_header`:

fiji_process_firmware_header
============================

.. c:function:: int fiji_process_firmware_header(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`fiji_process_firmware_header.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always  0

.. This file was automatic generated / don't edit.

