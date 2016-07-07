.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/thermal_core.c

.. _`bind_previous_governor`:

bind_previous_governor
======================

.. c:function:: void bind_previous_governor(struct thermal_zone_device *tz, const char *failed_gov_name)

    bind the previous governor of the thermal zone

    :param struct thermal_zone_device \*tz:
        a valid pointer to a struct thermal_zone_device

    :param const char \*failed_gov_name:
        the name of the governor that failed to register

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

    :param struct thermal_zone_device \*tz:
        a valid pointer to a struct thermal_zone_device

    :param struct thermal_governor \*new_gov:
        pointer to the new governor

.. _`thermal_set_governor.description`:

Description
-----------

Change the governor of thermal zone \ ``tz``\ .

.. _`thermal_set_governor.return`:

Return
------

0 on success, an error if the new governor's \ :c:func:`bind_to_tz`\  failed.

.. _`thermal_zone_get_temp`:

thermal_zone_get_temp
=====================

.. c:function:: int thermal_zone_get_temp(struct thermal_zone_device *tz, int *temp)

    returns the temperature of a thermal zone

    :param struct thermal_zone_device \*tz:
        a valid pointer to a struct thermal_zone_device

    :param int \*temp:
        a valid pointer to where to store the resulting temperature.

.. _`thermal_zone_get_temp.description`:

Description
-----------

When a valid thermal zone reference is passed, it will fetch its
temperature and fill \ ``temp``\ .

.. _`thermal_zone_get_temp.return`:

Return
------

On success returns 0, an error code otherwise

.. _`power_actor_get_max_power`:

power_actor_get_max_power
=========================

.. c:function:: int power_actor_get_max_power(struct thermal_cooling_device *cdev, struct thermal_zone_device *tz, u32 *max_power)

    get the maximum power that a cdev can consume

    :param struct thermal_cooling_device \*cdev:
        pointer to \ :c:type:`struct thermal_cooling_device <thermal_cooling_device>`

    :param struct thermal_zone_device \*tz:
        a valid thermal zone device pointer

    :param u32 \*max_power:
        pointer in which to store the maximum power

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

    :param struct thermal_cooling_device \*cdev:
        pointer to \ :c:type:`struct thermal_cooling_device <thermal_cooling_device>`

    :param struct thermal_zone_device \*tz:
        a valid thermal zone device pointer

    :param u32 \*min_power:
        pointer in which to store the minimum power

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

    limit the maximum power that a cooling device can consume

    :param struct thermal_cooling_device \*cdev:
        pointer to \ :c:type:`struct thermal_cooling_device <thermal_cooling_device>`

    :param struct thermal_instance \*instance:
        thermal instance to update

    :param u32 power:
        the power in milliwatts

.. _`power_actor_set_power.description`:

Description
-----------

Set the cooling device to consume at most \ ``power``\  milliwatts.

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

    :param struct thermal_zone_device \*tz:
        pointer to struct thermal_zone_device

    :param int trip:
        indicates which trip point the cooling devices is
        associated with in this thermal zone.

    :param struct thermal_cooling_device \*cdev:
        pointer to struct thermal_cooling_device

    :param unsigned long upper:
        the Maximum cooling state for this trip point.
        THERMAL_NO_LIMIT means no upper limit,
        and the cooling device can be in max_state.

    :param unsigned long lower:
        the Minimum cooling state can be used for this trip point.
        THERMAL_NO_LIMIT means no lower limit,
        and the cooling device can be in cooling state 0.

    :param unsigned int weight:
        The weight of the cooling device to be bound to the
        thermal zone. Use THERMAL_WEIGHT_DEFAULT for the
        default value

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

    :param struct thermal_zone_device \*tz:
        pointer to a struct thermal_zone_device.

    :param int trip:
        indicates which trip point the cooling devices is
        associated with in this thermal zone.

    :param struct thermal_cooling_device \*cdev:
        pointer to a struct thermal_cooling_device.

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

__thermal_cooling_device_register
=================================

