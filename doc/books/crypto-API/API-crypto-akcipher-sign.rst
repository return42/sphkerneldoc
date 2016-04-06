
.. _API-crypto-akcipher-sign:

====================
crypto_akcipher_sign
====================

*man crypto_akcipher_sign(9)*

*4.6.0-rc1*

Invoke public key sign operation


Synopsis
========

.. c:function:: int crypto_akcipher_sign( struct akcipher_request * req )

Arguments
=========

``req``
    asymmetric key request


Description
===========

Function invokes the specific public key sign operation for a given public key algorithm


Return
======

zero on success; error code in case of error
