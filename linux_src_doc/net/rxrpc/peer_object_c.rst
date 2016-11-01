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

.. This file was automatic generated / don't edit.

