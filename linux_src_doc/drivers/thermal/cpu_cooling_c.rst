.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/cpu_cooling.c

.. _`freq_table`:

struct freq_table
=================

.. c:type:: struct freq_table

    frequency table along with power entries

.. _`freq_table.definition`:

Definition
----------

.. code-block:: c

    struct freq_table {
        u32 frequency;
        u32 power;
    }

.. _`freq_table.members`:

Members
-------

frequency
    frequency in KHz

power
    power in mW

.. _`freq_table.description`:

Description
-----------

This structure is built when the cooling device registers and helps
in translating frequency to power and vice versa.

.. _`time_in_idle`:

struct time_in_idle
===================

.. c:type:: struct time_in_idle

    Idle time stats

.. _`time_in_idle.definition`:

Definition
----------

.. code-block:: c

    struct time_in_idle {
        u64 time;
        u64 timestamp;
    }

.. _`time_in_idle.members`:

Members
-------

time
    previous reading of the absolute time that this cpu was idle

timestamp
    wall time of the last invocation of \ :c:func:`get_cpu_idle_time_us`\ 

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
        u32 last_load;
        unsigned int cpufreq_state;
        unsigned int clipped_freq;
        unsigned int max_level;
        struct freq_table *freq_table;
        struct thermal_cooling_device *cdev;
        struct cpufreq_policy *policy;
        struct list_head node;
        struct time_in_idle *idle_time;
    }

.. _`cpufreq_cooling_device.members`:

Members
-------

id
    unique integer value corresponding to each cpufreq_cooling_device
    registered.

last_load
    load measured by the latest call to \ :c:func:`cpufreq_get_requested_power`\ 

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
    Freq table in descending order of frequencies

cdev
    thermal_cooling_device pointer to keep track of the
    registered cooling device.

policy
    cpufreq policy.

node
    list_head to link all cpufreq_cooling_device together.

idle_time
    idle time stats

.. _`cpufreq_cooling_device.description`:

Description
-----------

This structure is required for keeping information of each registered
cpufreq_cooling_device.

.. _`get_level`:

get_level
=========

.. c:function:: unsigned long get_level(struct cpufreq_cooling_device *cpufreq_cdev, unsigned int freq)

    Find the level for a particular frequency

    :param struct cpufreq_cooling_device \*cpufreq_cdev:
        cpufreq_cdev for which the property is required

    :param unsigned int freq:
        Frequency

.. _`get_level.return`:

Return
------

level corresponding to the frequency.

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

.. _`update_freq_table`:

update_freq_table
=================

.. c:function:: int update_freq_table(struct cpufreq_cooling_device *cpufreq_cdev, u32 capacitance)

    Update the freq table with power numbers

    :param struct cpufreq_cooling_device \*cpufreq_cdev:
        the cpufreq cooling device in which to update the table

    :param u32 capacitance:
        dynamic power coefficient for these cpus

.. _`update_freq_table.description`:

Description
-----------

Update the freq table with power numbers.  This table will be used in
\ :c:func:`cpu_power_to_freq`\  and \ :c:func:`cpu_freq_to_power`\  to convert between power and
frequency efficiently.  Power is stored in mW, frequency in KHz.  The
resulting table is in descending order.

.. _`update_freq_table.return`:

Return
------

0 on success, -EINVAL if there are no OPPs for any CPUs,
or -ENOMEM if we run out of memory.

.. _`get_load`:

get_load
========

.. c:function:: u32 get_load(struct cpufreq_cooling_device *cpufreq_cdev, int cpu, int cpu_idx)

    get load for a cpu since last updated

    :param struct cpufreq_cooling_device \*cpufreq_cdev:
        &struct cpufreq_cooling_device for this cpu

    :param int cpu:
        cpu number

    :param int cpu_idx:
        index of the cpu in time_in_idle\*

.. _`get_load.return`:

Return
------

The average load of cpu \ ``cpu``\  in percentage since this
function was last called.

.. _`get_dynamic_power`:

get_dynamic_power
=================

.. c:function:: u32 get_dynamic_power(struct cpufreq_cooling_device *cpufreq_cdev, unsigned long freq)

    calculate the dynamic power

    :param struct cpufreq_cooling_device \*cpufreq_cdev:
        &cpufreq_cooling_device for this cdev

    :param unsigned long freq:
        current frequency

.. _`get_dynamic_power.return`:

Return
------

the dynamic power consumed by the cpus described by
\ ``cpufreq_cdev``\ .

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
        &thermal_cooling_device pointer

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
        &thermal_cooling_device pointer

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
        &thermal_cooling_device pointer

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

.. c:function:: struct thermal_cooling_device *__cpufreq_cooling_register(struct device_node *np, struct cpufreq_policy *policy, u32 capacitance)

    helper function to create cpufreq cooling device

    :param struct device_node \*np:
        a valid struct device_node to the cooling device device tree node

    :param struct cpufreq_policy \*policy:
        cpufreq policy
        Normally this should be same as cpufreq policy->related_cpus.

    :param u32 capacitance:
        dynamic power coefficient for these cpus

.. _`__cpufreq_cooling_register.description`:

Description
-----------

This interface function registers the cpufreq cooling device with the name
"thermal-cpufreq-%x". This api can support multiple instances of cpufreq
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

.. c:function:: struct thermal_cooling_device *cpufreq_cooling_register(struct cpufreq_policy *policy)

    function to create cpufreq cooling device.

    :param struct cpufreq_policy \*policy:
        cpufreq policy

.. _`cpufreq_cooling_register.description`:

Description
-----------

This interface function registers the cpufreq cooling device with the name
"thermal-cpufreq-%x". This api can support multiple instances of cpufreq
cooling devices.

.. _`cpufreq_cooling_register.return`:

Return
------

a valid struct thermal_cooling_device pointer on success,
on failure, it returns a corresponding \ :c:func:`ERR_PTR`\ .

.. _`of_cpufreq_cooling_register`:

of_cpufreq_cooling_register
===========================

.. c:function:: struct thermal_cooling_device *of_cpufreq_cooling_register(struct cpufreq_policy *policy)

    function to create cpufreq cooling device.

    :param struct cpufreq_policy \*policy:
        cpufreq policy

.. _`of_cpufreq_cooling_register.description`:

Description
-----------

This interface function registers the cpufreq cooling device with the name
"thermal-cpufreq-%x". This api can support multiple instances of cpufreq
cooling devices. Using this API, the cpufreq cooling device will be
linked to the device tree node provided.

Using this function, the cooling device will implement the power
extensions by using a simple cpu power model.  The cpus must have
registered their OPPs using the OPP library.

It also takes into account, if property present in policy CPU node, the
static power consumed by the cpu.

.. _`of_cpufreq_cooling_register.return`:

Return
------

a valid struct thermal_cooling_device pointer on success,
and NULL on failure.

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

This interface function unregisters the "thermal-cpufreq-%x" cooling device.

.. This file was automatic generated / don't edit.

