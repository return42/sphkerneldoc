.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/cpu_cooling.c

.. _`power_table`:

struct power_table
==================

.. c:type:: struct power_table

    frequency to power conversion

.. _`power_table.definition`:

Definition
----------

.. code-block:: c

    struct power_table {
        u32 frequency;
        u32 power;
    }

.. _`power_table.members`:

Members
-------

frequency
    frequency in KHz

power
    power in mW

.. _`power_table.description`:

Description
-----------

This structure is built when the cooling device registers and helps
in translating frequency to power and viceversa.

.. _`cpufreq_cooling_device`:

struct cpufreq_cooling_device
=============================

.. c:type:: struct cpufreq_cooling_device

    data for cooling device with cpufreq

.. _`cpufreq_cooling_device.definition`:

Definition
----------

.. code-block:: c

    struct cpufreq_cooling_device {
        int id;
        struct thermal_cooling_device *cool_dev;
        unsigned int cpufreq_state;
        unsigned int clipped_freq;
        unsigned int max_level;
        unsigned int *freq_table;
        struct cpumask allowed_cpus;
        struct list_head node;
        u32 last_load;
        u64 *time_in_idle;
        u64 *time_in_idle_timestamp;
        struct power_table *dyn_power_table;
        int dyn_power_table_entries;
        struct device *cpu_dev;
        get_static_t plat_get_static_power;
    }

.. _`cpufreq_cooling_device.members`:

Members
-------

id
    unique integer value corresponding to each cpufreq_cooling_device
    registered.

cool_dev
    thermal_cooling_device pointer to keep track of the
    registered cooling device.

cpufreq_state
    integer value representing the current state of cpufreq
    cooling devices.

clipped_freq
    integer value representing the absolute value of the clipped
    frequency.

max_level
    maximum cooling level. One less than total number of valid
    cpufreq frequencies.

freq_table
    *undescribed*

allowed_cpus
    all the cpus involved for this cpufreq_cooling_device.

node
    list_head to link all cpufreq_cooling_device together.

last_load
    load measured by the latest call to \ :c:func:`cpufreq_get_actual_power`\ 

time_in_idle
    previous reading of the absolute time that this cpu was idle

time_in_idle_timestamp
    wall time of the last invocation of
    \ :c:func:`get_cpu_idle_time_us`\ 

dyn_power_table
    array of struct power_table for frequency to power
    conversion, sorted in ascending order.

dyn_power_table_entries
    number of entries in the \ ``dyn_power_table``\  array

cpu_dev
    the first cpu_device from \ ``allowed_cpus``\  that has OPPs registered

plat_get_static_power
    callback to calculate the static power

.. _`cpufreq_cooling_device.description`:

Description
-----------

This structure is required for keeping information of each registered
cpufreq_cooling_device.

.. _`get_idr`:

get_idr
=======

.. c:function:: int get_idr(struct idr *idr, int *id)

    function to get a unique id.

    :param struct idr \*idr:
        struct idr \* handle used to create a id.

    :param int \*id:
        int \* value generated by this function.

.. _`get_idr.description`:

Description
-----------

This function will populate \ ``id``\  with an unique
id, using the idr API.

.. _`get_idr.return`:

Return
------

0 on success, an error code on failure.

.. _`release_idr`:

release_idr
===========

.. c:function:: void release_idr(struct idr *idr, int id)

    function to free the unique id.

    :param struct idr \*idr:
        struct idr \* handle used for creating the id.

    :param int id:
        int value representing the unique id.

.. _`get_level`:

get_level
=========

.. c:function:: unsigned long get_level(struct cpufreq_cooling_device *cpufreq_dev, unsigned int freq)

    Find the level for a particular frequency

    :param struct cpufreq_cooling_device \*cpufreq_dev:
        cpufreq_dev for which the property is required

    :param unsigned int freq:
        Frequency

.. _`get_level.return`:

Return
------

level on success, THERMAL_CSTATE_INVALID on error.

.. _`cpufreq_cooling_get_level`:

cpufreq_cooling_get_level
=========================

