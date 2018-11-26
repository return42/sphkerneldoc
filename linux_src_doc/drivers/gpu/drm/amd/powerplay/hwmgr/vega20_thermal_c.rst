.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/vega20_thermal.c

.. _`vega20_thermal_get_temperature`:

vega20_thermal_get_temperature
==============================

.. c:function:: int vega20_thermal_get_temperature(struct pp_hwmgr *hwmgr)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega20_thermal_get_temperature.description`:

Description
-----------

\ ``param``\     hwmgr The address of the hardware manager.

.. _`vega20_thermal_set_temperature_range`:

vega20_thermal_set_temperature_range
====================================

.. c:function:: int vega20_thermal_set_temperature_range(struct pp_hwmgr *hwmgr, struct PP_TemperatureRange *range)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param range:
        *undescribed*
    :type range: struct PP_TemperatureRange \*

.. _`vega20_thermal_set_temperature_range.description`:

Description
-----------

\ ``param``\     hwmgr The address of the hardware manager.
\ ``param``\     range Temperature range to be programmed for
high and low alert signals
\ ``exception``\  PP_Result_BadInput if the input data is not valid.

.. _`vega20_thermal_enable_alert`:

vega20_thermal_enable_alert
===========================

.. c:function:: int vega20_thermal_enable_alert(struct pp_hwmgr *hwmgr)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega20_thermal_enable_alert.description`:

Description
-----------

\ ``param``\     hwmgr The address of the hardware manager.

.. _`vega20_thermal_disable_alert`:

vega20_thermal_disable_alert
============================

.. c:function:: int vega20_thermal_disable_alert(struct pp_hwmgr *hwmgr)

    \ ``param``\     hwmgr The address of the hardware manager.

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega20_thermal_stop_thermal_controller`:

vega20_thermal_stop_thermal_controller
======================================

.. c:function:: int vega20_thermal_stop_thermal_controller(struct pp_hwmgr *hwmgr)

    Currently just disables alerts. \ ``param``\     hwmgr The address of the hardware manager.

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega20_thermal_setup_fan_table`:

vega20_thermal_setup_fan_table
==============================

.. c:function:: int vega20_thermal_setup_fan_table(struct pp_hwmgr *hwmgr)

    \ ``param``\     hwmgr  the address of the powerplay hardware manager. \ ``param``\     pInput the pointer to input data \ ``param``\     pOutput the pointer to output data \ ``param``\     pStorage the pointer to temporary storage \ ``param``\     Result the last failure code \ ``return``\    result from set temperature range routine

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. This file was automatic generated / don't edit.

