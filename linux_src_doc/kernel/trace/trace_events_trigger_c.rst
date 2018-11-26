.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/trace_events_trigger.c

.. _`event_triggers_call`:

event_triggers_call
===================

.. c:function:: enum event_trigger_type event_triggers_call(struct trace_event_file *file, void *rec, struct ring_buffer_event *event)

    Call triggers associated with a trace event

    :param file:
        The trace_event_file associated with the event
    :type file: struct trace_event_file \*

    :param rec:
        The trace entry for the event, NULL for unconditional invocation
    :type rec: void \*

    :param event:
        *undescribed*
    :type event: struct ring_buffer_event \*

.. _`event_triggers_call.description`:

Description
-----------

For each trigger associated with an event, invoke the trigger
function registered with the associated trigger command.  If rec is
non-NULL, it means that the trigger requires further processing and
shouldn't be unconditionally invoked.  If rec is non-NULL and the
trigger has a filter associated with it, rec will checked against
the filter and if the record matches the trigger will be invoked.
If the trigger is a 'post_trigger', meaning it shouldn't be invoked
in any case until the current event is written, the trigger
function isn't invoked but the bit associated with the deferred
trigger is set in the return value.

Returns an enum event_trigger_type value containing a set bit for
any trigger that should be deferred, ETT_NONE if nothing to defer.

Called from tracepoint handlers (with \ :c:func:`rcu_read_lock_sched`\  held).

.. _`event_triggers_call.return`:

Return
------

an enum event_trigger_type value containing a set bit for
any trigger that should be deferred, ETT_NONE if nothing to defer.

.. _`event_triggers_post_call`:

event_triggers_post_call
========================

.. c:function:: void event_triggers_post_call(struct trace_event_file *file, enum event_trigger_type tt)

    Call 'post_triggers' for a trace event

    :param file:
        The trace_event_file associated with the event
    :type file: struct trace_event_file \*

    :param tt:
        enum event_trigger_type containing a set bit for each trigger to invoke
    :type tt: enum event_trigger_type

.. _`event_triggers_post_call.description`:

Description
-----------

For each trigger associated with an event, invoke the trigger
function registered with the associated trigger command, if the
corresponding bit is set in the tt enum passed into this function.
See \ ``event_triggers_call``\  for details on how those bits are set.

Called from tracepoint handlers (with \ :c:func:`rcu_read_lock_sched`\  held).

.. _`event_trigger_print`:

event_trigger_print
===================

.. c:function:: int event_trigger_print(const char *name, struct seq_file *m, void *data, char *filter_str)

    Generic event_trigger_ops \ ``print``\  implementation

    :param name:
        The name of the event trigger
    :type name: const char \*

    :param m:
        The seq_file being printed to
    :type m: struct seq_file \*

    :param data:
        Trigger-specific data
    :type data: void \*

    :param filter_str:
        filter_str to print, if present
    :type filter_str: char \*

.. _`event_trigger_print.description`:

Description
-----------

Common implementation for event triggers to print themselves.

Usually wrapped by a function that simply sets the \ ``name``\  of the
trigger command and then invokes this.

.. _`event_trigger_print.return`:

Return
------

0 on success, errno otherwise

.. _`event_trigger_init`:

event_trigger_init
==================

.. c:function:: int event_trigger_init(struct event_trigger_ops *ops, struct event_trigger_data *data)

    Generic event_trigger_ops \ ``init``\  implementation

    :param ops:
        The trigger ops associated with the trigger
    :type ops: struct event_trigger_ops \*

    :param data:
        Trigger-specific data
    :type data: struct event_trigger_data \*

.. _`event_trigger_init.description`:

Description
-----------

Common implementation of event trigger initialization.

Usually used directly as the \ ``init``\  method in event trigger
implementations.

.. _`event_trigger_init.return`:

Return
------

0 on success, errno otherwise

.. _`event_trigger_free`:

event_trigger_free
==================

.. c:function:: void event_trigger_free(struct event_trigger_ops *ops, struct event_trigger_data *data)

    Generic event_trigger_ops \ ``free``\  implementation

    :param ops:
        The trigger ops associated with the trigger
    :type ops: struct event_trigger_ops \*

    :param data:
        Trigger-specific data
    :type data: struct event_trigger_data \*

