.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/optee/rpc.c

.. _`optee_handle_rpc`:

optee_handle_rpc
================

.. c:function:: void optee_handle_rpc(struct tee_context *ctx, struct optee_rpc_param *param, struct optee_call_ctx *call_ctx)

    handle RPC from secure world

    :param ctx:
        context doing the RPC
    :type ctx: struct tee_context \*

    :param param:
        value of registers for the RPC
    :type param: struct optee_rpc_param \*

    :param call_ctx:
        call context. Preserved during one OP-TEE invocation
    :type call_ctx: struct optee_call_ctx \*

.. _`optee_handle_rpc.description`:

Description
-----------

Result of RPC is written back into \ ``param``\ .

.. This file was automatic generated / don't edit.

