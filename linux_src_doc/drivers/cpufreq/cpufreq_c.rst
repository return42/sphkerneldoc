.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/cpufreq.c

.. _`blocking_notifier_head`:

BLOCKING_NOTIFIER_HEAD
======================

.. c:function::  BLOCKING_NOTIFIER_HEAD( cpufreq_policy_notifier_list)

    the "policy" list is involved in the validation process for a new CPU frequency policy; the "transition" list for kernel code that needs to handle changes to devices when the CPU clock speed changes. The mutex locks both lists.

    :param cpufreq_policy_notifier_list:
        *undescribed*
    :type cpufreq_policy_notifier_list: 

.. _`cpufreq_cpu_get`:

cpufreq_cpu_get
===============

.. c:function:: struct cpufreq_policy *cpufreq_cpu_get(unsigned int cpu)

    returns policy for a cpu and marks it busy.

    :param cpu:
        cpu to find policy for.
    :type cpu: unsigned int

.. _`cpufreq_cpu_get.description`:

Description
-----------

This returns policy for 'cpu', returns NULL if it doesn't exist.
It also increments the kobject reference count to mark it busy and so would
require a corresponding call to \ :c:func:`cpufreq_cpu_put`\  to decrement it back.
If corresponding call \ :c:func:`cpufreq_cpu_put`\  isn't made, the policy wouldn't be
freed as that depends on the kobj count.

.. _`cpufreq_cpu_get.return`:

Return
------

A valid policy on success, otherwise NULL on failure.

.. _`cpufreq_cpu_put`:

cpufreq_cpu_put
===============

.. c:function:: void cpufreq_cpu_put(struct cpufreq_policy *policy)

    Decrements the usage count of a policy

    :param policy:
        policy earlier returned by \ :c:func:`cpufreq_cpu_get`\ .
    :type policy: struct cpufreq_policy \*

.. _`cpufreq_cpu_put.description`:

Description
-----------

This decrements the kobject reference count incremented earlier by calling
\ :c:func:`cpufreq_cpu_get`\ .

.. _`adjust_jiffies`:

adjust_jiffies
==============

.. c:function:: void adjust_jiffies(unsigned long val, struct cpufreq_freqs *ci)

    adjust the system "loops_per_jiffy"

    :param val:
        *undescribed*
    :type val: unsigned long

    :param ci:
        *undescribed*
    :type ci: struct cpufreq_freqs \*

.. _`adjust_jiffies.description`:

Description
-----------

This function alters the system "loops_per_jiffy" for the clock
speed change. Note that loops_per_jiffy cannot be updated on SMP
systems as each CPU might be scaled differently. So, use the arch
per-CPU loops_per_jiffy value wherever possible.

.. _`cpufreq_notify_transition`:

cpufreq_notify_transition
=========================

.. c:function:: void cpufreq_notify_transition(struct cpufreq_policy *policy, struct cpufreq_freqs *freqs, unsigned int state)

    Notify frequency transition and adjust_jiffies.

    :param policy:
        cpufreq policy to enable fast frequency switching for.
    :type policy: struct cpufreq_policy \*

    :param freqs:
        contain details of the frequency update.
    :type freqs: struct cpufreq_freqs \*

    :param state:
        set to CPUFREQ_PRECHANGE or CPUFREQ_POSTCHANGE.
    :type state: unsigned int

.. _`cpufreq_notify_transition.description`:

Description
-----------

This function calls the transition notifiers and the "adjust_jiffies"
function. It is called twice on all CPU frequency changes that have
external effects.

.. _`cpufreq_enable_fast_switch`:

cpufreq_enable_fast_switch
==========================

.. c:function:: void cpufreq_enable_fast_switch(struct cpufreq_policy *policy)

    Enable fast frequency switching for policy.

    :param policy:
        cpufreq policy to enable fast frequency switching for.
    :type policy: struct cpufreq_policy \*

.. _`cpufreq_enable_fast_switch.description`:

Description
-----------

Try to enable fast frequency switching for \ ``policy``\ .

The attempt will fail if there is at least one transition notifier registered
at this point, as fast frequency switching is quite fundamentally at odds
with transition notifiers.  Thus if successful, it will make registration of
transition notifiers fail going forward.

.. _`cpufreq_disable_fast_switch`:

cpufreq_disable_fast_switch
===========================

