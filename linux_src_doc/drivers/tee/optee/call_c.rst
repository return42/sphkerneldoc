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

.. _`optee_fill_pages_list`:

optee_fill_pages_list
=====================

.. c:function:: void optee_fill_pages_list(u64 *dst, struct page **pages, int num_pages, size_t page_offset)

    write list of user pages to given shared buffer.

    :param u64 \*dst:
        page-aligned buffer where list of pages will be stored

    :param struct page \*\*pages:
        array of pages that represents shared buffer

    :param int num_pages:
        number of entries in \ ``pages``\ 

    :param size_t page_offset:
        offset of user buffer from page start

.. _`optee_fill_pages_list.description`:

Description
-----------

\ ``dst``\  should be big enough to hold list of user page addresses and
links to the next pages of buffer

.. This file was automatic generated / don't edit.

