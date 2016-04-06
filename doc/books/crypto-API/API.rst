
.. _API:

=====================
Programming Interface
=====================

Please note that the kernel crypto API contains the AEAD givcrypt API (crypto_aead_giv⋆ and aead_givcrypt_⋆ function calls in include/crypto/aead.h). This API is obsolete and
will be removed in the future. To obtain the functionality of an AEAD cipher with internal IV generation, use the IV generator as a regular cipher. For example, rfc4106(gcm(aes))
is the AEAD cipher with external IV generation and seqniv(rfc4106(gcm(aes))) implies that the kernel crypto API generates the IV. Different IV generators are available.


Block Cipher Context Data Structures
====================================

These data structures define the operating context for each block cipher type.


.. toctree::
    :maxdepth: 1

    API-struct-aead-request

Block Cipher Algorithm Definitions
==================================

These data structures define modular crypto algorithm implementations, managed via ``crypto_register_alg`` and ``crypto_unregister_alg``.


.. toctree::
    :maxdepth: 1

    API-struct-crypto-alg
    API-struct-ablkcipher-alg
    API-struct-aead-alg
    API-struct-blkcipher-alg
    API-struct-cipher-alg
    API-struct-rng-alg

Symmetric Key Cipher API
========================

Symmetric key cipher API is used with the ciphers of type CRYPTO_ALG_TYPE_SKCIPHER (listed as type “skcipher” in /proc/crypto).

Asynchronous cipher operations imply that the function invocation for a cipher request returns immediately before the completion of the operation. The cipher request is scheduled
as a separate kernel thread and therefore load-balanced on the different CPUs via the process scheduler. To allow the kernel crypto API to inform the caller about the completion of
a cipher request, the caller must provide a callback function. That function is invoked with the cipher handle when the request completes.

To support the asynchronous operation, additional information than just the cipher handle must be supplied to the kernel crypto API. That additional information is given by filling
in the skcipher_request data structure.

For the symmetric key cipher API, the state is maintained with the tfm cipher handle. A single tfm can be used across multiple calls and in parallel. For asynchronous block cipher
calls, context data supplied and only used by the caller can be referenced the request data structure in addition to the IV used for the cipher request. The maintenance of such
state information would be important for a crypto driver implementer to have, because when calling the callback function upon completion of the cipher operation, that callback
function may need some information about which operation just finished if it invoked multiple in parallel. This state information is unused by the kernel crypto API.


.. toctree::
    :maxdepth: 1

    API-crypto-alloc-skcipher
    API-crypto-free-skcipher
    API-crypto-has-skcipher
    API-crypto-skcipher-ivsize
    API-crypto-skcipher-blocksize
    API-crypto-skcipher-setkey
    API-crypto-skcipher-reqtfm
    API-crypto-skcipher-encrypt
    API-crypto-skcipher-decrypt

Symmetric Key Cipher Request Handle
===================================

The skcipher_request data structure contains all pointers to data required for the symmetric key cipher operation. This includes the cipher handle (which can be used by multiple
skcipher_request instances), pointer to plaintext and ciphertext, asynchronous callback function, etc. It acts as a handle to the skcipher_request_⋆ API calls in a similar way
as skcipher handle to the crypto_skcipher_⋆ API calls.


.. toctree::
    :maxdepth: 1

    API-crypto-skcipher-reqsize
    API-skcipher-request-set-tfm
    API-skcipher-request-alloc
    API-skcipher-request-free
    API-skcipher-request-set-callback
    API-skcipher-request-set-crypt

Asynchronous Block Cipher API - Deprecated
==========================================

Asynchronous block cipher API is used with the ciphers of type CRYPTO_ALG_TYPE_ABLKCIPHER (listed as type “ablkcipher” in /proc/crypto).

Asynchronous cipher operations imply that the function invocation for a cipher request returns immediately before the completion of the operation. The cipher request is scheduled
as a separate kernel thread and therefore load-balanced on the different CPUs via the process scheduler. To allow the kernel crypto API to inform the caller about the completion of
a cipher request, the caller must provide a callback function. That function is invoked with the cipher handle when the request completes.

