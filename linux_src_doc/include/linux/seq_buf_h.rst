.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/seq_buf.h

.. _`seq_buf_get_buf`:

seq_buf_get_buf
===============

.. c:function:: size_t seq_buf_get_buf(struct seq_buf *s, char **bufp)

    get buffer to write arbitrary data to

    :param s:
        the seq_buf handle
    :type s: struct seq_buf \*

    :param bufp:
        the beginning of the buffer is stored here
    :type bufp: char \*\*

.. _`seq_buf_get_buf.description`:

Description
-----------

Return the number of bytes available in the buffer, or zero if
there's no space.

.. _`seq_buf_commit`:

seq_buf_commit
==============

.. c:function:: void seq_buf_commit(struct seq_buf *s, int num)

    commit data to the buffer

    :param s:
        the seq_buf handle
    :type s: struct seq_buf \*

    :param num:
        the number of bytes to commit
    :type num: int

.. _`seq_buf_commit.description`:

Description
-----------

Commit \ ``num``\  bytes of data written to a buffer previously acquired
by seq_buf_get.  To signal an error condition, or that the data
didn't fit in the available space, pass a negative \ ``num``\  value.

.. This file was automatic generated / don't edit.

