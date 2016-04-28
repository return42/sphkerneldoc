.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-ablkcipher-reqtfm:

========================
crypto_ablkcipher_reqtfm
========================

*man crypto_ablkcipher_reqtfm(9)*

*4.6.0-rc5*

obtain cipher handle from request


Synopsis
========

.. c:function:: struct crypto_ablkcipher * crypto_ablkcipher_reqtfm( struct ablkcipher_request * req )

Arguments
=========

``req``
    ablkcipher_request out of which the cipher handle is to be obtained


Description
===========

Return the crypto_ablkcipher handle when furnishing an
ablkcipher_request data structure.


Return
======

crypto_ablkcipher handle


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
