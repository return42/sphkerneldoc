.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/optee/rpc.c

.. _`optee_handle_rpc`:

optee_handle_rpc
================

.. c:function:: void optee_handle_rpc(struct tee_context *ctx, struct optee_rpc_param *param)

    handle RPC from secure world

    :param struct tee_context \*ctx:
        context doing the RPC

    :param struct optee_rpc_param \*param:
        value of registers for the RPC

.. _`optee_handle_rpc.description`:

Description
-----------

Result of RPC is written back into \ ``param``\ .

.. This file was automatic generated / don't edit.

