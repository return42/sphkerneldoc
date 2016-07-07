.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/seq_file.h

.. _`seq_has_overflowed`:

seq_has_overflowed
==================

.. c:function:: bool seq_has_overflowed(struct seq_file *m)

    check if the buffer has overflowed

    :param struct seq_file \*m:
        the seq_file handle

.. _`seq_has_overflowed.description`:

Description
-----------

seq_files have a buffer which may overflow. When this happens a larger
buffer is reallocated and all the data will be printed again.
The overflow state is true when m->count == m->size.

Returns true if the buffer received more than it can hold.

.. _`seq_get_buf`:

seq_get_buf
===========

.. c:function:: size_t seq_get_buf(struct seq_file *m, char **bufp)

    get buffer to write arbitrary data to

    :param struct seq_file \*m:
        the seq_file handle

    :param char \*\*bufp:
        the beginning of the buffer is stored here

.. _`seq_get_buf.description`:

Description
-----------

Return the number of bytes available in the buffer, or zero if
there's no space.

.. _`seq_commit`:

seq_commit
==========

.. c:function:: void seq_commit(struct seq_file *m, int num)

    commit data to the buffer

    :param struct seq_file \*m:
        the seq_file handle

    :param int num:
        the number of bytes to commit

.. _`seq_commit.description`:

Description
-----------

Commit \ ``num``\  bytes of data written to a buffer previously acquired
by seq_buf_get.  To signal an error condition, or that the data
didn't fit in the available space, pass a negative \ ``num``\  value.

.. _`seq_setwidth`:

seq_setwidth
============

.. c:function:: void seq_setwidth(struct seq_file *m, size_t size)

    set padding width

    :param struct seq_file \*m:
        the seq_file handle

    :param size_t size:
        the max number of bytes to pad.

.. _`seq_setwidth.description`:

Description
-----------

Call \ :c:func:`seq_setwidth`\  for setting max width, then call \ :c:func:`seq_printf`\  etc. and
finally call \ :c:func:`seq_pad`\  to pad the remaining bytes.

.. _`seq_show_option`:

seq_show_option
===============

.. c:function:: void seq_show_option(struct seq_file *m, const char *name, const char *value)

    display mount options with appropriate escapes.

    :param struct seq_file \*m:
        the seq_file handle

    :param const char \*name:
        the mount option name

    :param const char \*value:
        the mount option name's value, can be NULL

.. _`seq_show_option_n`:

seq_show_option_n
=================

.. c:function::  seq_show_option_n( m,  name,  value,  length)

    display mount options with appropriate escapes where \ ``value``\  must be a specific length.

    :param  m:
        the seq_file handle

    :param  name:
        the mount option name

    :param  value:
        the mount option name's value, cannot be NULL

    :param  length:
        the length of \ ``value``\  to display

.. _`seq_show_option_n.description`:

Description
-----------

This is a macro since this uses "length" to define the size of the
stack buffer.

.. This file was automatic generated / don't edit.

