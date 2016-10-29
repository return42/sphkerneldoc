.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/skcipher.h

.. _`skcipher_request`:

struct skcipher_request
=======================

.. c:type:: struct skcipher_request

    Symmetric key cipher request

.. _`skcipher_request.definition`:

Definition
----------

.. code-block:: c

    struct skcipher_request {
        unsigned int cryptlen;
        u8 *iv;
        struct scatterlist *src;
        struct scatterlist *dst;
        struct crypto_async_request base;
        void  *__ctx[];
    }

.. _`skcipher_request.members`:

Members
-------

cryptlen
    Number of bytes to encrypt or decrypt

iv
    Initialisation Vector

src
    Source SG list

dst
    Destination SG list

base
    Underlying async request request

__ctx
    Start of private context data

.. _`skcipher_givcrypt_request`:

struct skcipher_givcrypt_request
================================

.. c:type:: struct skcipher_givcrypt_request

    Crypto request with IV generation

.. _`skcipher_givcrypt_request.definition`:

Definition
----------

.. code-block:: c

    struct skcipher_givcrypt_request {
        u64 seq;
        u8 *giv;
        struct ablkcipher_request creq;
    }

.. _`skcipher_givcrypt_request.members`:

Members
-------

seq
    Sequence number for IV generation

giv
    Space for generated IV

creq
    The crypto request itself

.. _`crypto_alloc_skcipher`:

crypto_alloc_skcipher
=====================

.. c:function:: struct crypto_skcipher *crypto_alloc_skcipher(const char *alg_name, u32 type, u32 mask)

    allocate symmetric key cipher handle

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        skcipher cipher

    :param u32 type:
        specifies the type of the cipher

    :param u32 mask:
        specifies the mask for the cipher

.. _`crypto_alloc_skcipher.description`:

Description
-----------

Allocate a cipher handle for an skcipher. The returned struct
crypto_skcipher is the cipher handle that is required for any subsequent
API invocation for that skcipher.

.. _`crypto_alloc_skcipher.return`:

Return
------

allocated cipher handle in case of success; \ :c:func:`IS_ERR`\  is true in case
of an error, \ :c:func:`PTR_ERR`\  returns the error code.

.. _`crypto_free_skcipher`:

crypto_free_skcipher
====================

.. c:function:: void crypto_free_skcipher(struct crypto_skcipher *tfm)

    zeroize and free cipher handle

    :param struct crypto_skcipher \*tfm:
        cipher handle to be freed

.. _`crypto_has_skcipher`:

crypto_has_skcipher
===================

.. c:function:: int crypto_has_skcipher(const char *alg_name, u32 type, u32 mask)

    Search for the availability of an skcipher.

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        skcipher

    :param u32 type:
        specifies the type of the cipher

    :param u32 mask:
        specifies the mask for the cipher

.. _`crypto_has_skcipher.return`:

Return
------

true when the skcipher is known to the kernel crypto API; false
otherwise

.. _`crypto_skcipher_ivsize`:

crypto_skcipher_ivsize
======================

.. c:function:: unsigned int crypto_skcipher_ivsize(struct crypto_skcipher *tfm)

    obtain IV size

    :param struct crypto_skcipher \*tfm:
        cipher handle

.. _`crypto_skcipher_ivsize.description`:

Description
-----------

The size of the IV for the skcipher referenced by the cipher handle is
returned. This IV size may be zero if the cipher does not need an IV.

.. _`crypto_skcipher_ivsize.return`:

Return
------

IV size in bytes

.. _`crypto_skcipher_blocksize`:

crypto_skcipher_blocksize
=========================

.. c:function:: unsigned int crypto_skcipher_blocksize(struct crypto_skcipher *tfm)

    obtain block size of cipher

    :param struct crypto_skcipher \*tfm:
        cipher handle

.. _`crypto_skcipher_blocksize.description`:

Description
-----------

The block size for the skcipher referenced with the cipher handle is
returned. The caller may use that information to allocate appropriate
memory for the data returned by the encryption or decryption operation

.. _`crypto_skcipher_blocksize.return`:

Return
------

block size of cipher

.. _`crypto_skcipher_setkey`:

crypto_skcipher_setkey
======================

.. c:function:: int crypto_skcipher_setkey(struct crypto_skcipher *tfm, const u8 *key, unsigned int keylen)

    set key for cipher

    :param struct crypto_skcipher \*tfm:
        cipher handle

    :param const u8 \*key:
        buffer holding the key

    :param unsigned int keylen:
        length of the key in bytes

.. _`crypto_skcipher_setkey.description`:

Description
-----------

The caller provided key is set for the skcipher referenced by the cipher
handle.

Note, the key length determines the cipher type. Many block ciphers implement
different cipher modes depending on the key size, such as AES-128 vs AES-192
vs. AES-256. When providing a 16 byte key for an AES cipher handle, AES-128
is performed.

.. _`crypto_skcipher_setkey.return`:

Return
------

0 if the setting of the key was successful; < 0 if an error occurred

.. _`crypto_skcipher_reqtfm`:

crypto_skcipher_reqtfm
======================

.. c:function:: struct crypto_skcipher *crypto_skcipher_reqtfm(struct skcipher_request *req)

    obtain cipher handle from request

    :param struct skcipher_request \*req:
        skcipher_request out of which the cipher handle is to be obtained

.. _`crypto_skcipher_reqtfm.description`:

Description
-----------

Return the crypto_skcipher handle when furnishing an skcipher_request
data structure.

.. _`crypto_skcipher_reqtfm.return`:

Return
------

crypto_skcipher handle

