.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/cpu.c

.. _`cpuhp_invoke_callback`:

cpuhp_invoke_callback
=====================

.. c:function:: int cpuhp_invoke_callback(unsigned int cpu, enum cpuhp_state state, bool bringup, struct hlist_node *node, struct hlist_node **lastp)

    :param unsigned int cpu:
        The cpu for which the callback should be invoked

    :param enum cpuhp_state state:
        The state to do callbacks for

    :param bool bringup:
        True if the bringup callback should be invoked

    :param struct hlist_node \*node:
        For multi-instance, do a single entry callback for install/remove

    :param struct hlist_node \*\*lastp:
        For multi-instance rollback, remember how far we got

.. _`cpuhp_invoke_callback.description`:

Description
-----------

Called from cpu hotplug and from the state register machinery.

.. _`clear_tasks_mm_cpumask`:

clear_tasks_mm_cpumask
======================

.. c:function:: void clear_tasks_mm_cpumask(int cpu)

    Safely clear tasks' mm_cpumask for a CPU

    :param int cpu:
        a CPU id

.. _`clear_tasks_mm_cpumask.description`:

Description
-----------

This function walks all processes, finds a valid mm struct for each one and
then clears a corresponding bit in mm's cpumask.  While this all sounds
trivial, there are various non-obvious corner cases, which this function
tries to solve in a safe manner.

Also note that the function uses a somewhat relaxed locking scheme, so it may
be called only for an already offlined CPU.

.. _`notify_cpu_starting`:

notify_cpu_starting
===================

.. c:function:: void notify_cpu_starting(unsigned int cpu)

    Invoke the callbacks on the starting CPU

    :param unsigned int cpu:
        cpu that just started

.. _`notify_cpu_starting.description`:

Description
-----------

It must be called by the arch code on the new cpu, before the new cpu
enables interrupts and before the "boot" cpu returns from \__cpu_up().

.. _`__cpuhp_setup_state_cpuslocked`:

__cpuhp_setup_state_cpuslocked
==============================

.. c:function:: int __cpuhp_setup_state_cpuslocked(enum cpuhp_state state, const char *name, bool invoke, int (*startup)(unsigned int cpu), int (*teardown)(unsigned int cpu), bool multi_instance)

    Setup the callbacks for an hotplug machine state

    :param enum cpuhp_state state:
        The state to setup

    :param const char \*name:
        *undescribed*

    :param bool invoke:
        If true, the startup function is invoked for cpus where
        cpu state >= \ ``state``\ 

    :param int (\*startup)(unsigned int cpu):
        startup callback function

    :param int (\*teardown)(unsigned int cpu):
        teardown callback function

    :param bool multi_instance:
        State is set up for multiple instances which get
        added afterwards.

.. _`__cpuhp_setup_state_cpuslocked.description`:

Description
-----------

The caller needs to hold cpus read locked while calling this function.

.. _`__cpuhp_setup_state_cpuslocked.on-success`:

On success
----------

Positive state number if \ ``state``\  is CPUHP_AP_ONLINE_DYN
0 for all other states

.. _`__cpuhp_setup_state_cpuslocked.on-failure`:

On failure
----------

proper (negative) error code

.. _`__cpuhp_remove_state_cpuslocked`:

__cpuhp_remove_state_cpuslocked
===============================

.. c:function:: void __cpuhp_remove_state_cpuslocked(enum cpuhp_state state, bool invoke)

    Remove the callbacks for an hotplug machine state

    :param enum cpuhp_state state:
        The state to remove

    :param bool invoke:
        If true, the teardown function is invoked for cpus where
        cpu state >= \ ``state``\ 

.. _`__cpuhp_remove_state_cpuslocked.description`:

Description
-----------

The caller needs to hold cpus read locked while calling this function.
The teardown callback is currently not allowed to fail. Think
about module removal!

.. This file was automatic generated / don't edit.

