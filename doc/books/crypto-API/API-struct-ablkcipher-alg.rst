.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ablkcipher-alg:

=====================
struct ablkcipher_alg
=====================

*man struct ablkcipher_alg(9)*

*4.6.0-rc5*

asynchronous block cipher definition


Synopsis
========

.. code-block:: c

    struct ablkcipher_alg {
      int (* setkey) (struct crypto_ablkcipher *tfm, const u8 *key,unsigned int keylen);
      int (* encrypt) (struct ablkcipher_request *req);
      int (* decrypt) (struct ablkcipher_request *req);
      int (* givencrypt) (struct skcipher_givcrypt_request *req);
      int (* givdecrypt) (struct skcipher_givcrypt_request *req);
      const char * geniv;
      unsigned int min_keysize;
      unsigned int max_keysize;
      unsigned int ivsize;
    };


Members
=======

setkey
    Set key for the transformation. This function is used to either
    program a supplied key into the hardware or store the key in the
    transformation context for programming it later. Note that this
    function does modify the transformation context. This function can
    be called multiple times during the existence of the transformation
    object, so one must make sure the key is properly reprogrammed into
    the hardware. This function is also responsible for checking the key
    length for validity. In case a software fallback was put in place in
    the ``cra_init`` call, this function might need to use the fallback
    if the algorithm doesn't support all of the key sizes.

encrypt
    Encrypt a scatterlist of blocks. This function is used to encrypt
    the supplied scatterlist containing the blocks of data. The crypto
    API consumer is responsible for aligning the entries of the
    scatterlist properly and making sure the chunks are correctly sized.
    In case a software fallback was put in place in the ``cra_init``
    call, this function might need to use the fallback if the algorithm
    doesn't support all of the key sizes. In case the key was stored in
    transformation context, the key might need to be re-programmed into
    the hardware in this function. This function shall not modify the
    transformation context, as this function may be called in parallel
    with the same transformation object.

decrypt
    Decrypt a single block. This is a reverse counterpart to ``encrypt``
    and the conditions are exactly the same.

givencrypt
    Update the IV for encryption. With this function, a cipher
    implementation may provide the function on how to update the IV for
    encryption.

givdecrypt
    Update the IV for decryption. This is the reverse of ``givencrypt``
    .

geniv
    The transformation implementation may use an “IV generator” provided
    by the kernel crypto API. Several use cases have a predefined
    approach how IVs are to be updated. For such use cases, the kernel
    crypto API provides ready-to-use implementations that can be
    referenced with this variable.

min_keysize
    Minimum key size supported by the transformation. This is the
    smallest key length supported by this transformation algorithm. This
    must be set to one of the pre-defined values as this is not hardware
    specific. Possible values for this field can be found via git grep
    “_MIN_KEY_SIZE” include/crypto/

max_keysize
    Maximum key size supported by the transformation. This is the
    largest key length supported by this transformation algorithm. This
    must be set to one of the pre-defined values as this is not hardware
    specific. Possible values for this field can be found via git grep
    “_MAX_KEY_SIZE” include/crypto/

ivsize
    IV size applicable for transformation. The consumer must provide an
    IV of exactly that size to perform the encrypt or decrypt operation.


Description
===========

All fields except ``givencrypt`` , ``givdecrypt`` , ``geniv`` and
``ivsize`` are mandatory and must be filled.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