.. c:function:: void cpufreq_disable_fast_switch(struct cpufreq_policy *policy)

    Disable fast frequency switching for policy.

    :param policy:
        cpufreq policy to disable fast frequency switching for.
    :type policy: struct cpufreq_policy \*

.. _`cpufreq_driver_resolve_freq`:

cpufreq_driver_resolve_freq
===========================

.. c:function:: unsigned int cpufreq_driver_resolve_freq(struct cpufreq_policy *policy, unsigned int target_freq)

    Map a target frequency to a driver-supported one.

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param target_freq:
        target frequency to resolve.
    :type target_freq: unsigned int

.. _`cpufreq_driver_resolve_freq.description`:

Description
-----------

The target to driver frequency mapping is cached in the policy.

.. _`cpufreq_driver_resolve_freq.return`:

Return
------

Lowest driver-supported frequency greater than or equal to the
given target_freq, subject to policy (min/max) and driver limitations.

.. _`cpufreq_parse_governor`:

cpufreq_parse_governor
======================

.. c:function:: int cpufreq_parse_governor(char *str_governor, struct cpufreq_policy *policy)

    parse a governor string

    :param str_governor:
        *undescribed*
    :type str_governor: char \*

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

.. _`show_one`:

show_one
========

.. c:function::  show_one( file_name,  object)

    print out cpufreq information

    :param file_name:
        *undescribed*
    :type file_name: 

    :param object:
        *undescribed*
    :type object: 

.. _`show_one.description`:

Description
-----------

Write out information from cpufreq_driver->policy[cpu]; object must be
"unsigned int".

.. _`store_one`:

store_one
=========

.. c:function::  store_one( file_name,  object)

    sysfs write access

    :param file_name:
        *undescribed*
    :type file_name: 

    :param object:
        *undescribed*
    :type object: 

.. _`show_cpuinfo_cur_freq`:

show_cpuinfo_cur_freq
=====================

.. c:function:: ssize_t show_cpuinfo_cur_freq(struct cpufreq_policy *policy, char *buf)

    current CPU frequency as detected by hardware

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`show_scaling_governor`:

show_scaling_governor
=====================

.. c:function:: ssize_t show_scaling_governor(struct cpufreq_policy *policy, char *buf)

    show the current policy for the specified CPU

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`store_scaling_governor`:

store_scaling_governor
======================

.. c:function:: ssize_t store_scaling_governor(struct cpufreq_policy *policy, const char *buf, size_t count)

    store policy for the specified CPU

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param buf:
        *undescribed*
    :type buf: const char \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`show_scaling_driver`:

show_scaling_driver
===================

.. c:function:: ssize_t show_scaling_driver(struct cpufreq_policy *policy, char *buf)

    show the cpufreq driver currently loaded

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`show_scaling_available_governors`:

show_scaling_available_governors
================================

.. c:function:: ssize_t show_scaling_available_governors(struct cpufreq_policy *policy, char *buf)

    show the available CPUfreq governors

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`show_related_cpus`:

show_related_cpus
=================

.. c:function:: ssize_t show_related_cpus(struct cpufreq_policy *policy, char *buf)

    show the CPUs affected by each transition even if hw coordination is in use

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`show_affected_cpus`:

show_affected_cpus
==================

.. c:function:: ssize_t show_affected_cpus(struct cpufreq_policy *policy, char *buf)

    show the CPUs affected by each transition

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`show_bios_limit`:

show_bios_limit
===============

.. c:function:: ssize_t show_bios_limit(struct cpufreq_policy *policy, char *buf)

    show the current cpufreq HW/BIOS limitation

    :param policy:
        *undescribed*
    :type policy: struct cpufreq_policy \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`cpufreq_add_dev`:

cpufreq_add_dev
===============

.. c:function:: int cpufreq_add_dev(struct device *dev, struct subsys_interface *sif)

    the cpufreq interface for a CPU device.

    :param dev:
        CPU device.
    :type dev: struct device \*

    :param sif:
        Subsystem interface structure pointer (not used)
    :type sif: struct subsys_interface \*

.. _`cpufreq_remove_dev`:

cpufreq_remove_dev
==================

.. c:function:: void cpufreq_remove_dev(struct device *dev, struct subsys_interface *sif)

    remove a CPU device

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param sif:
        *undescribed*
    :type sif: struct subsys_interface \*

