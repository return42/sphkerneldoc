
.. _API-crypto-ablkcipher-decrypt:

=========================
crypto_ablkcipher_decrypt
=========================

*man crypto_ablkcipher_decrypt(9)*

*4.6.0-rc1*

decrypt ciphertext


Synopsis
========

.. c:function:: int crypto_ablkcipher_decrypt( struct ablkcipher_request * req )

Arguments
=========

``req``
    reference to the ablkcipher_request handle that holds all information needed to perform the cipher operation


Description
===========

Decrypt ciphertext data using the ablkcipher_request handle. That data structure and how it is filled with data is discussed with the ablkcipher_request_⋆ functions.


Return
======

0 if the cipher operation was successful; < 0 if an error occurred
