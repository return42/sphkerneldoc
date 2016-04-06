
.. _API-crypto-shash-final:

==================
crypto_shash_final
==================

*man crypto_shash_final(9)*

*4.6.0-rc1*

calculate message digest


Synopsis
========

.. c:function:: int crypto_shash_final( struct shash_desc * desc, u8 * out )

Arguments
=========

``desc``
    operational state handle that is already filled with data

``out``
    output buffer filled with the message digest


Description
===========

Finalize the message digest operation and create the message digest based on all data added to the cipher handle. The message digest is placed into the output buffer. The caller
must ensure that the output buffer is large enough by using crypto_shash_digestsize.


Return
======

0 if the message digest creation was successful; < 0 if an error occurred
