.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-akcipher-maxsize:

=======================
crypto_akcipher_maxsize
=======================

*man crypto_akcipher_maxsize(9)*

*4.6.0-rc5*

Get len for output buffer


Synopsis
========

.. c:function:: int crypto_akcipher_maxsize( struct crypto_akcipher * tfm )

Arguments
=========

``tfm``
    AKCIPHER tfm handle allocated with ``crypto_alloc_akcipher``


Description
===========

Function returns the dest buffer size required for a given key


Return
======

minimum len for output buffer or error code in key hasn't been set


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
