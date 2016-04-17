.. -*- coding: utf-8; mode: rst -*-

========
crypto.h
========


.. _`block-cipher-context-data-structures`:

Block Cipher Context Data Structures
====================================

These data structures define the operating context for each block cipher
type.



.. _`block-cipher-algorithm-definitions`:

Block Cipher Algorithm Definitions
==================================

These data structures define modular crypto algorithm implementations,
managed via :c:func:`crypto_register_alg` and :c:func:`crypto_unregister_alg`.



.. _`ablkcipher_alg`:

struct ablkcipher_alg
=====================

.. c:type:: ablkcipher_alg

    asynchronous block cipher definition


.. _`ablkcipher_alg.definition`:

Definition
----------

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


.. _`ablkcipher_alg.members`:

Members
-------

:``setkey``:
    Set key for the transformation. This function is used to either
    program a supplied key into the hardware or store the key in the
    transformation context for programming it later. Note that this
    function does modify the transformation context. This function can
    be called multiple times during the existence of the transformation
    object, so one must make sure the key is properly reprogrammed into
    the hardware. This function is also responsible for checking the key
    length for validity. In case a software fallback was put in place in
    the ``cra_init`` call, this function might need to use the fallback if
    the algorithm doesn't support all of the key sizes.

:``encrypt``:
    Encrypt a scatterlist of blocks. This function is used to encrypt
    the supplied scatterlist containing the blocks of data. The crypto
    API consumer is responsible for aligning the entries of the
    scatterlist properly and making sure the chunks are correctly
    sized. In case a software fallback was put in place in the
    ``cra_init`` call, this function might need to use the fallback if
    the algorithm doesn't support all of the key sizes. In case the
    key was stored in transformation context, the key might need to be
    re-programmed into the hardware in this function. This function
    shall not modify the transformation context, as this function may
    be called in parallel with the same transformation object.

:``decrypt``:
    Decrypt a single block. This is a reverse counterpart to ``encrypt``
    and the conditions are exactly the same.

:``givencrypt``:
    Update the IV for encryption. With this function, a cipher
    implementation may provide the function on how to update the IV
    for encryption.

:``givdecrypt``:
    Update the IV for decryption. This is the reverse of
    ``givencrypt`` .

:``geniv``:
    The transformation implementation may use an "IV generator" provided
    by the kernel crypto API. Several use cases have a predefined
    approach how IVs are to be updated. For such use cases, the kernel
    crypto API provides ready-to-use implementations that can be
    referenced with this variable.

:``min_keysize``:
    Minimum key size supported by the transformation. This is the
    smallest key length supported by this transformation algorithm.
    This must be set to one of the pre-defined values as this is
    not hardware specific. Possible values for this field can be
    found via git grep "_MIN_KEY_SIZE" include/crypto/

:``max_keysize``:
    Maximum key size supported by the transformation. This is the
    largest key length supported by this transformation algorithm.
    This must be set to one of the pre-defined values as this is
    not hardware specific. Possible values for this field can be
    found via git grep "_MAX_KEY_SIZE" include/crypto/

:``ivsize``:
    IV size applicable for transformation. The consumer must provide an
    IV of exactly that size to perform the encrypt or decrypt operation.




.. _`ablkcipher_alg.description`:

Description
-----------

All fields except ``givencrypt`` , ``givdecrypt`` , ``geniv`` and ``ivsize`` are
mandatory and must be filled.



.. _`blkcipher_alg`:

struct blkcipher_alg
====================

.. c:type:: blkcipher_alg

    synchronous block cipher definition


.. _`blkcipher_alg.definition`:

Definition
----------

.. code-block:: c

  struct blkcipher_alg {
    int (* setkey) (struct crypto_tfm *tfm, const u8 *key,unsigned int keylen);
    int (* encrypt) (struct blkcipher_desc *desc,struct scatterlist *dst, struct scatterlist *src,unsigned int nbytes);
    int (* decrypt) (struct blkcipher_desc *desc,struct scatterlist *dst, struct scatterlist *src,unsigned int nbytes);
    const char * geniv;
    unsigned int min_keysize;
    unsigned int max_keysize;
    unsigned int ivsize;
  };


.. _`blkcipher_alg.members`:

Members
-------

:``setkey``:
    see struct ablkcipher_alg

:``encrypt``:
    see struct ablkcipher_alg

:``decrypt``:
    see struct ablkcipher_alg

:``geniv``:
    see struct ablkcipher_alg

:``min_keysize``:
    see struct ablkcipher_alg

:``max_keysize``:
    see struct ablkcipher_alg

:``ivsize``:
    see struct ablkcipher_alg




.. _`blkcipher_alg.description`:

Description
-----------

All fields except ``geniv`` and ``ivsize`` are mandatory and must be filled.



.. _`cipher_alg`:

struct cipher_alg
=================

.. c:type:: cipher_alg

    single-block symmetric ciphers definition


.. _`cipher_alg.definition`:

Definition
----------

