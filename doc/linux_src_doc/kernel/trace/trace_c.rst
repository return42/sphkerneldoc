.. -*- coding: utf-8; mode: rst -*-

=======
trace.c
=======


.. _`tracing_is_enabled`:

tracing_is_enabled
==================

.. c:function:: int tracing_is_enabled ( void)

    Show if global_trace has been disabled

    :param void:
        no arguments



.. _`tracing_is_enabled.description`:

Description
-----------


Shows if the global trace has been enabled or not. It uses the
mirror flag "buffer_disabled" to be used in fast paths such as for
the irqsoff tracer. But it may be inaccurate due to races. If you
need to know the accurate state, use :c:func:`tracing_is_on` which is a little
slower, but accurate.



.. _`tracing_on`:

tracing_on
==========

.. c:function:: void tracing_on ( void)

    enable tracing buffers

    :param void:
        no arguments



.. _`tracing_on.description`:

Description
-----------


This function enables tracing buffers that may have been
disabled with tracing_off.



.. _`__trace_puts`:

__trace_puts
============

.. c:function:: int __trace_puts (unsigned long ip, const char *str, int size)

    write a constant string into the trace buffer.

    :param unsigned long ip:
        The address of the caller

    :param const char \*str:
        The constant string to write

    :param int size:
        The size of the string.



.. _`__trace_bputs`:

__trace_bputs
=============

.. c:function:: int __trace_bputs (unsigned long ip, const char *str)

    write the pointer to a constant string into trace buffer

    :param unsigned long ip:
        The address of the caller

    :param const char \*str:
        The constant string to write to the buffer to



.. _`tracing_snapshot`:

tracing_snapshot
================

.. c:function:: void tracing_snapshot ( void)

    take a snapshot of the current buffer.

    :param void:
        no arguments



.. _`tracing_snapshot.description`:

Description
-----------


This causes a swap between the snapshot buffer and the current live
tracing buffer. You can use this to take snapshots of the live
trace when some condition is triggered, but continue to trace.

Note, make sure to allocate the snapshot with either
a :c:func:`tracing_snapshot_alloc`, or by doing it manually



.. _`tracing_snapshot.with`:

with
----

echo 1 > /sys/kernel/debug/tracing/snapshot

If the snapshot buffer is not allocated, it will stop tracing.
Basically making a permanent snapshot.



.. _`tracing_alloc_snapshot`:

tracing_alloc_snapshot
======================

.. c:function:: int tracing_alloc_snapshot ( void)

    allocate snapshot buffer.

    :param void:
        no arguments



.. _`tracing_alloc_snapshot.description`:

Description
-----------


This only allocates the snapshot buffer if it isn't already
allocated - it doesn't also take a snapshot.

This is meant to be used in cases where the snapshot buffer needs
to be set up for events that can't sleep but need to be able to
trigger a snapshot.



.. _`tracing_snapshot_alloc`:

tracing_snapshot_alloc
======================

.. c:function:: void tracing_snapshot_alloc ( void)

    allocate and take a snapshot of the current buffer.

    :param void:
        no arguments



.. _`tracing_snapshot_alloc.description`:

Description
-----------


This is similar to :c:func:`trace_snapshot`, but it will allocate the
snapshot buffer if it isn't already allocated. Use this only
where it is safe to sleep, as the allocation may sleep.

This causes a swap between the snapshot buffer and the current live
tracing buffer. You can use this to take snapshots of the live
trace when some condition is triggered, but continue to trace.



.. _`tracing_off`:

tracing_off
===========

.. c:function:: void tracing_off ( void)

    turn off tracing buffers

    :param void:
        no arguments



.. _`tracing_off.description`:

Description
-----------


This function stops the tracing buffers from recording data.
It does not disable any overhead the tracers themselves may
be causing. This function simply causes all recording to
the ring buffers to fail.



.. _`tracer_tracing_is_on`:

tracer_tracing_is_on
====================