.. c:function:: struct thermal_cooling_device *__thermal_cooling_device_register(struct device_node *np, char *type, void *devdata, const struct thermal_cooling_device_ops *ops)

    register a new thermal cooling device

    :param struct device_node \*np:
        a pointer to a device tree node.

    :param char \*type:
        the thermal cooling device type.

    :param void \*devdata:
        device private data.

    :param const struct thermal_cooling_device_ops \*ops:
        standard thermal cooling devices callbacks.

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

    :param char \*type:
        the thermal cooling device type.

    :param void \*devdata:
        device private data.

    :param const struct thermal_cooling_device_ops \*ops:
        standard thermal cooling devices callbacks.

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

    :param struct device_node \*np:
        a pointer to a device tree node.

    :param char \*type:
        the thermal cooling device type.

    :param void \*devdata:
        device private data.

    :param const struct thermal_cooling_device_ops \*ops:
        standard thermal cooling devices callbacks.

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

    removes the registered thermal cooling device

    :param struct thermal_cooling_device \*cdev:
        the thermal cooling device to remove.

.. _`thermal_cooling_device_unregister.description`:

Description
-----------

\ :c:func:`thermal_cooling_device_unregister`\  must be called when the device is no
longer needed.

.. _`thermal_notify_framework`:

thermal_notify_framework
========================

.. c:function:: void thermal_notify_framework(struct thermal_zone_device *tz, int trip)

    Sensor drivers use this API to notify framework

    :param struct thermal_zone_device \*tz:
        thermal zone device

    :param int trip:
        indicates which trip point has been crossed

.. _`thermal_notify_framework.description`:

Description
-----------

This function handles the trip events from sensor drivers. It starts
throttling the cooling devices according to the policy configured.
For CRITICAL and HOT trip points, this notifies the respective drivers,
and does actual throttling for other trip points i.e ACTIVE and PASSIVE.
The throttling policy is based on the configured platform data; if no
platform data is provided, this uses the step_wise throttling policy.

.. _`create_trip_attrs`:

create_trip_attrs
=================

.. c:function:: int create_trip_attrs(struct thermal_zone_device *tz, int mask)

    create attributes for trip points

    :param struct thermal_zone_device \*tz:
        the thermal zone device

    :param int mask:
        Writeable trip point bitmap.

.. _`create_trip_attrs.description`:

Description
-----------

helper function to instantiate sysfs entries for every trip
point and its properties of a struct thermal_zone_device.

.. _`create_trip_attrs.return`:

Return
------

0 on success, the proper error value otherwise.

.. _`thermal_zone_device_register`:

thermal_zone_device_register
============================

.. c:function:: struct thermal_zone_device *thermal_zone_device_register(const char *type, int trips, int mask, void *devdata, struct thermal_zone_device_ops *ops, struct thermal_zone_params *tzp, int passive_delay, int polling_delay)

    register a new thermal zone device

    :param const char \*type:
        the thermal zone device type

    :param int trips:
        the number of trip points the thermal zone support

    :param int mask:
        a bit string indicating the writeablility of trip points

    :param void \*devdata:
        private device data

    :param struct thermal_zone_device_ops \*ops:
        standard thermal zone device callbacks

    :param struct thermal_zone_params \*tzp:
        thermal zone platform parameters

    :param int passive_delay:
        number of milliseconds to wait between polls when
        performing passive cooling

    :param int polling_delay:
        number of milliseconds to wait between polls when checking
        whether trip points have been crossed (0 for interrupt
        driven systems)

.. _`thermal_zone_device_register.description`:

Description
-----------

This interface function adds a new thermal zone device (sensor) to
/sys/class/thermal folder as thermal_zone[0-\*]. It tries to bind all the
thermal cooling devices registered at the same time.
\ :c:func:`thermal_zone_device_unregister`\  must be called when the device is no
longer needed. The passive cooling depends on the .\ :c:func:`get_trend`\  return value.

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

    :param struct thermal_zone_device \*tz:
        the thermal zone device to remove

.. _`thermal_zone_get_zone_by_name`:

thermal_zone_get_zone_by_name
=============================

.. c:function:: struct thermal_zone_device *thermal_zone_get_zone_by_name(const char *name)

    search for a zone and returns its ref

    :param const char \*name:
        thermal zone name to fetch the temperature

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

