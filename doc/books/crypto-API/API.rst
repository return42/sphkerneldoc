.. -*- coding: utf-8; mode: rst -*-

.. _API:

*********************
Programming Interface
*********************

Please note that the kernel crypto API contains the AEAD givcrypt API
(crypto_aead_giv* and aead_givcrypt_* function calls in
include/crypto/aead.h). This API is obsolete and will be removed in the
future. To obtain the functionality of an AEAD cipher with internal IV
generation, use the IV generator as a regular cipher. For example,
rfc4106(gcm(aes)) is the AEAD cipher with external IV generation and
seqniv(rfc4106(gcm(aes))) implies that the kernel crypto API generates
the IV. Different IV generators are available.


Block Cipher Context Data Structures
====================================


.. kernel-doc:: include/linux/crypto.h
    :doc: Block Cipher Context Data Structures

.. kernel-doc:: include/crypto/aead.h
    :functions: aead_request

Block Cipher Algorithm Definitions
==================================


.. kernel-doc:: include/linux/crypto.h
    :doc: Block Cipher Algorithm Definitions

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_alg

.. kernel-doc:: include/linux/crypto.h
    :functions: ablkcipher_alg

.. kernel-doc:: include/crypto/aead.h
    :functions: aead_alg

.. kernel-doc:: include/linux/crypto.h
    :functions: blkcipher_alg

.. kernel-doc:: include/linux/crypto.h
    :functions: cipher_alg

.. kernel-doc:: include/crypto/rng.h
    :functions: rng_alg

Symmetric Key Cipher API
========================


.. kernel-doc:: include/crypto/skcipher.h
    :doc: Symmetric Key Cipher API

.. kernel-doc:: include/crypto/skcipher.h
    :functions: crypto_alloc_skcipher

.. kernel-doc:: include/crypto/skcipher.h
    :functions: crypto_free_skcipher

.. kernel-doc:: include/crypto/skcipher.h
    :functions: crypto_has_skcipher

.. kernel-doc:: include/crypto/skcipher.h
    :functions: crypto_skcipher_ivsize

.. kernel-doc:: include/crypto/skcipher.h
    :functions: crypto_skcipher_blocksize

.. kernel-doc:: include/crypto/skcipher.h
    :functions: crypto_skcipher_setkey

.. kernel-doc:: include/crypto/skcipher.h
    :functions: crypto_skcipher_reqtfm

.. kernel-doc:: include/crypto/skcipher.h
    :functions: crypto_skcipher_encrypt

.. kernel-doc:: include/crypto/skcipher.h
    :functions: crypto_skcipher_decrypt

Symmetric Key Cipher Request Handle
===================================


.. kernel-doc:: include/crypto/skcipher.h
    :doc: Symmetric Key Cipher Request Handle

.. kernel-doc:: include/crypto/skcipher.h
    :functions: crypto_skcipher_reqsize

.. kernel-doc:: include/crypto/skcipher.h
    :functions: skcipher_request_set_tfm

.. kernel-doc:: include/crypto/skcipher.h
    :functions: skcipher_request_alloc

.. kernel-doc:: include/crypto/skcipher.h
    :functions: skcipher_request_free

.. kernel-doc:: include/crypto/skcipher.h
    :functions: skcipher_request_set_callback

.. kernel-doc:: include/crypto/skcipher.h
    :functions: skcipher_request_set_crypt

Asynchronous Block Cipher API - Deprecated
==========================================


.. kernel-doc:: include/linux/crypto.h
    :doc: Asynchronous Block Cipher API

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_alloc_ablkcipher

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_free_ablkcipher

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_has_ablkcipher

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_ablkcipher_ivsize

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_ablkcipher_blocksize

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_ablkcipher_setkey

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_ablkcipher_reqtfm

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_ablkcipher_encrypt

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_ablkcipher_decrypt

Asynchronous Cipher Request Handle - Deprecated
===============================================


