
.. _API-aead-request-set-ad:

===================
aead_request_set_ad
===================

*man aead_request_set_ad(9)*

*4.6.0-rc1*

set associated data information


Synopsis
========

.. c:function:: void aead_request_set_ad( struct aead_request * req, unsigned int assoclen )

Arguments
=========

``req``
    request handle

``assoclen``
    number of bytes in associated data


Description
===========

Setting the AD information. This function sets the length of the associated data.
