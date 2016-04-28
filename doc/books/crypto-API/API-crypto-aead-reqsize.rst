.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-aead-reqsize:

===================
crypto_aead_reqsize
===================

*man crypto_aead_reqsize(9)*

*4.6.0-rc5*

obtain size of the request data structure


Synopsis
========

.. c:function:: unsigned int crypto_aead_reqsize( struct crypto_aead * tfm )

Arguments
=========

``tfm``
    cipher handle


Return
======

number of bytes


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
