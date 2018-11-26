.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rxrpc/af_rxrpc.c

.. _`rxrpc_kernel_begin_call`:

rxrpc_kernel_begin_call
=======================

.. c:function:: struct rxrpc_call *rxrpc_kernel_begin_call(struct socket *sock, struct sockaddr_rxrpc *srx, struct key *key, unsigned long user_call_ID, s64 tx_total_len, gfp_t gfp, rxrpc_notify_rx_t notify_rx, bool upgrade, unsigned int debug_id)

    Allow a kernel service to begin a call

    :param sock:
        The socket on which to make the call
    :type sock: struct socket \*

    :param srx:
        The address of the peer to contact
    :type srx: struct sockaddr_rxrpc \*

    :param key:
        The security context to use (defaults to socket setting)
    :type key: struct key \*

    :param user_call_ID:
        The ID to use
    :type user_call_ID: unsigned long

    :param tx_total_len:
        Total length of data to transmit during the call (or -1)
    :type tx_total_len: s64

    :param gfp:
        The allocation constraints
    :type gfp: gfp_t

    :param notify_rx:
        Where to send notifications instead of socket queue
    :type notify_rx: rxrpc_notify_rx_t

    :param upgrade:
        Request service upgrade for call
    :type upgrade: bool

    :param debug_id:
        The debug ID for tracing to be assigned to the call
    :type debug_id: unsigned int

.. _`rxrpc_kernel_begin_call.description`:

Description
-----------

Allow a kernel service to begin a call on the nominated socket.  This just
sets up all the internal tracking structures and allocates connection and
call IDs as appropriate.  The call to be used is returned.

The default socket destination address and security may be overridden by
supplying \ ``srx``\  and \ ``key``\ .

.. _`rxrpc_kernel_end_call`:

rxrpc_kernel_end_call
=====================

.. c:function:: void rxrpc_kernel_end_call(struct socket *sock, struct rxrpc_call *call)

    Allow a kernel service to end a call it was using

    :param sock:
        The socket the call is on
    :type sock: struct socket \*

    :param call:
        The call to end
    :type call: struct rxrpc_call \*

.. _`rxrpc_kernel_end_call.description`:

Description
-----------

Allow a kernel service to end a call it was using.  The call must be
complete before this is called (the call should be aborted if necessary).

.. _`rxrpc_kernel_check_life`:

rxrpc_kernel_check_life
=======================

.. c:function:: u32 rxrpc_kernel_check_life(const struct socket *sock, const struct rxrpc_call *call)

    Check to see whether a call is still alive

    :param sock:
        The socket the call is on
    :type sock: const struct socket \*

    :param call:
        The call to check
    :type call: const struct rxrpc_call \*

.. _`rxrpc_kernel_check_life.description`:

Description
-----------

Allow a kernel service to find out whether a call is still alive - ie. we're
getting ACKs from the server.  Returns a number representing the life state
which can be compared to that returned by a previous call.

If the life state stalls, \ :c:func:`rxrpc_kernel_probe_life`\  should be called and
then 2RTT waited.

.. _`rxrpc_kernel_probe_life`:

rxrpc_kernel_probe_life
=======================

.. c:function:: void rxrpc_kernel_probe_life(struct socket *sock, struct rxrpc_call *call)

    Poke the peer to see if it's still alive

    :param sock:
        The socket the call is on
    :type sock: struct socket \*

    :param call:
        The call to check
    :type call: struct rxrpc_call \*

.. _`rxrpc_kernel_probe_life.description`:

Description
-----------

In conjunction with \ :c:func:`rxrpc_kernel_check_life`\ , allow a kernel service to
find out whether a call is still alive by pinging it.  This should cause the
life state to be bumped in about 2\*RTT.

The must be called in TASK_RUNNING state on pain of \ :c:func:`might_sleep`\  objecting.

.. _`rxrpc_kernel_get_epoch`:

rxrpc_kernel_get_epoch
======================

.. c:function:: u32 rxrpc_kernel_get_epoch(struct socket *sock, struct rxrpc_call *call)

    Retrieve the epoch value from a call.

    :param sock:
        The socket the call is on
    :type sock: struct socket \*

    :param call:
        The call to query
    :type call: struct rxrpc_call \*

.. _`rxrpc_kernel_get_epoch.description`:

Description
-----------

Allow a kernel service to retrieve the epoch value from a service call to
see if the client at the other end rebooted.

.. _`rxrpc_kernel_check_call`:

rxrpc_kernel_check_call
=======================

.. c:function:: int rxrpc_kernel_check_call(struct socket *sock, struct rxrpc_call *call, enum rxrpc_call_completion *_compl, u32 *_abort_code)

    Check a call's state

    :param sock:
        The socket the call is on
    :type sock: struct socket \*

    :param call:
        The call to check
    :type call: struct rxrpc_call \*

    :param _compl:
        Where to store the completion state
    :type _compl: enum rxrpc_call_completion \*

    :param _abort_code:
        Where to store any abort code
    :type _abort_code: u32 \*

.. _`rxrpc_kernel_check_call.description`:

Description
-----------

Allow a kernel service to query the state of a call and find out the manner
of its termination if it has completed.  Returns -EINPROGRESS if the call is
still going, 0 if the call finished successfully, -ECONNABORTED if the call
was aborted and an appropriate error if the call failed in some other way.

.. _`rxrpc_kernel_retry_call`:

rxrpc_kernel_retry_call
=======================

.. c:function:: int rxrpc_kernel_retry_call(struct socket *sock, struct rxrpc_call *call, struct sockaddr_rxrpc *srx, struct key *key)

    Allow a kernel service to retry a call

    :param sock:
        The socket the call is on
    :type sock: struct socket \*

    :param call:
        The call to retry
    :type call: struct rxrpc_call \*

    :param srx:
        The address of the peer to contact
    :type srx: struct sockaddr_rxrpc \*

    :param key:
        The security context to use (defaults to socket setting)
    :type key: struct key \*

.. _`rxrpc_kernel_retry_call.description`:

Description
-----------

Allow a kernel service to try resending a client call that failed due to a
network error to a new address.  The Tx queue is maintained intact, thereby
relieving the need to re-encrypt any request data that has already been
buffered.

.. _`rxrpc_kernel_new_call_notification`:

rxrpc_kernel_new_call_notification
==================================

.. c:function:: void rxrpc_kernel_new_call_notification(struct socket *sock, rxrpc_notify_new_call_t notify_new_call, rxrpc_discard_new_call_t discard_new_call)

    Get notifications of new calls

    :param sock:
        The socket to intercept received messages on
    :type sock: struct socket \*

    :param notify_new_call:
        Function to be called when new calls appear
    :type notify_new_call: rxrpc_notify_new_call_t

    :param discard_new_call:
        Function to discard preallocated calls
    :type discard_new_call: rxrpc_discard_new_call_t

.. _`rxrpc_kernel_new_call_notification.description`:

Description
-----------

Allow a kernel service to be given notifications about new calls.

.. This file was automatic generated / don't edit.

