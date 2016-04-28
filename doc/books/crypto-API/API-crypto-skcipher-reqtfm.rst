.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-skcipher-reqtfm:

======================
crypto_skcipher_reqtfm
======================

*man crypto_skcipher_reqtfm(9)*

*4.6.0-rc5*

obtain cipher handle from request


Synopsis
========

.. c:function:: struct crypto_skcipher * crypto_skcipher_reqtfm( struct skcipher_request * req )

Arguments
=========

``req``
    skcipher_request out of which the cipher handle is to be obtained


Description
===========

Return the crypto_skcipher handle when furnishing an skcipher_request
data structure.


Return
======

crypto_skcipher handle


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
