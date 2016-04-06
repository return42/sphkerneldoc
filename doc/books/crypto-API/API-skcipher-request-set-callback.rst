
.. _API-skcipher-request-set-callback:

=============================
skcipher_request_set_callback
=============================

*man skcipher_request_set_callback(9)*

*4.6.0-rc1*

set asynchronous callback function


Synopsis
========

.. c:function:: void skcipher_request_set_callback( struct skcipher_request * req, u32 flags, crypto_completion_t compl, void * data )

Arguments
=========

``req``
    request handle

``flags``
    specify zero or an ORing of the flags CRYPTO_TFM_REQ_MAY_BACKLOG the request queue may back log and increase the wait queue beyond the initial maximum size;
    CRYPTO_TFM_REQ_MAY_SLEEP the request processing may sleep

``compl``
    callback function pointer to be registered with the request handle

``data``
    The data pointer refers to memory that is not used by the kernel crypto API, but provided to the callback function for it to use. Here, the caller can provide a reference to
    memory the callback function can operate on. As the callback function is invoked asynchronously to the related functionality, it may need to access data structures of the
    related functionality which can be referenced using this pointer. The callback function can access the memory via the “data” field in the crypto_async_request data structure
    provided to the callback function.


Description
===========

This function allows setting the callback function that is triggered once the cipher operation completes.

The callback function is registered with the skcipher_request handle and must comply with the following template

void callback_function(struct crypto_async_request ⋆req, int error)
