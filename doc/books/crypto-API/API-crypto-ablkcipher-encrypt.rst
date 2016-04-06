
.. _API-crypto-ablkcipher-encrypt:

=========================
crypto_ablkcipher_encrypt
=========================

*man crypto_ablkcipher_encrypt(9)*

*4.6.0-rc1*

encrypt plaintext


Synopsis
========

.. c:function:: int crypto_ablkcipher_encrypt( struct ablkcipher_request * req )

Arguments
=========

``req``
    reference to the ablkcipher_request handle that holds all information needed to perform the cipher operation


Description
===========

Encrypt plaintext data using the ablkcipher_request handle. That data structure and how it is filled with data is discussed with the ablkcipher_request_⋆ functions.


Return
======

0 if the cipher operation was successful; < 0 if an error occurred
