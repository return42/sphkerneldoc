.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rxrpc/af_rxrpc.c

.. _`rxrpc_kernel_begin_call`:

rxrpc_kernel_begin_call
=======================

.. c:function:: struct rxrpc_call *rxrpc_kernel_begin_call(struct socket *sock, struct sockaddr_rxrpc *srx, struct key *key, unsigned long user_call_ID, gfp_t gfp, rxrpc_notify_rx_t notify_rx)

    Allow a kernel service to begin a call

    :param struct socket \*sock:
        The socket on which to make the call

    :param struct sockaddr_rxrpc \*srx:
        The address of the peer to contact

    :param struct key \*key:
        The security context to use (defaults to socket setting)

    :param unsigned long user_call_ID:
        The ID to use

    :param gfp_t gfp:
        The allocation constraints

    :param rxrpc_notify_rx_t notify_rx:
        Where to send notifications instead of socket queue

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

    :param struct socket \*sock:
        The socket the call is on

    :param struct rxrpc_call \*call:
        The call to end

.. _`rxrpc_kernel_end_call.description`:

Description
-----------

Allow a kernel service to end a call it was using.  The call must be
complete before this is called (the call should be aborted if necessary).

.. _`rxrpc_kernel_new_call_notification`:

rxrpc_kernel_new_call_notification
==================================

.. c:function:: void rxrpc_kernel_new_call_notification(struct socket *sock, rxrpc_notify_new_call_t notify_new_call, rxrpc_discard_new_call_t discard_new_call)

    Get notifications of new calls

    :param struct socket \*sock:
        The socket to intercept received messages on

    :param rxrpc_notify_new_call_t notify_new_call:
        Function to be called when new calls appear

    :param rxrpc_discard_new_call_t discard_new_call:
        Function to discard preallocated calls

.. _`rxrpc_kernel_new_call_notification.description`:

Description
-----------

Allow a kernel service to be given notifications about new calls.

.. This file was automatic generated / don't edit.

