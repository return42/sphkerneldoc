
.. _API-crypto-akcipher-verify:

======================
crypto_akcipher_verify
======================

*man crypto_akcipher_verify(9)*

*4.6.0-rc1*

Invoke public key verify operation


Synopsis
========

.. c:function:: int crypto_akcipher_verify( struct akcipher_request * req )

Arguments
=========

``req``
    asymmetric key request


Description
===========

Function invokes the specific public key verify operation for a given public key algorithm


Return
======

zero on success; error code in case of error
