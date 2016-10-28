.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rxrpc/ar-accept.c

.. _`rxrpc_kernel_accept_call`:

rxrpc_kernel_accept_call
========================

.. c:function:: struct rxrpc_call *rxrpc_kernel_accept_call(struct socket *sock, unsigned long user_call_ID)

    Allow a kernel service to accept an incoming call

    :param struct socket \*sock:
        The socket on which the impending call is waiting

    :param unsigned long user_call_ID:
        The tag to attach to the call

.. _`rxrpc_kernel_accept_call.description`:

Description
-----------

Allow a kernel service to accept an incoming call, assuming the incoming
call is still valid.

.. _`rxrpc_kernel_reject_call`:

rxrpc_kernel_reject_call
========================

.. c:function:: int rxrpc_kernel_reject_call(struct socket *sock)

    Allow a kernel service to reject an incoming call

    :param struct socket \*sock:
        The socket on which the impending call is waiting

.. _`rxrpc_kernel_reject_call.description`:

Description
-----------

Allow a kernel service to reject an incoming call with a BUSY message,
assuming the incoming call is still valid.

.. This file was automatic generated / don't edit.

