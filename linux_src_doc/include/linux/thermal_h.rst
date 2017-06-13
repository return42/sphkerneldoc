.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/thermal.h

.. _`thermal_zone_device`:

struct thermal_zone_device
==========================

.. c:type:: struct thermal_zone_device

    structure for a thermal zone

.. _`thermal_zone_device.definition`:

Definition
----------

.. code-block:: c

    struct thermal_zone_device {
        int id;
        char type[THERMAL_NAME_LENGTH];
        struct device device;
        struct attribute_group trips_attribute_group;
        struct thermal_attr *trip_temp_attrs;
        struct thermal_attr *trip_type_attrs;
        struct thermal_attr *trip_hyst_attrs;
        void *devdata;
        int trips;
        unsigned long trips_disabled;
        int passive_delay;
        int polling_delay;
        int temperature;
        int last_temperature;
        int emul_temperature;
        int passive;
        int prev_low_trip;
        int prev_high_trip;
        unsigned int forced_passive;
        atomic_t need_update;
        struct thermal_zone_device_ops *ops;
        struct thermal_zone_params *tzp;
        struct thermal_governor *governor;
        void *governor_data;
        struct list_head thermal_instances;
        struct ida ida;
        struct mutex lock;
        struct list_head node;
        struct delayed_work poll_queue;
        enum thermal_notify_event notify_event;
    }

.. _`thermal_zone_device.members`:

Members
-------

id
    unique id number for each thermal zone

type
    the thermal zone device type

device
    &struct device for this thermal zone

trips_attribute_group
    *undescribed*

trip_temp_attrs
    attributes for trip points for sysfs: trip temperature

trip_type_attrs
    attributes for trip points for sysfs: trip type

trip_hyst_attrs
    attributes for trip points for sysfs: trip hysteresis

devdata
    private pointer for device private data

trips
    number of trip points the thermal zone supports
    \ ``trips_disabled``\ ;     bitmap for disabled trips

trips_disabled
    *undescribed*

passive_delay
    number of milliseconds to wait between polls when
    performing passive cooling.

polling_delay
    number of milliseconds to wait between polls when
    checking whether trip points have been crossed (0 for
    interrupt driven systems)

temperature
    current temperature.  This is only for core code,
    drivers should use \ :c:func:`thermal_zone_get_temp`\  to get the
    current temperature

last_temperature
    previous temperature read

emul_temperature
    emulated temperature when using CONFIG_THERMAL_EMULATION

passive
    1 if you've crossed a passive trip point, 0 otherwise.

prev_low_trip
    the low current temperature if you've crossed a passive

prev_high_trip
    the above current temperature if you've crossed a

forced_passive
    If > 0, temperature at which to switch on all ACPI
    processor cooling devices.  Currently only used by the
    step-wise governor.

need_update
    if equals 1, thermal_zone_device_update needs to be invoked.

ops
    operations this \ :c:type:`struct thermal_zone_device <thermal_zone_device>`\  supports

tzp
    thermal zone parameters

governor
    pointer to the governor for this thermal zone

governor_data
    private pointer for governor data

thermal_instances
    list of \ :c:type:`struct thermal_instance <thermal_instance>`\  of this thermal zone

ida
    &struct ida to generate unique id for this zone's cooling
    devices

lock
    lock to protect thermal_instances list

node
    node in thermal_tz_list (in thermal_core.c)

poll_queue
    delayed work for polling

notify_event
    Last notification event

.. _`thermal_governor`:

struct thermal_governor
=======================

.. c:type:: struct thermal_governor

    structure that holds thermal governor information

.. _`thermal_governor.definition`:

Definition
----------

.. code-block:: c

    struct thermal_governor {
        char name[THERMAL_NAME_LENGTH];
        int (*bind_to_tz)(struct thermal_zone_device *tz);
        void (*unbind_from_tz)(struct thermal_zone_device *tz);
        int (*throttle)(struct thermal_zone_device *tz, int trip);
        struct list_head governor_list;
    }

.. _`thermal_governor.members`:

Members
-------

name
    name of the governor

bind_to_tz
    callback called when binding to a thermal zone.  If it
    returns 0, the governor is bound to the thermal zone,
    otherwise it fails.

unbind_from_tz
    callback called when a governor is unbound from a
    thermal zone.

throttle
    callback called for every trip point even if temperature is
    below the trip point temperature

governor_list
    node in thermal_governor_list (in thermal_core.c)

.. _`thermal_zone_of_device_ops`:

struct thermal_zone_of_device_ops
=================================

.. c:type:: struct thermal_zone_of_device_ops

    scallbacks for handling DT based zones

.. _`thermal_zone_of_device_ops.definition`:

Definition
----------

.. code-block:: c

    struct thermal_zone_of_device_ops {
        int (*get_temp)(void *, int *);
        int (*get_trend)(void *, int, enum thermal_trend *);
        int (*set_trips)(void *, int, int);
        int (*set_emul_temp)(void *, int);
        int (*set_trip_temp)(void *, int, int);
    }

.. _`thermal_zone_of_device_ops.members`:

Members
-------

get_temp
    a pointer to a function that reads the sensor temperature.

get_trend
    a pointer to a function that reads the sensor temperature trend.

set_trips
    a pointer to a function that sets a temperature window. When
    this window is left the driver must inform the thermal core via
    thermal_zone_device_update.

set_emul_temp
    a pointer to a function that sets sensor emulated
    temperature.

set_trip_temp
    a pointer to a function that sets the trip temperature on
    hardware.

.. _`thermal_trip`:

struct thermal_trip
===================

.. c:type:: struct thermal_trip

    representation of a point in temperature domain

.. _`thermal_trip.definition`:

Definition
----------

.. code-block:: c

    struct thermal_trip {
        struct device_node *np;
        int temperature;
        int hysteresis;
        enum thermal_trip_type type;
    }

.. _`thermal_trip.members`:

Members
-------

np
    pointer to struct device_node that this trip point was created from

temperature
    temperature value in miliCelsius

hysteresis
    relative hysteresis in miliCelsius

type
    trip point type

.. This file was automatic generated / don't edit.

