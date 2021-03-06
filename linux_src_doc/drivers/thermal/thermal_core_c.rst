.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/thermal_core.c

.. _`bind_previous_governor`:

bind_previous_governor
======================

.. c:function:: void bind_previous_governor(struct thermal_zone_device *tz, const char *failed_gov_name)

    bind the previous governor of the thermal zone

    :param tz:
        a valid pointer to a struct thermal_zone_device
    :type tz: struct thermal_zone_device \*

    :param failed_gov_name:
        the name of the governor that failed to register
    :type failed_gov_name: const char \*

.. _`bind_previous_governor.description`:

Description
-----------

Register the previous governor of the thermal zone after a new
governor has failed to be bound.

.. _`thermal_set_governor`:

thermal_set_governor
====================

.. c:function:: int thermal_set_governor(struct thermal_zone_device *tz, struct thermal_governor *new_gov)

    Switch to another governor

    :param tz:
        a valid pointer to a struct thermal_zone_device
    :type tz: struct thermal_zone_device \*

    :param new_gov:
        pointer to the new governor
    :type new_gov: struct thermal_governor \*

.. _`thermal_set_governor.description`:

Description
-----------

Change the governor of thermal zone \ ``tz``\ .

.. _`thermal_set_governor.return`:

Return
------

0 on success, an error if the new governor's \ :c:func:`bind_to_tz`\  failed.

.. _`thermal_emergency_poweroff_func`:

thermal_emergency_poweroff_func
===============================

.. c:function:: void thermal_emergency_poweroff_func(struct work_struct *work)

    emergency poweroff work after a known delay

    :param work:
        work_struct associated with the emergency poweroff function
    :type work: struct work_struct \*

.. _`thermal_emergency_poweroff_func.description`:

Description
-----------

This function is called in very critical situations to force
a kernel poweroff after a configurable timeout value.

.. _`thermal_emergency_poweroff`:

thermal_emergency_poweroff
==========================

.. c:function:: void thermal_emergency_poweroff( void)

    Trigger an emergency system poweroff

    :param void:
        no arguments
    :type void: 

.. _`thermal_emergency_poweroff.description`:

Description
-----------

This may be called from any critical situation to trigger a system shutdown
after a known period of time. By default this is not scheduled.

.. _`thermal_notify_framework`:

thermal_notify_framework
========================

.. c:function:: void thermal_notify_framework(struct thermal_zone_device *tz, int trip)

    Sensor drivers use this API to notify framework

    :param tz:
        thermal zone device
    :type tz: struct thermal_zone_device \*

    :param trip:
        indicates which trip point has been crossed
    :type trip: int

.. _`thermal_notify_framework.description`:

Description
-----------

This function handles the trip events from sensor drivers. It starts
throttling the cooling devices according to the policy configured.
For CRITICAL and HOT trip points, this notifies the respective drivers,
and does actual throttling for other trip points i.e ACTIVE and PASSIVE.
The throttling policy is based on the configured platform data; if no
platform data is provided, this uses the step_wise throttling policy.

.. _`power_actor_get_max_power`:

power_actor_get_max_power
=========================

.. c:function:: int power_actor_get_max_power(struct thermal_cooling_device *cdev, struct thermal_zone_device *tz, u32 *max_power)

    get the maximum power that a cdev can consume

    :param cdev:
        pointer to \ :c:type:`struct thermal_cooling_device <thermal_cooling_device>`\ 
    :type cdev: struct thermal_cooling_device \*

    :param tz:
        a valid thermal zone device pointer
    :type tz: struct thermal_zone_device \*

    :param max_power:
        pointer in which to store the maximum power
    :type max_power: u32 \*

.. _`power_actor_get_max_power.description`:

Description
-----------

Calculate the maximum power consumption in milliwats that the
cooling device can currently consume and store it in \ ``max_power``\ .

.. _`power_actor_get_max_power.return`:

Return
------

0 on success, -EINVAL if \ ``cdev``\  doesn't support the
power_actor API or -E\* on other error.

.. _`power_actor_get_min_power`:

power_actor_get_min_power
=========================

.. c:function:: int power_actor_get_min_power(struct thermal_cooling_device *cdev, struct thermal_zone_device *tz, u32 *min_power)

    get the mainimum power that a cdev can consume

    :param cdev:
        pointer to \ :c:type:`struct thermal_cooling_device <thermal_cooling_device>`\ 
    :type cdev: struct thermal_cooling_device \*

    :param tz:
        a valid thermal zone device pointer
    :type tz: struct thermal_zone_device \*

    :param min_power:
        pointer in which to store the minimum power
    :type min_power: u32 \*

.. _`power_actor_get_min_power.description`:

Description
-----------

Calculate the minimum power consumption in milliwatts that the
cooling device can currently consume and store it in \ ``min_power``\ .

.. _`power_actor_get_min_power.return`:

Return
------

0 on success, -EINVAL if \ ``cdev``\  doesn't support the
power_actor API or -E\* on other error.

.. _`power_actor_set_power`:

