
.. _API-crypto-has-cipher:

=================
crypto_has_cipher
=================

*man crypto_has_cipher(9)*

*4.6.0-rc1*

Search for the availability of a single block cipher


Synopsis
========

.. c:function:: int crypto_has_cipher( const char * alg_name, u32 type, u32 mask )

Arguments
=========

``alg_name``
    is the cra_name / name or cra_driver_name / driver name of the single block cipher

``type``
    specifies the type of the cipher

``mask``
    specifies the mask for the cipher


Return
======

true when the single block cipher is known to the kernel crypto API; false otherwise
