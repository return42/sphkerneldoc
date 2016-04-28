.. -*- coding: utf-8; mode: rst -*-

.. _API-ahash-request-set-crypt:

=======================
ahash_request_set_crypt
=======================

*man ahash_request_set_crypt(9)*

*4.6.0-rc5*

set data buffers


Synopsis
========

.. c:function:: void ahash_request_set_crypt( struct ahash_request * req, struct scatterlist * src, u8 * result, unsigned int nbytes )

Arguments
=========

``req``
    ahash_request handle to be updated

``src``
    source scatter/gather list

``result``
    buffer that is filled with the message digest -- the caller must
    ensure that the buffer has sufficient space by, for example, calling
    ``crypto_ahash_digestsize``

``nbytes``
    number of bytes to process from the source scatter/gather list


Description
===========

By using this call, the caller references the source scatter/gather
list. The source scatter/gather list points to the data the message
digest is to be calculated for.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