To support the asynchronous operation, additional information than just the cipher handle must be supplied to the kernel crypto API. That additional information is given by filling
in the ablkcipher_request data structure.

For the asynchronous block cipher API, the state is maintained with the tfm cipher handle. A single tfm can be used across multiple calls and in parallel. For asynchronous block
cipher calls, context data supplied and only used by the caller can be referenced the request data structure in addition to the IV used for the cipher request. The maintenance of
such state information would be important for a crypto driver implementer to have, because when calling the callback function upon completion of the cipher operation, that callback
function may need some information about which operation just finished if it invoked multiple in parallel. This state information is unused by the kernel crypto API.


.. toctree::
    :maxdepth: 1

    API-crypto-alloc-ablkcipher
    API-crypto-free-ablkcipher
    API-crypto-has-ablkcipher
    API-crypto-ablkcipher-ivsize
    API-crypto-ablkcipher-blocksize
    API-crypto-ablkcipher-setkey
    API-crypto-ablkcipher-reqtfm
    API-crypto-ablkcipher-encrypt
    API-crypto-ablkcipher-decrypt

Asynchronous Cipher Request Handle - Deprecated
===============================================

The ablkcipher_request data structure contains all pointers to data required for the asynchronous cipher operation. This includes the cipher handle (which can be used by multiple
ablkcipher_request instances), pointer to plaintext and ciphertext, asynchronous callback function, etc. It acts as a handle to the ablkcipher_request_⋆ API calls in a similar
way as ablkcipher handle to the crypto_ablkcipher_⋆ API calls.


.. toctree::
    :maxdepth: 1

    API-crypto-ablkcipher-reqsize
    API-ablkcipher-request-set-tfm
    API-ablkcipher-request-alloc
    API-ablkcipher-request-free
    API-ablkcipher-request-set-callback
    API-ablkcipher-request-set-crypt

Authenticated Encryption With Associated Data (AEAD) Cipher API
===============================================================

The AEAD cipher API is used with the ciphers of type CRYPTO_ALG_TYPE_AEAD (listed as type “aead” in /proc/crypto)

The most prominent examples for this type of encryption is GCM and CCM. However, the kernel supports other types of AEAD ciphers which are defined with the following cipher string:

authenc(keyed message digest, block cipher)

For example: authenc(hmac(sha256), cbc(aes))

The example code provided for the symmetric key cipher operation applies here as well. Naturally all ⋆skcipher⋆ symbols must be exchanged the ⋆aead⋆ pendants discussed in the
following. In addition, for the AEAD operation, the aead_request_set_ad function must be used to set the pointer to the associated data memory location before performing the
encryption or decryption operation. In case of an encryption, the associated data memory is filled during the encryption operation. For decryption, the associated data memory must
contain data that is used to verify the integrity of the decrypted data. Another deviation from the asynchronous block cipher operation is that the caller should explicitly check
for -EBADMSG of the crypto_aead_decrypt. That error indicates an authentication error, i.e. a breach in the integrity of the message. In essence, that -EBADMSG error code is the
key bonus an AEAD cipher has over “standard” block chaining modes.

Memory Structure:

To support the needs of the most prominent user of AEAD ciphers, namely IPSEC, the AEAD ciphers have a special memory layout the caller must adhere to.

The scatter list pointing to the input data must contain:

⋆ for RFC4106 ciphers, the concatenation of associated authentication data || IV || plaintext or ciphertext. Note, the same IV (buffer) is also set with the
aead_request_set_crypt call. Note, the API call of aead_request_set_ad must provide the length of the AAD and the IV. The API call of aead_request_set_crypt only points to
the size of the input plaintext or ciphertext.

⋆ for “normal” AEAD ciphers, the concatenation of associated authentication data || plaintext or ciphertext.

