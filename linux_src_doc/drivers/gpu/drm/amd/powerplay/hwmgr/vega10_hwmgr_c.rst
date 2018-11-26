.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/vega10_hwmgr.c

.. _`vega10_get_evv_voltages`:

vega10_get_evv_voltages
=======================

.. c:function:: int vega10_get_evv_voltages(struct pp_hwmgr *hwmgr)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_get_evv_voltages.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0.

.. _`vega10_patch_with_vdd_leakage`:

vega10_patch_with_vdd_leakage
=============================

.. c:function:: void vega10_patch_with_vdd_leakage(struct pp_hwmgr *hwmgr, uint16_t *voltage, struct vega10_leakage_voltage *leakage_table)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param voltage:
        *undescribed*
    :type voltage: uint16_t \*

    :param leakage_table:
        *undescribed*
    :type leakage_table: struct vega10_leakage_voltage \*

.. _`vega10_patch_with_vdd_leakage.description`:

Description
-----------

\ ``param``\      hwmgr  the address of the powerplay hardware manager.
\ ``param``\      pointer to changing voltage
\ ``param``\      pointer to leakage table

.. _`vega10_patch_lookup_table_with_leakage`:

vega10_patch_lookup_table_with_leakage
======================================

.. c:function:: int vega10_patch_lookup_table_with_leakage(struct pp_hwmgr *hwmgr, phm_ppt_v1_voltage_lookup_table *lookup_table, struct vega10_leakage_voltage *leakage_table)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param lookup_table:
        *undescribed*
    :type lookup_table: phm_ppt_v1_voltage_lookup_table \*

    :param leakage_table:
        *undescribed*
    :type leakage_table: struct vega10_leakage_voltage \*

.. _`vega10_patch_lookup_table_with_leakage.description`:

Description
-----------

\ ``param``\      hwmgr  the address of the powerplay hardware manager.
\ ``param``\      pointer to voltage lookup table
\ ``param``\      pointer to leakage table
\ ``return``\      always 0

.. _`vega10_trim_voltage_table`:

vega10_trim_voltage_table
=========================

.. c:function:: int vega10_trim_voltage_table(struct pp_hwmgr *hwmgr, struct pp_atomfwctrl_voltage_table *vol_table)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param vol_table:
        *undescribed*
    :type vol_table: struct pp_atomfwctrl_voltage_table \*

.. _`vega10_trim_voltage_table.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``param``\     vol_table  the pointer to changing voltage table
\ ``return``\     0 in success

.. _`vega10_construct_voltage_tables`:

vega10_construct_voltage_tables
===============================

.. c:function:: int vega10_construct_voltage_tables(struct pp_hwmgr *hwmgr)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_construct_voltage_tables.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`vega10_populate_single_gfx_level`:

vega10_populate_single_gfx_level
================================

.. c:function:: int vega10_populate_single_gfx_level(struct pp_hwmgr *hwmgr, uint32_t gfx_clock, PllSetting_t *current_gfxclk_level, uint32_t *acg_freq)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param gfx_clock:
        *undescribed*
    :type gfx_clock: uint32_t

    :param current_gfxclk_level:
        *undescribed*
    :type current_gfxclk_level: PllSetting_t \*

    :param acg_freq:
        *undescribed*
    :type acg_freq: uint32_t \*

.. _`vega10_populate_single_gfx_level.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager
\ ``param``\     gfx_clock  the GFX clock to use to populate the structure.
\ ``param``\     current_gfxclk_level  location in PPTable for the SMC GFXCLK structure.

.. _`vega10_populate_all_graphic_levels`:

vega10_populate_all_graphic_levels
==================================

.. c:function:: int vega10_populate_all_graphic_levels(struct pp_hwmgr *hwmgr)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_populate_all_graphic_levels.description`:

Description
-----------

\ ``param``\     hwmgr      the address of the hardware manager

.. _`vega10_init_smc_table`:

vega10_init_smc_table
=====================

.. c:function:: int vega10_init_smc_table(struct pp_hwmgr *hwmgr)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_init_smc_table.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.
\ ``param``\     pInput  the pointer to input data (PowerState)
\ ``return``\    always 0

.. This file was automatic generated / don't edit.