.. c:function:: int tracer_tracing_is_on (struct trace_array *tr)

    show real state of ring buffer enabled

    :param struct trace_array \*tr:
        the trace array to know if ring buffer is enabled



.. _`tracer_tracing_is_on.description`:

Description
-----------

Shows real state of the ring buffer if it is enabled or not.



.. _`tracing_is_on`:

tracing_is_on
=============

.. c:function:: int tracing_is_on ( void)

    show state of ring buffers enabled

    :param void:
        no arguments



.. _`update_max_tr`:

update_max_tr
=============

.. c:function:: void update_max_tr (struct trace_array *tr, struct task_struct *tsk, int cpu)

    snapshot all trace buffers from global_trace to max_tr

    :param struct trace_array \*tr:
        tracer

    :param struct task_struct \*tsk:
        the task with the latency

    :param int cpu:
        The cpu that initiated the trace.



.. _`update_max_tr.description`:

Description
-----------

Flip the buffers between the ``tr`` and the max_tr and record information
about which task was the cause of this latency.



.. _`update_max_tr_single`:

update_max_tr_single
====================

.. c:function:: void update_max_tr_single (struct trace_array *tr, struct task_struct *tsk, int cpu)

    only copy one trace over, and reset the rest @tr - tracer @tsk - task with the latency @cpu - the cpu of the buffer to copy.

    :param struct trace_array \*tr:

        *undescribed*

    :param struct task_struct \*tsk:

        *undescribed*

    :param int cpu:

        *undescribed*



.. _`update_max_tr_single.description`:

Description
-----------


Flip the trace of a single CPU buffer between the ``tr`` and the max_tr.



.. _`register_tracer`:

register_tracer
===============

.. c:function:: int register_tracer (struct tracer *type)

    register a tracer with the ftrace system. @type - the plugin for the tracer

    :param struct tracer \*type:

        *undescribed*



.. _`register_tracer.description`:

Description
-----------


Register a new plugin tracer.



.. _`tracing_start`:

tracing_start
=============

.. c:function:: void tracing_start ( void)

    quick start of the tracer

    :param void:
        no arguments



.. _`tracing_start.description`:

Description
-----------


If tracing is enabled but was stopped by tracing_stop,
this will start the tracer back up.



.. _`tracing_stop`:

tracing_stop
============

.. c:function:: void tracing_stop ( void)

    quick stop of the tracer

    :param void:
        no arguments



.. _`tracing_stop.description`:

Description
-----------


Light weight way to stop tracing. Use in conjunction with
tracing_start.



.. _`trace_dump_stack`:

trace_dump_stack
================

.. c:function:: void trace_dump_stack (int skip)

    record a stack back trace in the trace buffer

    :param int skip:
        Number of functions to skip (helper handlers)



.. _`trace_vbprintk`:

trace_vbprintk
==============

.. c:function:: int trace_vbprintk (unsigned long ip, const char *fmt, va_list args)

    write binary msg to tracing buffer

    :param unsigned long ip:

        *undescribed*

    :param const char \*fmt:

        *undescribed*

    :param va_list args:

        *undescribed*



.. _`tracing_update_buffers`:

tracing_update_buffers
======================

.. c:function:: int tracing_update_buffers ( void)

    used by tracing facility to expand ring buffers

    :param void:
        no arguments



.. _`tracing_update_buffers.description`:

Description
-----------



To save on memory when the tracing is never used on a system with it
configured in. The ring buffers are set to a minimum size. But once
a user starts to use the tracing facility, then they need to grow
to their default size.

This function is to be called when a tracer is about to be used.



.. _`tracing_init_dentry`:

tracing_init_dentry
===================

.. c:function:: struct dentry *tracing_init_dentry ( void)

    initialize top level trace array

    :param void:
        no arguments



.. _`tracing_init_dentry.description`:

Description
-----------


This is called when creating files or directories in the tracing
directory. It is called via :c:func:`fs_initcall` by any of the boot up code
and expects to return the dentry of the top level tracing directory.

