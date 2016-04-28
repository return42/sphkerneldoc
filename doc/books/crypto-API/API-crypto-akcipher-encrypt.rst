.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-akcipher-encrypt:

=======================
crypto_akcipher_encrypt
=======================

*man crypto_akcipher_encrypt(9)*

*4.6.0-rc5*

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

Function invokes the specific public key encrypt operation for a given
public key algorithm


Return
======

zero on success; error code in case of error


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
