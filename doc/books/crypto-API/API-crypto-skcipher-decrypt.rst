.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-skcipher-decrypt:

=======================
crypto_skcipher_decrypt
=======================

*man crypto_skcipher_decrypt(9)*

*4.6.0-rc5*

decrypt ciphertext


Synopsis
========

.. c:function:: int crypto_skcipher_decrypt( struct skcipher_request * req )

Arguments
=========

``req``
    reference to the skcipher_request handle that holds all information
    needed to perform the cipher operation


Description
===========

Decrypt ciphertext data using the skcipher_request handle. That data
structure and how it is filled with data is discussed with the
skcipher_request_* functions.


Return
======

0 if the cipher operation was successful; < 0 if an error occurred


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
