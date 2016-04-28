.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-blkcipher-get-iv:

=======================
crypto_blkcipher_get_iv
=======================

*man crypto_blkcipher_get_iv(9)*

*4.6.0-rc5*

obtain IV from cipher


Synopsis
========

.. c:function:: void crypto_blkcipher_get_iv( struct crypto_blkcipher * tfm, u8 * dst, unsigned int len )

Arguments
=========

``tfm``
    cipher handle

``dst``
    buffer filled with the IV

``len``
    length of the buffer dst


Description
===========

The caller can obtain the IV set for the block cipher referenced by the
cipher handle and store it into the user-provided buffer. If the buffer
has an insufficient space, the IV is truncated to fit the buffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