.. c:function:: unsigned long cpufreq_cooling_get_level(unsigned int cpu, unsigned int freq)

    for a given cpu, return the cooling level.

    :param unsigned int cpu:
        cpu for which the level is required

    :param unsigned int freq:
        the frequency of interest

.. _`cpufreq_cooling_get_level.description`:

Description
-----------

This function will match the cooling level corresponding to the
requested \ ``freq``\  and return it.

.. _`cpufreq_cooling_get_level.return`:

Return
------

The matched cooling level on success or THERMAL_CSTATE_INVALID
otherwise.

.. _`cpufreq_thermal_notifier`:

cpufreq_thermal_notifier
========================

.. c:function:: int cpufreq_thermal_notifier(struct notifier_block *nb, unsigned long event, void *data)

    notifier callback for cpufreq policy change.

    :param struct notifier_block \*nb:
        struct notifier_block \* with callback info.

    :param unsigned long event:
        value showing cpufreq event for which this function invoked.

    :param void \*data:
        callback-specific data

.. _`cpufreq_thermal_notifier.description`:

Description
-----------

Callback to hijack the notification on cpufreq policy transition.
Every time there is a change in policy, we will intercept and
update the cpufreq policy with thermal constraints.

.. _`cpufreq_thermal_notifier.return`:

Return
------

0 (success)

.. _`build_dyn_power_table`:

build_dyn_power_table
=====================

.. c:function:: int build_dyn_power_table(struct cpufreq_cooling_device *cpufreq_device, u32 capacitance)

    create a dynamic power to frequency table

    :param struct cpufreq_cooling_device \*cpufreq_device:
        the cpufreq cooling device in which to store the table

    :param u32 capacitance:
        dynamic power coefficient for these cpus

.. _`build_dyn_power_table.description`:

Description
-----------

Build a dynamic power to frequency table for this cpu and store it
in \ ``cpufreq_device``\ .  This table will be used in \ :c:func:`cpu_power_to_freq`\  and
\ :c:func:`cpu_freq_to_power`\  to convert between power and frequency
efficiently.  Power is stored in mW, frequency in KHz.  The
resulting table is in ascending order.

.. _`build_dyn_power_table.return`:

Return
------

0 on success, -EINVAL if there are no OPPs for any CPUs,
-ENOMEM if we run out of memory or -EAGAIN if an OPP was
added/enabled while the function was executing.

.. _`get_load`:

get_load
========

.. c:function:: u32 get_load(struct cpufreq_cooling_device *cpufreq_device, int cpu, int cpu_idx)

    get load for a cpu since last updated

    :param struct cpufreq_cooling_device \*cpufreq_device:
        \ :c:type:`struct cpufreq_cooling_device <cpufreq_cooling_device>`\  for this cpu

    :param int cpu:
        cpu number

    :param int cpu_idx:
        index of the cpu in cpufreq_device->allowed_cpus

.. _`get_load.return`:

Return
------

The average load of cpu \ ``cpu``\  in percentage since this
function was last called.

.. _`get_static_power`:

get_static_power
================

.. c:function:: int get_static_power(struct cpufreq_cooling_device *cpufreq_device, struct thermal_zone_device *tz, unsigned long freq, u32 *power)

    calculate the static power consumed by the cpus

    :param struct cpufreq_cooling_device \*cpufreq_device:
        struct \ :c:type:`struct cpufreq_cooling_device <cpufreq_cooling_device>` for this cpu cdev

    :param struct thermal_zone_device \*tz:
        thermal zone device in which we're operating

    :param unsigned long freq:
        frequency in KHz

    :param u32 \*power:
        pointer in which to store the calculated static power

.. _`get_static_power.description`:

Description
-----------

Calculate the static power consumed by the cpus described by
\ ``cpu_actor``\  running at frequency \ ``freq``\ .  This function relies on a
platform specific function that should have been provided when the
actor was registered.  If it wasn't, the static power is assumed to
be negligible.  The calculated static power is stored in \ ``power``\ .

.. _`get_static_power.return`:

Return
------

0 on success, -E\* on failure.

.. _`get_dynamic_power`:

get_dynamic_power
=================

