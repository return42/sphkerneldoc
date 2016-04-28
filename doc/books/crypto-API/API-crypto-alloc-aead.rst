.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-alloc-aead:

=================
crypto_alloc_aead
=================

*man crypto_alloc_aead(9)*

*4.6.0-rc5*

allocate AEAD cipher handle


Synopsis
========

.. c:function:: struct crypto_aead * crypto_alloc_aead( const char * alg_name, u32 type, u32 mask )

Arguments
=========

``alg_name``
    is the cra_name / name or cra_driver_name / driver name of the
    AEAD cipher

``type``
    specifies the type of the cipher

``mask``
    specifies the mask for the cipher


Description
===========

Allocate a cipher handle for an AEAD. The returned struct crypto_aead
is the cipher handle that is required for any subsequent API invocation
for that AEAD.


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
