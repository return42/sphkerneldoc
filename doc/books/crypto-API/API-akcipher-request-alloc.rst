.. -*- coding: utf-8; mode: rst -*-

.. _API-akcipher-request-alloc:

======================
akcipher_request_alloc
======================

*man akcipher_request_alloc(9)*

*4.6.0-rc5*

allocates public key request


Synopsis
========

.. c:function:: struct akcipher_request * akcipher_request_alloc( struct crypto_akcipher * tfm, gfp_t gfp )

Arguments
=========

``tfm``
    AKCIPHER tfm handle allocated with ``crypto_alloc_akcipher``

``gfp``
    allocation flags


Return
======

allocated handle in case of success or NULL in case of an error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
