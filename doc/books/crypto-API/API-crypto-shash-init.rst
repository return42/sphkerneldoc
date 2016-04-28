.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-shash-init:

=================
crypto_shash_init
=================

*man crypto_shash_init(9)*

*4.6.0-rc5*

(re)initialize message digest


Synopsis
========

.. c:function:: int crypto_shash_init( struct shash_desc * desc )

Arguments
=========

``desc``
    operational state handle that is already filled


Description
===========

The call (re-)initializes the message digest referenced by the
operational state handle. Any potentially existing state created by
previous operations is discarded.


Return
======

0 if the message digest initialization was successful; < 0 if an error
occurred


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
