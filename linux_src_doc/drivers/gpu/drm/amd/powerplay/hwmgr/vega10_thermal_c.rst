.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/vega10_thermal.c

.. _`vega10_fan_ctrl_set_static_mode`:

vega10_fan_ctrl_set_static_mode
===============================

.. c:function:: int vega10_fan_ctrl_set_static_mode(struct pp_hwmgr *hwmgr, uint32_t mode)

    so that the user can decide what speed to use. \ ``param``\     hwmgr  the address of the powerplay hardware manager. mode the fan control mode, 0 default, 1 by percent, 5, by RPM \ ``exception``\  Should always succeed.

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param mode:
        *undescribed*
    :type mode: uint32_t

.. _`vega10_fan_ctrl_set_default_mode`:

vega10_fan_ctrl_set_default_mode
================================

.. c:function:: int vega10_fan_ctrl_set_default_mode(struct pp_hwmgr *hwmgr)

    \ ``param``\     hwmgr  the address of the powerplay hardware manager. \ ``exception``\  Should always succeed.

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_fan_ctrl_set_fan_speed_percent`:

vega10_fan_ctrl_set_fan_speed_percent
=====================================

.. c:function:: int vega10_fan_ctrl_set_fan_speed_percent(struct pp_hwmgr *hwmgr, uint32_t speed)

    \ ``param``\     hwmgr  the address of the powerplay hardware manager. \ ``param``\     speed is the percentage value (0% - 100%) to be set. \ ``exception``\  Fails is the 100% setting appears to be 0.

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param speed:
        *undescribed*
    :type speed: uint32_t

.. _`vega10_fan_ctrl_reset_fan_speed_to_default`:

vega10_fan_ctrl_reset_fan_speed_to_default
==========================================

.. c:function:: int vega10_fan_ctrl_reset_fan_speed_to_default(struct pp_hwmgr *hwmgr)

    \ ``param``\     hwmgr  the address of the powerplay hardware manager. \ ``exception``\  Always succeeds.

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_fan_ctrl_set_fan_speed_rpm`:

vega10_fan_ctrl_set_fan_speed_rpm
=================================

.. c:function:: int vega10_fan_ctrl_set_fan_speed_rpm(struct pp_hwmgr *hwmgr, uint32_t speed)

    \ ``param``\     hwmgr  the address of the powerplay hardware manager. \ ``param``\     speed is the percentage value (min - max) to be set. \ ``exception``\  Fails is the speed not lie between min and max.

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param speed:
        *undescribed*
    :type speed: uint32_t

.. _`vega10_thermal_get_temperature`:

vega10_thermal_get_temperature
==============================

.. c:function:: int vega10_thermal_get_temperature(struct pp_hwmgr *hwmgr)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_thermal_get_temperature.description`:

Description
-----------

\ ``param``\     hwmgr The address of the hardware manager.

.. _`vega10_thermal_set_temperature_range`:

vega10_thermal_set_temperature_range
====================================

.. c:function:: int vega10_thermal_set_temperature_range(struct pp_hwmgr *hwmgr, struct PP_TemperatureRange *range)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param range:
        *undescribed*
    :type range: struct PP_TemperatureRange \*

.. _`vega10_thermal_set_temperature_range.description`:

Description
-----------

\ ``param``\     hwmgr The address of the hardware manager.
\ ``param``\     range Temperature range to be programmed for
high and low alert signals
\ ``exception``\  PP_Result_BadInput if the input data is not valid.

.. _`vega10_thermal_initialize`:

vega10_thermal_initialize
=========================

.. c:function:: int vega10_thermal_initialize(struct pp_hwmgr *hwmgr)

    time setting registers

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_thermal_initialize.description`:

Description
-----------

\ ``param``\     hwmgr The address of the hardware manager.

.. _`vega10_thermal_enable_alert`:

vega10_thermal_enable_alert
===========================

.. c:function:: int vega10_thermal_enable_alert(struct pp_hwmgr *hwmgr)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_thermal_enable_alert.description`:

Description
-----------

\ ``param``\     hwmgr The address of the hardware manager.

.. _`vega10_thermal_disable_alert`:

vega10_thermal_disable_alert
============================

.. c:function:: int vega10_thermal_disable_alert(struct pp_hwmgr *hwmgr)

    \ ``param``\     hwmgr The address of the hardware manager.

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_thermal_stop_thermal_controller`:

vega10_thermal_stop_thermal_controller
======================================

.. c:function:: int vega10_thermal_stop_thermal_controller(struct pp_hwmgr *hwmgr)

    Currently just disables alerts. \ ``param``\     hwmgr The address of the hardware manager.

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_thermal_setup_fan_table`:

vega10_thermal_setup_fan_table
==============================

.. c:function:: int vega10_thermal_setup_fan_table(struct pp_hwmgr *hwmgr)

    \ ``param``\     hwmgr  the address of the powerplay hardware manager. \ ``param``\     pInput the pointer to input data \ ``param``\     pOutput the pointer to output data \ ``param``\     pStorage the pointer to temporary storage \ ``param``\     Result the last failure code \ ``return``\    result from set temperature range routine

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`vega10_thermal_start_smc_fan_control`:

vega10_thermal_start_smc_fan_control
====================================

.. c:function:: int vega10_thermal_start_smc_fan_control(struct pp_hwmgr *hwmgr)

    \ ``param``\     hwmgr  the address of the powerplay hardware manager. \ ``param``\     pInput the pointer to input data \ ``param``\     pOutput the pointer to output data \ ``param``\     pStorage the pointer to temporary storage \ ``param``\     Result the last failure code \ ``return``\    result from set temperature range routine

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. This file was automatic generated / don't edit.

