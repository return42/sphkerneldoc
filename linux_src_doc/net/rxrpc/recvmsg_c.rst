.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rxrpc/recvmsg.c

.. _`rxrpc_kernel_recv_data`:

rxrpc_kernel_recv_data
======================

.. c:function:: int rxrpc_kernel_recv_data(struct socket *sock, struct rxrpc_call *call, struct iov_iter *iter, bool want_more, u32 *_abort, u16 *_service)

    Allow a kernel service to receive data/info

    :param sock:
        The socket that the call exists on
    :type sock: struct socket \*

    :param call:
        The call to send data through
    :type call: struct rxrpc_call \*

    :param iter:
        The buffer to receive into
    :type iter: struct iov_iter \*

    :param want_more:
        True if more data is expected to be read
    :type want_more: bool

    :param _abort:
        Where the abort code is stored if -ECONNABORTED is returned
    :type _abort: u32 \*

    :param _service:
        Where to store the actual service ID (may be upgraded)
    :type _service: u16 \*

.. _`rxrpc_kernel_recv_data.description`:

Description
-----------

Allow a kernel service to receive data and pick up information about the
state of a call.  Returns 0 if got what was asked for and there's more
available, 1 if we got what was asked for and we're at the end of the data
and -EAGAIN if we need more data.

Note that we may return -EAGAIN to drain empty packets at the end of the
data, even if we've already copied over the requested data.

\*\_abort should also be initialised to 0.

.. _`rxrpc_kernel_get_reply_time`:

rxrpc_kernel_get_reply_time
===========================

.. c:function:: bool rxrpc_kernel_get_reply_time(struct socket *sock, struct rxrpc_call *call, ktime_t *_ts)

    Get timestamp on first reply packet

    :param sock:
        The socket that the call exists on
    :type sock: struct socket \*

    :param call:
        The call to query
    :type call: struct rxrpc_call \*

    :param _ts:
        Where to put the timestamp
    :type _ts: ktime_t \*

.. _`rxrpc_kernel_get_reply_time.description`:

Description
-----------

Retrieve the timestamp from the first DATA packet of the reply if it is
in the ring.  Returns true if successful, false if not.

.. This file was automatic generated / don't edit.

