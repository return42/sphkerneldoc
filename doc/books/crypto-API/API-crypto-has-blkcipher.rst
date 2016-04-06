
.. _API-crypto-has-blkcipher:

====================
crypto_has_blkcipher
====================

*man crypto_has_blkcipher(9)*

*4.6.0-rc1*

Search for the availability of a block cipher


Synopsis
========

.. c:function:: int crypto_has_blkcipher( const char * alg_name, u32 type, u32 mask )

Arguments
=========

``alg_name``
    is the cra_name / name or cra_driver_name / driver name of the block cipher

``type``
    specifies the type of the cipher

``mask``
    specifies the mask for the cipher


Return
======

true when the block cipher is known to the kernel crypto API; false otherwise
