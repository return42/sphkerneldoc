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
        struct tee_context *ctx;
        struct mutex ctx_mutex;
        u32 func;
        u32 ret;
        size_t num_params;
        struct tee_param *param;
        bool req_posted;
        bool supp_next_send;
        struct mutex thrd_mutex;
        struct mutex supp_mutex;
        struct completion data_to_supp;
        struct completion data_from_supp;
    }

.. _`optee_supp.members`:

Members
-------

ctx
    *undescribed*

ctx_mutex
    held while accessing \ ``ctx``\ 

func
    supplicant function id to call

ret
    call return value

num_params
    number of elements in \ ``param``\ 

param
    parameters for \ ``func``\ 

req_posted
    if true, a request has been posted to the supplicant

supp_next_send
    if true, next step is for supplicant to send response

thrd_mutex
    held by the thread doing a request to supplicant

supp_mutex
    held by supplicant while operating on this struct

data_to_supp
    supplicant is waiting on this for next request

data_from_supp
    requesting thread is waiting on this to get the result

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

.. This file was automatic generated / don't edit.

