.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/traceevent/trace-seq.c

.. _`trace_seq_init`:

trace_seq_init
==============

.. c:function:: void trace_seq_init(struct trace_seq *s)

    initialize the trace_seq structure

    :param s:
        a pointer to the trace_seq structure to initialize
    :type s: struct trace_seq \*

.. _`trace_seq_reset`:

trace_seq_reset
===============

.. c:function:: void trace_seq_reset(struct trace_seq *s)

    re-initialize the trace_seq structure

    :param s:
        a pointer to the trace_seq structure to reset
    :type s: struct trace_seq \*

.. _`trace_seq_destroy`:

trace_seq_destroy
=================

.. c:function:: void trace_seq_destroy(struct trace_seq *s)

    free up memory of a trace_seq

    :param s:
        a pointer to the trace_seq to free the buffer
    :type s: struct trace_seq \*

.. _`trace_seq_destroy.description`:

Description
-----------

Only frees the buffer, not the trace_seq struct itself.

.. _`trace_seq_printf`:

trace_seq_printf
================

.. c:function:: int trace_seq_printf(struct trace_seq *s, const char *fmt,  ...)

    sequence printing of trace information

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

    :param fmt:
        printf format string
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`trace_seq_printf.description`:

Description
-----------

It returns 0 if the trace oversizes the buffer's free
space, 1 otherwise.

The tracer may use either sequence operations or its own
copy to user routines. To simplify formating of a trace
trace_seq_printf is used to store strings into a special
buffer (@s). Then the output may be either used by
the sequencer or pulled into another buffer.

.. _`trace_seq_vprintf`:

trace_seq_vprintf
=================

.. c:function:: int trace_seq_vprintf(struct trace_seq *s, const char *fmt, va_list args)

    sequence printing of trace information

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

    :param fmt:
        printf format string
    :type fmt: const char \*

    :param args:
        *undescribed*
    :type args: va_list

.. _`trace_seq_vprintf.description`:

Description
-----------

The tracer may use either sequence operations or its own
copy to user routines. To simplify formating of a trace
trace_seq_printf is used to store strings into a special
buffer (@s). Then the output may be either used by
the sequencer or pulled into another buffer.

.. _`trace_seq_puts`:

trace_seq_puts
==============

.. c:function:: int trace_seq_puts(struct trace_seq *s, const char *str)

    trace sequence printing of simple string

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

    :param str:
        simple string to record
    :type str: const char \*

.. _`trace_seq_puts.description`:

Description
-----------

The tracer may use either the sequence operations or its own
copy to user routines. This function records a simple string
into a special buffer (@s) for later retrieval by a sequencer
or other mechanism.

.. This file was automatic generated / don't edit.

