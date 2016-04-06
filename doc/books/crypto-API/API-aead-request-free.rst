
.. _API-aead-request-free:

=================
aead_request_free
=================

*man aead_request_free(9)*

*4.6.0-rc1*

zeroize and free request data structure


Synopsis
========

.. c:function:: void aead_request_free( struct aead_request * req )

Arguments
=========

``req``
    request data structure cipher handle to be freed
