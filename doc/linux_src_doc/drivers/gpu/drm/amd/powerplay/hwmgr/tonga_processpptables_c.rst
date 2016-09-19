.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/tonga_processpptables.c

.. _`set_hw_cap`:

set_hw_cap
==========

.. c:function:: void set_hw_cap(struct pp_hwmgr *hwmgr, bool setIt, enum phm_platform_caps cap)

    \ ``param``\  hwmgr Pointer to the hardware manager. \ ``param``\  setIt A flag indication if the capability should be set (TRUE) or reset (FALSE). \ ``param``\  cap Which capability to set/reset.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param bool setIt:
        *undescribed*

    :param enum phm_platform_caps cap:
        *undescribed*

.. _`set_platform_caps`:

set_platform_caps
=================

.. c:function:: int set_platform_caps(struct pp_hwmgr *hwmgr, uint32_t powerplay_caps)

    \ ``param``\  hwmgr Pointer to the hardware manager. \ ``param``\  powerplay_caps the bit array (from BIOS) of capability bits. \ ``exception``\  the current implementation always returns 1.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t powerplay_caps:
        *undescribed*

.. _`get_powerplay_table`:

get_powerplay_table
===================

.. c:function:: const void *get_powerplay_table(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`get_platform_power_management_table`:

get_platform_power_management_table
===================================

.. c:function:: int get_platform_power_management_table(struct pp_hwmgr *hwmgr, ATOM_Tonga_PPM_Table *atom_ppm_table)

    Initialize Platform Power Management Parameter table \ ``param``\  hwmgr Pointer to the hardware manager. \ ``param``\  atom_ppm_table Pointer to PPM table in VBIOS

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param ATOM_Tonga_PPM_Table \*atom_ppm_table:
        *undescribed*

.. _`init_dpm_2_parameters`:

init_dpm_2_parameters
=====================

.. c:function:: int init_dpm_2_parameters(struct pp_hwmgr *hwmgr, const ATOM_Tonga_POWERPLAYTABLE *powerplay_table)

    Initialize TDP limits for DPM2 \ ``param``\  hwmgr Pointer to the hardware manager. \ ``param``\  powerplay_table Pointer to the PowerPlay Table.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param const ATOM_Tonga_POWERPLAYTABLE \*powerplay_table:
        *undescribed*

.. _`init_clock_voltage_dependency`:

init_clock_voltage_dependency
=============================

.. c:function:: int init_clock_voltage_dependency(struct pp_hwmgr *hwmgr, const ATOM_Tonga_POWERPLAYTABLE *powerplay_table)

    Initialize clock voltage dependency \ ``param``\  hwmgr Pointer to the hardware manager. \ ``param``\  powerplay_table Pointer to the PowerPlay Table.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param const ATOM_Tonga_POWERPLAYTABLE \*powerplay_table:
        *undescribed*

.. _`init_thermal_controller`:

init_thermal_controller
=======================

.. c:function:: int init_thermal_controller(struct pp_hwmgr *hwmgr, const ATOM_Tonga_POWERPLAYTABLE *powerplay_table)

    Inspect the PowerPlay table for obvious signs of corruption. \ ``param``\  hwmgr Pointer to the hardware manager. \ ``param``\  powerplay_table Pointer to the PowerPlay Table. \ ``exception``\  This implementation always returns 1.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param const ATOM_Tonga_POWERPLAYTABLE \*powerplay_table:
        *undescribed*

.. _`check_powerplay_tables`:

check_powerplay_tables
======================

.. c:function:: int check_powerplay_tables(struct pp_hwmgr *hwmgr, const ATOM_Tonga_POWERPLAYTABLE *powerplay_table)

    Inspect the PowerPlay table for obvious signs of corruption. \ ``param``\  hwmgr Pointer to the hardware manager. \ ``param``\  powerplay_table Pointer to the PowerPlay Table. \ ``exception``\  2 if the powerplay table is incorrect.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param const ATOM_Tonga_POWERPLAYTABLE \*powerplay_table:
        *undescribed*

.. _`make_classification_flags`:

make_classification_flags
=========================

.. c:function:: uint32_t make_classification_flags(struct pp_hwmgr *hwmgr, uint16_t classification, uint16_t classification2)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint16_t classification:
        *undescribed*

    :param uint16_t classification2:
        *undescribed*

.. _`tonga_get_powerplay_table_entry`:

tonga_get_powerplay_table_entry
===============================

.. c:function:: int tonga_get_powerplay_table_entry(struct pp_hwmgr *hwmgr, uint32_t entry_index, struct pp_power_state *power_state, int (*call_back_func)(struct pp_hwmgr *, void *, struct pp_power_state *, void *, uint32_t))

    This function is called by the hardware back-end. \ ``param``\  hwmgr Pointer to the hardware manager. \ ``param``\  entry_index The index of the entry to be extracted from the table. \ ``param``\  power_state The address of the PowerState instance being created. \ ``return``\  -1 if the entry cannot be retrieved.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t entry_index:
        *undescribed*

    :param struct pp_power_state \*power_state:
        *undescribed*

    :param int (\*call_back_func)(struct pp_hwmgr \*, void \*, struct pp_power_state \*, void \*, uint32_t):
        *undescribed*

.. This file was automatic generated / don't edit.

