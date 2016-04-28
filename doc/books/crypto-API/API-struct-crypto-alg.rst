.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-crypto-alg:

=================
struct crypto_alg
=================

*man struct crypto_alg(9)*

*4.6.0-rc5*

definition of a cryptograpic cipher algorithm


Synopsis
========

.. code-block:: c

    struct crypto_alg {
      struct list_head cra_list;
      struct list_head cra_users;
      u32 cra_flags;
      unsigned int cra_blocksize;
      unsigned int cra_ctxsize;
      unsigned int cra_alignmask;
      int cra_priority;
      atomic_t cra_refcnt;
      char cra_name[CRYPTO_MAX_ALG_NAME];
      char cra_driver_name[CRYPTO_MAX_ALG_NAME];
      const struct crypto_type * cra_type;
      union cra_u;
      int (* cra_init) (struct crypto_tfm *tfm);
      void (* cra_exit) (struct crypto_tfm *tfm);
      void (* cra_destroy) (struct crypto_alg *alg);
      struct module * cra_module;
    };


Members
=======

cra_list
    internally used

cra_users
    internally used

cra_flags
    Flags describing this transformation. See include/linux/crypto.h
    CRYPTO_ALG_* flags for the flags which go in here. Those are used
    for fine-tuning the description of the transformation algorithm.

cra_blocksize
    Minimum block size of this transformation. The size in bytes of the
    smallest possible unit which can be transformed with this algorithm.
    The users must respect this value. In case of HASH transformation,
    it is possible for a smaller block than ``cra_blocksize`` to be
    passed to the crypto API for transformation, in case of any other
    transformation type, an error will be returned upon any attempt to
    transform smaller than ``cra_blocksize`` chunks.

cra_ctxsize
    Size of the operational context of the transformation. This value
    informs the kernel crypto API about the memory size needed to be
    allocated for the transformation context.

cra_alignmask
    Alignment mask for the input and output data buffer. The data buffer
    containing the input data for the algorithm must be aligned to this
    alignment mask. The data buffer for the output data must be aligned
    to this alignment mask. Note that the Crypto API will do the
    re-alignment in software, but only under special conditions and
    there is a performance hit. The re-alignment happens at these
    occasions for different

cra_priority
    Priority of this transformation implementation. In case multiple
    transformations with same ``cra_name`` are available to the Crypto
    API, the kernel will use the one with highest ``cra_priority``.

cra_refcnt
    internally used

cra_name[CRYPTO_MAX_ALG_NAME]
    Generic name (usable by multiple implementations) of the
    transformation algorithm. This is the name of the transformation
    itself. This field is used by the kernel when looking up the
    providers of particular transformation.

cra_driver_name[CRYPTO_MAX_ALG_NAME]
    Unique name of the transformation provider. This is the name of the
    provider of the transformation. This can be any arbitrary value, but
    in the usual case, this contains the name of the chip or provider
    and the name of the transformation algorithm.

cra_type
    Type of the cryptographic transformation. This is a pointer to
    struct crypto_type, which implements callbacks common for all
    transformation types. There are multiple options:
    ``crypto_blkcipher_type``, ``crypto_ablkcipher_type``,
    ``crypto_ahash_type``, ``crypto_rng_type``. This field might be
    empty. In that case, there are no common callbacks. This is the case
    for: cipher, compress, shash.

cra_u
    Callbacks implementing the transformation. This is a union of
    multiple structures. Depending on the type of transformation
    selected by ``cra_type`` and ``cra_flags`` above, the associated
    structure must be filled with callbacks. This field might be empty.
    This is the case for ahash, shash.

cra_init
    Initialize the cryptographic transformation object. This function is
    used to initialize the cryptographic transformation object. This
    function is called only once at the instantiation time, right after
    the transformation context was allocated. In case the cryptographic
    hardware has some special requirements which need to be handled by
    software, this function shall check for the precise requirement of
    the transformation and put any software fallbacks in place.

cra_exit
    Deinitialize the cryptographic transformation object. This is a
    counterpart to ``cra_init``, used to remove various changes set in
    ``cra_init``.

cra_destroy
    internally used

cra_module
    Owner of this transformation implementation. Set to THIS_MODULE


Description
===========

The struct crypto_alg describes a generic Crypto API algorithm and is
common for all of the transformations. Any variable not documented here
shall not be used by a cipher implementation as it is internal to the
Crypto API.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
