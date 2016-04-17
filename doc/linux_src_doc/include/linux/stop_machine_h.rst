.. -*- coding: utf-8; mode: rst -*-

==============
stop_machine.h
==============


.. _`stop_machine`:

stop_machine
============

.. c:function:: int stop_machine (cpu_stop_fn_t fn, void *data, const struct cpumask *cpus)

    :param cpu_stop_fn_t fn:
        the function to run

    :param void \*data:
        the data ptr for the @:c:func:`fn`

    :param const struct cpumask \*cpus:
        the cpus to run the @:c:func:`fn` on (NULL = any online cpu)



.. _`stop_machine.description`:

Description
-----------

This causes a thread to be scheduled on every cpu,
each of which disables interrupts.  The result is that no one is
holding a spinlock or inside any other preempt-disabled region when
@:c:func:`fn` runs.

This can be thought of as a very heavy write lock, equivalent to

