.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/step_wise.c

.. _`step_wise_throttle`:

step_wise_throttle
==================

.. c:function:: int step_wise_throttle(struct thermal_zone_device *tz, int trip)

    throttles devices associated with the given zone \ ``tz``\  - thermal_zone_device \ ``trip``\  - trip point index

    :param tz:
        *undescribed*
    :type tz: struct thermal_zone_device \*

    :param trip:
        *undescribed*
    :type trip: int

.. _`step_wise_throttle.throttling-logic`:

Throttling Logic
----------------

This uses the trend of the thermal zone to throttle.
If the thermal zone is 'heating up' this throttles all the cooling
devices associated with the zone and its particular trip point, by one
step. If the zone is 'cooling down' it brings back the performance of
the devices by one step.

.. This file was automatic generated / don't edit.

