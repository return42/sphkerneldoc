.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/smp.c

.. _`generic_smp_call_function_single_interrupt`:

generic_smp_call_function_single_interrupt
==========================================

.. c:function:: void generic_smp_call_function_single_interrupt( void)

    Execute SMP IPI callbacks

    :param void:
        no arguments
    :type void: 

.. _`generic_smp_call_function_single_interrupt.description`:

Description
-----------

Invoked by arch to handle an IPI for call function single.
Must be called with interrupts disabled.

.. _`flush_smp_call_function_queue`:

flush_smp_call_function_queue
=============================

.. c:function:: void flush_smp_call_function_queue(bool warn_cpu_offline)

    Flush pending smp-call-function callbacks

    :param warn_cpu_offline:
        If set to 'true', warn if callbacks were queued on an
        offline CPU. Skip this check if set to 'false'.
    :type warn_cpu_offline: bool

.. _`flush_smp_call_function_queue.description`:

Description
-----------

Flush any pending smp-call-function callbacks queued on this CPU. This is
invoked by the generic IPI handler, as well as by a CPU about to go offline,
to ensure that all pending IPI callbacks are run before it goes completely
offline.

Loop through the call_single_queue and run all the queued callbacks.
Must be called with interrupts disabled.

.. _`smp_call_function_single_async`:

smp_call_function_single_async
==============================

.. c:function:: int smp_call_function_single_async(int cpu, call_single_data_t *csd)

    Run an asynchronous function on a specific CPU.

    :param cpu:
        The CPU to run on.
    :type cpu: int

    :param csd:
        Pre-allocated and setup data structure
    :type csd: call_single_data_t \*

.. _`smp_call_function_single_async.description`:

Description
-----------

Like \ :c:func:`smp_call_function_single`\ , but the call is asynchonous and
can thus be done from contexts with disabled interrupts.

The caller passes his own pre-allocated data structure
(ie: embedded in an object) and is responsible for synchronizing it
such that the IPIs performed on the \ ``csd``\  are strictly serialized.

.. _`smp_call_function_single_async.note`:

NOTE
----

Be careful, there is unfortunately no current debugging facility to
validate the correctness of this serialization.

.. _`smp_call_function_many`:

smp_call_function_many
======================

.. c:function:: void smp_call_function_many(const struct cpumask *mask, smp_call_func_t func, void *info, bool wait)

    Run a function on a set of other CPUs.

    :param mask:
        The set of cpus to run on (only runs on online subset).
    :type mask: const struct cpumask \*

    :param func:
        The function to run. This must be fast and non-blocking.
    :type func: smp_call_func_t

    :param info:
        An arbitrary pointer to pass to the function.
    :type info: void \*

    :param wait:
        If true, wait (atomically) until function has completed
        on other CPUs.
    :type wait: bool

.. _`smp_call_function_many.description`:

Description
-----------

If \ ``wait``\  is true, then returns once \ ``func``\  has returned.

You must not call this function with disabled interrupts or from a
hardware interrupt handler or from a bottom half handler. Preemption
must be disabled when calling this function.

.. _`smp_call_function`:

smp_call_function
=================

.. c:function:: int smp_call_function(smp_call_func_t func, void *info, int wait)

    Run a function on all other CPUs.

    :param func:
        The function to run. This must be fast and non-blocking.
    :type func: smp_call_func_t

    :param info:
        An arbitrary pointer to pass to the function.
    :type info: void \*

    :param wait:
        If true, wait (atomically) until function has completed
        on other CPUs.
    :type wait: int

.. _`smp_call_function.description`:

Description
-----------

Returns 0.

If \ ``wait``\  is true, then returns once \ ``func``\  has returned; otherwise
it returns just before the target cpu calls \ ``func``\ .

You must not call this function with disabled interrupts or from a
hardware interrupt handler or from a bottom half handler.

.. _`on_each_cpu_mask`:

on_each_cpu_mask
================

.. c:function:: void on_each_cpu_mask(const struct cpumask *mask, smp_call_func_t func, void *info, bool wait)

    Run a function on processors specified by cpumask, which may include the local processor.

    :param mask:
        The set of cpus to run on (only runs on online subset).
    :type mask: const struct cpumask \*

    :param func:
        The function to run. This must be fast and non-blocking.
    :type func: smp_call_func_t

    :param info:
        An arbitrary pointer to pass to the function.
    :type info: void \*

    :param wait:
        If true, wait (atomically) until function has completed
        on other CPUs.
    :type wait: bool

.. _`on_each_cpu_mask.description`:

Description
-----------

If \ ``wait``\  is true, then returns once \ ``func``\  has returned.

You must not call this function with disabled interrupts or from a
hardware interrupt handler or from a bottom half handler.  The
exception is that it may be used during early boot while
early_boot_irqs_disabled is set.

.. _`kick_all_cpus_sync`:

kick_all_cpus_sync
==================

.. c:function:: void kick_all_cpus_sync( void)

    Force all cpus out of idle

    :param void:
        no arguments
    :type void: 

.. _`kick_all_cpus_sync.description`:

Description
-----------

Used to synchronize the update of pm_idle function pointer. It's
called after the pointer is updated and returns after the dummy
callback function has been executed on all cpus. The execution of
the function can only happen on the remote cpus after they have
left the idle function which had been called via pm_idle function
pointer. So it's guaranteed that nothing uses the previous pointer
anymore.

.. _`wake_up_all_idle_cpus`:

wake_up_all_idle_cpus
=====================

.. c:function:: void wake_up_all_idle_cpus( void)

    break all cpus out of idle wake_up_all_idle_cpus try to break all cpus which is in idle state even including idle polling cpus, for non-idle cpus, we will do nothing for them.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