.. _`event_trigger_free.description`:

Description
-----------

Common implementation of event trigger de-initialization.

Usually used directly as the \ ``free``\  method in event trigger
implementations.

.. _`clear_event_triggers`:

clear_event_triggers
====================

.. c:function:: void clear_event_triggers(struct trace_array *tr)

    Clear all triggers associated with a trace array

    :param tr:
        The trace array to clear
    :type tr: struct trace_array \*

.. _`clear_event_triggers.description`:

Description
-----------

For each trigger, the triggering event has its tm_ref decremented
via \ :c:func:`trace_event_trigger_enable_disable`\ , and any associated event
(in the case of enable/disable_event triggers) will have its sm_ref
decremented via \ :c:func:`free`\ ->trace_event_enable_disable().  That
combination effectively reverses the soft-mode/trigger state added
by trigger registration.

Must be called with event_mutex held.

.. _`update_cond_flag`:

update_cond_flag
================

.. c:function:: void update_cond_flag(struct trace_event_file *file)

    Set or reset the TRIGGER_COND bit

    :param file:
        The trace_event_file associated with the event
    :type file: struct trace_event_file \*

.. _`update_cond_flag.description`:

Description
-----------

If an event has triggers and any of those triggers has a filter or
a post_trigger, trigger invocation needs to be deferred until after
the current event has logged its data, and the event should have
its TRIGGER_COND bit set, otherwise the TRIGGER_COND bit should be
cleared.

.. _`register_trigger`:

register_trigger
================

.. c:function:: int register_trigger(char *glob, struct event_trigger_ops *ops, struct event_trigger_data *data, struct trace_event_file *file)

    Generic event_command \ ``reg``\  implementation

    :param glob:
        The raw string used to register the trigger
    :type glob: char \*

    :param ops:
        The trigger ops associated with the trigger
    :type ops: struct event_trigger_ops \*

    :param data:
        Trigger-specific data to associate with the trigger
    :type data: struct event_trigger_data \*

    :param file:
        The trace_event_file associated with the event
    :type file: struct trace_event_file \*

.. _`register_trigger.description`:

Description
-----------

Common implementation for event trigger registration.

Usually used directly as the \ ``reg``\  method in event command
implementations.

.. _`register_trigger.return`:

Return
------

0 on success, errno otherwise

.. _`unregister_trigger`:

unregister_trigger
==================

.. c:function:: void unregister_trigger(char *glob, struct event_trigger_ops *ops, struct event_trigger_data *test, struct trace_event_file *file)

    Generic event_command \ ``unreg``\  implementation

    :param glob:
        The raw string used to register the trigger
    :type glob: char \*

    :param ops:
        The trigger ops associated with the trigger
    :type ops: struct event_trigger_ops \*

    :param test:
        Trigger-specific data used to find the trigger to remove
    :type test: struct event_trigger_data \*

    :param file:
        The trace_event_file associated with the event
    :type file: struct trace_event_file \*

.. _`unregister_trigger.description`:

Description
-----------

Common implementation for event trigger unregistration.

Usually used directly as the \ ``unreg``\  method in event command
implementations.

.. _`event_trigger_callback`:

event_trigger_callback
======================

.. c:function:: int event_trigger_callback(struct event_command *cmd_ops, struct trace_event_file *file, char *glob, char *cmd, char *param)

    Generic event_command \ ``func``\  implementation

    :param cmd_ops:
        The command ops, used for trigger registration
    :type cmd_ops: struct event_command \*

    :param file:
        The trace_event_file associated with the event
    :type file: struct trace_event_file \*

    :param glob:
        The raw string used to register the trigger
    :type glob: char \*

    :param cmd:
        The cmd portion of the string used to register the trigger
    :type cmd: char \*

    :param param:
        The params portion of the string used to register the trigger
    :type param: char \*

.. _`event_trigger_callback.description`:

Description
-----------

Common implementation for event command parsing and trigger
instantiation.

Usually used directly as the \ ``func``\  method in event command
implementations.

.. _`event_trigger_callback.return`:

Return
------

0 on success, errno otherwise

.. _`set_trigger_filter`:

set_trigger_filter
==================

