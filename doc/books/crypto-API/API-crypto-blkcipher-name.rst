.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-blkcipher-name:

=====================
crypto_blkcipher_name
=====================

*man crypto_blkcipher_name(9)*

*4.6.0-rc5*

return the name / cra_name from the cipher handle


Synopsis
========

.. c:function:: const char * crypto_blkcipher_name( struct crypto_blkcipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Return
======

The character string holding the name of the cipher


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
