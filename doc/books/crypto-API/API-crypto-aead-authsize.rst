.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-aead-authsize:

====================
crypto_aead_authsize
====================

*man crypto_aead_authsize(9)*

*4.6.0-rc5*

obtain maximum authentication data size


Synopsis
========

.. c:function:: unsigned int crypto_aead_authsize( struct crypto_aead * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The maximum size of the authentication data for the AEAD cipher
referenced by the AEAD cipher handle is returned. The authentication
data size may be zero if the cipher implements a hard-coded maximum.

The authentication data may also be known as “tag value”.


Return
======

authentication data size / tag size in bytes


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
