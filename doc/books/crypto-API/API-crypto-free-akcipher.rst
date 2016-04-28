.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-free-akcipher:

====================
crypto_free_akcipher
====================

*man crypto_free_akcipher(9)*

*4.6.0-rc5*

free AKCIPHER tfm handle


Synopsis
========

.. c:function:: void crypto_free_akcipher( struct crypto_akcipher * tfm )

Arguments
=========

``tfm``
    AKCIPHER tfm handle allocated with ``crypto_alloc_akcipher``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