.. kernel-doc:: include/linux/crypto.h
    :doc: Asynchronous Cipher Request Handle

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_ablkcipher_reqsize

.. kernel-doc:: include/linux/crypto.h
    :functions: ablkcipher_request_set_tfm

.. kernel-doc:: include/linux/crypto.h
    :functions: ablkcipher_request_alloc

.. kernel-doc:: include/linux/crypto.h
    :functions: ablkcipher_request_free

.. kernel-doc:: include/linux/crypto.h
    :functions: ablkcipher_request_set_callback

.. kernel-doc:: include/linux/crypto.h
    :functions: ablkcipher_request_set_crypt

Authenticated Encryption With Associated Data (AEAD) Cipher API
===============================================================


.. kernel-doc:: include/crypto/aead.h
    :doc: Authenticated Encryption With Associated Data (AEAD) Cipher API

.. kernel-doc:: include/crypto/aead.h
    :functions: crypto_alloc_aead

.. kernel-doc:: include/crypto/aead.h
    :functions: crypto_free_aead

.. kernel-doc:: include/crypto/aead.h
    :functions: crypto_aead_ivsize

.. kernel-doc:: include/crypto/aead.h
    :functions: crypto_aead_authsize

.. kernel-doc:: include/crypto/aead.h
    :functions: crypto_aead_blocksize

.. kernel-doc:: include/crypto/aead.h
    :functions: crypto_aead_setkey

.. kernel-doc:: include/crypto/aead.h
    :functions: crypto_aead_setauthsize

.. kernel-doc:: include/crypto/aead.h
    :functions: crypto_aead_encrypt

.. kernel-doc:: include/crypto/aead.h
    :functions: crypto_aead_decrypt

Asynchronous AEAD Request Handle
================================


.. kernel-doc:: include/crypto/aead.h
    :doc: Asynchronous AEAD Request Handle

.. kernel-doc:: include/crypto/aead.h
    :functions: crypto_aead_reqsize

.. kernel-doc:: include/crypto/aead.h
    :functions: aead_request_set_tfm

.. kernel-doc:: include/crypto/aead.h
    :functions: aead_request_alloc

.. kernel-doc:: include/crypto/aead.h
    :functions: aead_request_free

.. kernel-doc:: include/crypto/aead.h
    :functions: aead_request_set_callback

.. kernel-doc:: include/crypto/aead.h
    :functions: aead_request_set_crypt

.. kernel-doc:: include/crypto/aead.h
    :functions: aead_request_set_ad

Synchronous Block Cipher API - Deprecated
=========================================


.. kernel-doc:: include/linux/crypto.h
    :doc: Synchronous Block Cipher API

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_alloc_blkcipher

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_free_blkcipher

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_has_blkcipher

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_blkcipher_name

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_blkcipher_ivsize

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_blkcipher_blocksize

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_blkcipher_setkey

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_blkcipher_encrypt

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_blkcipher_encrypt_iv

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_blkcipher_decrypt

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_blkcipher_decrypt_iv

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_blkcipher_set_iv

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_blkcipher_get_iv

Single Block Cipher API
=======================


.. kernel-doc:: include/linux/crypto.h
    :doc: Single Block Cipher API

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_alloc_cipher

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_free_cipher

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_has_cipher

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_cipher_blocksize

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_cipher_setkey

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_cipher_encrypt_one

.. kernel-doc:: include/linux/crypto.h
    :functions: crypto_cipher_decrypt_one

Message Digest Algorithm Definitions
====================================


.. kernel-doc:: include/crypto/hash.h
    :doc: Message Digest Algorithm Definitions

.. kernel-doc:: include/crypto/hash.h
    :functions: hash_alg_common

.. kernel-doc:: include/crypto/hash.h
    :functions: ahash_alg

.. kernel-doc:: include/crypto/hash.h
    :functions: shash_alg

Asynchronous Message Digest API
===============================


