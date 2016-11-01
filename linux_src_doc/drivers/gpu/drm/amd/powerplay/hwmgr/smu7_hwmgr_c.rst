.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/smu7_hwmgr.c

.. _`smu7_get_mc_microcode_version`:

smu7_get_mc_microcode_version
=============================

.. c:function:: int smu7_get_mc_microcode_version(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_get_mc_microcode_version.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`smu7_enable_smc_voltage_controller`:

smu7_enable_smc_voltage_controller
==================================

.. c:function:: int smu7_enable_smc_voltage_controller(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_enable_smc_voltage_controller.description`:

Description
-----------

@param    pHwMgr  the address of the powerplay hardware manager.
\ ``return``\    always PP_Result_OK

.. _`smu7_voltage_control`:

smu7_voltage_control
====================

.. c:function:: bool smu7_voltage_control(const struct pp_hwmgr *hwmgr)

    :param const struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_voltage_control.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.

.. _`smu7_enable_voltage_control`:

smu7_enable_voltage_control
===========================

.. c:function:: int smu7_enable_voltage_control(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_enable_voltage_control.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`smu7_construct_voltage_tables`:

smu7_construct_voltage_tables
=============================

.. c:function:: int smu7_construct_voltage_tables(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_construct_voltage_tables.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`smu7_program_static_screen_threshold_parameters`:

smu7_program_static_screen_threshold_parameters
===============================================

.. c:function:: int smu7_program_static_screen_threshold_parameters(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_program_static_screen_threshold_parameters.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`smu7_enable_display_gap`:

smu7_enable_display_gap
=======================

.. c:function:: int smu7_enable_display_gap(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_enable_display_gap.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always  0

.. _`smu7_program_voting_clients`:

smu7_program_voting_clients
===========================

.. c:function:: int smu7_program_voting_clients(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_program_voting_clients.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always  0

.. _`smu7_initial_switch_from_arbf0_to_f1`:

smu7_initial_switch_from_arbf0_to_f1
====================================

.. c:function:: int smu7_initial_switch_from_arbf0_to_f1(struct pp_hwmgr *hwmgr)

    >F1

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_initial_switch_from_arbf0_to_f1.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0
This function is to be called from the SetPowerState table.

.. _`smu7_get_evv_voltages`:

smu7_get_evv_voltages
=====================

.. c:function:: int smu7_get_evv_voltages(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_get_evv_voltages.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`smu7_patch_ppt_v1_with_vdd_leakage`:

smu7_patch_ppt_v1_with_vdd_leakage
==================================

.. c:function:: void smu7_patch_ppt_v1_with_vdd_leakage(struct pp_hwmgr *hwmgr, uint16_t *voltage, struct smu7_leakage_voltage *leakage_table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint16_t \*voltage:
        *undescribed*

    :param struct smu7_leakage_voltage \*leakage_table:
        *undescribed*

.. _`smu7_patch_ppt_v1_with_vdd_leakage.description`:

Description
-----------

@param     hwmgr  the address of the powerplay hardware manager.
\ ``param``\      pointer to changing voltage
\ ``param``\      pointer to leakage table

.. _`smu7_patch_lookup_table_with_leakage`:

smu7_patch_lookup_table_with_leakage
====================================

.. c:function:: int smu7_patch_lookup_table_with_leakage(struct pp_hwmgr *hwmgr, phm_ppt_v1_voltage_lookup_table *lookup_table, struct smu7_leakage_voltage *leakage_table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param phm_ppt_v1_voltage_lookup_table \*lookup_table:
        *undescribed*

    :param struct smu7_leakage_voltage \*leakage_table:
        *undescribed*

.. _`smu7_patch_lookup_table_with_leakage.description`:

Description
-----------

@param     hwmgr  the address of the powerplay hardware manager.
\ ``param``\      pointer to voltage lookup table
\ ``param``\      pointer to leakage table
\ ``return``\      always 0

.. _`smu7_patch_ppt_v0_with_vdd_leakage`:

smu7_patch_ppt_v0_with_vdd_leakage
==================================

.. c:function:: void smu7_patch_ppt_v0_with_vdd_leakage(struct pp_hwmgr *hwmgr, uint32_t *voltage, struct smu7_leakage_voltage *leakage_table)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t \*voltage:
        *undescribed*

    :param struct smu7_leakage_voltage \*leakage_table:
        *undescribed*

.. _`smu7_patch_ppt_v0_with_vdd_leakage.description`:

Description
-----------

@param     hwmgr  the address of the powerplay hardware manager.
\ ``param``\      pointer to changing voltage
\ ``param``\      pointer to leakage table

.. _`smu7_program_display_gap`:

smu7_program_display_gap
========================

.. c:function:: int smu7_program_display_gap(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_program_display_gap.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always OK

.. _`smu7_set_max_fan_rpm_output`:

smu7_set_max_fan_rpm_output
===========================

.. c:function:: int smu7_set_max_fan_rpm_output(struct pp_hwmgr *hwmgr, uint16_t us_max_fan_rpm)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint16_t us_max_fan_rpm:
        *undescribed*

.. _`smu7_get_memory_type`:

smu7_get_memory_type
====================

.. c:function:: int smu7_get_memory_type(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_get_memory_type.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`smu7_enable_acpi_power_management`:

smu7_enable_acpi_power_management
=================================

.. c:function:: int smu7_enable_acpi_power_management(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_enable_acpi_power_management.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. _`smu7_init_power_gate_state`:

smu7_init_power_gate_state
==========================

.. c:function:: int smu7_init_power_gate_state(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_init_power_gate_state.description`:

Description
-----------

@param    hwmgr  the address of the powerplay hardware manager.
\ ``return``\    always 0

.. This file was automatic generated / don't edit.