.. _`cpufreq_remove_dev.description`:

Description
-----------

Removes the cpufreq interface for a CPU device.

.. _`cpufreq_out_of_sync`:

cpufreq_out_of_sync
===================

.. c:function:: void cpufreq_out_of_sync(struct cpufreq_policy *policy, unsigned int new_freq)

    If actual and saved CPU frequency differs, we're in deep trouble.

    :param policy:
        policy managing CPUs
    :type policy: struct cpufreq_policy \*

    :param new_freq:
        CPU frequency the CPU actually runs at
    :type new_freq: unsigned int

.. _`cpufreq_out_of_sync.description`:

Description
-----------

We adjust to current frequency first, and need to clean up later.
So either call to \ :c:func:`cpufreq_update_policy`\  or schedule \ :c:func:`handle_update`\ ).

.. _`cpufreq_quick_get`:

cpufreq_quick_get
=================

.. c:function:: unsigned int cpufreq_quick_get(unsigned int cpu)

    get the CPU frequency (in kHz) from policy->cur

    :param cpu:
        CPU number
    :type cpu: unsigned int

.. _`cpufreq_quick_get.description`:

Description
-----------

This is the last known freq, without actually getting it from the driver.
Return value will be same as what is shown in scaling_cur_freq in sysfs.

.. _`cpufreq_quick_get_max`:

cpufreq_quick_get_max
=====================

.. c:function:: unsigned int cpufreq_quick_get_max(unsigned int cpu)

    get the max reported CPU frequency for this CPU

    :param cpu:
        CPU number
    :type cpu: unsigned int

.. _`cpufreq_quick_get_max.description`:

Description
-----------

Just return the max possible frequency for a given CPU.

.. _`cpufreq_get`:

cpufreq_get
===========

.. c:function:: unsigned int cpufreq_get(unsigned int cpu)

    get the current CPU frequency (in kHz)

    :param cpu:
        CPU number
    :type cpu: unsigned int

.. _`cpufreq_get.description`:

Description
-----------

Get the CPU current (static) CPU frequency

.. _`cpufreq_suspend`:

cpufreq_suspend
===============

.. c:function:: void cpufreq_suspend( void)

    Suspend CPUFreq governors

    :param void:
        no arguments
    :type void: 

.. _`cpufreq_suspend.description`:

Description
-----------

Called during system wide Suspend/Hibernate cycles for suspending governors
as some platforms can't change frequency after this point in suspend cycle.
Because some of the devices (like: i2c, regulators, etc) they use for
changing frequency are suspended quickly after this point.

.. _`cpufreq_resume`:

cpufreq_resume
==============

.. c:function:: void cpufreq_resume( void)

    Resume CPUFreq governors

    :param void:
        no arguments
    :type void: 

.. _`cpufreq_resume.description`:

Description
-----------

Called during system wide Suspend/Hibernate cycle for resuming governors that
are suspended with \ :c:func:`cpufreq_suspend`\ .

.. _`cpufreq_get_current_driver`:

cpufreq_get_current_driver
==========================

.. c:function:: const char *cpufreq_get_current_driver( void)

    return current driver's name

    :param void:
        no arguments
    :type void: 

.. _`cpufreq_get_current_driver.description`:

Description
-----------

Return the name string of the currently loaded cpufreq driver
or NULL, if none.

.. _`cpufreq_get_driver_data`:

cpufreq_get_driver_data
=======================

.. c:function:: void *cpufreq_get_driver_data( void)

    return current driver data

    :param void:
        no arguments
    :type void: 

.. _`cpufreq_get_driver_data.description`:

Description
-----------

Return the private data of the currently loaded cpufreq
driver, or NULL if no cpufreq driver is loaded.

.. _`cpufreq_register_notifier`:

cpufreq_register_notifier
=========================

.. c:function:: int cpufreq_register_notifier(struct notifier_block *nb, unsigned int list)

    register a driver with cpufreq

    :param nb:
        notifier function to register
    :type nb: struct notifier_block \*

    :param list:
        CPUFREQ_TRANSITION_NOTIFIER or CPUFREQ_POLICY_NOTIFIER
    :type list: unsigned int

.. _`cpufreq_register_notifier.add-a-driver-to-one-of-two-lists`:

