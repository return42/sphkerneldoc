.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/stop_machine.h

.. _`stop_machine`:

stop_machine
============

.. c:function:: int stop_machine(cpu_stop_fn_t fn, void *data, const struct cpumask *cpus)

    freeze the machine on all CPUs and run this function

    :param cpu_stop_fn_t fn:
        the function to run

    :param void \*data:
        the data ptr for the \ ``fn``\ ()

    :param const struct cpumask \*cpus:
        the cpus to run the \ ``fn``\ () on (NULL = any online cpu)

.. _`stop_machine.description`:

Description
-----------

This causes a thread to be scheduled on every cpu,
each of which disables interrupts.  The result is that no one is
holding a spinlock or inside any other preempt-disabled region when
\ ``fn``\ () runs.

This can be thought of as a very heavy write lock, equivalent to
grabbing every spinlock in the kernel.

Protects against CPU hotplug.

.. _`stop_machine_cpuslocked`:

stop_machine_cpuslocked
=======================

.. c:function:: int stop_machine_cpuslocked(cpu_stop_fn_t fn, void *data, const struct cpumask *cpus)

    freeze the machine on all CPUs and run this function

    :param cpu_stop_fn_t fn:
        the function to run

    :param void \*data:
        the data ptr for the \ ``fn``\ ()

    :param const struct cpumask \*cpus:
        the cpus to run the \ ``fn``\ () on (NULL = any online cpu)

.. _`stop_machine_cpuslocked.description`:

Description
-----------

Same as above. Must be called from with in a \ :c:func:`cpus_read_lock`\  protected
region. Avoids nested calls to \ :c:func:`cpus_read_lock`\ .

.. This file was automatic generated / don't edit.

