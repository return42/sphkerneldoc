.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/trace_seq.h

.. _`trace_seq_used`:

trace_seq_used
==============

.. c:function:: int trace_seq_used(struct trace_seq *s)

    amount of actual data written to buffer

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

.. _`trace_seq_used.description`:

Description
-----------

Returns the amount of data written to the buffer.

IMPORTANT!

Use this instead of \ ``s->seq.len``\  if you need to pass the amount
of data from the buffer to another buffer (userspace, or what not).
The \ ``s->seq.len``\  on overflow is bigger than the buffer size and
using it can cause access to undefined memory.

.. _`trace_seq_buffer_ptr`:

trace_seq_buffer_ptr
====================

.. c:function:: unsigned char *trace_seq_buffer_ptr(struct trace_seq *s)

    return pointer to next location in buffer

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

.. _`trace_seq_buffer_ptr.description`:

Description
-----------

Returns the pointer to the buffer where the next write to
the buffer will happen. This is useful to save the location
that is about to be written to and then return the result
of that write.

.. _`trace_seq_has_overflowed`:

trace_seq_has_overflowed
========================

.. c:function:: bool trace_seq_has_overflowed(struct trace_seq *s)

    return true if the trace_seq took too much

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

.. _`trace_seq_has_overflowed.description`:

Description
-----------

Returns true if too much data was added to the trace_seq and it is
now full and will not take anymore.

.. This file was automatic generated / don't edit.

