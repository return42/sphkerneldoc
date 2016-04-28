.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-alloc-cipher:

===================
crypto_alloc_cipher
===================

*man crypto_alloc_cipher(9)*

*4.6.0-rc5*

allocate single block cipher handle


Synopsis
========

.. c:function:: struct crypto_cipher * crypto_alloc_cipher( const char * alg_name, u32 type, u32 mask )

Arguments
=========

``alg_name``
    is the cra_name / name or cra_driver_name / driver name of the
    single block cipher

``type``
    specifies the type of the cipher

``mask``
    specifies the mask for the cipher


Description
===========

Allocate a cipher handle for a single block cipher. The returned struct
crypto_cipher is the cipher handle that is required for any subsequent
API invocation for that single block cipher.


Return
======

allocated cipher handle in case of success; ``IS_ERR`` is true in case
of an error, ``PTR_ERR`` returns the error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
