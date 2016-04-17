.. -*- coding: utf-8; mode: rst -*-

============
of-thermal.c
============


.. _`__thermal_bind_params`:

struct __thermal_bind_params
============================

.. c:type:: __thermal_bind_params

    a match between trip and cooling device


.. _`__thermal_bind_params.definition`:

Definition
----------

.. code-block:: c

  struct __thermal_bind_params {
    struct device_node * cooling_device;
    unsigned int trip_id;
    unsigned int usage;
    unsigned long min;
    unsigned long max;
  };


.. _`__thermal_bind_params.members`:

Members
-------

:``cooling_device``:
    a pointer to identify the referred cooling device

:``trip_id``:
    the trip point index

:``usage``:
    the percentage (from 0 to 100) of cooling contribution

:``min``:
    minimum cooling state used at this trip point

:``max``:
    maximum cooling state used at this trip point




.. _`__thermal_zone`:

struct __thermal_zone
=====================

.. c:type:: __thermal_zone

    internal representation of a thermal zone


.. _`__thermal_zone.definition`:

Definition
----------

.. code-block:: c

  struct __thermal_zone {
    enum thermal_device_mode mode;
    int passive_delay;
    int polling_delay;
    int slope;
    int offset;
    int ntrips;
    struct thermal_trip * trips;
    int num_tbps;
    struct __thermal_bind_params * tbps;
    void * sensor_data;
    const struct thermal_zone_of_device_ops * ops;
  };


.. _`__thermal_zone.members`:

Members
-------

:``mode``:
    current thermal zone device mode (enabled/disabled)

:``passive_delay``:
    polling interval while passive cooling is activated

:``polling_delay``:
    zone polling interval

:``slope``:
    slope of the temperature adjustment curve

:``offset``:
    offset of the temperature adjustment curve

:``ntrips``:
    number of trip points

:``trips``:
    an array of trip points (0..ntrips - 1)

:``num_tbps``:
    number of thermal bind params

:``tbps``:
    an array of thermal bind params (0..num_tbps - 1)

:``sensor_data``:
    sensor private data used while reading temperature and trend

:``ops``:
    set of callbacks to handle the thermal zone based on DT




.. _`of_thermal_get_ntrips`:

of_thermal_get_ntrips
=====================

.. c:function:: int of_thermal_get_ntrips (struct thermal_zone_device *tz)

    function to export number of available trip points.

    :param struct thermal_zone_device \*tz:
        pointer to a thermal zone



.. _`of_thermal_get_ntrips.description`:

Description
-----------

This function is a globally visible wrapper to get number of trip points
stored in the local struct __thermal_zone



.. _`of_thermal_get_ntrips.return`:

Return
------

number of available trip points, -ENODEV when data not available



.. _`of_thermal_is_trip_valid`:

of_thermal_is_trip_valid
========================

.. c:function:: bool of_thermal_is_trip_valid (struct thermal_zone_device *tz, int trip)

    function to check if trip point is valid

    :param struct thermal_zone_device \*tz:
        pointer to a thermal zone

    :param int trip:
        trip point to evaluate



.. _`of_thermal_is_trip_valid.description`:

Description
-----------

This function is responsible for checking if passed trip point is valid



.. _`of_thermal_is_trip_valid.return`:

Return
------

true if trip point is valid, false otherwise



.. _`of_thermal_get_trip_points`:

of_thermal_get_trip_points
==========================

.. c:function:: const struct thermal_trip *of_thermal_get_trip_points (struct thermal_zone_device *tz)

    function to get access to a globally exported trip points

    :param struct thermal_zone_device \*tz:
        pointer to a thermal zone



.. _`of_thermal_get_trip_points.description`:

Description
-----------

This function provides a pointer to trip points table



.. _`of_thermal_get_trip_points.return`:

Return
------

pointer to trip points table, NULL otherwise



.. _`of_thermal_set_emul_temp`:

of_thermal_set_emul_temp
========================

.. c:function:: int of_thermal_set_emul_temp (struct thermal_zone_device *tz, int temp)

    function to set emulated temperature

    :param struct thermal_zone_device \*tz:
        pointer to a thermal zone

    :param int temp:
        temperature to set



.. _`of_thermal_set_emul_temp.description`:

Description
-----------

This function gives the ability to set emulated value of temperature,
which is handy for debugging



.. _`of_thermal_set_emul_temp.return`:

Return
------

zero on success, error code otherwise



.. _`thermal_zone_of_sensor_register`:

thermal_zone_of_sensor_register
===============================

