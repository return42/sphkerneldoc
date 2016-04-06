
.. _API-crypto-alloc-akcipher:

=====================
crypto_alloc_akcipher
=====================

*man crypto_alloc_akcipher(9)*

*4.6.0-rc1*

allocate AKCIPHER tfm handle


Synopsis
========

.. c:function:: struct crypto_akcipher ⋆ crypto_alloc_akcipher( const char * alg_name, u32 type, u32 mask )

Arguments
=========

``alg_name``
    is the cra_name / name or cra_driver_name / driver name of the public key algorithm e.g. “rsa”

``type``
    specifies the type of the algorithm

``mask``
    specifies the mask for the algorithm


Description
===========

Allocate a handle for public key algorithm. The returned struct crypto_akcipher is the handle that is required for any subsequent API invocation for the public key operations.


Return
======

allocated handle in case of success; ``IS_ERR`` is true in case of an error, ``PTR_ERR`` returns the error code.
