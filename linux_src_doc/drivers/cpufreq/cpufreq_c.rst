.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/cpufreq.c

.. _`blocking_notifier_head`:

BLOCKING_NOTIFIER_HEAD
======================

.. c:function::  BLOCKING_NOTIFIER_HEAD( cpufreq_policy_notifier_list)

    the "policy" list is involved in the validation process for a new CPU frequency policy; the "transition" list for kernel code that needs to handle changes to devices when the CPU clock speed changes. The mutex locks both lists.

    :param  cpufreq_policy_notifier_list:
        *undescribed*

.. _`cpufreq_cpu_get`:

cpufreq_cpu_get
===============

.. c:function:: struct cpufreq_policy *cpufreq_cpu_get(unsigned int cpu)

    returns policy for a cpu and marks it busy.

    :param unsigned int cpu:
        cpu to find policy for.

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

    :param struct cpufreq_policy \*policy:
        policy earlier returned by \ :c:func:`cpufreq_cpu_get`\ .

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

    :param unsigned long val:
        *undescribed*

    :param struct cpufreq_freqs \*ci:
        *undescribed*

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

    call notifier chain and adjust_jiffies on frequency transition.

    :param struct cpufreq_policy \*policy:
        *undescribed*

    :param struct cpufreq_freqs \*freqs:
        *undescribed*

    :param unsigned int state:
        *undescribed*

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

    :param struct cpufreq_policy \*policy:
        cpufreq policy to enable fast frequency switching for.

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

    :param struct cpufreq_policy \*policy:
        cpufreq policy to disable fast frequency switching for.

.. _`cpufreq_parse_governor`:

cpufreq_parse_governor
======================

.. c:function:: int cpufreq_parse_governor(char *str_governor, unsigned int *policy, struct cpufreq_governor **governor)

    parse a governor string

    :param char \*str_governor:
        *undescribed*

    :param unsigned int \*policy:
        *undescribed*

    :param struct cpufreq_governor \*\*governor:
        *undescribed*

.. _`show_one`:

show_one
========

.. c:function::  show_one( file_name,  object)

    print out cpufreq information

    :param  file_name:
        *undescribed*

    :param  object:
        *undescribed*

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

    :param  file_name:
        *undescribed*

    :param  object:
        *undescribed*

.. _`show_cpuinfo_cur_freq`:

show_cpuinfo_cur_freq
=====================

.. c:function:: ssize_t show_cpuinfo_cur_freq(struct cpufreq_policy *policy, char *buf)

    current CPU frequency as detected by hardware

    :param struct cpufreq_policy \*policy:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`show_scaling_governor`:

show_scaling_governor
=====================

.. c:function:: ssize_t show_scaling_governor(struct cpufreq_policy *policy, char *buf)

    show the current policy for the specified CPU

    :param struct cpufreq_policy \*policy:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`store_scaling_governor`:

store_scaling_governor
======================

.. c:function:: ssize_t store_scaling_governor(struct cpufreq_policy *policy, const char *buf, size_t count)

    store policy for the specified CPU

    :param struct cpufreq_policy \*policy:
        *undescribed*

    :param const char \*buf:
        *undescribed*

    :param size_t count:
        *undescribed*

.. _`show_scaling_driver`:

show_scaling_driver
===================

.. c:function:: ssize_t show_scaling_driver(struct cpufreq_policy *policy, char *buf)

    show the cpufreq driver currently loaded

    :param struct cpufreq_policy \*policy:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`show_scaling_available_governors`:

show_scaling_available_governors
================================

.. c:function:: ssize_t show_scaling_available_governors(struct cpufreq_policy *policy, char *buf)

    show the available CPUfreq governors

    :param struct cpufreq_policy \*policy:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`show_related_cpus`:

show_related_cpus
=================

.. c:function:: ssize_t show_related_cpus(struct cpufreq_policy *policy, char *buf)

    show the CPUs affected by each transition even if hw coordination is in use

    :param struct cpufreq_policy \*policy:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`show_affected_cpus`:

show_affected_cpus
==================

.. c:function:: ssize_t show_affected_cpus(struct cpufreq_policy *policy, char *buf)

    show the CPUs affected by each transition

    :param struct cpufreq_policy \*policy:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`show_bios_limit`:

show_bios_limit
===============

.. c:function:: ssize_t show_bios_limit(struct cpufreq_policy *policy, char *buf)

    show the current cpufreq HW/BIOS limitation

    :param struct cpufreq_policy \*policy:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`cpufreq_add_dev`:

cpufreq_add_dev
===============