.. kernel-doc:: include/crypto/hash.h
    :doc: Asynchronous Message Digest API

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_alloc_ahash

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_free_ahash

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_ahash_init

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_ahash_digestsize

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_ahash_reqtfm

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_ahash_reqsize

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_ahash_setkey

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_ahash_finup

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_ahash_final

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_ahash_digest

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_ahash_export

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_ahash_import

Asynchronous Hash Request Handle
================================


.. kernel-doc:: include/crypto/hash.h
    :doc: Asynchronous Hash Request Handle

.. kernel-doc:: include/crypto/hash.h
    :functions: ahash_request_set_tfm

.. kernel-doc:: include/crypto/hash.h
    :functions: ahash_request_alloc

.. kernel-doc:: include/crypto/hash.h
    :functions: ahash_request_free

.. kernel-doc:: include/crypto/hash.h
    :functions: ahash_request_set_callback

.. kernel-doc:: include/crypto/hash.h
    :functions: ahash_request_set_crypt

Synchronous Message Digest API
==============================


.. kernel-doc:: include/crypto/hash.h
    :doc: Synchronous Message Digest API

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_alloc_shash

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_free_shash

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_shash_blocksize

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_shash_digestsize

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_shash_descsize

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_shash_setkey

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_shash_digest

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_shash_export

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_shash_import

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_shash_init

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_shash_update

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_shash_final

.. kernel-doc:: include/crypto/hash.h
    :functions: crypto_shash_finup

Crypto API Random Number API
============================


.. kernel-doc:: include/crypto/rng.h
    :doc: Random number generator API

.. kernel-doc:: include/crypto/rng.h
    :functions: crypto_alloc_rng

.. kernel-doc:: include/crypto/rng.h
    :functions: crypto_rng_alg

.. kernel-doc:: include/crypto/rng.h
    :functions: crypto_free_rng

.. kernel-doc:: include/crypto/rng.h
    :functions: crypto_rng_generate

.. kernel-doc:: include/crypto/rng.h
    :functions: crypto_rng_get_bytes

.. kernel-doc:: include/crypto/rng.h
    :functions: crypto_rng_reset

.. kernel-doc:: include/crypto/rng.h
    :functions: crypto_rng_seedsize


.. NOT SUPPORTED: '!Cinclude/crypto/rng.h '

Asymmetric Cipher API
=====================


.. kernel-doc:: include/crypto/akcipher.h
    :doc: Generic Public Key API

.. kernel-doc:: include/crypto/akcipher.h
    :functions: akcipher_alg

.. kernel-doc:: include/crypto/akcipher.h
    :functions: akcipher_request

.. kernel-doc:: include/crypto/akcipher.h
    :functions: crypto_alloc_akcipher

.. kernel-doc:: include/crypto/akcipher.h
    :functions: crypto_free_akcipher

.. kernel-doc:: include/crypto/akcipher.h
    :functions: crypto_akcipher_set_pub_key

.. kernel-doc:: include/crypto/akcipher.h
    :functions: crypto_akcipher_set_priv_key

Asymmetric Cipher Request Handle
================================


.. kernel-doc:: include/crypto/akcipher.h
    :functions: akcipher_request_alloc

.. kernel-doc:: include/crypto/akcipher.h
    :functions: akcipher_request_free

.. kernel-doc:: include/crypto/akcipher.h
    :functions: akcipher_request_set_callback

.. kernel-doc:: include/crypto/akcipher.h
    :functions: akcipher_request_set_crypt

.. kernel-doc:: include/crypto/akcipher.h
    :functions: crypto_akcipher_maxsize

.. kernel-doc:: include/crypto/akcipher.h
    :functions: crypto_akcipher_encrypt

.. kernel-doc:: include/crypto/akcipher.h
    :functions: crypto_akcipher_decrypt

.. kernel-doc:: include/crypto/akcipher.h
    :functions: crypto_akcipher_sign

.. kernel-doc:: include/crypto/akcipher.h
    :functions: crypto_akcipher_verify



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
