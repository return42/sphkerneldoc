.. -*- coding: utf-8; mode: rst -*-

=====
cpu.c
=====


.. _`cpuhp_invoke_callback`:

cpuhp_invoke_callback
=====================

.. c:function:: int cpuhp_invoke_callback (unsigned int cpu, enum cpuhp_state step, int (*cb) (unsigned int)

    :param unsigned int cpu:
        The cpu for which the callback should be invoked

    :param enum cpuhp_state step:
        The step in the state machine

    :param int (\*cb) (unsigned int):
        The callback function to invoke



.. _`cpuhp_invoke_callback.description`:

Description
-----------

Called from cpu hotplug and from the state register machinery



.. _`clear_tasks_mm_cpumask`:

clear_tasks_mm_cpumask
======================

.. c:function:: void clear_tasks_mm_cpumask (int cpu)

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

.. c:function:: void notify_cpu_starting (unsigned int cpu)

    call the CPU_STARTING notifiers

    :param unsigned int cpu:
        cpu that just started



.. _`notify_cpu_starting.description`:

Description
-----------

This function calls the cpu_chain notifiers with CPU_STARTING.
It must be called by the arch code on the new cpu, before the new cpu
enables interrupts and before the "boot" cpu returns from :c:func:`__cpu_up`.



.. _`__cpuhp_setup_state`:

__cpuhp_setup_state
===================

.. c:function:: int __cpuhp_setup_state (enum cpuhp_state state, const char *name, bool invoke, int (*startup) (unsigned int cpu, int (*teardown) (unsigned int cpu)

    Setup the callbacks for an hotplug machine state

    :param enum cpuhp_state state:
        The state to setup

    :param const char \*name:

        *undescribed*

    :param bool invoke:
        If true, the startup function is invoked for cpus where
        cpu state >= ``state``

    :param int (\*startup) (unsigned int cpu):
        startup callback function

    :param int (\*teardown) (unsigned int cpu):
        teardown callback function



.. _`__cpuhp_setup_state.description`:

Description
-----------

Returns 0 if successful, otherwise a proper error code



.. _`__cpuhp_remove_state`:

__cpuhp_remove_state
====================

.. c:function:: void __cpuhp_remove_state (enum cpuhp_state state, bool invoke)

    Remove the callbacks for an hotplug machine state

    :param enum cpuhp_state state:
        The state to remove

    :param bool invoke:
        If true, the teardown function is invoked for cpus where
        cpu state >= ``state``



.. _`__cpuhp_remove_state.description`:

Description
-----------

The teardown callback is currently not allowed to fail. Think
about module removal!

