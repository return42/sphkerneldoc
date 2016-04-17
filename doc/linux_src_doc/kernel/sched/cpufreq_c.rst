.. -*- coding: utf-8; mode: rst -*-

=========
cpufreq.c
=========


.. _`cpufreq_set_update_util_data`:

cpufreq_set_update_util_data
============================

.. c:function:: void cpufreq_set_update_util_data (int cpu, struct update_util_data *data)

    Populate the CPU's update_util_data pointer.

    :param int cpu:
        The CPU to set the pointer for.

    :param struct update_util_data \*data:
        New pointer value.



.. _`cpufreq_set_update_util_data.description`:

Description
-----------

Set and publish the update_util_data pointer for the given CPU.  That pointer
points to a struct update_util_data object containing a callback function
to call from :c:func:`cpufreq_update_util`.  That function will be called from an RCU
read-side critical section, so it must not sleep.

Callers must use RCU-sched callbacks to free any memory that might be
accessed via the old update_util_data pointer or invoke :c:func:`synchronize_sched`
right after this function to avoid use-after-free.

