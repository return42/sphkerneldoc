.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/trace_events.c

.. _`trace_set_clr_event`:

trace_set_clr_event
===================

.. c:function:: int trace_set_clr_event(const char *system, const char *event, int set)

    enable or disable an event

    :param system:
        system name to match (NULL for any system)
    :type system: const char \*

    :param event:
        event name to match (NULL for all events, within system)
    :type event: const char \*

    :param set:
        1 to enable, 0 to disable
    :type set: int

.. _`trace_set_clr_event.description`:

Description
-----------

This is a way for other parts of the kernel to enable or disable
event recording.

Returns 0 on success, -EINVAL if the parameters do not match any
registered events.

.. _`event_trace_add_tracer`:

event_trace_add_tracer
======================

.. c:function:: int event_trace_add_tracer(struct dentry *parent, struct trace_array *tr)

    add a instance of a trace_array to events

    :param parent:
        The parent dentry to place the files/directories for events in
    :type parent: struct dentry \*

    :param tr:
        The trace array associated with these events
    :type tr: struct trace_array \*

.. _`event_trace_add_tracer.description`:

Description
-----------

When a new instance is created, it needs to set up its events
directory, as well as other files associated with events. It also
creates the event hierachry in the \ ``parent``\ /events directory.

Returns 0 on success.

Must be called with event_mutex held.

.. This file was automatic generated / don't edit.

