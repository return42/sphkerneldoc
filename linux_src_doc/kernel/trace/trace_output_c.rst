.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/trace_output.c

.. _`trace_print_hex_seq`:

trace_print_hex_seq
===================

.. c:function:: const char *trace_print_hex_seq(struct trace_seq *p, const unsigned char *buf, int buf_len, bool concatenate)

    print buffer as hex sequence

    :param struct trace_seq \*p:
        trace seq struct to write to

    :param const unsigned char \*buf:
        The buffer to print

    :param int buf_len:
        Length of \ ``buf``\  in bytes

    :param bool concatenate:
        Print \ ``buf``\  as single hex string or with spacing

.. _`trace_print_hex_seq.description`:

Description
-----------

Prints the passed buffer as a hex sequence either as a whole,
single hex string if \ ``concatenate``\  is true or with spacing after
each byte in case \ ``concatenate``\  is false.

.. _`trace_print_lat_fmt`:

trace_print_lat_fmt
===================

.. c:function:: int trace_print_lat_fmt(struct trace_seq *s, struct trace_entry *entry)

    print the irq, preempt and lockdep fields

    :param struct trace_seq \*s:
        trace seq struct to write to

    :param struct trace_entry \*entry:
        The trace entry field from the ring buffer

.. _`trace_print_lat_fmt.description`:

Description
-----------

Prints the generic fields of irqs off, in hard or softirq, preempt
count.

.. _`ftrace_find_event`:

ftrace_find_event
=================

.. c:function:: struct trace_event *ftrace_find_event(int type)

    find a registered event

    :param int type:
        the type of event to look for

.. _`ftrace_find_event.description`:

Description
-----------

Returns an event of type \ ``type``\  otherwise NULL
Called with \ :c:func:`trace_event_read_lock`\  held.

.. _`register_trace_event`:

register_trace_event
====================

.. c:function:: int register_trace_event(struct trace_event *event)

    register output for an event type

    :param struct trace_event \*event:
        the event type to register

.. _`register_trace_event.description`:

Description
-----------

Event types are stored in a hash and this hash is used to
find a way to print an event. If the \ ``event``\ ->type is set
then it will use that type, otherwise it will assign a
type to use.

If you assign your own type, please make sure it is added
to the trace_type enum in trace.h, to avoid collisions
with the dynamic types.

Returns the event type number or zero on error.

.. _`unregister_trace_event`:

unregister_trace_event
======================

.. c:function:: int unregister_trace_event(struct trace_event *event)

    remove a no longer used event

    :param struct trace_event \*event:
        the event to remove

.. This file was automatic generated / don't edit.