.. c:function:: u32 get_dynamic_power(struct cpufreq_cooling_device *cpufreq_device, unsigned long freq)

    calculate the dynamic power

    :param struct cpufreq_cooling_device \*cpufreq_device:
        \ :c:type:`struct cpufreq_cooling_device <cpufreq_cooling_device>` for this cdev

    :param unsigned long freq:
        current frequency

.. _`get_dynamic_power.return`:

Return
------

the dynamic power consumed by the cpus described by
\ ``cpufreq_device``\ .

.. _`cpufreq_get_max_state`:

cpufreq_get_max_state
=====================

.. c:function:: int cpufreq_get_max_state(struct thermal_cooling_device *cdev, unsigned long *state)

    callback function to get the max cooling state.

    :param struct thermal_cooling_device \*cdev:
        thermal cooling device pointer.

    :param unsigned long \*state:
        fill this variable with the max cooling state.

.. _`cpufreq_get_max_state.description`:

Description
-----------

Callback for the thermal cooling device to return the cpufreq
max cooling state.

.. _`cpufreq_get_max_state.return`:

Return
------

0 on success, an error code otherwise.

.. _`cpufreq_get_cur_state`:

cpufreq_get_cur_state
=====================

.. c:function:: int cpufreq_get_cur_state(struct thermal_cooling_device *cdev, unsigned long *state)

    callback function to get the current cooling state.

    :param struct thermal_cooling_device \*cdev:
        thermal cooling device pointer.

    :param unsigned long \*state:
        fill this variable with the current cooling state.

.. _`cpufreq_get_cur_state.description`:

Description
-----------

Callback for the thermal cooling device to return the cpufreq
current cooling state.

.. _`cpufreq_get_cur_state.return`:

Return
------

0 on success, an error code otherwise.

.. _`cpufreq_set_cur_state`:

cpufreq_set_cur_state
=====================

.. c:function:: int cpufreq_set_cur_state(struct thermal_cooling_device *cdev, unsigned long state)

    callback function to set the current cooling state.

    :param struct thermal_cooling_device \*cdev:
        thermal cooling device pointer.

    :param unsigned long state:
        set this variable to the current cooling state.

.. _`cpufreq_set_cur_state.description`:

Description
-----------

Callback for the thermal cooling device to change the cpufreq
current cooling state.

.. _`cpufreq_set_cur_state.return`:

Return
------

0 on success, an error code otherwise.

.. _`cpufreq_get_requested_power`:

cpufreq_get_requested_power
===========================

.. c:function:: int cpufreq_get_requested_power(struct thermal_cooling_device *cdev, struct thermal_zone_device *tz, u32 *power)

    get the current power

    :param struct thermal_cooling_device \*cdev:
        \ :c:type:`struct thermal_cooling_device <thermal_cooling_device>` pointer

    :param struct thermal_zone_device \*tz:
        a valid thermal zone device pointer

    :param u32 \*power:
        pointer in which to store the resulting power

.. _`cpufreq_get_requested_power.description`:

Description
-----------

Calculate the current power consumption of the cpus in milliwatts
and store it in \ ``power``\ .  This function should actually calculate
the requested power, but it's hard to get the frequency that
cpufreq would have assigned if there were no thermal limits.
Instead, we calculate the current power on the assumption that the
immediate future will look like the immediate past.

We use the current frequency and the average load since this
function was last called.  In reality, there could have been
multiple opps since this function was last called and that affects
the load calculation.  While it's not perfectly accurate, this
simplification is good enough and works.  REVISIT this, as more
complex code may be needed if experiments show that it's not
accurate enough.

.. _`cpufreq_get_requested_power.return`:

Return
------

0 on success, -E\* if getting the static power failed.

.. _`cpufreq_state2power`:

cpufreq_state2power
===================

.. c:function:: int cpufreq_state2power(struct thermal_cooling_device *cdev, struct thermal_zone_device *tz, unsigned long state, u32 *power)

    convert a cpu cdev state to power consumed

    :param struct thermal_cooling_device \*cdev:
        \ :c:type:`struct thermal_cooling_device <thermal_cooling_device>` pointer

    :param struct thermal_zone_device \*tz:
        a valid thermal zone device pointer

    :param unsigned long state:
        cooling device state to be converted

    :param u32 \*power:
        pointer in which to store the resulting power

