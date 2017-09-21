.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/trace.c

.. _`trace_find_filtered_pid`:

trace_find_filtered_pid
=======================

.. c:function:: bool trace_find_filtered_pid(struct trace_pid_list *filtered_pids, pid_t search_pid)

    check if a pid exists in a filtered_pid list

    :param struct trace_pid_list \*filtered_pids:
        The list of pids to check

    :param pid_t search_pid:
        The PID to find in \ ``filtered_pids``\ 

.. _`trace_find_filtered_pid.description`:

Description
-----------

Returns true if \ ``search_pid``\  is fonud in \ ``filtered_pids``\ , and false otherwis.

.. _`trace_ignore_this_task`:

trace_ignore_this_task
======================

.. c:function:: bool trace_ignore_this_task(struct trace_pid_list *filtered_pids, struct task_struct *task)

    should a task be ignored for tracing

    :param struct trace_pid_list \*filtered_pids:
        The list of pids to check

    :param struct task_struct \*task:
        The task that should be ignored if not filtered

.. _`trace_ignore_this_task.description`:

Description
-----------

Checks if \ ``task``\  should be traced or not from \ ``filtered_pids``\ .
Returns true if \ ``task``\  should \*NOT\* be traced.
Returns false if \ ``task``\  should be traced.

.. _`trace_filter_add_remove_task`:

trace_filter_add_remove_task
============================

.. c:function:: void trace_filter_add_remove_task(struct trace_pid_list *pid_list, struct task_struct *self, struct task_struct *task)

    Add or remove a task from a pid_list

    :param struct trace_pid_list \*pid_list:
        The list to modify

    :param struct task_struct \*self:
        The current task for fork or NULL for exit

    :param struct task_struct \*task:
        The task to add or remove

.. _`trace_filter_add_remove_task.description`:

Description
-----------

If adding a task, if \ ``self``\  is defined, the task is only added if \ ``self``\ 
is also included in \ ``pid_list``\ . This happens on fork and tasks should
only be added when the parent is listed. If \ ``self``\  is NULL, then the
\ ``task``\  pid will be removed from the list, which would happen on exit
of a task.

.. _`trace_pid_next`:

trace_pid_next
==============

.. c:function:: void *trace_pid_next(struct trace_pid_list *pid_list, void *v, loff_t *pos)

    Used for seq_file to get to the next pid of a pid_list

    :param struct trace_pid_list \*pid_list:
        The pid list to show

    :param void \*v:
        The last pid that was shown (+1 the actual pid to let zero be displayed)

    :param loff_t \*pos:
        The position of the file

.. _`trace_pid_next.description`:

Description
-----------

This is used by the seq_file "next" operation to iterate the pids
listed in a trace_pid_list structure.

Returns the pid+1 as we want to display pid of zero, but NULL would
stop the iteration.

.. _`trace_pid_start`:

trace_pid_start
===============

.. c:function:: void *trace_pid_start(struct trace_pid_list *pid_list, loff_t *pos)

    Used for seq_file to start reading pid lists

    :param struct trace_pid_list \*pid_list:
        The pid list to show

    :param loff_t \*pos:
        The position of the file

.. _`trace_pid_start.description`:

Description
-----------

This is used by seq_file "start" operation to start the iteration
of listing pids.

Returns the pid+1 as we want to display pid of zero, but NULL would
stop the iteration.

.. _`trace_pid_show`:

trace_pid_show
==============

.. c:function:: int trace_pid_show(struct seq_file *m, void *v)

    show the current pid in seq_file processing

    :param struct seq_file \*m:
        The seq_file structure to write into

    :param void \*v:
        A void pointer of the pid (+1) value to display

.. _`trace_pid_show.description`:

Description
-----------

Can be directly used by seq_file operations to display the current
pid value.

.. _`tracing_is_enabled`:

tracing_is_enabled
==================

.. c:function:: int tracing_is_enabled( void)

    Show if global_trace has been disabled

    :param  void:
        no arguments