.. code-block:: c

  struct cipher_alg {
    unsigned int cia_min_keysize;
    unsigned int cia_max_keysize;
    int (* cia_setkey) (struct crypto_tfm *tfm, const u8 *key,unsigned int keylen);
    void (* cia_encrypt) (struct crypto_tfm *tfm, u8 *dst, const u8 *src);
    void (* cia_decrypt) (struct crypto_tfm *tfm, u8 *dst, const u8 *src);
  };


.. _`cipher_alg.members`:

Members
-------

:``cia_min_keysize``:
    Minimum key size supported by the transformation. This is
    the smallest key length supported by this transformation
    algorithm. This must be set to one of the pre-defined
    values as this is not hardware specific. Possible values
    for this field can be found via git grep "_MIN_KEY_SIZE"
    include/crypto/

:``cia_max_keysize``:
    Maximum key size supported by the transformation. This is
    the largest key length supported by this transformation
    algorithm. This must be set to one of the pre-defined values
    as this is not hardware specific. Possible values for this
    field can be found via git grep "_MAX_KEY_SIZE"
    include/crypto/

:``cia_setkey``:
    Set key for the transformation. This function is used to either
    program a supplied key into the hardware or store the key in the
    transformation context for programming it later. Note that this
    function does modify the transformation context. This function
    can be called multiple times during the existence of the
    transformation object, so one must make sure the key is properly
    reprogrammed into the hardware. This function is also
    responsible for checking the key length for validity.

:``cia_encrypt``:
    Encrypt a single block. This function is used to encrypt a
    single block of data, which must be ``cra_blocksize`` big. This
    always operates on a full ``cra_blocksize`` and it is not possible
    to encrypt a block of smaller size. The supplied buffers must
    therefore also be at least of ``cra_blocksize`` size. Both the
    input and output buffers are always aligned to ``cra_alignmask``\ .
    In case either of the input or output buffer supplied by user
    of the crypto API is not aligned to ``cra_alignmask``\ , the crypto
    API will re-align the buffers. The re-alignment means that a
    new buffer will be allocated, the data will be copied into the
    new buffer, then the processing will happen on the new buffer,
    then the data will be copied back into the original buffer and
    finally the new buffer will be freed. In case a software
    fallback was put in place in the ``cra_init`` call, this function
    might need to use the fallback if the algorithm doesn't support
    all of the key sizes. In case the key was stored in
    transformation context, the key might need to be re-programmed
    into the hardware in this function. This function shall not
    modify the transformation context, as this function may be
    called in parallel with the same transformation object.

:``cia_decrypt``:
    Decrypt a single block. This is a reverse counterpart to
    ``cia_encrypt``\ , and the conditions are exactly the same.




.. _`cipher_alg.description`:

Description
-----------

All fields are mandatory and must be filled.



.. _`crypto_alg`:

struct crypto_alg
=================

.. c:type:: crypto_alg

    definition of a cryptograpic cipher algorithm


.. _`crypto_alg.definition`:

Definition
----------

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


.. _`crypto_alg.members`:

Members
-------

:``cra_list``:
    internally used

:``cra_users``:
    internally used

:``cra_flags``:
    Flags describing this transformation. See include/linux/crypto.h
    CRYPTO_ALG\_\* flags for the flags which go in here. Those are
    used for fine-tuning the description of the transformation
    algorithm.

:``cra_blocksize``:
    Minimum block size of this transformation. The size in bytes
    of the smallest possible unit which can be transformed with
    this algorithm. The users must respect this value.
    In case of HASH transformation, it is possible for a smaller
    block than ``cra_blocksize`` to be passed to the crypto API for
    transformation, in case of any other transformation type, an
    error will be returned upon any attempt to transform smaller
    than ``cra_blocksize`` chunks.

:``cra_ctxsize``:
    Size of the operational context of the transformation. This
    value informs the kernel crypto API about the memory size
    needed to be allocated for the transformation context.

:``cra_alignmask``:
    Alignment mask for the input and output data buffer. The data
    buffer containing the input data for the algorithm must be
    aligned to this alignment mask. The data buffer for the
    output data must be aligned to this alignment mask. Note that
    the Crypto API will do the re-alignment in software, but
    only under special conditions and there is a performance hit.
    The re-alignment happens at these occasions for different

:``cra_priority``:
    Priority of this transformation implementation. In case
    multiple transformations with same ``cra_name`` are available to
    the Crypto API, the kernel will use the one with highest
    ``cra_priority``\ .

:``cra_refcnt``:
    internally used

:``cra_name[CRYPTO_MAX_ALG_NAME]``:
    Generic name (usable by multiple implementations) of the
    transformation algorithm. This is the name of the transformation
    itself. This field is used by the kernel when looking up the
    providers of particular transformation.

:``cra_driver_name[CRYPTO_MAX_ALG_NAME]``:
    Unique name of the transformation provider. This is the
    name of the provider of the transformation. This can be any
    arbitrary value, but in the usual case, this contains the
    name of the chip or provider and the name of the
    transformation algorithm.

