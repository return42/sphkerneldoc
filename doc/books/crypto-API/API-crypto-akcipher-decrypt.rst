
.. _API-crypto-akcipher-decrypt:

=======================
crypto_akcipher_decrypt
=======================

*man crypto_akcipher_decrypt(9)*

*4.6.0-rc1*

Invoke public key decrypt operation


Synopsis
========

.. c:function:: int crypto_akcipher_decrypt( struct akcipher_request * req )

Arguments
=========

``req``
    asymmetric key request


Description
===========

Function invokes the specific public key decrypt operation for a given public key algorithm


Return
======

zero on success; error code in case of error
