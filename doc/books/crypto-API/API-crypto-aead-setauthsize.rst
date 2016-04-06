
.. _API-crypto-aead-setauthsize:

=======================
crypto_aead_setauthsize
=======================

*man crypto_aead_setauthsize(9)*

*4.6.0-rc1*

set authentication data size


Synopsis
========

.. c:function:: int crypto_aead_setauthsize( struct crypto_aead * tfm, unsigned int authsize )

Arguments
=========

``tfm``
    cipher handle

``authsize``
    size of the authentication data / tag in bytes


Description
===========

Set the authentication data size / tag size. AEAD requires an authentication tag (or MAC) in addition to the associated data.


Return
======

0 if the setting of the key was successful; < 0 if an error occurred
