.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/optee/call.c

.. _`optee_do_call_with_arg`:

optee_do_call_with_arg
======================

.. c:function:: u32 optee_do_call_with_arg(struct tee_context *ctx, phys_addr_t parg)

    Do an SMC to OP-TEE in secure world

    :param struct tee_context \*ctx:
        calling context

    :param phys_addr_t parg:
        physical address of message to pass to secure world

.. _`optee_do_call_with_arg.description`:

Description
-----------

Does and SMC to OP-TEE in secure world and handles eventual resulting
Remote Procedure Calls (RPC) from OP-TEE.

Returns return code from secure world, 0 is OK

.. _`optee_enable_shm_cache`:

optee_enable_shm_cache
======================

.. c:function:: void optee_enable_shm_cache(struct optee *optee)

    Enables caching of some shared memory allocation in OP-TEE

    :param struct optee \*optee:
        main service struct

.. _`optee_disable_shm_cache`:

optee_disable_shm_cache
=======================

.. c:function:: void optee_disable_shm_cache(struct optee *optee)

    Disables caching of some shared memory allocation in OP-TEE

    :param struct optee \*optee:
        main service struct

.. This file was automatic generated / don't edit.

