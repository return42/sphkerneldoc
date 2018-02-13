.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/optee/optee_private.h

.. _`optee_supp`:

struct optee_supp
=================

.. c:type:: struct optee_supp

    supplicant synchronization struct \ ``ctx``\                  the context of current connected supplicant. if !NULL the supplicant device is available for use, else busy

.. _`optee_supp.definition`:

Definition
----------

.. code-block:: c

    struct optee_supp {
        struct mutex mutex;
        struct tee_context *ctx;
        int req_id;
        struct list_head reqs;
        struct idr idr;
        struct completion reqs_c;
    }

.. _`optee_supp.members`:

Members
-------

mutex
    held while accessing content of this struct

ctx
    *undescribed*

req_id
    current request id if supplicant is doing synchronous
    communication, else -1

reqs
    queued request not yet retrieved by supplicant

idr
    IDR holding all requests currently being processed
    by supplicant

reqs_c
    completion used by supplicant when waiting for a
    request to be queued.

.. _`optee`:

struct optee
============

.. c:type:: struct optee

    main service struct

.. _`optee.definition`:

Definition
----------

.. code-block:: c

    struct optee {
        struct tee_device *supp_teedev;
        struct tee_device *teedev;
        optee_invoke_fn *invoke_fn;
        struct optee_call_queue call_queue;
        struct optee_wait_queue wait_queue;
        struct optee_supp supp;
        struct tee_shm_pool *pool;
        void *memremaped_shm;
        u32 sec_caps;
    }

.. _`optee.members`:

Members
-------

supp_teedev
    supplicant device

teedev
    client device

invoke_fn
    function to issue smc or hvc

call_queue
    queue of threads waiting to call \ ``invoke_fn``\ 

wait_queue
    queue of threads from secure world waiting for a
    secure world sync object

supp
    supplicant synchronization struct for RPC to supplicant

pool
    shared memory pool
    \ ``memremaped_shm``\       virtual address of memory in shared memory pool

memremaped_shm
    *undescribed*

sec_caps
    secure world capabilities defined by
    OPTEE_SMC_SEC_CAP\_\* in optee_smc.h

.. This file was automatic generated / don't edit.