It is important to note that if multiple scatter gather list entries form the input data mentioned above, the first entry must not point to a NULL buffer. If there is any potential
where the AAD buffer can be NULL, the calling code must contain a precaution to ensure that this does not result in the first scatter gather list entry pointing to a NULL buffer.


.. toctree::
    :maxdepth: 1

    API-crypto-alloc-aead
    API-crypto-free-aead
    API-crypto-aead-ivsize
    API-crypto-aead-authsize
    API-crypto-aead-blocksize
    API-crypto-aead-setkey
    API-crypto-aead-setauthsize
    API-crypto-aead-encrypt
    API-crypto-aead-decrypt

Asynchronous AEAD Request Handle
================================

The aead_request data structure contains all pointers to data required for the AEAD cipher operation. This includes the cipher handle (which can be used by multiple aead_request
instances), pointer to plaintext and ciphertext, asynchronous callback function, etc. It acts as a handle to the aead_request_⋆ API calls in a similar way as AEAD handle to the
crypto_aead_⋆ API calls.


.. toctree::
    :maxdepth: 1

    API-crypto-aead-reqsize
    API-aead-request-set-tfm
    API-aead-request-alloc
    API-aead-request-free
    API-aead-request-set-callback
    API-aead-request-set-crypt
    API-aead-request-set-ad

Synchronous Block Cipher API - Deprecated
=========================================

The synchronous block cipher API is used with the ciphers of type CRYPTO_ALG_TYPE_BLKCIPHER (listed as type “blkcipher” in /proc/crypto)

Synchronous calls, have a context in the tfm. But since a single tfm can be used in multiple calls and in parallel, this info should not be changeable (unless a lock is used). This
applies, for example, to the symmetric key. However, the IV is changeable, so there is an iv field in blkcipher_tfm structure for synchronous blkcipher api. So, its the only state
info that can be kept for synchronous calls without using a big lock across a tfm.

The block cipher API allows the use of a complete cipher, i.e. a cipher consisting of a template (a block chaining mode) and a single block cipher primitive (e.g. AES).

The plaintext data buffer and the ciphertext data buffer are pointed to by using scatter/gather lists. The cipher operation is performed on all segments of the provided
scatter/gather lists.

The kernel crypto API supports a cipher operation “in-place” which means that the caller may provide the same scatter/gather list for the plaintext and cipher text. After the
completion of the cipher operation, the plaintext data is replaced with the ciphertext data in case of an encryption and vice versa for a decryption. The caller must ensure that
the scatter/gather lists for the output data point to sufficiently large buffers, i.e. multiples of the block size of the cipher.


.. toctree::
    :maxdepth: 1

    API-crypto-alloc-blkcipher
    API-crypto-free-blkcipher
    API-crypto-has-blkcipher
    API-crypto-blkcipher-name
    API-crypto-blkcipher-ivsize
    API-crypto-blkcipher-blocksize
    API-crypto-blkcipher-setkey
    API-crypto-blkcipher-encrypt
    API-crypto-blkcipher-encrypt-iv
    API-crypto-blkcipher-decrypt
    API-crypto-blkcipher-decrypt-iv
    API-crypto-blkcipher-set-iv
    API-crypto-blkcipher-get-iv

Single Block Cipher API
=======================

The single block cipher API is used with the ciphers of type CRYPTO_ALG_TYPE_CIPHER (listed as type “cipher” in /proc/crypto).

Using the single block cipher API calls, operations with the basic cipher primitive can be implemented. These cipher primitives exclude any block chaining operations including IV
handling.

The purpose of this single block cipher API is to support the implementation of templates or other concepts that only need to perform the cipher operation on one block at a time.
Templates invoke the underlying cipher primitive block-wise and process either the input or the output data of these cipher operations.


.. toctree::
    :maxdepth: 1

    API-crypto-alloc-cipher
    API-crypto-free-cipher
    API-crypto-has-cipher
    API-crypto-cipher-blocksize
    API-crypto-cipher-setkey
    API-crypto-cipher-encrypt-one
    API-crypto-cipher-decrypt-one

