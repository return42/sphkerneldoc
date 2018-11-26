.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fuse/file.c

.. _`fuse_aio_complete`:

fuse_aio_complete
=================

.. c:function:: void fuse_aio_complete(struct fuse_io_priv *io, int err, ssize_t pos)

    actual end of fuse request in IO request. Otherwise, if bytes_requested == bytes_transferred or rw == WRITE, the caller sets 'pos' to -1.

    :param io:
        *undescribed*
    :type io: struct fuse_io_priv \*

    :param err:
        *undescribed*
    :type err: int

    :param pos:
        *undescribed*
    :type pos: ssize_t

.. _`fuse_aio_complete.an-example`:

An example
----------

User requested DIO read of 64K. It was splitted into two 32K fuse requests,
both submitted asynchronously. The first of them was ACKed by userspace as
fully completed (req->out.args[0].size == 32K) resulting in pos == -1. The
second request was ACKed as short, e.g. only 1K was read, resulting in
pos == 33K.

Thus, when all fuse requests are completed, the minimal non-negative 'pos'
will be equal to the length of the longest contiguous fragment of
transferred data starting from the beginning of IO request.

.. This file was automatic generated / don't edit.

