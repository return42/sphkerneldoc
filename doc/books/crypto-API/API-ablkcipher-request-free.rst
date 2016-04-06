
.. _API-ablkcipher-request-free:

=======================
ablkcipher_request_free
=======================

*man ablkcipher_request_free(9)*

*4.6.0-rc1*

zeroize and free request data structure


Synopsis
========

.. c:function:: void ablkcipher_request_free( struct ablkcipher_request * req )

Arguments
=========

``req``
    request data structure cipher handle to be freed
