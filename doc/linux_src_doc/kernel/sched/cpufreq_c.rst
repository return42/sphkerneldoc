.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/cpufreq.c

.. _`cpufreq_add_update_util_hook`:

cpufreq_add_update_util_hook
============================

.. c:function:: void cpufreq_add_update_util_hook(int cpu, struct update_util_data *data, void (*) func (struct update_util_data *data, u64 time, unsigned long util, unsigned long max)

    Populate the CPU's update_util_data pointer.

    :param int cpu:
        The CPU to set the pointer for.

    :param struct update_util_data \*data:
        New pointer value.

    :param (void (\*) func (struct update_util_data \*data, u64 time, unsigned long util, unsigned long max):
        Callback function to set for the CPU.

.. _`cpufreq_add_update_util_hook.description`:

Description
-----------

Set and publish the update_util_data pointer for the given CPU.

The update_util_data pointer of \ ``cpu``\  is set to \ ``data``\  and the callback
function pointer in the target struct update_util_data is set to \ ``func``\ .
That function will be called by \ :c:func:`cpufreq_update_util`\  from RCU-sched
read-side critical sections, so it must not sleep.  \ ``data``\  will always be
passed to it as the first argument which allows the function to get to the
target update_util_data structure and its container.

The update_util_data pointer of \ ``cpu``\  must be NULL when this function is
called or it will \ :c:func:`WARN`\  and return with no effect.

.. _`cpufreq_remove_update_util_hook`:

cpufreq_remove_update_util_hook
===============================

.. c:function:: void cpufreq_remove_update_util_hook(int cpu)

    Clear the CPU's update_util_data pointer.

    :param int cpu:
        The CPU to clear the pointer for.

.. _`cpufreq_remove_update_util_hook.description`:

Description
-----------

Clear the update_util_data pointer for the given CPU.

Callers must use RCU-sched callbacks to free any memory that might be
accessed via the old update_util_data pointer or invoke \ :c:func:`synchronize_sched`\ 
right after this function to avoid use-after-free.

.. This file was automatic generated / don't edit.

