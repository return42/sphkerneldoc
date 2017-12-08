.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rxrpc/peer_object.c

.. _`rxrpc_kernel_get_peer`:

rxrpc_kernel_get_peer
=====================

.. c:function:: void rxrpc_kernel_get_peer(struct socket *sock, struct rxrpc_call *call, struct sockaddr_rxrpc *_srx)

    Get the peer address of a call

    :param struct socket \*sock:
        The socket on which the call is in progress.

    :param struct rxrpc_call \*call:
        The call to query

    :param struct sockaddr_rxrpc \*_srx:
        Where to place the result

.. _`rxrpc_kernel_get_peer.description`:

Description
-----------

Get the address of the remote peer in a call.

.. _`rxrpc_kernel_get_rtt`:

rxrpc_kernel_get_rtt
====================

.. c:function:: u64 rxrpc_kernel_get_rtt(struct socket *sock, struct rxrpc_call *call)

    Get a call's peer RTT

    :param struct socket \*sock:
        The socket on which the call is in progress.

    :param struct rxrpc_call \*call:
        The call to query

.. _`rxrpc_kernel_get_rtt.description`:

Description
-----------

Get the call's peer RTT.

.. This file was automatic generated / don't edit.

