.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rxrpc/recvmsg.c

.. _`rxrpc_kernel_recv_data`:

rxrpc_kernel_recv_data
======================

.. c:function:: int rxrpc_kernel_recv_data(struct socket *sock, struct rxrpc_call *call, void *buf, size_t size, size_t *_offset, bool want_more, u32 *_abort)

    Allow a kernel service to receive data/info

    :param struct socket \*sock:
        The socket that the call exists on

    :param struct rxrpc_call \*call:
        The call to send data through

    :param void \*buf:
        The buffer to receive into

    :param size_t size:
        The size of the buffer, including data already read

    :param size_t \*_offset:
        The running offset into the buffer.

    :param bool want_more:
        True if more data is expected to be read

    :param u32 \*_abort:
        Where the abort code is stored if -ECONNABORTED is returned

.. _`rxrpc_kernel_recv_data.description`:

Description
-----------

Allow a kernel service to receive data and pick up information about the
state of a call.  Returns 0 if got what was asked for and there's more
available, 1 if we got what was asked for and we're at the end of the data
and -EAGAIN if we need more data.

Note that we may return -EAGAIN to drain empty packets at the end of the
data, even if we've already copied over the requested data.

This function adds the amount it transfers to \*\_offset, so this should be
precleared as appropriate.  Note that the amount remaining in the buffer is
taken to be size - \*\_offset.

\*\_abort should also be initialised to 0.

.. This file was automatic generated / don't edit.

