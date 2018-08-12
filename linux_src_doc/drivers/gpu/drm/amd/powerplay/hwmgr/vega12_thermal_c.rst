.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/vega12_thermal.c

.. _`vega12_fan_ctrl_reset_fan_speed_to_default`:

vega12_fan_ctrl_reset_fan_speed_to_default
==========================================

.. c:function:: int vega12_fan_ctrl_reset_fan_speed_to_default(struct pp_hwmgr *hwmgr)

    \ ``param``\     hwmgr  the address of the powerplay hardware manager. \ ``exception``\  Always succeeds.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`vega12_thermal_get_temperature`:

vega12_thermal_get_temperature
==============================

.. c:function:: int vega12_thermal_get_temperature(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`vega12_thermal_get_temperature.description`:

Description
-----------

\ ``param``\     hwmgr The address of the hardware manager.

.. _`vega12_thermal_set_temperature_range`:

vega12_thermal_set_temperature_range
====================================

.. c:function:: int vega12_thermal_set_temperature_range(struct pp_hwmgr *hwmgr, struct PP_TemperatureRange *range)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param struct PP_TemperatureRange \*range:
        *undescribed*

.. _`vega12_thermal_set_temperature_range.description`:

Description
-----------

\ ``param``\     hwmgr The address of the hardware manager.
\ ``param``\     range Temperature range to be programmed for
high and low alert signals
\ ``exception``\  PP_Result_BadInput if the input data is not valid.

.. _`vega12_thermal_enable_alert`:

vega12_thermal_enable_alert
===========================

.. c:function:: int vega12_thermal_enable_alert(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`vega12_thermal_enable_alert.description`:

Description
-----------

\ ``param``\     hwmgr The address of the hardware manager.

.. _`vega12_thermal_disable_alert`:

vega12_thermal_disable_alert
============================

.. c:function:: int vega12_thermal_disable_alert(struct pp_hwmgr *hwmgr)

    \ ``param``\     hwmgr The address of the hardware manager.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`vega12_thermal_stop_thermal_controller`:

vega12_thermal_stop_thermal_controller
======================================

.. c:function:: int vega12_thermal_stop_thermal_controller(struct pp_hwmgr *hwmgr)

    Currently just disables alerts. \ ``param``\     hwmgr The address of the hardware manager.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`vega12_thermal_setup_fan_table`:

vega12_thermal_setup_fan_table
==============================

.. c:function:: int vega12_thermal_setup_fan_table(struct pp_hwmgr *hwmgr)

    \ ``param``\     hwmgr  the address of the powerplay hardware manager. \ ``param``\     pInput the pointer to input data \ ``param``\     pOutput the pointer to output data \ ``param``\     pStorage the pointer to temporary storage \ ``param``\     Result the last failure code \ ``return``\    result from set temperature range routine

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`vega12_thermal_start_smc_fan_control`:

vega12_thermal_start_smc_fan_control
====================================

.. c:function:: int vega12_thermal_start_smc_fan_control(struct pp_hwmgr *hwmgr)

    \ ``param``\     hwmgr  the address of the powerplay hardware manager. \ ``param``\     pInput the pointer to input data \ ``param``\     pOutput the pointer to output data \ ``param``\     pStorage the pointer to temporary storage \ ``param``\     Result the last failure code \ ``return``\    result from set temperature range routine

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. This file was automatic generated / don't edit.

