
.. _API-skcipher-request-free:

=====================
skcipher_request_free
=====================

*man skcipher_request_free(9)*

*4.6.0-rc1*

zeroize and free request data structure


Synopsis
========

.. c:function:: void skcipher_request_free( struct skcipher_request * req )

Arguments
=========

``req``
    request data structure cipher handle to be freed