:``cra_type``:
    Type of the cryptographic transformation. This is a pointer to
    struct crypto_type, which implements callbacks common for all
    transformation types. There are multiple options:
    :c:type:`struct crypto_blkcipher_type <crypto_blkcipher_type>`, :c:type:`struct crypto_ablkcipher_type <crypto_ablkcipher_type>`,
    :c:type:`struct crypto_ahash_type <crypto_ahash_type>`, :c:type:`struct crypto_rng_type <crypto_rng_type>`.
    This field might be empty. In that case, there are no common
    callbacks. This is the case for: cipher, compress, shash.

:``cra_u``:
    Callbacks implementing the transformation. This is a union of
    multiple structures. Depending on the type of transformation selected
    by ``cra_type`` and ``cra_flags`` above, the associated structure must be
    filled with callbacks. This field might be empty. This is the case
    for ahash, shash.

:``cra_init``:
    Initialize the cryptographic transformation object. This function
    is used to initialize the cryptographic transformation object.
    This function is called only once at the instantiation time, right
    after the transformation context was allocated. In case the
    cryptographic hardware has some special requirements which need to
    be handled by software, this function shall check for the precise
    requirement of the transformation and put any software fallbacks
    in place.

:``cra_exit``:
    Deinitialize the cryptographic transformation object. This is a
    counterpart to ``cra_init``\ , used to remove various changes set in
    ``cra_init``\ .

:``cra_destroy``:
    internally used

:``cra_module``:
    Owner of this transformation implementation. Set to THIS_MODULE




.. _`crypto_alg.description`:

Description
-----------

The struct crypto_alg describes a generic Crypto API algorithm and is common
for all of the transformations. Any variable not documented here shall not
be used by a cipher implementation as it is internal to the Crypto API.



.. _`asynchronous-block-cipher-api`:

Asynchronous Block Cipher API
=============================

Asynchronous block cipher API is used with the ciphers of type
CRYPTO_ALG_TYPE_ABLKCIPHER (listed as type "ablkcipher" in /proc/crypto).

Asynchronous cipher operations imply that the function invocation for a
cipher request returns immediately before the completion of the operation.
The cipher request is scheduled as a separate kernel thread and therefore
load-balanced on the different CPUs via the process scheduler. To allow
the kernel crypto API to inform the caller about the completion of a cipher
request, the caller must provide a callback function. That function is
invoked with the cipher handle when the request completes.

To support the asynchronous operation, additional information than just the
cipher handle must be supplied to the kernel crypto API. That additional
information is given by filling in the ablkcipher_request data structure.

For the asynchronous block cipher API, the state is maintained with the tfm
cipher handle. A single tfm can be used across multiple calls and in
parallel. For asynchronous block cipher calls, context data supplied and
only used by the caller can be referenced the request data structure in
addition to the IV used for the cipher request. The maintenance of such
state information would be important for a crypto driver implementer to
have, because when calling the callback function upon completion of the
cipher operation, that callback function may need some information about
which operation just finished if it invoked multiple in parallel. This
state information is unused by the kernel crypto API.



.. _`crypto_alloc_ablkcipher`:

crypto_alloc_ablkcipher
=======================

.. c:function:: struct crypto_ablkcipher *crypto_alloc_ablkcipher (const char *alg_name, u32 type, u32 mask)

    allocate asynchronous block cipher handle

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        ablkcipher cipher

    :param u32 type:
        specifies the type of the cipher

    :param u32 mask:
        specifies the mask for the cipher



.. _`crypto_alloc_ablkcipher.description`:

Description
-----------

Allocate a cipher handle for an ablkcipher. The returned struct
crypto_ablkcipher is the cipher handle that is required for any subsequent
API invocation for that ablkcipher.



.. _`crypto_alloc_ablkcipher.return`:

Return
------

allocated cipher handle in case of success; :c:func:`IS_ERR` is true in case
of an error, :c:func:`PTR_ERR` returns the error code.



.. _`crypto_free_ablkcipher`:

crypto_free_ablkcipher
======================

.. c:function:: void crypto_free_ablkcipher (struct crypto_ablkcipher *tfm)

    zeroize and free cipher handle

    :param struct crypto_ablkcipher \*tfm:
        cipher handle to be freed



.. _`crypto_has_ablkcipher`:

crypto_has_ablkcipher
=====================

.. c:function:: int crypto_has_ablkcipher (const char *alg_name, u32 type, u32 mask)

    Search for the availability of an ablkcipher.

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        ablkcipher

    :param u32 type:
        specifies the type of the cipher

    :param u32 mask:
        specifies the mask for the cipher



.. _`crypto_has_ablkcipher.return`:

Return
------

true when the ablkcipher is known to the kernel crypto API; false
otherwise



.. _`crypto_ablkcipher_ivsize`:

crypto_ablkcipher_ivsize
========================