Add a driver to one of two lists
--------------------------------

either a list of drivers that
are notified about clock rate changes (once before and once after
the transition), or a list of drivers that are notified about
changes in cpufreq policy.

This function may sleep, and has the same return conditions as
blocking_notifier_chain_register.

.. _`cpufreq_unregister_notifier`:

cpufreq_unregister_notifier
===========================

.. c:function:: int cpufreq_unregister_notifier(struct notifier_block *nb, unsigned int list)

    unregister a driver with cpufreq

    :param nb:
        notifier block to be unregistered
    :type nb: struct notifier_block \*

    :param list:
        CPUFREQ_TRANSITION_NOTIFIER or CPUFREQ_POLICY_NOTIFIER
    :type list: unsigned int

.. _`cpufreq_unregister_notifier.description`:

Description
-----------

Remove a driver from the CPU frequency notifier list.

This function may sleep, and has the same return conditions as
blocking_notifier_chain_unregister.

.. _`cpufreq_driver_fast_switch`:

cpufreq_driver_fast_switch
==========================

.. c:function:: unsigned int cpufreq_driver_fast_switch(struct cpufreq_policy *policy, unsigned int target_freq)

    Carry out a fast CPU frequency switch.

    :param policy:
        cpufreq policy to switch the frequency for.
    :type policy: struct cpufreq_policy \*

    :param target_freq:
        New frequency to set (may be approximate).
    :type target_freq: unsigned int

.. _`cpufreq_driver_fast_switch.description`:

Description
-----------

Carry out a fast frequency switch without sleeping.

The driver's ->fast_switch() callback invoked by this function must be
suitable for being called from within RCU-sched read-side critical sections
and it is expected to select the minimum available frequency greater than or
equal to \ ``target_freq``\  (CPUFREQ_RELATION_L).

This function must not be called if policy->fast_switch_enabled is unset.

Governors calling this function must guarantee that it will never be invoked
twice in parallel for the same policy and that it will never be called in
parallel with either ->target() or ->target_index() for the same policy.

Returns the actual frequency set for the CPU.

If 0 is returned by the driver's ->fast_switch() callback to indicate an
error condition, the hardware configuration must be preserved.

.. _`cpufreq_get_policy`:

cpufreq_get_policy
==================

.. c:function:: int cpufreq_get_policy(struct cpufreq_policy *policy, unsigned int cpu)

    get the current cpufreq_policy

    :param policy:
        struct cpufreq_policy into which the current cpufreq_policy
        is written
    :type policy: struct cpufreq_policy \*

    :param cpu:
        *undescribed*
    :type cpu: unsigned int

.. _`cpufreq_get_policy.description`:

Description
-----------

Reads the current cpufreq policy.

.. _`cpufreq_update_policy`:

cpufreq_update_policy
=====================

.. c:function:: void cpufreq_update_policy(unsigned int cpu)

    re-evaluate an existing cpufreq policy

    :param cpu:
        CPU which shall be re-evaluated
    :type cpu: unsigned int

.. _`cpufreq_update_policy.description`:

Description
-----------

Useful for policy notifiers which have different necessities
at different times.

.. _`cpufreq_register_driver`:

cpufreq_register_driver
=======================

.. c:function:: int cpufreq_register_driver(struct cpufreq_driver *driver_data)

    register a CPU Frequency driver

    :param driver_data:
        A struct cpufreq_driver containing the values#
        submitted by the CPU Frequency driver.
    :type driver_data: struct cpufreq_driver \*

.. _`cpufreq_register_driver.description`:

Description
-----------

Registers a CPU Frequency driver to this core code. This code
returns zero on success, -EEXIST when another driver got here first
(and isn't unregistered in the meantime).

.. _`cpufreq_unregister_driver`:

cpufreq_unregister_driver
=========================

.. c:function:: int cpufreq_unregister_driver(struct cpufreq_driver *driver)

    unregister the current CPUFreq driver

    :param driver:
        *undescribed*
    :type driver: struct cpufreq_driver \*

.. _`cpufreq_unregister_driver.description`:

Description
-----------

Unregister the current CPUFreq driver. Only call this if you have
the right to do so, i.e. if you have succeeded in initialising before!
Returns zero if successful, and -EINVAL if the cpufreq_driver is
currently not initialised.

.. This file was automatic generated / don't edit.

