
.. _API-crypto-shash-finup:

==================
crypto_shash_finup
==================

*man crypto_shash_finup(9)*

*4.6.0-rc1*

calculate message digest of buffer


Synopsis
========

.. c:function:: int crypto_shash_finup( struct shash_desc * desc, const u8 * data, unsigned int len, u8 * out )

Arguments
=========

``desc``
    see ``crypto_shash_final``

``data``
    see ``crypto_shash_update``

``len``
    see ``crypto_shash_update``

``out``
    see ``crypto_shash_final``


Description
===========

This function is a “short-hand” for the function calls of crypto_shash_update and crypto_shash_final. The parameters have the same meaning as discussed for those separate
functions.


Return
======

0 if the message digest creation was successful; < 0 if an error occurred