power_actor_set_power
=====================

.. c:function:: int power_actor_set_power(struct thermal_cooling_device *cdev, struct thermal_instance *instance, u32 power)

    limit the maximum power a cooling device consumes

    :param cdev:
        pointer to \ :c:type:`struct thermal_cooling_device <thermal_cooling_device>`\ 
    :type cdev: struct thermal_cooling_device \*

    :param instance:
        thermal instance to update
    :type instance: struct thermal_instance \*

    :param power:
        the power in milliwatts
    :type power: u32

.. _`power_actor_set_power.description`:

Description
-----------

Set the cooling device to consume at most \ ``power``\  milliwatts. The limit is
expected to be a cap at the maximum power consumption.

.. _`power_actor_set_power.return`:

Return
------

0 on success, -EINVAL if the cooling device does not
implement the power actor API or -E\* for other failures.

.. _`thermal_zone_bind_cooling_device`:

thermal_zone_bind_cooling_device
================================

.. c:function:: int thermal_zone_bind_cooling_device(struct thermal_zone_device *tz, int trip, struct thermal_cooling_device *cdev, unsigned long upper, unsigned long lower, unsigned int weight)

    bind a cooling device to a thermal zone

    :param tz:
        pointer to struct thermal_zone_device
    :type tz: struct thermal_zone_device \*

    :param trip:
        indicates which trip point the cooling devices is
        associated with in this thermal zone.
    :type trip: int

    :param cdev:
        pointer to struct thermal_cooling_device
    :type cdev: struct thermal_cooling_device \*

    :param upper:
        the Maximum cooling state for this trip point.
        THERMAL_NO_LIMIT means no upper limit,
        and the cooling device can be in max_state.
    :type upper: unsigned long

    :param lower:
        the Minimum cooling state can be used for this trip point.
        THERMAL_NO_LIMIT means no lower limit,
        and the cooling device can be in cooling state 0.
    :type lower: unsigned long

    :param weight:
        The weight of the cooling device to be bound to the
        thermal zone. Use THERMAL_WEIGHT_DEFAULT for the
        default value
    :type weight: unsigned int

.. _`thermal_zone_bind_cooling_device.description`:

Description
-----------

This interface function bind a thermal cooling device to the certain trip
point of a thermal zone device.
This function is usually called in the thermal zone device .bind callback.

.. _`thermal_zone_bind_cooling_device.return`:

Return
------

0 on success, the proper error value otherwise.

.. _`thermal_zone_unbind_cooling_device`:

thermal_zone_unbind_cooling_device
==================================

.. c:function:: int thermal_zone_unbind_cooling_device(struct thermal_zone_device *tz, int trip, struct thermal_cooling_device *cdev)

    unbind a cooling device from a thermal zone.

    :param tz:
        pointer to a struct thermal_zone_device.
    :type tz: struct thermal_zone_device \*

    :param trip:
        indicates which trip point the cooling devices is
        associated with in this thermal zone.
    :type trip: int

    :param cdev:
        pointer to a struct thermal_cooling_device.
    :type cdev: struct thermal_cooling_device \*

.. _`thermal_zone_unbind_cooling_device.description`:

Description
-----------

This interface function unbind a thermal cooling device from the certain
trip point of a thermal zone device.
This function is usually called in the thermal zone device .unbind callback.

.. _`thermal_zone_unbind_cooling_device.return`:

Return
------

0 on success, the proper error value otherwise.

.. _`__thermal_cooling_device_register`:

\__thermal_cooling_device_register
==================================

.. c:function:: struct thermal_cooling_device *__thermal_cooling_device_register(struct device_node *np, char *type, void *devdata, const struct thermal_cooling_device_ops *ops)

    register a new thermal cooling device

    :param np:
        a pointer to a device tree node.
    :type np: struct device_node \*

    :param type:
        the thermal cooling device type.
    :type type: char \*

    :param devdata:
        device private data.
    :type devdata: void \*

    :param ops:
        standard thermal cooling devices callbacks.
    :type ops: const struct thermal_cooling_device_ops \*

.. _`__thermal_cooling_device_register.description`:

Description
-----------

This interface function adds a new thermal cooling device (fan/processor/...)
to /sys/class/thermal/ folder as cooling_device[0-\*]. It tries to bind itself
to all the thermal zone devices registered at the same time.
It also gives the opportunity to link the cooling device to a device tree
node, so that it can be bound to a thermal zone created out of device tree.

.. _`__thermal_cooling_device_register.return`:

Return
------

a pointer to the created struct thermal_cooling_device or an
ERR_PTR. Caller must check return value with IS_ERR\*() helpers.

.. _`thermal_cooling_device_register`:

thermal_cooling_device_register
===============================

.. c:function:: struct thermal_cooling_device *thermal_cooling_device_register(char *type, void *devdata, const struct thermal_cooling_device_ops *ops)

    register a new thermal cooling device

    :param type:
        the thermal cooling device type.
    :type type: char \*

    :param devdata:
        device private data.
    :type devdata: void \*

    :param ops:
        standard thermal cooling devices callbacks.
    :type ops: const struct thermal_cooling_device_ops \*

