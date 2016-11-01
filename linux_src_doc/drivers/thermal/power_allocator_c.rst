.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/power_allocator.c

.. _`mul_frac`:

mul_frac
========

.. c:function:: s64 mul_frac(s64 x, s64 y)

    multiply two fixed-point numbers

    :param s64 x:
        first multiplicand

    :param s64 y:
        second multiplicand

.. _`mul_frac.return`:

Return
------

the result of multiplying two fixed-point numbers.  The
result is also a fixed-point number.

.. _`div_frac`:

div_frac
========

.. c:function:: s64 div_frac(s64 x, s64 y)

    divide two fixed-point numbers

    :param s64 x:
        the dividend

    :param s64 y:
        the divisor

.. _`div_frac.return`:

Return
------

the result of dividing two fixed-point numbers.  The
result is also a fixed-point number.

.. _`power_allocator_params`:

struct power_allocator_params
=============================

.. c:type:: struct power_allocator_params

    parameters for the power allocator governor

.. _`power_allocator_params.definition`:

Definition
----------

.. code-block:: c

    struct power_allocator_params {
        bool allocated_tzp;
        s64 err_integral;
        s32 prev_err;
        int trip_switch_on;
        int trip_max_desired_temperature;
    }

.. _`power_allocator_params.members`:

Members
-------

allocated_tzp
    whether we have allocated tzp for this thermal zone and
    it needs to be freed on unbind

err_integral
    accumulated error in the PID controller.

prev_err
    error in the previous iteration of the PID controller.
    Used to calculate the derivative term.

trip_switch_on
    first passive trip point of the thermal zone.  The
    governor switches on when this trip point is crossed.
    If the thermal zone only has one passive trip point,
    \ ``trip_switch_on``\  should be INVALID_TRIP.

trip_max_desired_temperature
    last passive trip point of the thermal
    zone.  The temperature we are
    controlling for.

.. _`estimate_sustainable_power`:

estimate_sustainable_power
==========================

.. c:function:: u32 estimate_sustainable_power(struct thermal_zone_device *tz)

    Estimate the sustainable power of a thermal zone

    :param struct thermal_zone_device \*tz:
        thermal zone we are operating in

.. _`estimate_sustainable_power.description`:

Description
-----------

For thermal zones that don't provide a sustainable_power in their
thermal_zone_params, estimate one.  Calculate it using the minimum
power of all the cooling devices as that gives a valid value that
can give some degree of functionality.  For optimal performance of
this governor, provide a sustainable_power in the thermal zone's
thermal_zone_params.

.. _`estimate_pid_constants`:

estimate_pid_constants
======================

.. c:function:: void estimate_pid_constants(struct thermal_zone_device *tz, u32 sustainable_power, int trip_switch_on, int control_temp, bool force)

    Estimate the constants for the PID controller

    :param struct thermal_zone_device \*tz:
        thermal zone for which to estimate the constants

    :param u32 sustainable_power:
        sustainable power for the thermal zone

    :param int trip_switch_on:
        trip point number for the switch on temperature

    :param int control_temp:
        target temperature for the power allocator governor

    :param bool force:
        whether to force the update of the constants

.. _`estimate_pid_constants.description`:

Description
-----------

This function is used to update the estimation of the PID
controller constants in struct thermal_zone_parameters.
Sustainable power is provided in case it was estimated.  The
estimated sustainable_power should not be stored in the
thermal_zone_parameters so it has to be passed explicitly to this
function.

If \ ``force``\  is not set, the values in the thermal zone's parameters
are preserved if they are not zero.  If \ ``force``\  is set, the values
in thermal zone's parameters are overwritten.

.. _`pid_controller`:

pid_controller
==============

.. c:function:: u32 pid_controller(struct thermal_zone_device *tz, int control_temp, u32 max_allocatable_power)

    PID controller

    :param struct thermal_zone_device \*tz:
        thermal zone we are operating in

    :param int control_temp:
        the target temperature in millicelsius

    :param u32 max_allocatable_power:
        maximum allocatable power for this thermal zone

.. _`pid_controller.description`:

Description
-----------

This PID controller increases the available power budget so that the
temperature of the thermal zone gets as close as possible to
\ ``control_temp``\  and limits the power if it exceeds it.  k_po is the
proportional term when we are overshooting, k_pu is the
proportional term when we are undershooting.  integral_cutoff is a
threshold below which we stop accumulating the error.  The
accumulated error is only valid if the requested power will make
the system warmer.  If the system is mostly idle, there's no point
in accumulating positive error.

.. _`pid_controller.return`:

Return
------

The power budget for the next period.

.. _`divvy_up_power`:

divvy_up_power
==============

.. c:function:: void divvy_up_power(u32 *req_power, u32 *max_power, int num_actors, u32 total_req_power, u32 power_range, u32 *granted_power, u32 *extra_actor_power)

    divvy the allocated power between the actors

    :param u32 \*req_power:
        each actor's requested power

    :param u32 \*max_power:
        each actor's maximum available power

    :param int num_actors:
        size of the \ ``req_power``\ , \ ``max_power``\  and \ ``granted_power``\ 's array

    :param u32 total_req_power:
        sum of \ ``req_power``\ 

    :param u32 power_range:
        total allocated power

    :param u32 \*granted_power:
        output array: each actor's granted power

    :param u32 \*extra_actor_power:
        an appropriately sized array to be used in the
        function as temporary storage of the extra power given
        to the actors

.. _`divvy_up_power.description`:

Description
-----------

This function divides the total allocated power (@power_range)
fairly between the actors.  It first tries to give each actor a
share of the \ ``power_range``\  according to how much power it requested
compared to the rest of the actors.  For example, if only one actor
requests power, then it receives all the \ ``power_range``\ .  If
three actors each requests 1mW, each receives a third of the
\ ``power_range``\ .

If any actor received more than their maximum power, then that
surplus is re-divvied among the actors based on how far they are
from their respective maximums.

Granted power for each actor is written to \ ``granted_power``\ , which
should've been allocated by the calling function.

.. _`get_governor_trips`:

get_governor_trips
==================

.. c:function:: void get_governor_trips(struct thermal_zone_device *tz, struct power_allocator_params *params)

    get the number of the two trip points that are key for this governor

    :param struct thermal_zone_device \*tz:
        thermal zone to operate on

    :param struct power_allocator_params \*params:
        pointer to private data for this governor

.. _`get_governor_trips.the-power-allocator-governor-works-optimally-with-two-trips-points`:

The power allocator governor works optimally with two trips points
------------------------------------------------------------------

a "switch on" trip point and a "maximum desired temperature".  These
are defined as the first and last passive trip points.

If there is only one trip point, then that's considered to be the
"maximum desired temperature" trip point and the governor is always
on.  If there are no passive or active trip points, then the
governor won't do anything.  In fact, its throttle function
won't be called at all.

.. _`power_allocator_bind`:

power_allocator_bind
====================

.. c:function:: int power_allocator_bind(struct thermal_zone_device *tz)

    bind the power_allocator governor to a thermal zone

    :param struct thermal_zone_device \*tz:
        thermal zone to bind it to

.. _`power_allocator_bind.description`:

Description
-----------

Initialize the PID controller parameters and bind it to the thermal
zone.

.. _`power_allocator_bind.return`:

Return
------

0 on success, or -ENOMEM if we ran out of memory.

.. This file was automatic generated / don't edit.