.. c:function:: struct thermal_zone_device *thermal_zone_of_sensor_register (struct device *dev, int sensor_id, void *data, const struct thermal_zone_of_device_ops *ops)

    registers a sensor to a DT thermal zone

    :param struct device \*dev:
        a valid struct device pointer of a sensor device. Must contain
        a valid .of_node, for the sensor node.

    :param int sensor_id:
        a sensor identifier, in case the sensor IP has more
        than one sensors

    :param void \*data:
        a private pointer (owned by the caller) that will be passed
        back, when a temperature reading is needed.

    :param const struct thermal_zone_of_device_ops \*ops:
        struct thermal_zone_of_device_ops *. Must contain at least .get_temp.



.. _`thermal_zone_of_sensor_register.description`:

Description
-----------

This function will search the list of thermal zones described in device
tree and look for the zone that refer to the sensor device pointed by
``dev``\ ->of_node as temperature providers. For the zone pointing to the
sensor node, the sensor will be added to the DT thermal zone device.

The thermal zone temperature is provided by the ``get_temp`` function
pointer. When called, it will have the private pointer ``data`` back.

The thermal zone temperature trend is provided by the ``get_trend`` function
pointer. When called, it will have the private pointer ``data`` back.



.. _`thermal_zone_of_sensor_register.todo`:

TODO
----

01 - This function must enqueue the new sensor instead of using
it as the only source of temperature values.

02 - There must be a way to match the sensor with all thermal zones
that refer to it.



.. _`thermal_zone_of_sensor_register.return`:

Return
------

On success returns a valid struct thermal_zone_device,
otherwise, it returns a corresponding :c:func:`ERR_PTR`. Caller must
check the return value with help of :c:func:`IS_ERR` helper.



.. _`thermal_zone_of_sensor_unregister`:

thermal_zone_of_sensor_unregister
=================================

.. c:function:: void thermal_zone_of_sensor_unregister (struct device *dev, struct thermal_zone_device *tzd)

    unregisters a sensor from a DT thermal zone

    :param struct device \*dev:
        a valid struct device pointer of a sensor device. Must contain
        a valid .of_node, for the sensor node.

    :param struct thermal_zone_device \*tzd:
        a pointer to struct thermal_zone_device where the sensor is registered.



.. _`thermal_zone_of_sensor_unregister.description`:

Description
-----------

This function removes the sensor callbacks and private data from the
thermal zone device registered with :c:func:`thermal_zone_of_sensor_register`
API. It will also silent the zone by remove the .:c:func:`get_temp` and .:c:func:`get_trend`
thermal zone device callbacks.



.. _`thermal_zone_of_sensor_unregister.todo`:

TODO
----

When the support to several sensors per zone is added, this
function must search the sensor list based on ``dev`` parameter.



.. _`devm_thermal_zone_of_sensor_register`:

devm_thermal_zone_of_sensor_register
====================================

.. c:function:: struct thermal_zone_device *devm_thermal_zone_of_sensor_register (struct device *dev, int sensor_id, void *data, const struct thermal_zone_of_device_ops *ops)

    Resource managed version of thermal_zone_of_sensor_register()

    :param struct device \*dev:
        a valid struct device pointer of a sensor device. Must contain
        a valid .of_node, for the sensor node.

    :param int sensor_id:
        a sensor identifier, in case the sensor IP has more
        than one sensors

    :param void \*data:
        a private pointer (owned by the caller) that will be passed
        back, when a temperature reading is needed.

    :param const struct thermal_zone_of_device_ops \*ops:
        struct thermal_zone_of_device_ops *. Must contain at least .get_temp.



.. _`devm_thermal_zone_of_sensor_register.description`:

Description
-----------

Refer :c:func:`thermal_zone_of_sensor_register` for more details.



.. _`devm_thermal_zone_of_sensor_register.return`:

Return
------

On success returns a valid struct thermal_zone_device,
otherwise, it returns a corresponding :c:func:`ERR_PTR`. Caller must
check the return value with help of :c:func:`IS_ERR` helper.
Registered hermal_zone_device device will automatically be
released when device is unbounded.



.. _`devm_thermal_zone_of_sensor_unregister`:

devm_thermal_zone_of_sensor_unregister
======================================

.. c:function:: void devm_thermal_zone_of_sensor_unregister (struct device *dev, struct thermal_zone_device *tzd)

    Resource managed version of thermal_zone_of_sensor_unregister().

    :param struct device \*dev:
        Device for which which resource was allocated.

    :param struct thermal_zone_device \*tzd:
        a pointer to struct thermal_zone_device where the sensor is registered.



