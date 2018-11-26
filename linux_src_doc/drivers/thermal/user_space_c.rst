.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/user_space.c

.. _`notify_user_space`:

notify_user_space
=================

.. c:function:: int notify_user_space(struct thermal_zone_device *tz, int trip)

    Notifies user space about thermal events \ ``tz``\  - thermal_zone_device \ ``trip``\  - trip point index

    :param tz:
        *undescribed*
    :type tz: struct thermal_zone_device \*

    :param trip:
        *undescribed*
    :type trip: int

.. _`notify_user_space.description`:

Description
-----------

This function notifies the user space through UEvents.

.. This file was automatic generated / don't edit.

