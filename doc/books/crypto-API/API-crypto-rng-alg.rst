.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-rng-alg:

==============
crypto_rng_alg
==============

*man crypto_rng_alg(9)*

*4.6.0-rc5*

obtain name of RNG


Synopsis
========

.. c:function:: struct rng_alg * crypto_rng_alg( struct crypto_rng * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

Return the generic name (cra_name) of the initialized random number
generator


Return
======

generic name string


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