.. c:function:: unsigned int crypto_ablkcipher_ivsize (struct crypto_ablkcipher *tfm)

    obtain IV size

    :param struct crypto_ablkcipher \*tfm:
        cipher handle



.. _`crypto_ablkcipher_ivsize.description`:

Description
-----------

The size of the IV for the ablkcipher referenced by the cipher handle is
returned. This IV size may be zero if the cipher does not need an IV.



.. _`crypto_ablkcipher_ivsize.return`:

Return
------

IV size in bytes



.. _`crypto_ablkcipher_blocksize`:

crypto_ablkcipher_blocksize
===========================

.. c:function:: unsigned int crypto_ablkcipher_blocksize (struct crypto_ablkcipher *tfm)

    obtain block size of cipher

    :param struct crypto_ablkcipher \*tfm:
        cipher handle



.. _`crypto_ablkcipher_blocksize.description`:

Description
-----------

The block size for the ablkcipher referenced with the cipher handle is
returned. The caller may use that information to allocate appropriate
memory for the data returned by the encryption or decryption operation



.. _`crypto_ablkcipher_blocksize.return`:

Return
------

block size of cipher



.. _`crypto_ablkcipher_setkey`:

crypto_ablkcipher_setkey
========================

.. c:function:: int crypto_ablkcipher_setkey (struct crypto_ablkcipher *tfm, const u8 *key, unsigned int keylen)

    set key for cipher

    :param struct crypto_ablkcipher \*tfm:
        cipher handle

    :param const u8 \*key:
        buffer holding the key

    :param unsigned int keylen:
        length of the key in bytes



.. _`crypto_ablkcipher_setkey.description`:

Description
-----------

The caller provided key is set for the ablkcipher referenced by the cipher
handle.

Note, the key length determines the cipher type. Many block ciphers implement
different cipher modes depending on the key size, such as AES-128 vs AES-192
vs. AES-256. When providing a 16 byte key for an AES cipher handle, AES-128
is performed.



.. _`crypto_ablkcipher_setkey.return`:

Return
------

0 if the setting of the key was successful; < 0 if an error occurred



.. _`crypto_ablkcipher_reqtfm`:

crypto_ablkcipher_reqtfm
========================

.. c:function:: struct crypto_ablkcipher *crypto_ablkcipher_reqtfm (struct ablkcipher_request *req)

    obtain cipher handle from request

    :param struct ablkcipher_request \*req:
        ablkcipher_request out of which the cipher handle is to be obtained



.. _`crypto_ablkcipher_reqtfm.description`:

Description
-----------

Return the crypto_ablkcipher handle when furnishing an ablkcipher_request
data structure.



.. _`crypto_ablkcipher_reqtfm.return`:

Return
------

crypto_ablkcipher handle



.. _`crypto_ablkcipher_encrypt`:

crypto_ablkcipher_encrypt
=========================

.. c:function:: int crypto_ablkcipher_encrypt (struct ablkcipher_request *req)

    encrypt plaintext

    :param struct ablkcipher_request \*req:
        reference to the ablkcipher_request handle that holds all information
        needed to perform the cipher operation



.. _`crypto_ablkcipher_encrypt.description`:

Description
-----------

Encrypt plaintext data using the ablkcipher_request handle. That data
structure and how it is filled with data is discussed with the
ablkcipher_request\_\* functions.



.. _`crypto_ablkcipher_encrypt.return`:

Return
------

0 if the cipher operation was successful; < 0 if an error occurred



.. _`crypto_ablkcipher_decrypt`:

crypto_ablkcipher_decrypt
=========================

.. c:function:: int crypto_ablkcipher_decrypt (struct ablkcipher_request *req)

    decrypt ciphertext

    :param struct ablkcipher_request \*req:
        reference to the ablkcipher_request handle that holds all information
        needed to perform the cipher operation



.. _`crypto_ablkcipher_decrypt.description`:

Description
-----------

Decrypt ciphertext data using the ablkcipher_request handle. That data
structure and how it is filled with data is discussed with the
ablkcipher_request\_\* functions.



.. _`crypto_ablkcipher_decrypt.return`:

Return
------

0 if the cipher operation was successful; < 0 if an error occurred



.. _`asynchronous-cipher-request-handle`:

Asynchronous Cipher Request Handle
==================================

The ablkcipher_request data structure contains all pointers to data
required for the asynchronous cipher operation. This includes the cipher
handle (which can be used by multiple ablkcipher_request instances), pointer
to plaintext and ciphertext, asynchronous callback function, etc. It acts
as a handle to the ablkcipher_request\_\* API calls in a similar way as
ablkcipher handle to the crypto_ablkcipher\_\* API calls.



.. _`crypto_ablkcipher_reqsize`:

crypto_ablkcipher_reqsize
=========================

.. c:function:: unsigned int crypto_ablkcipher_reqsize (struct crypto_ablkcipher *tfm)

    obtain size of the request data structure

    :param struct crypto_ablkcipher \*tfm:
        cipher handle



.. _`crypto_ablkcipher_reqsize.return`:

