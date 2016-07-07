.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rxrpc/ar-output.c

.. _`rxrpc_kernel_send_data`:

rxrpc_kernel_send_data
======================

.. c:function:: int rxrpc_kernel_send_data(struct rxrpc_call *call, struct msghdr *msg, size_t len)

    Allow a kernel service to send data on a call

    :param struct rxrpc_call \*call:
        The call to send data through

    :param struct msghdr \*msg:
        The data to send

    :param size_t len:
        The amount of data to send

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

.. c:function:: void rxrpc_kernel_abort_call(struct rxrpc_call *call, u32 abort_code)

    Allow a kernel service to abort a call

    :param struct rxrpc_call \*call:
        The call to be aborted

    :param u32 abort_code:
        The abort code to stick into the ABORT packet

.. _`rxrpc_kernel_abort_call.description`:

Description
-----------

Allow a kernel service to abort a call, if it's still in an abortable state.

.. This file was automatic generated / don't edit.

