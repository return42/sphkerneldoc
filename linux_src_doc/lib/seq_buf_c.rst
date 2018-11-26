.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/seq_buf.c

.. _`seq_buf_can_fit`:

seq_buf_can_fit
===============

.. c:function:: bool seq_buf_can_fit(struct seq_buf *s, size_t len)

    can the new data fit in the current buffer?

    :param s:
        the seq_buf descriptor
    :type s: struct seq_buf \*

    :param len:
        The length to see if it can fit in the current buffer
    :type len: size_t

.. _`seq_buf_can_fit.description`:

Description
-----------

Returns true if there's enough unused space in the seq_buf buffer
to fit the amount of new data according to \ ``len``\ .

.. _`seq_buf_print_seq`:

seq_buf_print_seq
=================

.. c:function:: int seq_buf_print_seq(struct seq_file *m, struct seq_buf *s)

    move the contents of seq_buf into a seq_file

    :param m:
        the seq_file descriptor that is the destination
    :type m: struct seq_file \*

    :param s:
        the seq_buf descriptor that is the source.
    :type s: struct seq_buf \*

.. _`seq_buf_print_seq.description`:

Description
-----------

Returns zero on success, non zero otherwise

.. _`seq_buf_vprintf`:

seq_buf_vprintf
===============

.. c:function:: int seq_buf_vprintf(struct seq_buf *s, const char *fmt, va_list args)

    sequence printing of information.

    :param s:
        seq_buf descriptor
    :type s: struct seq_buf \*

    :param fmt:
        printf format string
    :type fmt: const char \*

    :param args:
        va_list of arguments from a \ :c:func:`printf`\  type function
    :type args: va_list

.. _`seq_buf_vprintf.description`:

Description
-----------

Writes a \ :c:func:`vnprintf`\  format into the sequencce buffer.

Returns zero on success, -1 on overflow.

.. _`seq_buf_printf`:

seq_buf_printf
==============

.. c:function:: int seq_buf_printf(struct seq_buf *s, const char *fmt,  ...)

    sequence printing of information

    :param s:
        seq_buf descriptor
    :type s: struct seq_buf \*

    :param fmt:
        printf format string
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`seq_buf_printf.description`:

Description
-----------

Writes a \ :c:func:`printf`\  format into the sequence buffer.

Returns zero on success, -1 on overflow.

.. _`seq_buf_bprintf`:

seq_buf_bprintf
===============

.. c:function:: int seq_buf_bprintf(struct seq_buf *s, const char *fmt, const u32 *binary)

    Write the printf string from binary arguments

    :param s:
        seq_buf descriptor
    :type s: struct seq_buf \*

    :param fmt:
        The format string for the \ ``binary``\  arguments
    :type fmt: const char \*

    :param binary:
        The binary arguments for \ ``fmt``\ .
    :type binary: const u32 \*

.. _`seq_buf_bprintf.description`:

Description
-----------

When recording in a fast path, a printf may be recorded with just
saving the format and the arguments as they were passed to the
function, instead of wasting cycles converting the arguments into
ASCII characters. Instead, the arguments are saved in a 32 bit
word array that is defined by the format string constraints.

This function will take the format and the binary array and finish
the conversion into the ASCII string within the buffer.

Returns zero on success, -1 on overflow.

.. _`seq_buf_puts`:

seq_buf_puts
============

.. c:function:: int seq_buf_puts(struct seq_buf *s, const char *str)

    sequence printing of simple string

    :param s:
        seq_buf descriptor
    :type s: struct seq_buf \*

    :param str:
        simple string to record
    :type str: const char \*

.. _`seq_buf_puts.description`:

Description
-----------

Copy a simple string into the sequence buffer.

Returns zero on success, -1 on overflow

.. _`seq_buf_putc`:

seq_buf_putc
============

.. c:function:: int seq_buf_putc(struct seq_buf *s, unsigned char c)

    sequence printing of simple character

    :param s:
        seq_buf descriptor
    :type s: struct seq_buf \*

    :param c:
        simple character to record
    :type c: unsigned char

.. _`seq_buf_putc.description`:

Description
-----------

Copy a single character into the sequence buffer.

Returns zero on success, -1 on overflow

.. _`seq_buf_putmem`:

seq_buf_putmem
==============

.. c:function:: int seq_buf_putmem(struct seq_buf *s, const void *mem, unsigned int len)

    write raw data into the sequenc buffer

    :param s:
        seq_buf descriptor
    :type s: struct seq_buf \*

    :param mem:
        The raw memory to copy into the buffer
    :type mem: const void \*

    :param len:
        The length of the raw memory to copy (in bytes)
    :type len: unsigned int

.. _`seq_buf_putmem.description`:

Description
-----------

There may be cases where raw memory needs to be written into the
buffer and a \ :c:func:`strcpy`\  would not work. Using this function allows
for such cases.

Returns zero on success, -1 on overflow

.. _`seq_buf_putmem_hex`:

seq_buf_putmem_hex
==================

.. c:function:: int seq_buf_putmem_hex(struct seq_buf *s, const void *mem, unsigned int len)

    write raw memory into the buffer in ASCII hex

    :param s:
        seq_buf descriptor
    :type s: struct seq_buf \*

    :param mem:
        The raw memory to write its hex ASCII representation of
    :type mem: const void \*

    :param len:
        The length of the raw memory to copy (in bytes)
    :type len: unsigned int

.. _`seq_buf_putmem_hex.description`:

Description
-----------

This is similar to \ :c:func:`seq_buf_putmem`\  except instead of just copying the
raw memory into the buffer it writes its ASCII representation of it
in hex characters.

Returns zero on success, -1 on overflow

.. _`seq_buf_path`:

seq_buf_path
============

.. c:function:: int seq_buf_path(struct seq_buf *s, const struct path *path, const char *esc)

    copy a path into the sequence buffer

    :param s:
        seq_buf descriptor
    :type s: struct seq_buf \*

    :param path:
        path to write into the sequence buffer.
    :type path: const struct path \*

    :param esc:
        set of characters to escape in the output
    :type esc: const char \*

.. _`seq_buf_path.description`:

Description
-----------

Write a path name into the sequence buffer.

Returns the number of written bytes on success, -1 on overflow

.. _`seq_buf_to_user`:

seq_buf_to_user
===============

.. c:function:: int seq_buf_to_user(struct seq_buf *s, char __user *ubuf, int cnt)

    copy the squence buffer to user space

    :param s:
        seq_buf descriptor
    :type s: struct seq_buf \*

    :param ubuf:
        The userspace memory location to copy to
    :type ubuf: char __user \*

    :param cnt:
        The amount to copy
    :type cnt: int

.. _`seq_buf_to_user.description`:

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
sequence (@s->len == \ ``s->readpos``\ ).

Returns -EFAULT if the copy to userspace fails.

.. This file was automatic generated / don't edit.