Return
------

number of bytes



.. _`ablkcipher_request_set_tfm`:

ablkcipher_request_set_tfm
==========================

.. c:function:: void ablkcipher_request_set_tfm (struct ablkcipher_request *req, struct crypto_ablkcipher *tfm)

    update cipher handle reference in request

    :param struct ablkcipher_request \*req:
        request handle to be modified

    :param struct crypto_ablkcipher \*tfm:
        cipher handle that shall be added to the request handle



.. _`ablkcipher_request_set_tfm.description`:

Description
-----------

Allow the caller to replace the existing ablkcipher handle in the request
data structure with a different one.



.. _`ablkcipher_request_alloc`:

ablkcipher_request_alloc
========================

.. c:function:: struct ablkcipher_request *ablkcipher_request_alloc (struct crypto_ablkcipher *tfm, gfp_t gfp)

    allocate request data structure

    :param struct crypto_ablkcipher \*tfm:
        cipher handle to be registered with the request

    :param gfp_t gfp:
        memory allocation flag that is handed to kmalloc by the API call.



.. _`ablkcipher_request_alloc.description`:

Description
-----------

Allocate the request data structure that must be used with the ablkcipher
encrypt and decrypt API calls. During the allocation, the provided ablkcipher
handle is registered in the request data structure.



.. _`ablkcipher_request_alloc.return`:

Return
------

allocated request handle in case of success; :c:func:`IS_ERR` is true in case
of an error, :c:func:`PTR_ERR` returns the error code.



.. _`ablkcipher_request_free`:

ablkcipher_request_free
=======================

.. c:function:: void ablkcipher_request_free (struct ablkcipher_request *req)

    zeroize and free request data structure

    :param struct ablkcipher_request \*req:
        request data structure cipher handle to be freed



.. _`ablkcipher_request_set_callback`:

ablkcipher_request_set_callback
===============================

.. c:function:: void ablkcipher_request_set_callback (struct ablkcipher_request *req, u32 flags, crypto_completion_t compl, void *data)

    set asynchronous callback function

    :param struct ablkcipher_request \*req:
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



.. _`ablkcipher_request_set_callback.description`:

Description
-----------

This function allows setting the callback function that is triggered once the
cipher operation completes.

The callback function is registered with the ablkcipher_request handle and
must comply with the following template

void callback_function(struct crypto_async_request \*req, int error)



.. _`ablkcipher_request_set_crypt`:

ablkcipher_request_set_crypt
============================

.. c:function:: void ablkcipher_request_set_crypt (struct ablkcipher_request *req, struct scatterlist *src, struct scatterlist *dst, unsigned int nbytes, void *iv)

    set data buffers

    :param struct ablkcipher_request \*req:
        request handle

    :param struct scatterlist \*src:
        source scatter / gather list

    :param struct scatterlist \*dst:
        destination scatter / gather list

    :param unsigned int nbytes:
        number of bytes to process from ``src``

    :param void \*iv:
        IV for the cipher operation which must comply with the IV size defined
        by crypto_ablkcipher_ivsize



.. _`ablkcipher_request_set_crypt.description`:

Description
-----------

This function allows setting of the source data and destination data
scatter / gather lists.

For encryption, the source is treated as the plaintext and the
destination is the ciphertext. For a decryption operation, the use is
reversed - the source is the ciphertext and the destination is the plaintext.



.. _`synchronous-block-cipher-api`:

Synchronous Block Cipher API
============================

The synchronous block cipher API is used with the ciphers of type
CRYPTO_ALG_TYPE_BLKCIPHER (listed as type "blkcipher" in /proc/crypto)

Synchronous calls, have a context in the tfm. But since a single tfm can be
used in multiple calls and in parallel, this info should not be changeable
(unless a lock is used). This applies, for example, to the symmetric key.
However, the IV is changeable, so there is an iv field in blkcipher_tfm
structure for synchronous blkcipher api. So, its the only state info that can
be kept for synchronous calls without using a big lock across a tfm.

The block cipher API allows the use of a complete cipher, i.e. a cipher
consisting of a template (a block chaining mode) and a single block cipher
primitive (e.g. AES).

The plaintext data buffer and the ciphertext data buffer are pointed to
by using scatter/gather lists. The cipher operation is performed
on all segments of the provided scatter/gather lists.

The kernel crypto API supports a cipher operation "in-place" which means that
the caller may provide the same scatter/gather list for the plaintext and
cipher text. After the completion of the cipher operation, the plaintext
data is replaced with the ciphertext data in case of an encryption and vice
versa for a decryption. The caller must ensure that the scatter/gather lists
for the output data point to sufficiently large buffers, i.e. multiples of
the block size of the cipher.



.. _`crypto_alloc_blkcipher`:

crypto_alloc_blkcipher
======================

.. c:function:: struct crypto_blkcipher *crypto_alloc_blkcipher (const char *alg_name, u32 type, u32 mask)

    allocate synchronous block cipher handle

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        blkcipher cipher

    :param u32 type:
        specifies the type of the cipher

    :param u32 mask:
        specifies the mask for the cipher



