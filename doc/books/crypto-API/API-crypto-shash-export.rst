.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-shash-export:

===================
crypto_shash_export
===================

*man crypto_shash_export(9)*

*4.6.0-rc5*

extract operational state for message digest


Synopsis
========

.. c:function:: int crypto_shash_export( struct shash_desc * desc, void * out )

Arguments
=========

``desc``
    reference to the operational state handle whose state is exported

``out``
    output buffer of sufficient size that can hold the hash state


Description
===========

This function exports the hash state of the operational state handle
into the caller-allocated output buffer out which must have sufficient
size (e.g. by calling crypto_shash_descsize).


Return
======

0 if the export creation was successful; < 0 if an error occurred


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
