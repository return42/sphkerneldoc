.. -*- coding: utf-8; mode: rst -*-

===============
tonga_thermal.c
===============


.. _`tonga_fan_ctrl_get_fan_speed_info`:

tonga_fan_ctrl_get_fan_speed_info
=================================

.. c:function:: int tonga_fan_ctrl_get_fan_speed_info (struct pp_hwmgr *hwmgr, struct phm_fan_speed_info *fan_speed_info)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param struct phm_fan_speed_info \*fan_speed_info:

        *undescribed*



.. _`tonga_fan_ctrl_get_fan_speed_info.description`:

Description
-----------

``param``    hwmgr  the address of the powerplay hardware manager.
``param``    pSpeed is the address of the structure where the result is to be placed.
``exception`` Always succeeds except if we cannot zero out the output structure.



.. _`tonga_fan_ctrl_get_fan_speed_percent`:

tonga_fan_ctrl_get_fan_speed_percent
====================================

.. c:function:: int tonga_fan_ctrl_get_fan_speed_percent (struct pp_hwmgr *hwmgr, uint32_t *speed)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param uint32_t \*speed:

        *undescribed*



.. _`tonga_fan_ctrl_get_fan_speed_percent.description`:

Description
-----------

``param``    hwmgr  the address of the powerplay hardware manager.
``param``    pSpeed is the address of the structure where the result is to be placed.
``exception`` Fails is the 100% setting appears to be 0.



.. _`tonga_fan_ctrl_get_fan_speed_rpm`:

tonga_fan_ctrl_get_fan_speed_rpm
================================

.. c:function:: int tonga_fan_ctrl_get_fan_speed_rpm (struct pp_hwmgr *hwmgr, uint32_t *speed)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param uint32_t \*speed:

        *undescribed*



.. _`tonga_fan_ctrl_get_fan_speed_rpm.description`:

Description
-----------

``param``    hwmgr  the address of the powerplay hardware manager.
``param``    speed is the address of the structure where the result is to be placed.
``exception`` Returns not supported if no fan is found or if pulses per revolution are not set



.. _`tonga_fan_ctrl_set_static_mode`:

tonga_fan_ctrl_set_static_mode
==============================

.. c:function:: int tonga_fan_ctrl_set_static_mode (struct pp_hwmgr *hwmgr, uint32_t mode)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param uint32_t mode:

        *undescribed*



.. _`tonga_fan_ctrl_set_static_mode.description`:

Description
-----------

``param``    hwmgr  the address of the powerplay hardware manager.
mode    the fan control mode, 0 default, 1 by percent, 5, by RPM

``exception`` Should always succeed.



.. _`tonga_fan_ctrl_set_default_mode`:

tonga_fan_ctrl_set_default_mode
===============================

