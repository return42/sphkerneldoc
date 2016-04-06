
.. _API-crypto-alloc-shash:

==================
crypto_alloc_shash
==================

*man crypto_alloc_shash(9)*

*4.6.0-rc1*

allocate message digest handle


Synopsis
========

.. c:function:: struct crypto_shash ⋆ crypto_alloc_shash( const char * alg_name, u32 type, u32 mask )

Arguments
=========

``alg_name``
    is the cra_name / name or cra_driver_name / driver name of the message digest cipher

``type``
    specifies the type of the cipher

``mask``
    specifies the mask for the cipher


Description
===========

Allocate a cipher handle for a message digest. The returned ``struct
   crypto_shash`` is the cipher handle that is required for any subsequent API invocation for that message digest.


Return
======

allocated cipher handle in case of success; ``IS_ERR`` is true in case of an error, ``PTR_ERR`` returns the error code.