.. _`cpufreq_state2power.description`:

Description
-----------

Convert cooling device state \ ``state``\  into power consumption in
milliwatts assuming 100% load.  Store the calculated power in
\ ``power``\ .

.. _`cpufreq_state2power.return`:

Return
------

0 on success, -EINVAL if the cooling device state could not
be converted into a frequency or other -E\* if there was an error
when calculating the static power.

.. _`cpufreq_power2state`:

cpufreq_power2state
===================

.. c:function:: int cpufreq_power2state(struct thermal_cooling_device *cdev, struct thermal_zone_device *tz, u32 power, unsigned long *state)

    convert power to a cooling device state

    :param struct thermal_cooling_device \*cdev:
        \ :c:type:`struct thermal_cooling_device <thermal_cooling_device>` pointer

    :param struct thermal_zone_device \*tz:
        a valid thermal zone device pointer

    :param u32 power:
        power in milliwatts to be converted

    :param unsigned long \*state:
        pointer in which to store the resulting state

.. _`cpufreq_power2state.description`:

Description
-----------

Calculate a cooling device state for the cpus described by \ ``cdev``\ 
that would allow them to consume at most \ ``power``\  mW and store it in
\ ``state``\ .  Note that this calculation depends on external factors
such as the cpu load or the current static power.  Calling this
function with the same power as input can yield different cooling
device states depending on those external factors.

.. _`cpufreq_power2state.return`:

Return
------

0 on success, -ENODEV if no cpus are online or -EINVAL if
the calculated frequency could not be converted to a valid state.
The latter should not happen unless the frequencies available to
cpufreq have changed since the initialization of the cpu cooling
device.

.. _`__cpufreq_cooling_register`:

__cpufreq_cooling_register
==========================

.. c:function:: struct thermal_cooling_device *__cpufreq_cooling_register(struct device_node *np, const struct cpumask *clip_cpus, u32 capacitance, get_static_t plat_static_func)

    helper function to create cpufreq cooling device

    :param struct device_node \*np:
        a valid struct device_node to the cooling device device tree node

    :param const struct cpumask \*clip_cpus:
        cpumask of cpus where the frequency constraints will happen.
        Normally this should be same as cpufreq policy->related_cpus.

    :param u32 capacitance:
        dynamic power coefficient for these cpus

    :param get_static_t plat_static_func:
        function to calculate the static power consumed by these
        cpus (optional)

.. _`__cpufreq_cooling_register.description`:

Description
-----------

This interface function registers the cpufreq cooling device with the name
"thermal-cpufreq-\ ``x``\ ". This api can support multiple instances of cpufreq
cooling devices. It also gives the opportunity to link the cooling device
with a device tree node, in order to bind it via the thermal DT code.

.. _`__cpufreq_cooling_register.return`:

Return
------

a valid struct thermal_cooling_device pointer on success,
on failure, it returns a corresponding \ :c:func:`ERR_PTR`\ .

.. _`cpufreq_cooling_register`:

cpufreq_cooling_register
========================

.. c:function:: struct thermal_cooling_device *cpufreq_cooling_register(const struct cpumask *clip_cpus)

    function to create cpufreq cooling device.

    :param const struct cpumask \*clip_cpus:
        cpumask of cpus where the frequency constraints will happen.

.. _`cpufreq_cooling_register.description`:

Description
-----------

This interface function registers the cpufreq cooling device with the name
"thermal-cpufreq-\ ``x``\ ". This api can support multiple instances of cpufreq
cooling devices.

.. _`cpufreq_cooling_register.return`:

Return
------

a valid struct thermal_cooling_device pointer on success,
on failure, it returns a corresponding \ :c:func:`ERR_PTR`\ .

.. _`of_cpufreq_cooling_register`:

of_cpufreq_cooling_register
===========================