Message Digest Algorithm Definitions
====================================

These data structures define modular message digest algorithm implementations, managed via ``crypto_register_ahash``, ``crypto_register_shash``, ``crypto_unregister_ahash`` and
``crypto_unregister_shash``.


.. toctree::
    :maxdepth: 1

    API-struct-hash-alg-common
    API-struct-ahash-alg
    API-struct-shash-alg

Asynchronous Message Digest API
===============================

The asynchronous message digest API is used with the ciphers of type CRYPTO_ALG_TYPE_AHASH (listed as type “ahash” in /proc/crypto)

The asynchronous cipher operation discussion provided for the CRYPTO_ALG_TYPE_ABLKCIPHER API applies here as well.


.. toctree::
    :maxdepth: 1

    API-crypto-alloc-ahash
    API-crypto-free-ahash
    API-crypto-ahash-init
    API-crypto-ahash-digestsize
    API-crypto-ahash-reqtfm
    API-crypto-ahash-reqsize
    API-crypto-ahash-setkey
    API-crypto-ahash-finup
    API-crypto-ahash-final
    API-crypto-ahash-digest
    API-crypto-ahash-export
    API-crypto-ahash-import

Asynchronous Hash Request Handle
================================

The ``ahash_request`` data structure contains all pointers to data required for the asynchronous cipher operation. This includes the cipher handle (which can be used by multiple
``ahash_request`` instances), pointer to plaintext and the message digest output buffer, asynchronous callback function, etc. It acts as a handle to the ahash_request_⋆ API calls
in a similar way as ahash handle to the crypto_ahash_⋆ API calls.


.. toctree::
    :maxdepth: 1

    API-ahash-request-set-tfm
    API-ahash-request-alloc
    API-ahash-request-free
    API-ahash-request-set-callback
    API-ahash-request-set-crypt

Synchronous Message Digest API
==============================

The synchronous message digest API is used with the ciphers of type CRYPTO_ALG_TYPE_SHASH (listed as type “shash” in /proc/crypto)

The message digest API is able to maintain state information for the caller.

The synchronous message digest API can store user-related context in in its shash_desc request data structure.


.. toctree::
    :maxdepth: 1

    API-crypto-alloc-shash
    API-crypto-free-shash
    API-crypto-shash-blocksize
    API-crypto-shash-digestsize
    API-crypto-shash-descsize
    API-crypto-shash-setkey
    API-crypto-shash-digest
    API-crypto-shash-export
    API-crypto-shash-import
    API-crypto-shash-init
    API-crypto-shash-update
    API-crypto-shash-final
    API-crypto-shash-finup

Crypto API Random Number API
============================

The random number generator API is used with the ciphers of type CRYPTO_ALG_TYPE_RNG (listed as type “rng” in /proc/crypto)


.. toctree::
    :maxdepth: 1

    API-crypto-alloc-rng
    API-crypto-rng-alg
    API-crypto-free-rng
    API-crypto-rng-generate
    API-crypto-rng-get-bytes
    API-crypto-rng-reset
    API-crypto-rng-seedsize

Asymmetric Cipher API
=====================

The Public Key API is used with the algorithms of type CRYPTO_ALG_TYPE_AKCIPHER (listed as type “akcipher” in /proc/crypto)


.. toctree::
    :maxdepth: 1

    API-struct-akcipher-alg
    API-struct-akcipher-request
    API-crypto-alloc-akcipher
    API-crypto-free-akcipher
    API-crypto-akcipher-set-pub-key
    API-crypto-akcipher-set-priv-key

Asymmetric Cipher Request Handle
================================


.. toctree::
    :maxdepth: 1

    API-akcipher-request-alloc
    API-akcipher-request-free
    API-akcipher-request-set-callback
    API-akcipher-request-set-crypt
    API-crypto-akcipher-maxsize
    API-crypto-akcipher-encrypt
    API-crypto-akcipher-decrypt
    API-crypto-akcipher-sign
    API-crypto-akcipher-verify
