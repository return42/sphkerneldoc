.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rxrpc/ar-recvmsg.c

.. _`rxrpc_kernel_data_delivered`:

rxrpc_kernel_data_delivered
===========================

.. c:function:: void rxrpc_kernel_data_delivered(struct sk_buff *skb)

    Record delivery of data message

    :param struct sk_buff \*skb:
        Message holding data

.. _`rxrpc_kernel_data_delivered.description`:

Description
-----------

Record the delivery of a data message.  This permits RxRPC to keep its
tracking correct.  The socket buffer will be deleted.

.. _`rxrpc_kernel_is_data_last`:

rxrpc_kernel_is_data_last
=========================

.. c:function:: bool rxrpc_kernel_is_data_last(struct sk_buff *skb)

    Determine if data message is last one

    :param struct sk_buff \*skb:
        Message holding data

.. _`rxrpc_kernel_is_data_last.description`:

Description
-----------

Determine if data message is last one for the parent call.

.. _`rxrpc_kernel_get_abort_code`:

rxrpc_kernel_get_abort_code
===========================

.. c:function:: u32 rxrpc_kernel_get_abort_code(struct sk_buff *skb)

    Get the abort code from an RxRPC abort message

    :param struct sk_buff \*skb:
        Message indicating an abort

.. _`rxrpc_kernel_get_abort_code.description`:

Description
-----------

Get the abort code from an RxRPC abort message.

.. _`rxrpc_kernel_get_error_number`:

rxrpc_kernel_get_error_number
=============================

.. c:function:: int rxrpc_kernel_get_error_number(struct sk_buff *skb)

    Get the error number from an RxRPC error message

    :param struct sk_buff \*skb:
        Message indicating an error

.. _`rxrpc_kernel_get_error_number.description`:

Description
-----------

Get the error number from an RxRPC error message.

.. This file was automatic generated / don't edit.

