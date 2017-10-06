.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/thermal_sysfs.c

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

.. _`destroy_trip_attrs`:

destroy_trip_attrs
==================

.. c:function:: void destroy_trip_attrs(struct thermal_zone_device *tz)

    destroy attributes for trip points

    :param struct thermal_zone_device \*tz:
        the thermal zone device

.. _`destroy_trip_attrs.description`:

Description
-----------

helper function to free resources allocated by \ :c:func:`create_trip_attrs`\ 

.. This file was automatic generated / don't edit.