.. c:function:: int set_trigger_filter(char *filter_str, struct event_trigger_data *trigger_data, struct trace_event_file *file)

    Generic event_command \ ``set_filter``\  implementation

    :param filter_str:
        The filter string for the trigger, NULL to remove filter
    :type filter_str: char \*

    :param trigger_data:
        Trigger-specific data
    :type trigger_data: struct event_trigger_data \*

    :param file:
        The trace_event_file associated with the event
    :type file: struct trace_event_file \*

.. _`set_trigger_filter.description`:

Description
-----------

Common implementation for event command filter parsing and filter
instantiation.

Usually used directly as the \ ``set_filter``\  method in event command
implementations.

Also used to remove a filter (if filter_str = NULL).

.. _`set_trigger_filter.return`:

Return
------

0 on success, errno otherwise

.. _`find_named_trigger`:

find_named_trigger
==================

.. c:function:: struct event_trigger_data *find_named_trigger(const char *name)

    Find the common named trigger associated with \ ``name``\ 

    :param name:
        The name of the set of named triggers to find the common data for
    :type name: const char \*

.. _`find_named_trigger.description`:

Description
-----------

Named triggers are sets of triggers that share a common set of
trigger data.  The first named trigger registered with a given name
owns the common trigger data that the others subsequently
registered with the same name will reference.  This function
returns the common trigger data associated with that first
registered instance.

.. _`find_named_trigger.return`:

Return
------

the common trigger data for the given named trigger on
success, NULL otherwise.

.. _`is_named_trigger`:

is_named_trigger
================

.. c:function:: bool is_named_trigger(struct event_trigger_data *test)

    determine if a given trigger is a named trigger

    :param test:
        The trigger data to test
    :type test: struct event_trigger_data \*

.. _`is_named_trigger.return`:

Return
------

true if 'test' is a named trigger, false otherwise.

.. _`save_named_trigger`:

save_named_trigger
==================

.. c:function:: int save_named_trigger(const char *name, struct event_trigger_data *data)

    save the trigger in the named trigger list

    :param name:
        The name of the named trigger set
    :type name: const char \*

    :param data:
        The trigger data to save
    :type data: struct event_trigger_data \*

.. _`save_named_trigger.return`:

Return
------

0 if successful, negative error otherwise.

.. _`del_named_trigger`:

del_named_trigger
=================

.. c:function:: void del_named_trigger(struct event_trigger_data *data)

    delete a trigger from the named trigger list

    :param data:
        The trigger data to delete
    :type data: struct event_trigger_data \*

.. _`pause_named_trigger`:

pause_named_trigger
===================

.. c:function:: void pause_named_trigger(struct event_trigger_data *data)

    Pause all named triggers with the same name

    :param data:
        The trigger data of a named trigger to pause
    :type data: struct event_trigger_data \*

.. _`pause_named_trigger.description`:

Description
-----------

Pauses a named trigger along with all other triggers having the
same name.  Because named triggers share a common set of data,
pausing only one is meaningless, so pausing one named trigger needs
to pause all triggers with the same name.

.. _`unpause_named_trigger`:

unpause_named_trigger
=====================

.. c:function:: void unpause_named_trigger(struct event_trigger_data *data)

    Un-pause all named triggers with the same name

    :param data:
        The trigger data of a named trigger to unpause
    :type data: struct event_trigger_data \*

.. _`unpause_named_trigger.description`:

Description
-----------

Un-pauses a named trigger along with all other triggers having the
same name.  Because named triggers share a common set of data,
unpausing only one is meaningless, so unpausing one named trigger
needs to unpause all triggers with the same name.

.. _`set_named_trigger_data`:

set_named_trigger_data
======================

.. c:function:: void set_named_trigger_data(struct event_trigger_data *data, struct event_trigger_data *named_data)

    Associate common named trigger data

    :param data:
        The trigger data of a named trigger to unpause
    :type data: struct event_trigger_data \*

    :param named_data:
        *undescribed*
    :type named_data: struct event_trigger_data \*

.. _`set_named_trigger_data.description`:

Description
-----------

Named triggers are sets of triggers that share a common set of
trigger data.  The first named trigger registered with a given name
owns the common trigger data that the others subsequently
registered with the same name will reference.  This function
associates the common trigger data from the first trigger with the
given trigger.

.. This file was automatic generated / don't edit.

