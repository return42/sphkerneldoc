
.. _API-crypto-alloc-ahash:

==================
crypto_alloc_ahash
==================

*man crypto_alloc_ahash(9)*

*4.6.0-rc1*

allocate ahash cipher handle


Synopsis
========

.. c:function:: struct crypto_ahash ⋆ crypto_alloc_ahash( const char * alg_name, u32 type, u32 mask )

Arguments
=========

``alg_name``
    is the cra_name / name or cra_driver_name / driver name of the ahash cipher

``type``
    specifies the type of the cipher

``mask``
    specifies the mask for the cipher


Description
===========

Allocate a cipher handle for an ahash. The returned struct crypto_ahash is the cipher handle that is required for any subsequent API invocation for that ahash.


Return
======

allocated cipher handle in case of success; ``IS_ERR`` is true in case of an error, ``PTR_ERR`` returns the error code.