.. c:function:: struct thermal_cooling_device *of_cpufreq_cooling_register(struct device_node *np, const struct cpumask *clip_cpus)

    function to create cpufreq cooling device.

    :param struct device_node \*np:
        a valid struct device_node to the cooling device device tree node

    :param const struct cpumask \*clip_cpus:
        cpumask of cpus where the frequency constraints will happen.

.. _`of_cpufreq_cooling_register.description`:

Description
-----------

This interface function registers the cpufreq cooling device with the name
"thermal-cpufreq-\ ``x``\ ". This api can support multiple instances of cpufreq
cooling devices. Using this API, the cpufreq cooling device will be
linked to the device tree node provided.

.. _`of_cpufreq_cooling_register.return`:

Return
------

a valid struct thermal_cooling_device pointer on success,
on failure, it returns a corresponding \ :c:func:`ERR_PTR`\ .

.. _`cpufreq_power_cooling_register`:

cpufreq_power_cooling_register
==============================

.. c:function:: struct thermal_cooling_device *cpufreq_power_cooling_register(const struct cpumask *clip_cpus, u32 capacitance, get_static_t plat_static_func)

    create cpufreq cooling device with power extensions

    :param const struct cpumask \*clip_cpus:
        cpumask of cpus where the frequency constraints will happen

    :param u32 capacitance:
        dynamic power coefficient for these cpus

    :param get_static_t plat_static_func:
        function to calculate the static power consumed by these
        cpus (optional)

.. _`cpufreq_power_cooling_register.description`:

Description
-----------

This interface function registers the cpufreq cooling device with
the name "thermal-cpufreq-\ ``x``\ ".  This api can support multiple
instances of cpufreq cooling devices.  Using this function, the
cooling device will implement the power extensions by using a
simple cpu power model.  The cpus must have registered their OPPs
using the OPP library.

An optional \ ``plat_static_func``\  may be provided to calculate the
static power consumed by these cpus.  If the platform's static
power consumption is unknown or negligible, make it NULL.

.. _`cpufreq_power_cooling_register.return`:

Return
------

a valid struct thermal_cooling_device pointer on success,
on failure, it returns a corresponding \ :c:func:`ERR_PTR`\ .

.. _`of_cpufreq_power_cooling_register`:

of_cpufreq_power_cooling_register
=================================

.. c:function:: struct thermal_cooling_device *of_cpufreq_power_cooling_register(struct device_node *np, const struct cpumask *clip_cpus, u32 capacitance, get_static_t plat_static_func)

    create cpufreq cooling device with power extensions

    :param struct device_node \*np:
        a valid struct device_node to the cooling device device tree node

    :param const struct cpumask \*clip_cpus:
        cpumask of cpus where the frequency constraints will happen

    :param u32 capacitance:
        dynamic power coefficient for these cpus

    :param get_static_t plat_static_func:
        function to calculate the static power consumed by these
        cpus (optional)

.. _`of_cpufreq_power_cooling_register.description`:

Description
-----------

This interface function registers the cpufreq cooling device with
the name "thermal-cpufreq-\ ``x``\ ".  This api can support multiple
instances of cpufreq cooling devices.  Using this API, the cpufreq
cooling device will be linked to the device tree node provided.
Using this function, the cooling device will implement the power
extensions by using a simple cpu power model.  The cpus must have
registered their OPPs using the OPP library.

An optional \ ``plat_static_func``\  may be provided to calculate the
static power consumed by these cpus.  If the platform's static
power consumption is unknown or negligible, make it NULL.

.. _`of_cpufreq_power_cooling_register.return`:

Return
------

a valid struct thermal_cooling_device pointer on success,
on failure, it returns a corresponding \ :c:func:`ERR_PTR`\ .

.. _`cpufreq_cooling_unregister`:

cpufreq_cooling_unregister
==========================

.. c:function:: void cpufreq_cooling_unregister(struct thermal_cooling_device *cdev)

    function to remove cpufreq cooling device.

    :param struct thermal_cooling_device \*cdev:
        thermal cooling device pointer.

.. _`cpufreq_cooling_unregister.description`:

Description
-----------

This interface function unregisters the "thermal-cpufreq-\ ``x``\ " cooling device.

.. This file was automatic generated / don't edit.
