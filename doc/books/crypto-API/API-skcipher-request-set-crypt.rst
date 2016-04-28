.. -*- coding: utf-8; mode: rst -*-

.. _API-skcipher-request-set-crypt:

==========================
skcipher_request_set_crypt
==========================

*man skcipher_request_set_crypt(9)*

*4.6.0-rc5*

set data buffers


Synopsis
========

.. c:function:: void skcipher_request_set_crypt( struct skcipher_request * req, struct scatterlist * src, struct scatterlist * dst, unsigned int cryptlen, void * iv )

Arguments
=========

``req``
    request handle

``src``
    source scatter / gather list

``dst``
    destination scatter / gather list

``cryptlen``
    number of bytes to process from ``src``

``iv``
    IV for the cipher operation which must comply with the IV size
    defined by crypto_skcipher_ivsize


Description
===========

This function allows setting of the source data and destination data
scatter / gather lists.

For encryption, the source is treated as the plaintext and the
destination is the ciphertext. For a decryption operation, the use is
reversed - the source is the ciphertext and the destination is the
plaintext.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