.. _`crypto_alloc_blkcipher.description`:

Description
-----------

Allocate a cipher handle for a block cipher. The returned struct
crypto_blkcipher is the cipher handle that is required for any subsequent
API invocation for that block cipher.



.. _`crypto_alloc_blkcipher.return`:

Return
------

allocated cipher handle in case of success; :c:func:`IS_ERR` is true in case
of an error, :c:func:`PTR_ERR` returns the error code.



.. _`crypto_free_blkcipher`:

crypto_free_blkcipher
=====================

.. c:function:: void crypto_free_blkcipher (struct crypto_blkcipher *tfm)

    zeroize and free the block cipher handle

    :param struct crypto_blkcipher \*tfm:
        cipher handle to be freed



.. _`crypto_has_blkcipher`:

crypto_has_blkcipher
====================

.. c:function:: int crypto_has_blkcipher (const char *alg_name, u32 type, u32 mask)

    Search for the availability of a block cipher

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        block cipher

    :param u32 type:
        specifies the type of the cipher

    :param u32 mask:
        specifies the mask for the cipher



.. _`crypto_has_blkcipher.return`:

Return
------

true when the block cipher is known to the kernel crypto API; false
otherwise



.. _`crypto_blkcipher_name`:

crypto_blkcipher_name
=====================

.. c:function:: const char *crypto_blkcipher_name (struct crypto_blkcipher *tfm)

    return the name / cra_name from the cipher handle

    :param struct crypto_blkcipher \*tfm:
        cipher handle



.. _`crypto_blkcipher_name.return`:

Return
------

The character string holding the name of the cipher



.. _`crypto_blkcipher_ivsize`:

crypto_blkcipher_ivsize
=======================

.. c:function:: unsigned int crypto_blkcipher_ivsize (struct crypto_blkcipher *tfm)

    obtain IV size

    :param struct crypto_blkcipher \*tfm:
        cipher handle



.. _`crypto_blkcipher_ivsize.description`:

Description
-----------

The size of the IV for the block cipher referenced by the cipher handle is
returned. This IV size may be zero if the cipher does not need an IV.



.. _`crypto_blkcipher_ivsize.return`:

Return
------

IV size in bytes



.. _`crypto_blkcipher_blocksize`:

crypto_blkcipher_blocksize
==========================

.. c:function:: unsigned int crypto_blkcipher_blocksize (struct crypto_blkcipher *tfm)

    obtain block size of cipher

    :param struct crypto_blkcipher \*tfm:
        cipher handle



.. _`crypto_blkcipher_blocksize.description`:

Description
-----------

The block size for the block cipher referenced with the cipher handle is
returned. The caller may use that information to allocate appropriate
memory for the data returned by the encryption or decryption operation.



.. _`crypto_blkcipher_blocksize.return`:

Return
------

block size of cipher



.. _`crypto_blkcipher_setkey`:

crypto_blkcipher_setkey
=======================

.. c:function:: int crypto_blkcipher_setkey (struct crypto_blkcipher *tfm, const u8 *key, unsigned int keylen)

    set key for cipher

    :param struct crypto_blkcipher \*tfm:
        cipher handle

    :param const u8 \*key:
        buffer holding the key

    :param unsigned int keylen:
        length of the key in bytes



.. _`crypto_blkcipher_setkey.description`:

Description
-----------

The caller provided key is set for the block cipher referenced by the cipher
handle.

Note, the key length determines the cipher type. Many block ciphers implement
different cipher modes depending on the key size, such as AES-128 vs AES-192
vs. AES-256. When providing a 16 byte key for an AES cipher handle, AES-128
is performed.



.. _`crypto_blkcipher_setkey.return`:

Return
------

0 if the setting of the key was successful; < 0 if an error occurred



.. _`crypto_blkcipher_encrypt`:

crypto_blkcipher_encrypt
========================

.. c:function:: int crypto_blkcipher_encrypt (struct blkcipher_desc *desc, struct scatterlist *dst, struct scatterlist *src, unsigned int nbytes)

    encrypt plaintext

    :param struct blkcipher_desc \*desc:
        reference to the block cipher handle with meta data

    :param struct scatterlist \*dst:
        scatter/gather list that is filled by the cipher operation with the
        ciphertext

    :param struct scatterlist \*src:
        scatter/gather list that holds the plaintext

    :param unsigned int nbytes:
        number of bytes of the plaintext to encrypt.



.. _`crypto_blkcipher_encrypt.description`:

Description
-----------

Encrypt plaintext data using the IV set by the caller with a preceding
call of crypto_blkcipher_set_iv.

The blkcipher_desc data structure must be filled by the caller and can
reside on the stack. The caller must fill desc as follows: desc.tfm is filled
with the block cipher handle; desc.flags is filled with either
CRYPTO_TFM_REQ_MAY_SLEEP or 0.



