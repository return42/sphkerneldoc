.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rxrpc/sendmsg.c

.. _`rxrpc_kernel_send_data`:

rxrpc_kernel_send_data
======================

.. c:function:: int rxrpc_kernel_send_data(struct socket *sock, struct rxrpc_call *call, struct msghdr *msg, size_t len, rxrpc_notify_end_tx_t notify_end_tx)

    Allow a kernel service to send data on a call

    :param struct socket \*sock:
        The socket the call is on

    :param struct rxrpc_call \*call:
        The call to send data through

    :param struct msghdr \*msg:
        The data to send

    :param size_t len:
        The amount of data to send

    :param rxrpc_notify_end_tx_t notify_end_tx:
        Notification that the last packet is queued.

.. _`rxrpc_kernel_send_data.description`:

Description
-----------

Allow a kernel service to send data on a call.  The call must be in an state
appropriate to sending data.  No control data should be supplied in \ ``msg``\ ,
nor should an address be supplied.  MSG_MORE should be flagged if there's
more data to come, otherwise this data will end the transmission phase.

.. _`rxrpc_kernel_abort_call`:

rxrpc_kernel_abort_call
=======================

.. c:function:: bool rxrpc_kernel_abort_call(struct socket *sock, struct rxrpc_call *call, u32 abort_code, int error, const char *why)

    Allow a kernel service to abort a call

    :param struct socket \*sock:
        The socket the call is on

    :param struct rxrpc_call \*call:
        The call to be aborted

    :param u32 abort_code:
        The abort code to stick into the ABORT packet

    :param int error:
        Local error value

    :param const char \*why:
        3-char string indicating why.

.. _`rxrpc_kernel_abort_call.description`:

Description
-----------

Allow a kernel service to abort a call, if it's still in an abortable state
and return true if the call was aborted, false if it was already complete.

.. _`rxrpc_kernel_set_tx_length`:

rxrpc_kernel_set_tx_length
==========================

.. c:function:: void rxrpc_kernel_set_tx_length(struct socket *sock, struct rxrpc_call *call, s64 tx_total_len)

    Set the total Tx length on a call

    :param struct socket \*sock:
        The socket the call is on

    :param struct rxrpc_call \*call:
        The call to be informed

    :param s64 tx_total_len:
        The amount of data to be transmitted for this call

.. _`rxrpc_kernel_set_tx_length.description`:

Description
-----------

Allow a kernel service to set the total transmit length on a call.  This
allows buffer-to-packet encrypt-and-copy to be performed.

This function is primarily for use for setting the reply length since the
request length can be set when beginning the call.

.. This file was automatic generated / don't edit.

