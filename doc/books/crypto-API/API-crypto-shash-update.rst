
.. _API-crypto-shash-update:

===================
crypto_shash_update
===================

*man crypto_shash_update(9)*

*4.6.0-rc1*

add data to message digest for processing


Synopsis
========

.. c:function:: int crypto_shash_update( struct shash_desc * desc, const u8 * data, unsigned int len )

Arguments
=========

``desc``
    operational state handle that is already initialized

``data``
    input data to be added to the message digest

``len``
    length of the input data


Description
===========

Updates the message digest state of the operational state handle.


Return
======

0 if the message digest update was successful; < 0 if an error occurred
