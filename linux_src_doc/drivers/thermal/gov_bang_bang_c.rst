.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/gov_bang_bang.c

.. _`bang_bang_control`:

bang_bang_control
=================

.. c:function:: int bang_bang_control(struct thermal_zone_device *tz, int trip)

    controls devices associated with the given zone \ ``tz``\  - thermal_zone_device \ ``trip``\  - the trip point

    :param struct thermal_zone_device \*tz:
        *undescribed*

    :param int trip:
        *undescribed*

.. _`bang_bang_control.regulation-logic`:

Regulation Logic
----------------

a two point regulation, deliver cooling state depending

.. _`bang_bang_control.on-the-previous-state-shown-in-this-diagram`:

on the previous state shown in this diagram
-------------------------------------------


Fan:   OFF    ON

\|
\|
trip_temp:    +---->+
\|     \|        ^
\|     \|        \|
\|     \|   Temperature
(trip_temp - hyst):    +<----+
\|
\|
\|

\* If the fan is not running and temperature exceeds trip_temp, the fan
gets turned on.
\* In case the fan is running, temperature must fall below
(trip_temp - hyst) so that the fan gets turned off again.

.. This file was automatic generated / don't edit.