.. _`thermal_cooling_device_register.description`:

Description
-----------

This interface function adds a new thermal cooling device (fan/processor/...)
to /sys/class/thermal/ folder as cooling_device[0-\*]. It tries to bind itself
to all the thermal zone devices registered at the same time.

.. _`thermal_cooling_device_register.return`:

Return
------

a pointer to the created struct thermal_cooling_device or an
ERR_PTR. Caller must check return value with IS_ERR\*() helpers.

.. _`thermal_of_cooling_device_register`:

thermal_of_cooling_device_register
==================================

.. c:function:: struct thermal_cooling_device *thermal_of_cooling_device_register(struct device_node *np, char *type, void *devdata, const struct thermal_cooling_device_ops *ops)

    register an OF thermal cooling device

    :param np:
        a pointer to a device tree node.
    :type np: struct device_node \*

    :param type:
        the thermal cooling device type.
    :type type: char \*

    :param devdata:
        device private data.
    :type devdata: void \*

    :param ops:
        standard thermal cooling devices callbacks.
    :type ops: const struct thermal_cooling_device_ops \*

.. _`thermal_of_cooling_device_register.description`:

Description
-----------

This function will register a cooling device with device tree node reference.
This interface function adds a new thermal cooling device (fan/processor/...)
to /sys/class/thermal/ folder as cooling_device[0-\*]. It tries to bind itself
to all the thermal zone devices registered at the same time.

.. _`thermal_of_cooling_device_register.return`:

Return
------

a pointer to the created struct thermal_cooling_device or an
ERR_PTR. Caller must check return value with IS_ERR\*() helpers.

.. _`thermal_cooling_device_unregister`:

thermal_cooling_device_unregister
=================================

.. c:function:: void thermal_cooling_device_unregister(struct thermal_cooling_device *cdev)

    removes a thermal cooling device

    :param cdev:
        the thermal cooling device to remove.
    :type cdev: struct thermal_cooling_device \*

.. _`thermal_cooling_device_unregister.description`:

Description
-----------

\ :c:func:`thermal_cooling_device_unregister`\  must be called when a registered
thermal cooling device is no longer needed.

.. _`thermal_zone_device_register`:

thermal_zone_device_register
============================

.. c:function:: struct thermal_zone_device *thermal_zone_device_register(const char *type, int trips, int mask, void *devdata, struct thermal_zone_device_ops *ops, struct thermal_zone_params *tzp, int passive_delay, int polling_delay)

    register a new thermal zone device

    :param type:
        the thermal zone device type
    :type type: const char \*

    :param trips:
        the number of trip points the thermal zone support
    :type trips: int

    :param mask:
        a bit string indicating the writeablility of trip points
    :type mask: int

    :param devdata:
        private device data
    :type devdata: void \*

    :param ops:
        standard thermal zone device callbacks
    :type ops: struct thermal_zone_device_ops \*

    :param tzp:
        thermal zone platform parameters
    :type tzp: struct thermal_zone_params \*

    :param passive_delay:
        number of milliseconds to wait between polls when
        performing passive cooling
    :type passive_delay: int

    :param polling_delay:
        number of milliseconds to wait between polls when checking
        whether trip points have been crossed (0 for interrupt
        driven systems)
    :type polling_delay: int

.. _`thermal_zone_device_register.description`:

Description
-----------

This interface function adds a new thermal zone device (sensor) to
/sys/class/thermal folder as thermal_zone[0-\*]. It tries to bind all the
thermal cooling devices registered at the same time.
\ :c:func:`thermal_zone_device_unregister`\  must be called when the device is no
longer needed. The passive cooling depends on the .get_trend() return value.

.. _`thermal_zone_device_register.return`:

Return
------

a pointer to the created struct thermal_zone_device or an
in case of error, an ERR_PTR. Caller must check return value with
IS_ERR\*() helpers.

.. _`thermal_zone_device_unregister`:

thermal_zone_device_unregister
==============================

.. c:function:: void thermal_zone_device_unregister(struct thermal_zone_device *tz)

    removes the registered thermal zone device

    :param tz:
        the thermal zone device to remove
    :type tz: struct thermal_zone_device \*

.. _`thermal_zone_get_zone_by_name`:

thermal_zone_get_zone_by_name
=============================

.. c:function:: struct thermal_zone_device *thermal_zone_get_zone_by_name(const char *name)

    search for a zone and returns its ref

    :param name:
        thermal zone name to fetch the temperature
    :type name: const char \*

.. _`thermal_zone_get_zone_by_name.description`:

Description
-----------

When only one zone is found with the passed name, returns a reference to it.

.. _`thermal_zone_get_zone_by_name.return`:

Return
------

On success returns a reference to an unique thermal zone with
matching name equals to \ ``name``\ , an ERR_PTR otherwise (-EINVAL for invalid
paramenters, -ENODEV for not found and -EEXIST for multiple matches).

.. This file was automatic generated / don't edit.

