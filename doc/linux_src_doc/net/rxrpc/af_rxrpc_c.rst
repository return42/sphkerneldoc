.. -*- coding: utf-8; mode: rst -*-

==========
af_rxrpc.c
==========


.. _`rxrpc_kernel_begin_call`:

rxrpc_kernel_begin_call
=======================

.. c:function:: struct rxrpc_call *rxrpc_kernel_begin_call (struct socket *sock, struct sockaddr_rxrpc *srx, struct key *key, unsigned long user_call_ID, gfp_t gfp)

    Allow a kernel service to begin a call

    :param struct socket \*sock:
        The socket on which to make the call

    :param struct sockaddr_rxrpc \*srx:
        The address of the peer to contact (defaults to socket setting)

    :param struct key \*key:
        The security context to use (defaults to socket setting)

    :param unsigned long user_call_ID:
        The ID to use

    :param gfp_t gfp:

        *undescribed*



.. _`rxrpc_kernel_begin_call.description`:

Description
-----------

Allow a kernel service to begin a call on the nominated socket.  This just
sets up all the internal tracking structures and allocates connection and
call IDs as appropriate.  The call to be used is returned.

The default socket destination address and security may be overridden by
supplying ``srx`` and ``key``\ .



.. _`rxrpc_kernel_end_call`:

rxrpc_kernel_end_call
=====================

.. c:function:: void rxrpc_kernel_end_call (struct rxrpc_call *call)

    Allow a kernel service to end a call it was using

    :param struct rxrpc_call \*call:
        The call to end



.. _`rxrpc_kernel_end_call.description`:

Description
-----------

Allow a kernel service to end a call it was using.  The call must be
complete before this is called (the call should be aborted if necessary).



.. _`rxrpc_kernel_intercept_rx_messages`:

rxrpc_kernel_intercept_rx_messages
==================================

.. c:function:: void rxrpc_kernel_intercept_rx_messages (struct socket *sock, rxrpc_interceptor_t interceptor)

    Intercept received RxRPC messages

    :param struct socket \*sock:
        The socket to intercept received messages on

    :param rxrpc_interceptor_t interceptor:
        The function to pass the messages to



.. _`rxrpc_kernel_intercept_rx_messages.description`:

Description
-----------

Allow a kernel service to intercept messages heading for the Rx queue on an
RxRPC socket.  They get passed to the specified function instead.
``interceptor`` should free the socket buffers it is given.  ``interceptor`` is
called with the socket receive queue spinlock held and softirqs disabled -
this ensures that the messages will be delivered in the right order.

