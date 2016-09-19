.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/trace.h

.. _`tracer`:

struct tracer
=============

.. c:type:: struct tracer

    a specific tracer and its callbacks to interact with tracefs

.. _`tracer.definition`:

Definition
----------

.. code-block:: c

    struct tracer {
        const char *name;
        int (*init)(struct trace_array *tr);
        void (*reset)(struct trace_array *tr);
        void (*start)(struct trace_array *tr);
        void (*stop)(struct trace_array *tr);
        int (*update_thresh)(struct trace_array *tr);
        void (*open)(struct trace_iterator *iter);
        void (*pipe_open)(struct trace_iterator *iter);
        void (*close)(struct trace_iterator *iter);
        void (*pipe_close)(struct trace_iterator *iter);
        ssize_t (*read)(struct trace_iterator *iter,struct file *filp, char __user *ubuf,size_t cnt, loff_t *ppos);
        ssize_t (*splice_read)(struct trace_iterator *iter,struct file *filp,loff_t *ppos,struct pipe_inode_info *pipe,size_t len,unsigned int flags);
        #ifdef CONFIG_FTRACE_STARTUP_TEST
        int (*selftest)(struct tracer *trace,struct trace_array *tr);
        #endif
        void (*print_header)(struct seq_file *m);
        enum print_line_t (*print_line)(struct trace_iterator *iter);
        int (*set_flag)(struct trace_array *tr,u32 old_flags, u32 bit, int set);
        int (*flag_changed)(struct trace_array *tr,u32 mask, int set);
        struct tracer *next;
        struct tracer_flags *flags;
        int enabled;
        int ref;
        bool print_max;
        bool allow_instances;
        #ifdef CONFIG_TRACER_MAX_TRACE
        bool use_max_tr;
        #endif
    }

.. _`tracer.members`:

Members
-------

name
    the name chosen to select it on the available_tracers file

init
    called when one switches to this tracer (echo name > current_tracer)

reset
    called when one switches to another tracer

start
    called when tracing is unpaused (echo 1 > tracing_on)

stop
    called when tracing is paused (echo 0 > tracing_on)

update_thresh
    called when tracing_thresh is updated

open
    called when the trace file is opened

pipe_open
    called when the trace_pipe file is opened

close
    called when the trace file is released

pipe_close
    called when the trace_pipe file is released

read
    override the default read callback on trace_pipe

splice_read
    override the default splice_read callback on trace_pipe

selftest
    selftest to run on boot (see trace_selftest.c)

print_header
    *undescribed*

print_line
    callback that prints a trace

set_flag
    signals one of your private flags changed (trace_options file)

flag_changed
    *undescribed*

next
    *undescribed*

flags
    your private flags

enabled
    *undescribed*

ref
    *undescribed*

print_max
    *undescribed*

allow_instances
    *undescribed*

use_max_tr
    *undescribed*

.. _`event_trigger_unlock_commit`:

event_trigger_unlock_commit
===========================

.. c:function:: void event_trigger_unlock_commit(struct trace_event_file *file, struct ring_buffer *buffer, struct ring_buffer_event *event, void *entry, unsigned long irq_flags, int pc)

    handle triggers and finish event commit

    :param struct trace_event_file \*file:
        The file pointer assoctiated to the event

    :param struct ring_buffer \*buffer:
        The ring buffer that the event is being written to

    :param struct ring_buffer_event \*event:
        The event meta data in the ring buffer

    :param void \*entry:
        The event itself

    :param unsigned long irq_flags:
        The state of the interrupts at the start of the event

    :param int pc:
        The state of the preempt count at the start of the event.

.. _`event_trigger_unlock_commit.description`:

Description
-----------

This is a helper function to handle triggers that require data
from the event itself. It also tests the event against filters and
if the event is soft disabled and should be discarded.

.. _`event_trigger_unlock_commit_regs`:

event_trigger_unlock_commit_regs
================================

