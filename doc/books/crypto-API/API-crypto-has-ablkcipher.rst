
.. _API-crypto-has-ablkcipher:

=====================
crypto_has_ablkcipher
=====================

*man crypto_has_ablkcipher(9)*

*4.6.0-rc1*

Search for the availability of an ablkcipher.


Synopsis
========

.. c:function:: int crypto_has_ablkcipher( const char * alg_name, u32 type, u32 mask )

Arguments
=========

``alg_name``
    is the cra_name / name or cra_driver_name / driver name of the ablkcipher

``type``
    specifies the type of the cipher

``mask``
    specifies the mask for the cipher


Return
======

true when the ablkcipher is known to the kernel crypto API; false otherwise