.. _`crypto_blkcipher_encrypt.return`:

Return
------

0 if the cipher operation was successful; < 0 if an error occurred



.. _`crypto_blkcipher_encrypt_iv`:

crypto_blkcipher_encrypt_iv
===========================

.. c:function:: int crypto_blkcipher_encrypt_iv (struct blkcipher_desc *desc, struct scatterlist *dst, struct scatterlist *src, unsigned int nbytes)

    encrypt plaintext with dedicated IV

    :param struct blkcipher_desc \*desc:
        reference to the block cipher handle with meta data

    :param struct scatterlist \*dst:
        scatter/gather list that is filled by the cipher operation with the
        ciphertext

    :param struct scatterlist \*src:
        scatter/gather list that holds the plaintext

    :param unsigned int nbytes:
        number of bytes of the plaintext to encrypt.



.. _`crypto_blkcipher_encrypt_iv.description`:

Description
-----------

Encrypt plaintext data with the use of an IV that is solely used for this
cipher operation. Any previously set IV is not used.

The blkcipher_desc data structure must be filled by the caller and can
reside on the stack. The caller must fill desc as follows: desc.tfm is filled
with the block cipher handle; desc.info is filled with the IV to be used for
the current operation; desc.flags is filled with either
CRYPTO_TFM_REQ_MAY_SLEEP or 0.



.. _`crypto_blkcipher_encrypt_iv.return`:

Return
------

0 if the cipher operation was successful; < 0 if an error occurred



.. _`crypto_blkcipher_decrypt`:

crypto_blkcipher_decrypt
========================

.. c:function:: int crypto_blkcipher_decrypt (struct blkcipher_desc *desc, struct scatterlist *dst, struct scatterlist *src, unsigned int nbytes)

    decrypt ciphertext

    :param struct blkcipher_desc \*desc:
        reference to the block cipher handle with meta data

    :param struct scatterlist \*dst:
        scatter/gather list that is filled by the cipher operation with the
        plaintext

    :param struct scatterlist \*src:
        scatter/gather list that holds the ciphertext

    :param unsigned int nbytes:
        number of bytes of the ciphertext to decrypt.



.. _`crypto_blkcipher_decrypt.description`:

Description
-----------

Decrypt ciphertext data using the IV set by the caller with a preceding
call of crypto_blkcipher_set_iv.

The blkcipher_desc data structure must be filled by the caller as documented
for the crypto_blkcipher_encrypt call above.



.. _`crypto_blkcipher_decrypt.return`:

Return
------

0 if the cipher operation was successful; < 0 if an error occurred



.. _`crypto_blkcipher_decrypt_iv`:

crypto_blkcipher_decrypt_iv
===========================

.. c:function:: int crypto_blkcipher_decrypt_iv (struct blkcipher_desc *desc, struct scatterlist *dst, struct scatterlist *src, unsigned int nbytes)

    decrypt ciphertext with dedicated IV

    :param struct blkcipher_desc \*desc:
        reference to the block cipher handle with meta data

    :param struct scatterlist \*dst:
        scatter/gather list that is filled by the cipher operation with the
        plaintext

    :param struct scatterlist \*src:
        scatter/gather list that holds the ciphertext

    :param unsigned int nbytes:
        number of bytes of the ciphertext to decrypt.



.. _`crypto_blkcipher_decrypt_iv.description`:

Description
-----------

Decrypt ciphertext data with the use of an IV that is solely used for this
cipher operation. Any previously set IV is not used.

The blkcipher_desc data structure must be filled by the caller as documented
for the crypto_blkcipher_encrypt_iv call above.



.. _`crypto_blkcipher_decrypt_iv.return`:

Return
------

0 if the cipher operation was successful; < 0 if an error occurred



.. _`crypto_blkcipher_set_iv`:

crypto_blkcipher_set_iv
=======================

.. c:function:: void crypto_blkcipher_set_iv (struct crypto_blkcipher *tfm, const u8 *src, unsigned int len)

    set IV for cipher

    :param struct crypto_blkcipher \*tfm:
        cipher handle

    :param const u8 \*src:
        buffer holding the IV

    :param unsigned int len:
        length of the IV in bytes



.. _`crypto_blkcipher_set_iv.description`:

Description
-----------

The caller provided IV is set for the block cipher referenced by the cipher
handle.



.. _`crypto_blkcipher_get_iv`:

crypto_blkcipher_get_iv
=======================

.. c:function:: void crypto_blkcipher_get_iv (struct crypto_blkcipher *tfm, u8 *dst, unsigned int len)

    obtain IV from cipher

    :param struct crypto_blkcipher \*tfm:
        cipher handle

    :param u8 \*dst:
        buffer filled with the IV

    :param unsigned int len:
        length of the buffer dst



.. _`crypto_blkcipher_get_iv.description`:

Description
-----------

The caller can obtain the IV set for the block cipher referenced by the
cipher handle and store it into the user-provided buffer. If the buffer
has an insufficient space, the IV is truncated to fit the buffer.