.. c:function:: void event_trigger_unlock_commit_regs(struct trace_event_file *file, struct ring_buffer *buffer, struct ring_buffer_event *event, void *entry, unsigned long irq_flags, int pc, struct pt_regs *regs)

    handle triggers and finish event commit

    :param struct trace_event_file \*file:
        The file pointer assoctiated to the event

    :param struct ring_buffer \*buffer:
        The ring buffer that the event is being written to

    :param struct ring_buffer_event \*event:
        The event meta data in the ring buffer

    :param void \*entry:
        The event itself

    :param unsigned long irq_flags:
        The state of the interrupts at the start of the event

    :param int pc:
        The state of the preempt count at the start of the event.

    :param struct pt_regs \*regs:
        *undescribed*

.. _`event_trigger_unlock_commit_regs.description`:

Description
-----------

This is a helper function to handle triggers that require data
from the event itself. It also tests the event against filters and
if the event is soft disabled and should be discarded.

Same as \ :c:func:`event_trigger_unlock_commit`\  but calls
\ :c:func:`trace_buffer_unlock_commit_regs`\  instead of \ :c:func:`trace_buffer_unlock_commit`\ .

.. _`event_trigger_ops`:

struct event_trigger_ops
========================

.. c:type:: struct event_trigger_ops

    callbacks for trace event triggers

.. _`event_trigger_ops.definition`:

Definition
----------

.. code-block:: c

    struct event_trigger_ops {
        void (*func)(struct event_trigger_data *data,void *rec);
        int (*init)(struct event_trigger_ops *ops,struct event_trigger_data *data);
        void (*free)(struct event_trigger_ops *ops,struct event_trigger_data *data);
        int (*print)(struct seq_file *m,struct event_trigger_ops *ops,struct event_trigger_data *data);
    }

.. _`event_trigger_ops.members`:

Members
-------

func
    The trigger 'probe' function called when the triggering
    event occurs.  The data passed into this callback is the data
    that was supplied to the event_command @\ :c:func:`reg`\  function that
    registered the trigger (see struct event_command) along with
    the trace record, rec.

init
    An optional initialization function called for the trigger
    when the trigger is registered (via the event_command \ :c:func:`reg`\ 
    function).  This can be used to perform per-trigger
    initialization such as incrementing a per-trigger reference
    count, for instance.  This is usually implemented by the
    generic utility function @\ :c:func:`event_trigger_init`\  (see
    trace_event_triggers.c).

free
    An optional de-initialization function called for the
    trigger when the trigger is unregistered (via the
    event_command @\ :c:func:`reg`\  function).  This can be used to perform
    per-trigger de-initialization such as decrementing a
    per-trigger reference count and freeing corresponding trigger
    data, for instance.  This is usually implemented by the
    generic utility function @\ :c:func:`event_trigger_free`\  (see
    trace_event_triggers.c).

print
    The callback function invoked to have the trigger print
    itself.  This is usually implemented by a wrapper function
    that calls the generic utility function @\ :c:func:`event_trigger_print`\ 
    (see trace_event_triggers.c).

.. _`event_trigger_ops.description`:

Description
-----------

The methods in this structure provide per-event trigger hooks for
various trigger operations.

All the methods below, except for @\ :c:func:`init`\  and @\ :c:func:`free`\ , must be
implemented.

.. _`event_command`:

struct event_command
====================

.. c:type:: struct event_command

    callbacks and data members for event commands

.. _`event_command.definition`:

Definition
----------

.. code-block:: c

    struct event_command {
        struct list_head list;
        char *name;
        enum event_trigger_type trigger_type;
        int flags;
        int (*func)(struct event_command *cmd_ops,struct trace_event_file *file,char *glob, char *cmd, char *params);
        int (*reg)(char *glob,struct event_trigger_ops *ops,struct event_trigger_data *data,struct trace_event_file *file);
        void (*unreg)(char *glob,struct event_trigger_ops *ops,struct event_trigger_data *data,struct trace_event_file *file);
        void (*unreg_all)(struct trace_event_file *file);
        int (*set_filter)(char *filter_str,struct event_trigger_data *data,struct trace_event_file *file);
        struct event_trigger_ops *(*get_trigger_ops)(char *cmd, char *param);
    }