.. c:function:: int cpufreq_add_dev(struct device *dev, struct subsys_interface *sif)

    the cpufreq interface for a CPU device.

    :param struct device \*dev:
        CPU device.

    :param struct subsys_interface \*sif:
        Subsystem interface structure pointer (not used)

.. _`cpufreq_remove_dev`:

cpufreq_remove_dev
==================

.. c:function:: void cpufreq_remove_dev(struct device *dev, struct subsys_interface *sif)

    remove a CPU device

    :param struct device \*dev:
        *undescribed*

    :param struct subsys_interface \*sif:
        *undescribed*

.. _`cpufreq_remove_dev.description`:

Description
-----------

Removes the cpufreq interface for a CPU device.

.. _`cpufreq_out_of_sync`:

cpufreq_out_of_sync
===================

.. c:function:: void cpufreq_out_of_sync(struct cpufreq_policy *policy, unsigned int new_freq)

    If actual and saved CPU frequency differs, we're in deep trouble.

    :param struct cpufreq_policy \*policy:
        policy managing CPUs

    :param unsigned int new_freq:
        CPU frequency the CPU actually runs at

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

    :param unsigned int cpu:
        CPU number

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

    :param unsigned int cpu:
        CPU number

.. _`cpufreq_quick_get_max.description`:

Description
-----------

Just return the max possible frequency for a given CPU.

.. _`cpufreq_get`:

cpufreq_get
===========

.. c:function:: unsigned int cpufreq_get(unsigned int cpu)

    get the current CPU frequency (in kHz)

    :param unsigned int cpu:
        CPU number

.. _`cpufreq_get.description`:

Description
-----------

Get the CPU current (static) CPU frequency

.. _`cpufreq_suspend`:

cpufreq_suspend
===============

.. c:function:: void cpufreq_suspend( void)

    Suspend CPUFreq governors

    :param  void:
        no arguments

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

    :param  void:
        no arguments

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

    :param  void:
        no arguments

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

    :param  void:
        no arguments

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

    :param struct notifier_block \*nb:
        notifier function to register

    :param unsigned int list:
        CPUFREQ_TRANSITION_NOTIFIER or CPUFREQ_POLICY_NOTIFIER

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

    :param struct notifier_block \*nb:
        notifier block to be unregistered

    :param unsigned int list:
        CPUFREQ_TRANSITION_NOTIFIER or CPUFREQ_POLICY_NOTIFIER

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

    :param struct cpufreq_policy \*policy:
        cpufreq policy to switch the frequency for.

    :param unsigned int target_freq:
        New frequency to set (may be approximate).

.. _`cpufreq_driver_fast_switch.description`:

Description
-----------

Carry out a fast frequency switch without sleeping.

The driver's ->\ :c:func:`fast_switch`\  callback invoked by this function must be
suitable for being called from within RCU-sched read-side critical sections
and it is expected to select the minimum available frequency greater than or
equal to \ ``target_freq``\  (CPUFREQ_RELATION_L).

This function must not be called if policy->fast_switch_enabled is unset.

Governors calling this function must guarantee that it will never be invoked
twice in parallel for the same policy and that it will never be called in
parallel with either ->\ :c:func:`target`\  or ->\ :c:func:`target_index`\  for the same policy.

If CPUFREQ_ENTRY_INVALID is returned by the driver's ->\ :c:func:`fast_switch`\ 
callback to indicate an error condition, the hardware configuration must be
preserved.

.. _`cpufreq_get_policy`:

cpufreq_get_policy
==================

.. c:function:: int cpufreq_get_policy(struct cpufreq_policy *policy, unsigned int cpu)

    get the current cpufreq_policy

    :param struct cpufreq_policy \*policy:
        struct cpufreq_policy into which the current cpufreq_policy
        is written

    :param unsigned int cpu:
        *undescribed*

.. _`cpufreq_get_policy.description`:

Description
-----------

Reads the current cpufreq policy.

.. _`cpufreq_update_policy`:

cpufreq_update_policy
=====================

.. c:function:: int cpufreq_update_policy(unsigned int cpu)

    re-evaluate an existing cpufreq policy

    :param unsigned int cpu:
        CPU which shall be re-evaluated

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

    :param struct cpufreq_driver \*driver_data:
        A struct cpufreq_driver containing the values#
        submitted by the CPU Frequency driver.

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

    :param struct cpufreq_driver \*driver:
        *undescribed*

.. _`cpufreq_unregister_driver.description`:

Description
-----------

Unregister the current CPUFreq driver. Only call this if you have
the right to do so, i.e. if you have succeeded in initialising before!
Returns zero if successful, and -EINVAL if the cpufreq_driver is
currently not initialised.

.. This file was automatic generated / don't edit.