.. _`devm_thermal_zone_of_sensor_unregister.description`:

Description
-----------

This function removes the sensor callbacks and private data from the
thermal zone device registered with :c:func:`devm_thermal_zone_of_sensor_register`
API. It will also silent the zone by remove the .:c:func:`get_temp` and .:c:func:`get_trend`
thermal zone device callbacks.
Normally this function will not need to be called and the resource
management code will ensure that the resource is freed.



.. _`thermal_of_populate_bind_params`:

thermal_of_populate_bind_params
===============================

.. c:function:: int thermal_of_populate_bind_params (struct device_node *np, struct __thermal_bind_params *__tbp, struct thermal_trip *trips, int ntrips)

    parse and fill cooling map data

    :param struct device_node \*np:
        DT node containing a cooling-map node

    :param struct __thermal_bind_params \*__tbp:
        data structure to be filled with cooling map info

    :param struct thermal_trip \*trips:
        array of thermal zone trip points

    :param int ntrips:
        number of trip points inside trips.



.. _`thermal_of_populate_bind_params.description`:

Description
-----------

This function parses a cooling-map type of node represented by
``np`` parameter and fills the read data into ``__tbp`` data structure.
It needs the already parsed array of trip points of the thermal zone
in consideration.



.. _`thermal_of_populate_bind_params.return`:

Return
------

0 on success, proper error code otherwise



.. _`thermal_of_get_trip_type`:

thermal_of_get_trip_type
========================

.. c:function:: int thermal_of_get_trip_type (struct device_node *np, enum thermal_trip_type *type)

    Get phy mode for given device_node

    :param struct device_node \*np:
        Pointer to the given device_node

    :param enum thermal_trip_type \*type:
        Pointer to resulting trip type



.. _`thermal_of_get_trip_type.description`:

Description
-----------

The function gets trip type string from property 'type',
and store its index in trip_types table in ``type``\ ,



.. _`thermal_of_get_trip_type.return`:

Return
------

0 on success, or errno in error case.



.. _`thermal_of_populate_trip`:

thermal_of_populate_trip
========================

.. c:function:: int thermal_of_populate_trip (struct device_node *np, struct thermal_trip *trip)

    parse and fill one trip point data

    :param struct device_node \*np:
        DT node containing a trip point node

    :param struct thermal_trip \*trip:
        trip point data structure to be filled up



.. _`thermal_of_populate_trip.description`:

Description
-----------

This function parses a trip point type of node represented by
``np`` parameter and fills the read data into ``trip`` data structure.



.. _`thermal_of_populate_trip.return`:

Return
------

0 on success, proper error code otherwise



.. _`thermal_of_build_thermal_zone`:

thermal_of_build_thermal_zone
=============================

.. c:function:: struct __thermal_zone *thermal_of_build_thermal_zone (struct device_node *np)

    parse and fill one thermal zone data

    :param struct device_node \*np:
        DT node containing a thermal zone node



.. _`thermal_of_build_thermal_zone.description`:

Description
-----------

This function parses a thermal zone type of node represented by
``np`` parameter and fills the read data into a __thermal_zone data structure
and return this pointer.



.. _`thermal_of_build_thermal_zone.todo`:

TODO
----

Missing properties to parse: thermal-sensor-names



.. _`thermal_of_build_thermal_zone.return`:

Return
------

On success returns a valid struct __thermal_zone,
otherwise, it returns a corresponding :c:func:`ERR_PTR`. Caller must
check the return value with help of :c:func:`IS_ERR` helper.



.. _`of_parse_thermal_zones`:

of_parse_thermal_zones
======================

.. c:function:: int of_parse_thermal_zones ( void)

    parse device tree thermal data

    :param void:
        no arguments



.. _`of_parse_thermal_zones.description`:

Description
-----------


Initialization function that can be called by machine initialization
code to parse thermal data and populate the thermal framework
with hardware thermal zones info. This function only parses thermal zones.
Cooling devices and sensor devices nodes are supposed to be parsed
by their respective drivers.



.. _`of_parse_thermal_zones.return`:

Return
------

0 on success, proper error code otherwise



.. _`of_thermal_destroy_zones`:

of_thermal_destroy_zones
========================

.. c:function:: void of_thermal_destroy_zones ( void)

    remove all zones parsed and allocated resources

    :param void:
        no arguments



.. _`of_thermal_destroy_zones.description`:

Description
-----------


Finds all zones parsed and added to the thermal framework and remove them
from the system, together with their resources.

