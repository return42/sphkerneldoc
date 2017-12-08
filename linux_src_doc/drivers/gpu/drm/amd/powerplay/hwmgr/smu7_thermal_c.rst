.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/smu7_thermal.c

.. _`smu7_fan_ctrl_set_static_mode`:

smu7_fan_ctrl_set_static_mode
=============================

.. c:function:: int smu7_fan_ctrl_set_static_mode(struct pp_hwmgr *hwmgr, uint32_t mode)

    @param    hwmgr  the address of the powerplay hardware manager. mode    the fan control mode, 0 default, 1 by percent, 5, by RPM \ ``exception``\  Should always succeed.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t mode:
        *undescribed*

.. _`smu7_fan_ctrl_set_default_mode`:

smu7_fan_ctrl_set_default_mode
==============================

.. c:function:: int smu7_fan_ctrl_set_default_mode(struct pp_hwmgr *hwmgr)

    @param    hwmgr  the address of the powerplay hardware manager. \ ``exception``\  Should always succeed.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_fan_ctrl_set_fan_speed_percent`:

smu7_fan_ctrl_set_fan_speed_percent
===================================

.. c:function:: int smu7_fan_ctrl_set_fan_speed_percent(struct pp_hwmgr *hwmgr, uint32_t speed)

    @param    hwmgr  the address of the powerplay hardware manager. \ ``param``\     speed is the percentage value (0% - 100%) to be set. \ ``exception``\  Fails is the 100% setting appears to be 0.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t speed:
        *undescribed*

.. _`smu7_fan_ctrl_reset_fan_speed_to_default`:

smu7_fan_ctrl_reset_fan_speed_to_default
========================================

.. c:function:: int smu7_fan_ctrl_reset_fan_speed_to_default(struct pp_hwmgr *hwmgr)

    @param    hwmgr  the address of the powerplay hardware manager. \ ``exception``\  Always succeeds.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_fan_ctrl_set_fan_speed_rpm`:

smu7_fan_ctrl_set_fan_speed_rpm
===============================

.. c:function:: int smu7_fan_ctrl_set_fan_speed_rpm(struct pp_hwmgr *hwmgr, uint32_t speed)

    @param    hwmgr  the address of the powerplay hardware manager. \ ``param``\     speed is the percentage value (min - max) to be set. \ ``exception``\  Fails is the speed not lie between min and max.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t speed:
        *undescribed*

.. _`smu7_thermal_get_temperature`:

smu7_thermal_get_temperature
============================

.. c:function:: int smu7_thermal_get_temperature(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_thermal_get_temperature.description`:

Description
-----------

@param    hwmgr The address of the hardware manager.

.. _`smu7_thermal_set_temperature_range`:

smu7_thermal_set_temperature_range
==================================

.. c:function:: int smu7_thermal_set_temperature_range(struct pp_hwmgr *hwmgr, uint32_t low_temp, uint32_t high_temp)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param uint32_t low_temp:
        *undescribed*

    :param uint32_t high_temp:
        *undescribed*

.. _`smu7_thermal_set_temperature_range.description`:

Description
-----------

@param    hwmgr The address of the hardware manager.
\ ``param``\     range Temperature range to be programmed for high and low alert signals
\ ``exception``\  PP_Result_BadInput if the input data is not valid.

.. _`smu7_thermal_initialize`:

smu7_thermal_initialize
=======================

.. c:function:: int smu7_thermal_initialize(struct pp_hwmgr *hwmgr)

    time setting registers

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_thermal_initialize.description`:

Description
-----------

@param    hwmgr The address of the hardware manager.

.. _`smu7_thermal_enable_alert`:

smu7_thermal_enable_alert
=========================

.. c:function:: void smu7_thermal_enable_alert(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_thermal_enable_alert.description`:

Description
-----------

@param    hwmgr The address of the hardware manager.

.. _`smu7_thermal_disable_alert`:

smu7_thermal_disable_alert
==========================

.. c:function:: int smu7_thermal_disable_alert(struct pp_hwmgr *hwmgr)

    @param    hwmgr The address of the hardware manager.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_thermal_stop_thermal_controller`:

smu7_thermal_stop_thermal_controller
====================================

.. c:function:: int smu7_thermal_stop_thermal_controller(struct pp_hwmgr *hwmgr)

    Currently just disables alerts. \ ``param``\     hwmgr The address of the hardware manager.

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`smu7_thermal_start_smc_fan_control`:

smu7_thermal_start_smc_fan_control
==================================

.. c:function:: int smu7_thermal_start_smc_fan_control(struct pp_hwmgr *hwmgr)

    @param    hwmgr  the address of the powerplay hardware manager. \ ``param``\     pInput the pointer to input data \ ``param``\     pOutput the pointer to output data \ ``param``\     pStorage the pointer to temporary storage \ ``param``\     Result the last failure code \ ``return``\    result from set temperature range routine

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. This file was automatic generated / don't edit.