.. c:function:: int tonga_fan_ctrl_set_default_mode (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`tonga_fan_ctrl_set_default_mode.description`:

Description
-----------

``param``    hwmgr  the address of the powerplay hardware manager.
``exception`` Should always succeed.



.. _`tonga_fan_ctrl_set_fan_speed_percent`:

tonga_fan_ctrl_set_fan_speed_percent
====================================

.. c:function:: int tonga_fan_ctrl_set_fan_speed_percent (struct pp_hwmgr *hwmgr, uint32_t speed)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param uint32_t speed:

        *undescribed*



.. _`tonga_fan_ctrl_set_fan_speed_percent.description`:

Description
-----------

``param``    hwmgr  the address of the powerplay hardware manager.
``param``    speed is the percentage value (0% - 100%) to be set.
``exception`` Fails is the 100% setting appears to be 0.



.. _`tonga_fan_ctrl_reset_fan_speed_to_default`:

tonga_fan_ctrl_reset_fan_speed_to_default
=========================================

.. c:function:: int tonga_fan_ctrl_reset_fan_speed_to_default (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`tonga_fan_ctrl_reset_fan_speed_to_default.description`:

Description
-----------

``param``    hwmgr  the address of the powerplay hardware manager.
``exception`` Always succeeds.



.. _`tonga_fan_ctrl_set_fan_speed_rpm`:

tonga_fan_ctrl_set_fan_speed_rpm
================================

.. c:function:: int tonga_fan_ctrl_set_fan_speed_rpm (struct pp_hwmgr *hwmgr, uint32_t speed)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param uint32_t speed:

        *undescribed*



.. _`tonga_fan_ctrl_set_fan_speed_rpm.description`:

Description
-----------

``param``    hwmgr  the address of the powerplay hardware manager.
``param``    speed is the percentage value (min - max) to be set.
``exception`` Fails is the speed not lie between min and max.



.. _`tonga_thermal_get_temperature`:

tonga_thermal_get_temperature
=============================

.. c:function:: int tonga_thermal_get_temperature (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`tonga_thermal_get_temperature.description`:

Description
-----------


``param``    hwmgr The address of the hardware manager.



.. _`tonga_thermal_set_temperature_range`:

tonga_thermal_set_temperature_range
===================================

.. c:function:: int tonga_thermal_set_temperature_range (struct pp_hwmgr *hwmgr, uint32_t low_temp, uint32_t high_temp)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param uint32_t low_temp:

        *undescribed*

    :param uint32_t high_temp:

        *undescribed*



.. _`tonga_thermal_set_temperature_range.description`:

Description
-----------


``param``    hwmgr The address of the hardware manager.
``param``    range Temperature range to be programmed for high and low alert signals
``exception`` PP_Result_BadInput if the input data is not valid.



.. _`tonga_thermal_initialize`:

tonga_thermal_initialize
========================

.. c:function:: int tonga_thermal_initialize (struct pp_hwmgr *hwmgr)

    time setting registers

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`tonga_thermal_initialize.description`:

Description
-----------


``param``    hwmgr The address of the hardware manager.



.. _`tonga_thermal_enable_alert`:

tonga_thermal_enable_alert
==========================

.. c:function:: int tonga_thermal_enable_alert (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`tonga_thermal_enable_alert.description`:

Description
-----------


``param``    hwmgr The address of the hardware manager.



.. _`tonga_thermal_disable_alert`:

tonga_thermal_disable_alert
===========================

.. c:function:: int tonga_thermal_disable_alert (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`tonga_thermal_disable_alert.description`:

Description
-----------

``param``    hwmgr The address of the hardware manager.



.. _`tonga_thermal_stop_thermal_controller`:

tonga_thermal_stop_thermal_controller
=====================================

.. c:function:: int tonga_thermal_stop_thermal_controller (struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*



.. _`tonga_thermal_stop_thermal_controller.description`:

Description
-----------

Currently just disables alerts.
``param``    hwmgr The address of the hardware manager.



.. _`tf_tonga_thermal_setup_fan_table`:

tf_tonga_thermal_setup_fan_table
================================

.. c:function:: int tf_tonga_thermal_setup_fan_table (struct pp_hwmgr *hwmgr, void *input, void *output, void *storage, int result)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param void \*input:

        *undescribed*

    :param void \*output:

        *undescribed*

    :param void \*storage:

        *undescribed*

    :param int result:

        *undescribed*



.. _`tf_tonga_thermal_setup_fan_table.description`:

Description
-----------

``param``    hwmgr  the address of the powerplay hardware manager.
``param``    pInput the pointer to input data
``param``    pOutput the pointer to output data
``param``    pStorage the pointer to temporary storage
``param``    Result the last failure code
``return``   result from set temperature range routine



.. _`tf_tonga_thermal_start_smc_fan_control`:

tf_tonga_thermal_start_smc_fan_control
======================================

.. c:function:: int tf_tonga_thermal_start_smc_fan_control (struct pp_hwmgr *hwmgr, void *input, void *output, void *storage, int result)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param void \*input:

        *undescribed*

    :param void \*output:

        *undescribed*

    :param void \*storage:

        *undescribed*

    :param int result:

        *undescribed*



.. _`tf_tonga_thermal_start_smc_fan_control.description`:

Description
-----------

``param``    hwmgr  the address of the powerplay hardware manager.
``param``    pInput the pointer to input data
``param``    pOutput the pointer to output data
``param``    pStorage the pointer to temporary storage
``param``    Result the last failure code
``return``   result from set temperature range routine



.. _`tf_tonga_thermal_set_temperature_range`:

tf_tonga_thermal_set_temperature_range
======================================

.. c:function:: int tf_tonga_thermal_set_temperature_range (struct pp_hwmgr *hwmgr, void *input, void *output, void *storage, int result)

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param void \*input:

        *undescribed*

    :param void \*output:

        *undescribed*

    :param void \*storage:

        *undescribed*

    :param int result:

        *undescribed*



.. _`tf_tonga_thermal_set_temperature_range.description`:

Description
-----------

``param``    hwmgr  the address of the powerplay hardware manager.
``param``    pInput the pointer to input data
``param``    pOutput the pointer to output data
``param``    pStorage the pointer to temporary storage
``param``    Result the last failure code
``return``   result from set temperature range routine



.. _`tf_tonga_thermal_initialize`:

tf_tonga_thermal_initialize
===========================

.. c:function:: int tf_tonga_thermal_initialize (struct pp_hwmgr *hwmgr, void *input, void *output, void *storage, int result)

    time setting registers @param hwmgr the address of the powerplay hardware manager. @param pInput the pointer to input data @param pOutput the pointer to output data @param pStorage the pointer to temporary storage @param Result the last failure code @return result from initialize thermal controller routine

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param void \*input:

        *undescribed*

    :param void \*output:

        *undescribed*

    :param void \*storage:

        *undescribed*

    :param int result:

        *undescribed*



.. _`tf_tonga_thermal_enable_alert`:

tf_tonga_thermal_enable_alert
=============================

.. c:function:: int tf_tonga_thermal_enable_alert (struct pp_hwmgr *hwmgr, void *input, void *output, void *storage, int result)

     @param hwmgr the address of the powerplay hardware manager. @param pInput the pointer to input data @param pOutput the pointer to output data @param pStorage the pointer to temporary storage @param Result the last failure code @return result from enable alert routine

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param void \*input:

        *undescribed*

    :param void \*output:

        *undescribed*

    :param void \*storage:

        *undescribed*

    :param int result:

        *undescribed*



.. _`tf_tonga_thermal_disable_alert`:

tf_tonga_thermal_disable_alert
==============================

.. c:function:: int tf_tonga_thermal_disable_alert (struct pp_hwmgr *hwmgr, void *input, void *output, void *storage, int result)

     @param hwmgr the address of the powerplay hardware manager. @param pInput the pointer to input data @param pOutput the pointer to output data @param pStorage the pointer to temporary storage @param Result the last failure code @return result from disable alert routine

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

    :param void \*input:

        *undescribed*

    :param void \*output:

        *undescribed*

    :param void \*storage:

        *undescribed*

    :param int result:

        *undescribed*



.. _`pp_tonga_thermal_initialize`:

pp_tonga_thermal_initialize
===========================

.. c:function:: int pp_tonga_thermal_initialize (struct pp_hwmgr *hwmgr)

     @param hwmgr The address of the hardware manager. @exception Any error code from the low-level communication.

    :param struct pp_hwmgr \*hwmgr:

        *undescribed*

