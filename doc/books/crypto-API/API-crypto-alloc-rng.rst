.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-alloc-rng:

================
crypto_alloc_rng
================

*man crypto_alloc_rng(9)*

*4.6.0-rc5*

- allocate RNG handle


Synopsis
========

.. c:function:: struct crypto_rng * crypto_alloc_rng( const char * alg_name, u32 type, u32 mask )

Arguments
=========

``alg_name``
    is the cra_name / name or cra_driver_name / driver name of the
    message digest cipher

``type``
    specifies the type of the cipher

``mask``
    specifies the mask for the cipher


Description
===========

Allocate a cipher handle for a random number generator. The returned
struct crypto_rng is the cipher handle that is required for any
subsequent API invocation for that random number generator.

For all random number generators, this call creates a new private copy
of the random number generator that does not share a state with other
instances. The only exception is the “krng” random number generator
which is a kernel crypto API use case for the ``get_random_bytes``
function of the /dev/random driver.


Return
======

allocated cipher handle in case of success; ``IS_ERR`` is true in case
of an error, ``PTR_ERR`` returns the error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
