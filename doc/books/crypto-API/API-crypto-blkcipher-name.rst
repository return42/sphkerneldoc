
.. _API-crypto-blkcipher-name:

=====================
crypto_blkcipher_name
=====================

*man crypto_blkcipher_name(9)*

*4.6.0-rc1*

return the name / cra_name from the cipher handle


Synopsis
========

.. c:function:: const char ⋆ crypto_blkcipher_name( struct crypto_blkcipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Return
======

The character string holding the name of the cipher
