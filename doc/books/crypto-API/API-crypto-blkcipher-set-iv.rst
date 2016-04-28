.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-blkcipher-set-iv:

=======================
crypto_blkcipher_set_iv
=======================

*man crypto_blkcipher_set_iv(9)*

*4.6.0-rc5*

set IV for cipher


Synopsis
========

.. c:function:: void crypto_blkcipher_set_iv( struct crypto_blkcipher * tfm, const u8 * src, unsigned int len )

Arguments
=========

``tfm``
    cipher handle

``src``
    buffer holding the IV

``len``
    length of the IV in bytes


Description
===========

The caller provided IV is set for the block cipher referenced by the
cipher handle.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