.. _`event_command.members`:

Members
-------

list
    *undescribed*

name
    The unique name that identifies the event command.  This is
    the name used when setting triggers via trigger files.

trigger_type
    A unique id that identifies the event command
    'type'.  This value has two purposes, the first to ensure that
    only one trigger of the same type can be set at a given time
    for a particular event e.g. it doesn't make sense to have both
    a traceon and traceoff trigger attached to a single event at
    the same time, so traceon and traceoff have the same type
    though they have different names.  The \ ``trigger_type``\  value is
    also used as a bit value for deferring the actual trigger
    action until after the current event is finished.  Some
    commands need to do this if they themselves log to the trace
    buffer (see the @\ :c:func:`post_trigger`\  member below).  \ ``trigger_type``\ 
    values are defined by adding new values to the trigger_type
    enum in include/linux/trace_events.h.

flags
    See the enum event_command_flags below.

func
    The callback function responsible for parsing and
    registering the trigger written to the 'trigger' file by the
    user.  It allocates the trigger instance and registers it with
    the appropriate trace event.  It makes use of the other
    event_command callback functions to orchestrate this, and is
    usually implemented by the generic utility function
    @\ :c:func:`event_trigger_callback`\  (see trace_event_triggers.c).

reg
    Adds the trigger to the list of triggers associated with the
    event, and enables the event trigger itself, after
    initializing it (via the event_trigger_ops @\ :c:func:`init`\  function).
    This is also where commands can use the \ ``trigger_type``\  value to
    make the decision as to whether or not multiple instances of
    the trigger should be allowed.  This is usually implemented by
    the generic utility function @\ :c:func:`register_trigger`\  (see
    trace_event_triggers.c).

unreg
    Removes the trigger from the list of triggers associated
    with the event, and disables the event trigger itself, after
    initializing it (via the event_trigger_ops @\ :c:func:`free`\  function).
    This is usually implemented by the generic utility function
    @\ :c:func:`unregister_trigger`\  (see trace_event_triggers.c).

unreg_all
    An optional function called to remove all the triggers
    from the list of triggers associated with the event.  Called
    when a trigger file is opened in truncate mode.

set_filter
    An optional function called to parse and set a filter
    for the trigger.  If no @\ :c:func:`set_filter`\  method is set for the
    event command, filters set by the user for the command will be
    ignored.  This is usually implemented by the generic utility
    function @\ :c:func:`set_trigger_filter`\  (see trace_event_triggers.c).

get_trigger_ops
    The callback function invoked to retrieve the
    event_trigger_ops implementation associated with the command.

.. _`event_command.description`:

Description
-----------

Event commands are invoked by users by writing the command name
into the 'trigger' file associated with a trace event.  The
parameters associated with a specific invocation of an event
command are used to create an event trigger instance, which is
added to the list of trigger instances associated with that trace
event.  When the event is hit, the set of triggers associated with
that event is invoked.

The data members in this structure provide per-event command data
for various event commands.

All the data members below, except for \ ``post_trigger``\ , must be set
for each event command.

All the methods below, except for @\ :c:func:`set_filter`\  and @\ :c:func:`unreg_all`\ ,
must be implemented.

.. _`event_command_flags`:

enum event_command_flags
========================

.. c:type:: enum event_command_flags

    flags for struct event_command

.. _`event_command_flags.definition`:

Definition
----------

.. code-block:: c

    enum event_command_flags {
        EVENT_CMD_FL_POST_TRIGGER,
        EVENT_CMD_FL_NEEDS_REC
    };

.. _`event_command_flags.constants`:

Constants
---------

EVENT_CMD_FL_POST_TRIGGER
    *undescribed*

EVENT_CMD_FL_NEEDS_REC
    *undescribed*

.. This file was automatic generated / don't edit.

