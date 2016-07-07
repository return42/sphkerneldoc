.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/fair_share.c

.. _`get_trip_level`:

get_trip_level
==============

.. c:function:: int get_trip_level(struct thermal_zone_device *tz)

    - obtains the current trip level for a zone

    :param struct thermal_zone_device \*tz:
        thermal zone device

.. _`fair_share_throttle`:

fair_share_throttle
===================

.. c:function:: int fair_share_throttle(struct thermal_zone_device *tz, int trip)

    throttles devices associated with the given zone \ ``tz``\  - thermal_zone_device

    :param struct thermal_zone_device \*tz:
        *undescribed*

    :param int trip:
        *undescribed*

.. _`fair_share_throttle.throttling-logic`:

Throttling Logic
----------------

This uses three parameters to calculate the new
throttle state of the cooling devices associated with the given zone.

.. _`fair_share_throttle.parameters-used-for-throttling`:

Parameters used for Throttling
------------------------------

P1. max_state: Maximum throttle state exposed by the cooling device.
P2. percentage[i]/100:
How 'effective' the 'i'th device is, in cooling the given zone.
P3. cur_trip_level/max_no_of_trips:
This describes the extent to which the devices should be throttled.
We do not want to throttle too much when we trip a lower temperature,
whereas the throttling is at full swing if we trip critical levels.
(Heavily assumes the trip points are in ascending order)
new_state of cooling device = P3 \* P2 \* P1

.. This file was automatic generated / don't edit.

