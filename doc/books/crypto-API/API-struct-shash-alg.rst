.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-shash-alg:

================
struct shash_alg
================

*man struct shash_alg(9)*

*4.6.0-rc5*

synchronous message digest definition


Synopsis
========

.. code-block:: c

    struct shash_alg {
      int (* init) (struct shash_desc *desc);
      int (* update) (struct shash_desc *desc, const u8 *data,unsigned int len);
      int (* final) (struct shash_desc *desc, u8 *out);
      int (* finup) (struct shash_desc *desc, const u8 *data,unsigned int len, u8 *out);
      int (* digest) (struct shash_desc *desc, const u8 *data,unsigned int len, u8 *out);
      int (* export) (struct shash_desc *desc, void *out);
      int (* import) (struct shash_desc *desc, const void *in);
      int (* setkey) (struct crypto_shash *tfm, const u8 *key,unsigned int keylen);
      unsigned int descsize;
      unsigned int digestsize;
      unsigned int statesize;
      struct crypto_alg base;
    };


Members
=======

init
    see struct ahash_alg

update
    see struct ahash_alg

final
    see struct ahash_alg

finup
    see struct ahash_alg

digest
    see struct ahash_alg

export
    see struct ahash_alg

import
    see struct ahash_alg

setkey
    see struct ahash_alg

descsize
    Size of the operational state for the message digest. This state
    size is the memory size that needs to be allocated for
    shash_desc.__ctx

digestsize
    see struct ahash_alg

statesize
    see struct ahash_alg

base
    internally used


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
