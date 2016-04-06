
.. _API-crypto-akcipher-encrypt:

=======================
crypto_akcipher_encrypt
=======================

*man crypto_akcipher_encrypt(9)*

*4.6.0-rc1*

Invoke public key encrypt operation


Synopsis
========

.. c:function:: int crypto_akcipher_encrypt( struct akcipher_request * req )

Arguments
=========

``req``
    asymmetric key request


Description
===========

Function invokes the specific public key encrypt operation for a given public key algorithm


Return
======

zero on success; error code in case of error