.. _`tracing_is_enabled.description`:

Description
-----------

Shows if the global trace has been enabled or not. It uses the
mirror flag "buffer_disabled" to be used in fast paths such as for
the irqsoff tracer. But it may be inaccurate due to races. If you
need to know the accurate state, use \ :c:func:`tracing_is_on`\  which is a little
slower, but accurate.

.. _`tracing_on`:

tracing_on
==========

.. c:function:: void tracing_on( void)

    enable tracing buffers

    :param  void:
        no arguments

.. _`tracing_on.description`:

Description
-----------

This function enables tracing buffers that may have been
disabled with tracing_off.

.. _`__trace_puts`:

__trace_puts
============

.. c:function:: int __trace_puts(unsigned long ip, const char *str, int size)

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

.. c:function:: int __trace_bputs(unsigned long ip, const char *str)

    write the pointer to a constant string into trace buffer

    :param unsigned long ip:
        The address of the caller

    :param const char \*str:
        The constant string to write to the buffer to

.. _`tracing_snapshot`:

tracing_snapshot
================

.. c:function:: void tracing_snapshot( void)

    take a snapshot of the current buffer.

    :param  void:
        no arguments

.. _`tracing_snapshot.description`:

Description
-----------

This causes a swap between the snapshot buffer and the current live
tracing buffer. You can use this to take snapshots of the live
trace when some condition is triggered, but continue to trace.

Note, make sure to allocate the snapshot with either
a \ :c:func:`tracing_snapshot_alloc`\ , or by doing it manually

.. _`tracing_snapshot.with`:

with
----

echo 1 > /sys/kernel/debug/tracing/snapshot

If the snapshot buffer is not allocated, it will stop tracing.
Basically making a permanent snapshot.

.. _`tracing_alloc_snapshot`:

tracing_alloc_snapshot
======================

.. c:function:: int tracing_alloc_snapshot( void)

    allocate snapshot buffer.

    :param  void:
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

.. c:function:: void tracing_snapshot_alloc( void)

    allocate and take a snapshot of the current buffer.

    :param  void:
        no arguments

.. _`tracing_snapshot_alloc.description`:

Description
-----------

This is similar to \ :c:func:`trace_snapshot`\ , but it will allocate the
snapshot buffer if it isn't already allocated. Use this only
where it is safe to sleep, as the allocation may sleep.

This causes a swap between the snapshot buffer and the current live
tracing buffer. You can use this to take snapshots of the live
trace when some condition is triggered, but continue to trace.

.. _`tracing_off`:

tracing_off
===========

.. c:function:: void tracing_off( void)

    turn off tracing buffers

    :param  void:
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

.. c:function:: int tracer_tracing_is_on(struct trace_array *tr)

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

.. c:function:: int tracing_is_on( void)

    show state of ring buffers enabled

    :param  void:
        no arguments

.. _`update_max_tr`:

update_max_tr
=============

.. c:function:: void update_max_tr(struct trace_array *tr, struct task_struct *tsk, int cpu)

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

Flip the buffers between the \ ``tr``\  and the max_tr and record information
about which task was the cause of this latency.

.. _`update_max_tr_single`:

update_max_tr_single
====================

.. c:function:: void update_max_tr_single(struct trace_array *tr, struct task_struct *tsk, int cpu)

    only copy one trace over, and reset the rest \ ``tr``\  - tracer \ ``tsk``\  - task with the latency \ ``cpu``\  - the cpu of the buffer to copy.

    :param struct trace_array \*tr:
        *undescribed*

    :param struct task_struct \*tsk:
        *undescribed*

    :param int cpu:
        *undescribed*

.. _`update_max_tr_single.description`:

Description
-----------

Flip the trace of a single CPU buffer between the \ ``tr``\  and the max_tr.

.. _`register_tracer`:

register_tracer
===============

.. c:function:: int register_tracer(struct tracer *type)

    register a tracer with the ftrace system. \ ``type``\  - the plugin for the tracer

    :param struct tracer \*type:
        *undescribed*

