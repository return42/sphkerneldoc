
.. _API-crypto-shash-import:

===================
crypto_shash_import
===================

*man crypto_shash_import(9)*

*4.6.0-rc1*

import operational state


Synopsis
========

.. c:function:: int crypto_shash_import( struct shash_desc * desc, const void * in )

Arguments
=========

``desc``
    reference to the operational state handle the state imported into

``in``
    buffer holding the state


Description
===========

This function imports the hash state into the operational state handle from the input buffer. That buffer should have been generated with the crypto_ahash_export function.


Return
======

0 if the import was successful; < 0 if an error occurred