.. _`crypto_skcipher_encrypt`:

crypto_skcipher_encrypt
=======================

.. c:function:: int crypto_skcipher_encrypt(struct skcipher_request *req)

    encrypt plaintext

    :param struct skcipher_request \*req:
        reference to the skcipher_request handle that holds all information
        needed to perform the cipher operation

.. _`crypto_skcipher_encrypt.description`:

Description
-----------

Encrypt plaintext data using the skcipher_request handle. That data
structure and how it is filled with data is discussed with the
skcipher_request\_\* functions.

.. _`crypto_skcipher_encrypt.return`:

Return
------

0 if the cipher operation was successful; < 0 if an error occurred

.. _`crypto_skcipher_decrypt`:

crypto_skcipher_decrypt
=======================

.. c:function:: int crypto_skcipher_decrypt(struct skcipher_request *req)

    decrypt ciphertext

    :param struct skcipher_request \*req:
        reference to the skcipher_request handle that holds all information
        needed to perform the cipher operation

.. _`crypto_skcipher_decrypt.description`:

Description
-----------

Decrypt ciphertext data using the skcipher_request handle. That data
structure and how it is filled with data is discussed with the
skcipher_request\_\* functions.

.. _`crypto_skcipher_decrypt.return`:

Return
------

0 if the cipher operation was successful; < 0 if an error occurred

.. _`crypto_skcipher_reqsize`:

crypto_skcipher_reqsize
=======================

.. c:function:: unsigned int crypto_skcipher_reqsize(struct crypto_skcipher *tfm)

    obtain size of the request data structure

    :param struct crypto_skcipher \*tfm:
        cipher handle

.. _`crypto_skcipher_reqsize.return`:

Return
------

number of bytes

.. _`skcipher_request_set_tfm`:

skcipher_request_set_tfm
========================

.. c:function:: void skcipher_request_set_tfm(struct skcipher_request *req, struct crypto_skcipher *tfm)

    update cipher handle reference in request

    :param struct skcipher_request \*req:
        request handle to be modified

    :param struct crypto_skcipher \*tfm:
        cipher handle that shall be added to the request handle

.. _`skcipher_request_set_tfm.description`:

Description
-----------

Allow the caller to replace the existing skcipher handle in the request
data structure with a different one.

.. _`skcipher_request_alloc`:

skcipher_request_alloc
======================

.. c:function:: struct skcipher_request *skcipher_request_alloc(struct crypto_skcipher *tfm, gfp_t gfp)

    allocate request data structure

    :param struct crypto_skcipher \*tfm:
        cipher handle to be registered with the request

    :param gfp_t gfp:
        memory allocation flag that is handed to kmalloc by the API call.

.. _`skcipher_request_alloc.description`:

Description
-----------

Allocate the request data structure that must be used with the skcipher
encrypt and decrypt API calls. During the allocation, the provided skcipher
handle is registered in the request data structure.

.. _`skcipher_request_alloc.return`:

Return
------

allocated request handle in case of success, or NULL if out of memory

.. _`skcipher_request_free`:

skcipher_request_free
=====================

.. c:function:: void skcipher_request_free(struct skcipher_request *req)

    zeroize and free request data structure

    :param struct skcipher_request \*req:
        request data structure cipher handle to be freed

.. _`skcipher_request_set_callback`:

skcipher_request_set_callback
=============================

.. c:function:: void skcipher_request_set_callback(struct skcipher_request *req, u32 flags, crypto_completion_t compl, void *data)

    set asynchronous callback function

    :param struct skcipher_request \*req:
        request handle

    :param u32 flags:
        specify zero or an ORing of the flags
        CRYPTO_TFM_REQ_MAY_BACKLOG the request queue may back log and
        increase the wait queue beyond the initial maximum size;
        CRYPTO_TFM_REQ_MAY_SLEEP the request processing may sleep

    :param crypto_completion_t compl:
        callback function pointer to be registered with the request handle

    :param void \*data:
        The data pointer refers to memory that is not used by the kernel
        crypto API, but provided to the callback function for it to use. Here,
        the caller can provide a reference to memory the callback function can
        operate on. As the callback function is invoked asynchronously to the
        related functionality, it may need to access data structures of the
        related functionality which can be referenced using this pointer. The
        callback function can access the memory via the "data" field in the
        crypto_async_request data structure provided to the callback function.

.. _`skcipher_request_set_callback.description`:

Description
-----------

This function allows setting the callback function that is triggered once the
cipher operation completes.

The callback function is registered with the skcipher_request handle and
must comply with the following template

void callback_function(struct crypto_async_request \*req, int error)

.. _`skcipher_request_set_crypt`:

skcipher_request_set_crypt
==========================

.. c:function:: void skcipher_request_set_crypt(struct skcipher_request *req, struct scatterlist *src, struct scatterlist *dst, unsigned int cryptlen, void *iv)

    set data buffers

    :param struct skcipher_request \*req:
        request handle

    :param struct scatterlist \*src:
        source scatter / gather list

    :param struct scatterlist \*dst:
        destination scatter / gather list

    :param unsigned int cryptlen:
        number of bytes to process from \ ``src``\ 

    :param void \*iv:
        IV for the cipher operation which must comply with the IV size defined
        by crypto_skcipher_ivsize

.. _`skcipher_request_set_crypt.description`:

Description
-----------

This function allows setting of the source data and destination data
scatter / gather lists.

For encryption, the source is treated as the plaintext and the
destination is the ciphertext. For a decryption operation, the use is
reversed - the source is the ciphertext and the destination is the plaintext.

.. This file was automatic generated / don't edit.