.. _`register_tracer.description`:

Description
-----------

Register a new plugin tracer.

.. _`tracing_start`:

tracing_start
=============

.. c:function:: void tracing_start( void)

    quick start of the tracer

    :param  void:
        no arguments

.. _`tracing_start.description`:

Description
-----------

If tracing is enabled but was stopped by tracing_stop,
this will start the tracer back up.

.. _`tracing_stop`:

tracing_stop
============

.. c:function:: void tracing_stop( void)

    quick stop of the tracer

    :param  void:
        no arguments

.. _`tracing_stop.description`:

Description
-----------

Light weight way to stop tracing. Use in conjunction with
tracing_start.

.. _`tracing_record_taskinfo`:

tracing_record_taskinfo
=======================

.. c:function:: void tracing_record_taskinfo(struct task_struct *task, int flags)

    record the task info of a task

    :param struct task_struct \*task:
        *undescribed*

    :param int flags:
        *undescribed*

.. _`tracing_record_taskinfo.description`:

Description
-----------

@task  - task to record
\ ``flags``\  - TRACE_RECORD_CMDLINE for recording comm
- TRACE_RECORD_TGID for recording tgid

.. _`tracing_record_taskinfo_sched_switch`:

tracing_record_taskinfo_sched_switch
====================================

.. c:function:: void tracing_record_taskinfo_sched_switch(struct task_struct *prev, struct task_struct *next, int flags)

    record task info for sched_switch

    :param struct task_struct \*prev:
        *undescribed*

    :param struct task_struct \*next:
        *undescribed*

    :param int flags:
        *undescribed*

.. _`tracing_record_taskinfo_sched_switch.description`:

Description
-----------

@prev - previous task during sched_switch
\ ``next``\  - next task during sched_switch
\ ``flags``\  - TRACE_RECORD_CMDLINE for recording comm
TRACE_RECORD_TGID for recording tgid

.. _`trace_buffered_event_enable`:

trace_buffered_event_enable
===========================

.. c:function:: void trace_buffered_event_enable( void)

    enable buffering events

    :param  void:
        no arguments

.. _`trace_buffered_event_enable.description`:

Description
-----------

When events are being filtered, it is quicker to use a temporary
buffer to write the event data into if there's a likely chance
that it will not be committed. The discard of the ring buffer
is not as fast as committing, and is much slower than copying
a commit.

When an event is to be filtered, allocate per cpu buffers to
write the event data into, and if the event is filtered and discarded
it is simply dropped, otherwise, the entire data is to be committed
in one shot.

.. _`trace_buffered_event_disable`:

trace_buffered_event_disable
============================

.. c:function:: void trace_buffered_event_disable( void)

    disable buffering events

    :param  void:
        no arguments

.. _`trace_buffered_event_disable.description`:

Description
-----------

When a filter is removed, it is faster to not use the buffered
events, and to commit directly into the ring buffer. Free up
the temp buffers when there are no more users. This requires
special synchronization with current events.

.. _`trace_dump_stack`:

trace_dump_stack
================

.. c:function:: void trace_dump_stack(int skip)

    record a stack back trace in the trace buffer

    :param int skip:
        Number of functions to skip (helper handlers)

.. _`trace_vbprintk`:

trace_vbprintk
==============

.. c:function:: int trace_vbprintk(unsigned long ip, const char *fmt, va_list args)

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

.. c:function:: int tracing_update_buffers( void)

    used by tracing facility to expand ring buffers

    :param  void:
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

.. c:function:: struct dentry *tracing_init_dentry( void)

    initialize top level trace array

    :param  void:
        no arguments

.. _`tracing_init_dentry.description`:

Description
-----------

This is called when creating files or directories in the tracing
directory. It is called via \ :c:func:`fs_initcall`\  by any of the boot up code
and expects to return the dentry of the top level tracing directory.

.. This file was automatic generated / don't edit.

