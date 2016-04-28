.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-free-blkcipher:

=====================
crypto_free_blkcipher
=====================

*man crypto_free_blkcipher(9)*

*4.6.0-rc5*

zeroize and free the block cipher handle


Synopsis
========

.. c:function:: void crypto_free_blkcipher( struct crypto_blkcipher * tfm )

Arguments
=========

``tfm``
    cipher handle to be freed


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