.. _`single-block-cipher-api`:

Single Block Cipher API
=======================

The single block cipher API is used with the ciphers of type
CRYPTO_ALG_TYPE_CIPHER (listed as type "cipher" in /proc/crypto).

Using the single block cipher API calls, operations with the basic cipher
primitive can be implemented. These cipher primitives exclude any block
chaining operations including IV handling.

The purpose of this single block cipher API is to support the implementation
of templates or other concepts that only need to perform the cipher operation
on one block at a time. Templates invoke the underlying cipher primitive
block-wise and process either the input or the output data of these cipher
operations.



.. _`crypto_alloc_cipher`:

crypto_alloc_cipher
===================

.. c:function:: struct crypto_cipher *crypto_alloc_cipher (const char *alg_name, u32 type, u32 mask)

    allocate single block cipher handle

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        single block cipher

    :param u32 type:
        specifies the type of the cipher

    :param u32 mask:
        specifies the mask for the cipher



.. _`crypto_alloc_cipher.description`:

Description
-----------

Allocate a cipher handle for a single block cipher. The returned struct
crypto_cipher is the cipher handle that is required for any subsequent API
invocation for that single block cipher.



.. _`crypto_alloc_cipher.return`:

Return
------

allocated cipher handle in case of success; :c:func:`IS_ERR` is true in case
of an error, :c:func:`PTR_ERR` returns the error code.



.. _`crypto_free_cipher`:

crypto_free_cipher
==================

.. c:function:: void crypto_free_cipher (struct crypto_cipher *tfm)

    zeroize and free the single block cipher handle

    :param struct crypto_cipher \*tfm:
        cipher handle to be freed



.. _`crypto_has_cipher`:

crypto_has_cipher
=================

.. c:function:: int crypto_has_cipher (const char *alg_name, u32 type, u32 mask)

    Search for the availability of a single block cipher

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        single block cipher

    :param u32 type:
        specifies the type of the cipher

    :param u32 mask:
        specifies the mask for the cipher



.. _`crypto_has_cipher.return`:

Return
------

true when the single block cipher is known to the kernel crypto API;
false otherwise



.. _`crypto_cipher_blocksize`:

crypto_cipher_blocksize
=======================

.. c:function:: unsigned int crypto_cipher_blocksize (struct crypto_cipher *tfm)

    obtain block size for cipher

    :param struct crypto_cipher \*tfm:
        cipher handle



.. _`crypto_cipher_blocksize.description`:

Description
-----------

The block size for the single block cipher referenced with the cipher handle
tfm is returned. The caller may use that information to allocate appropriate
memory for the data returned by the encryption or decryption operation



.. _`crypto_cipher_blocksize.return`:

Return
------

block size of cipher



.. _`crypto_cipher_setkey`:

crypto_cipher_setkey
====================

.. c:function:: int crypto_cipher_setkey (struct crypto_cipher *tfm, const u8 *key, unsigned int keylen)

    set key for cipher

    :param struct crypto_cipher \*tfm:
        cipher handle

    :param const u8 \*key:
        buffer holding the key

    :param unsigned int keylen:
        length of the key in bytes



.. _`crypto_cipher_setkey.description`:

Description
-----------

The caller provided key is set for the single block cipher referenced by the
cipher handle.

Note, the key length determines the cipher type. Many block ciphers implement
different cipher modes depending on the key size, such as AES-128 vs AES-192
vs. AES-256. When providing a 16 byte key for an AES cipher handle, AES-128
is performed.



.. _`crypto_cipher_setkey.return`:

Return
------

0 if the setting of the key was successful; < 0 if an error occurred



.. _`crypto_cipher_encrypt_one`:

crypto_cipher_encrypt_one
=========================

.. c:function:: void crypto_cipher_encrypt_one (struct crypto_cipher *tfm, u8 *dst, const u8 *src)

    encrypt one block of plaintext

    :param struct crypto_cipher \*tfm:
        cipher handle

    :param u8 \*dst:
        points to the buffer that will be filled with the ciphertext

    :param const u8 \*src:
        buffer holding the plaintext to be encrypted



.. _`crypto_cipher_encrypt_one.description`:

Description
-----------

Invoke the encryption operation of one block. The caller must ensure that
the plaintext and ciphertext buffers are at least one block in size.



.. _`crypto_cipher_decrypt_one`:

crypto_cipher_decrypt_one
=========================

.. c:function:: void crypto_cipher_decrypt_one (struct crypto_cipher *tfm, u8 *dst, const u8 *src)

    decrypt one block of ciphertext

    :param struct crypto_cipher \*tfm:
        cipher handle

    :param u8 \*dst:
        points to the buffer that will be filled with the plaintext

    :param const u8 \*src:
        buffer holding the ciphertext to be decrypted



.. _`crypto_cipher_decrypt_one.description`:

Description
-----------

Invoke the decryption operation of one block. The caller must ensure that
the plaintext and ciphertext buffers are at least one block in size.

