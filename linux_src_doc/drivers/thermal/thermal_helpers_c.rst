.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/thermal_helpers.c

.. _`thermal_zone_get_temp`:

thermal_zone_get_temp
=====================

.. c:function:: int thermal_zone_get_temp(struct thermal_zone_device *tz, int *temp)

    returns the temperature of a thermal zone

    :param tz:
        a valid pointer to a struct thermal_zone_device
    :type tz: struct thermal_zone_device \*

    :param temp:
        a valid pointer to where to store the resulting temperature.
    :type temp: int \*

.. _`thermal_zone_get_temp.description`:

Description
-----------

When a valid thermal zone reference is passed, it will fetch its
temperature and fill \ ``temp``\ .

.. _`thermal_zone_get_temp.return`:

Return
------

On success returns 0, an error code otherwise

.. _`thermal_zone_get_slope`:

thermal_zone_get_slope
======================

.. c:function:: int thermal_zone_get_slope(struct thermal_zone_device *tz)

    return the slope attribute of the thermal zone

    :param tz:
        thermal zone device with the slope attribute
    :type tz: struct thermal_zone_device \*

.. _`thermal_zone_get_slope.return`:

Return
------

If the thermal zone device has a slope attribute, return it, else
return 1.

.. _`thermal_zone_get_offset`:

thermal_zone_get_offset
=======================

.. c:function:: int thermal_zone_get_offset(struct thermal_zone_device *tz)

    return the offset attribute of the thermal zone

    :param tz:
        thermal zone device with the offset attribute
    :type tz: struct thermal_zone_device \*

.. _`thermal_zone_get_offset.return`:

Return
------

If the thermal zone device has a offset attribute, return it, else
return 0.

.. This file was automatic generated / don't edit.

