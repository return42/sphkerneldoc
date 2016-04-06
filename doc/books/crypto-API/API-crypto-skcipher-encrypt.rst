
.. _API-crypto-skcipher-encrypt:

=======================
crypto_skcipher_encrypt
=======================

*man crypto_skcipher_encrypt(9)*

*4.6.0-rc1*

encrypt plaintext


Synopsis
========

.. c:function:: int crypto_skcipher_encrypt( struct skcipher_request * req )

Arguments
=========

``req``
    reference to the skcipher_request handle that holds all information needed to perform the cipher operation


Description
===========

Encrypt plaintext data using the skcipher_request handle. That data structure and how it is filled with data is discussed with the skcipher_request_⋆ functions.


Return
======

0 if the cipher operation was successful; < 0 if an error occurred
