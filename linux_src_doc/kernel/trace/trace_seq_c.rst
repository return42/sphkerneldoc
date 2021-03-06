.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/trace_seq.c

.. _`trace_print_seq`:

trace_print_seq
===============

.. c:function:: int trace_print_seq(struct seq_file *m, struct trace_seq *s)

    move the contents of trace_seq into a seq_file

    :param m:
        the seq_file descriptor that is the destination
    :type m: struct seq_file \*

    :param s:
        the trace_seq descriptor that is the source.
    :type s: struct trace_seq \*

.. _`trace_print_seq.description`:

Description
-----------

Returns 0 on success and non zero on error. If it succeeds to
write to the seq_file it will reset the trace_seq, otherwise
it does not modify the trace_seq to let the caller try again.

.. _`trace_seq_printf`:

trace_seq_printf
================

.. c:function:: void trace_seq_printf(struct trace_seq *s, const char *fmt,  ...)

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

The tracer may use either sequence operations or its own
copy to user routines. To simplify formating of a trace
\ :c:func:`trace_seq_printf`\  is used to store strings into a special
buffer (@s). Then the output may be either used by
the sequencer or pulled into another buffer.

.. _`trace_seq_bitmask`:

trace_seq_bitmask
=================

.. c:function:: void trace_seq_bitmask(struct trace_seq *s, const unsigned long *maskp, int nmaskbits)

    write a bitmask array in its ASCII representation

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

    :param maskp:
        points to an array of unsigned longs that represent a bitmask
    :type maskp: const unsigned long \*

    :param nmaskbits:
        The number of bits that are valid in \ ``maskp``\ 
    :type nmaskbits: int

.. _`trace_seq_bitmask.description`:

Description
-----------

Writes a ASCII representation of a bitmask string into \ ``s``\ .

.. _`trace_seq_vprintf`:

trace_seq_vprintf
=================

.. c:function:: void trace_seq_vprintf(struct trace_seq *s, const char *fmt, va_list args)

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

.. _`trace_seq_bprintf`:

trace_seq_bprintf
=================

.. c:function:: void trace_seq_bprintf(struct trace_seq *s, const char *fmt, const u32 *binary)

    Write the printf string from binary arguments

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

    :param fmt:
        The format string for the \ ``binary``\  arguments
    :type fmt: const char \*

    :param binary:
        The binary arguments for \ ``fmt``\ .
    :type binary: const u32 \*

.. _`trace_seq_bprintf.description`:

Description
-----------

When recording in a fast path, a printf may be recorded with just
saving the format and the arguments as they were passed to the
function, instead of wasting cycles converting the arguments into
ASCII characters. Instead, the arguments are saved in a 32 bit
word array that is defined by the format string constraints.

This function will take the format and the binary array and finish
the conversion into the ASCII string within the buffer.

.. _`trace_seq_puts`:

trace_seq_puts
==============

.. c:function:: void trace_seq_puts(struct trace_seq *s, const char *str)

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

.. _`trace_seq_putc`:

trace_seq_putc
==============

.. c:function:: void trace_seq_putc(struct trace_seq *s, unsigned char c)

    trace sequence printing of simple character

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

    :param c:
        simple character to record
    :type c: unsigned char

.. _`trace_seq_putc.description`:

Description
-----------

The tracer may use either the sequence operations or its own
copy to user routines. This function records a simple charater
into a special buffer (@s) for later retrieval by a sequencer
or other mechanism.

.. _`trace_seq_putmem`:

trace_seq_putmem
================

.. c:function:: void trace_seq_putmem(struct trace_seq *s, const void *mem, unsigned int len)

    write raw data into the trace_seq buffer

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

    :param mem:
        The raw memory to copy into the buffer
    :type mem: const void \*

    :param len:
        The length of the raw memory to copy (in bytes)
    :type len: unsigned int

.. _`trace_seq_putmem.description`:

Description
-----------

There may be cases where raw memory needs to be written into the
buffer and a \ :c:func:`strcpy`\  would not work. Using this function allows
for such cases.

.. _`trace_seq_putmem_hex`:

trace_seq_putmem_hex
====================

.. c:function:: void trace_seq_putmem_hex(struct trace_seq *s, const void *mem, unsigned int len)

    write raw memory into the buffer in ASCII hex

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

    :param mem:
        The raw memory to write its hex ASCII representation of
    :type mem: const void \*

    :param len:
        The length of the raw memory to copy (in bytes)
    :type len: unsigned int

.. _`trace_seq_putmem_hex.description`:

Description
-----------

This is similar to \ :c:func:`trace_seq_putmem`\  except instead of just copying the
raw memory into the buffer it writes its ASCII representation of it
in hex characters.

.. _`trace_seq_path`:

trace_seq_path
==============

.. c:function:: int trace_seq_path(struct trace_seq *s, const struct path *path)

    copy a path into the sequence buffer

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

    :param path:
        path to write into the sequence buffer.
    :type path: const struct path \*

.. _`trace_seq_path.description`:

Description
-----------

Write a path name into the sequence buffer.

Returns 1 if we successfully written all the contents to
the buffer.
Returns 0 if we the length to write is bigger than the
reserved buffer space. In this case, nothing gets written.

.. _`trace_seq_to_user`:

trace_seq_to_user
=================

.. c:function:: int trace_seq_to_user(struct trace_seq *s, char __user *ubuf, int cnt)

    copy the squence buffer to user space

    :param s:
        trace sequence descriptor
    :type s: struct trace_seq \*

    :param ubuf:
        The userspace memory location to copy to
    :type ubuf: char __user \*

    :param cnt:
        The amount to copy
    :type cnt: int

.. _`trace_seq_to_user.description`:

Description
-----------

Copies the sequence buffer into the userspace memory pointed to
by \ ``ubuf``\ . It starts from the last read position (@s->readpos)
and writes up to \ ``cnt``\  characters or till it reaches the end of
the content in the buffer (@s->len), which ever comes first.

On success, it returns a positive number of the number of bytes
it copied.

On failure it returns -EBUSY if all of the content in the
sequence has been already read, which includes nothing in the
sequenc (@s->len == \ ``s->readpos``\ ).

Returns -EFAULT if the copy to userspace fails.

.. This file was automatic generated / don't edit.

