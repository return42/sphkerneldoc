.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/stop_machine.c

.. _`stop_one_cpu`:

stop_one_cpu
============

.. c:function:: int stop_one_cpu(unsigned int cpu, cpu_stop_fn_t fn, void *arg)

    stop a cpu

    :param cpu:
        cpu to stop
    :type cpu: unsigned int

    :param fn:
        function to execute
    :type fn: cpu_stop_fn_t

    :param arg:
        argument to \ ``fn``\ 
    :type arg: void \*

.. _`stop_one_cpu.description`:

Description
-----------

Execute \ ``fn``\ (@arg) on \ ``cpu``\ .  \ ``fn``\  is run in a process context with
the highest priority preempting any task on the cpu and
monopolizing it.  This function returns after the execution is
complete.

This function doesn't guarantee \ ``cpu``\  stays online till \ ``fn``\ 
completes.  If \ ``cpu``\  goes down in the middle, execution may happen
partially or fully on different cpus.  \ ``fn``\  should either be ready
for that or the caller should ensure that \ ``cpu``\  stays online until
this function completes.

.. _`stop_one_cpu.context`:

Context
-------

Might sleep.

.. _`stop_one_cpu.return`:

Return
------

-ENOENT if \ ``fn``\ (@arg) was not executed because \ ``cpu``\  was offline;
otherwise, the return value of \ ``fn``\ .

.. _`stop_two_cpus`:

stop_two_cpus
=============

.. c:function:: int stop_two_cpus(unsigned int cpu1, unsigned int cpu2, cpu_stop_fn_t fn, void *arg)

    stops two cpus

    :param cpu1:
        the cpu to stop
    :type cpu1: unsigned int

    :param cpu2:
        the other cpu to stop
    :type cpu2: unsigned int

    :param fn:
        function to execute
    :type fn: cpu_stop_fn_t

    :param arg:
        argument to \ ``fn``\ 
    :type arg: void \*

.. _`stop_two_cpus.description`:

Description
-----------

Stops both the current and specified CPU and runs \ ``fn``\  on one of them.

returns when both are completed.

.. _`stop_one_cpu_nowait`:

stop_one_cpu_nowait
===================

.. c:function:: bool stop_one_cpu_nowait(unsigned int cpu, cpu_stop_fn_t fn, void *arg, struct cpu_stop_work *work_buf)

    stop a cpu but don't wait for completion

    :param cpu:
        cpu to stop
    :type cpu: unsigned int

    :param fn:
        function to execute
    :type fn: cpu_stop_fn_t

    :param arg:
        argument to \ ``fn``\ 
    :type arg: void \*

    :param work_buf:
        pointer to cpu_stop_work structure
    :type work_buf: struct cpu_stop_work \*

.. _`stop_one_cpu_nowait.description`:

Description
-----------

Similar to \ :c:func:`stop_one_cpu`\  but doesn't wait for completion.  The
caller is responsible for ensuring \ ``work_buf``\  is currently unused
and will remain untouched until stopper starts executing \ ``fn``\ .

.. _`stop_one_cpu_nowait.context`:

Context
-------

Don't care.

.. _`stop_one_cpu_nowait.return`:

Return
------

true if cpu_stop_work was queued successfully and \ ``fn``\  will be called,
false otherwise.

.. _`stop_cpus`:

stop_cpus
=========

.. c:function:: int stop_cpus(const struct cpumask *cpumask, cpu_stop_fn_t fn, void *arg)

    stop multiple cpus

    :param cpumask:
        cpus to stop
    :type cpumask: const struct cpumask \*

    :param fn:
        function to execute
    :type fn: cpu_stop_fn_t

    :param arg:
        argument to \ ``fn``\ 
    :type arg: void \*

.. _`stop_cpus.description`:

Description
-----------

Execute \ ``fn``\ (@arg) on online cpus in \ ``cpumask``\ .  On each target cpu,
\ ``fn``\  is run in a process context with the highest priority
preempting any task on the cpu and monopolizing it.  This function
returns after all executions are complete.

This function doesn't guarantee the cpus in \ ``cpumask``\  stay online
till \ ``fn``\  completes.  If some cpus go down in the middle, execution
on the cpu may happen partially or fully on different cpus.  \ ``fn``\ 
should either be ready for that or the caller should ensure that
the cpus stay online until this function completes.

All \ :c:func:`stop_cpus`\  calls are serialized making it safe for \ ``fn``\  to wait
for all cpus to start executing it.

.. _`stop_cpus.context`:

Context
-------

Might sleep.

.. _`stop_cpus.return`:

Return
------

-ENOENT if \ ``fn``\ (@arg) was not executed at all because all cpus in
\ ``cpumask``\  were offline; otherwise, 0 if all executions of \ ``fn``\ 
returned 0, any non zero return value if any returned non zero.

.. _`try_stop_cpus`:

try_stop_cpus
=============

.. c:function:: int try_stop_cpus(const struct cpumask *cpumask, cpu_stop_fn_t fn, void *arg)

    try to stop multiple cpus

    :param cpumask:
        cpus to stop
    :type cpumask: const struct cpumask \*

    :param fn:
        function to execute
    :type fn: cpu_stop_fn_t

    :param arg:
        argument to \ ``fn``\ 
    :type arg: void \*

.. _`try_stop_cpus.description`:

Description
-----------

Identical to \ :c:func:`stop_cpus`\  except that it fails with -EAGAIN if
someone else is already using the facility.

.. _`try_stop_cpus.context`:

Context
-------

Might sleep.

.. _`try_stop_cpus.return`:

Return
------

-EAGAIN if someone else is already stopping cpus, -ENOENT if
\ ``fn``\ (@arg) was not executed at all because all cpus in \ ``cpumask``\  were
offline; otherwise, 0 if all executions of \ ``fn``\  returned 0, any non
zero return value if any returned non zero.

.. _`stop_machine_from_inactive_cpu`:

stop_machine_from_inactive_cpu
==============================

.. c:function:: int stop_machine_from_inactive_cpu(cpu_stop_fn_t fn, void *data, const struct cpumask *cpus)

    \ :c:func:`stop_machine`\  from inactive CPU

    :param fn:
        the function to run
    :type fn: cpu_stop_fn_t

    :param data:
        the data ptr for the \ ``fn``\ ()
    :type data: void \*

    :param cpus:
        the cpus to run the \ ``fn``\ () on (NULL = any online cpu)
    :type cpus: const struct cpumask \*

.. _`stop_machine_from_inactive_cpu.description`:

Description
-----------

This is identical to \ :c:func:`stop_machine`\  but can be called from a CPU which
is not active.  The local CPU is in the process of hotplug (so no other
CPU hotplug can start) and not marked active and doesn't have enough
context to sleep.

This function provides \ :c:func:`stop_machine`\  functionality for such state by
using busy-wait for synchronization and executing \ ``fn``\  directly for local
CPU.

.. _`stop_machine_from_inactive_cpu.context`:

Context
-------

Local CPU is inactive.  Temporarily stops all active CPUs.

.. _`stop_machine_from_inactive_cpu.return`:

Return
------

0 if all executions of \ ``fn``\  returned 0, any non zero return value if any
returned non zero.

.. This file was automatic generated / don't edit.

