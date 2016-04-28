.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-rng-seedsize:

===================
crypto_rng_seedsize
===================

*man crypto_rng_seedsize(9)*

*4.6.0-rc5*

obtain seed size of RNG


Synopsis
========

.. c:function:: int crypto_rng_seedsize( struct crypto_rng * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The function returns the seed size for the random number generator
referenced by the cipher handle. This value may be zero if the random
number generator does not implement or require a reseeding. For example,
the SP800-90A DRBGs implement an automated reseeding after reaching a
pre-defined threshold.


Return
======

seed size for the random number generator


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
