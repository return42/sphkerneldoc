.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-skcipher-reqsize:

=======================
crypto_skcipher_reqsize
=======================

*man crypto_skcipher_reqsize(9)*

*4.6.0-rc5*

obtain size of the request data structure


Synopsis
========

.. c:function:: unsigned int crypto_skcipher_reqsize( struct crypto_skcipher * tfm )

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
