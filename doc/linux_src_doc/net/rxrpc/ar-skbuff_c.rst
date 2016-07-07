.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rxrpc/ar-skbuff.c

.. _`rxrpc_kernel_free_skb`:

rxrpc_kernel_free_skb
=====================

.. c:function:: void rxrpc_kernel_free_skb(struct sk_buff *skb)

    Free an RxRPC socket buffer

    :param struct sk_buff \*skb:
        The socket buffer to be freed

.. _`rxrpc_kernel_free_skb.description`:

Description
-----------

Let RxRPC free its own socket buffer, permitting it to maintain debug
accounting.

.. This file was automatic generated / don't edit.

