.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/hash.h

.. _`hash_alg_common`:

struct hash_alg_common
======================

.. c:type:: struct hash_alg_common

    define properties of message digest

.. _`hash_alg_common.definition`:

Definition
----------

.. code-block:: c

    struct hash_alg_common {
        unsigned int digestsize;
        unsigned int statesize;
        struct crypto_alg base;
    }

.. _`hash_alg_common.members`:

Members
-------

digestsize
    Size of the result of the transformation. A buffer of this size
    must be available to the \ ``final``\  and \ ``finup``\  calls, so they can
    store the resulting hash into it. For various predefined sizes,
    search include/crypto/ using
    git grep \_DIGEST_SIZE include/crypto.

statesize
    Size of the block for partial state of the transformation. A
    buffer of this size must be passed to the \ ``export``\  function as it
    will save the partial state of the transformation into it. On the
    other side, the \ ``import``\  function will load the state from a
    buffer of this size as well.

base
    Start of data structure of cipher algorithm. The common data
    structure of crypto_alg contains information common to all ciphers.
    The hash_alg_common data structure now adds the hash-specific
    information.

.. _`ahash_alg`:

struct ahash_alg
================

.. c:type:: struct ahash_alg

    asynchronous message digest definition

.. _`ahash_alg.definition`:

Definition
----------

.. code-block:: c

    struct ahash_alg {
        int (*init)(struct ahash_request *req);
        int (*update)(struct ahash_request *req);
        int (*final)(struct ahash_request *req);
        int (*finup)(struct ahash_request *req);
        int (*digest)(struct ahash_request *req);
        int (*export)(struct ahash_request *req, void *out);
        int (*import)(struct ahash_request *req, const void *in);
        int (*setkey)(struct crypto_ahash *tfm, const u8 *key,unsigned int keylen);
        struct hash_alg_common halg;
    }

.. _`ahash_alg.members`:

Members
-------

init
    Initialize the transformation context. Intended only to initialize the
    state of the HASH transformation at the beginning. This shall fill in
    the internal structures used during the entire duration of the whole
    transformation. No data processing happens at this point.

update
    Push a chunk of data into the driver for transformation. This
    function actually pushes blocks of data from upper layers into the
    driver, which then passes those to the hardware as seen fit. This
    function must not finalize the HASH transformation by calculating the
    final message digest as this only adds more data into the
    transformation. This function shall not modify the transformation
    context, as this function may be called in parallel with the same
    transformation object. Data processing can happen synchronously
    [SHASH] or asynchronously [AHASH] at this point.

final
    Retrieve result from the driver. This function finalizes the
    transformation and retrieves the resulting hash from the driver and
    pushes it back to upper layers. No data processing happens at this
    point.

finup
    Combination of \ ``update``\  and \ ``final``\ . This function is effectively a
    combination of \ ``update``\  and \ ``final``\  calls issued in sequence. As some
    hardware cannot do \ ``update``\  and \ ``final``\  separately, this callback was
    added to allow such hardware to be used at least by IPsec. Data
    processing can happen synchronously [SHASH] or asynchronously [AHASH]
    at this point.

digest
    Combination of \ ``init``\  and \ ``update``\  and \ ``final``\ . This function
    effectively behaves as the entire chain of operations, \ ``init``\ ,
    \ ``update``\  and \ ``final``\  issued in sequence. Just like \ ``finup``\ , this was
    added for hardware which cannot do even the \ ``finup``\ , but can only do
    the whole transformation in one run. Data processing can happen
    synchronously [SHASH] or asynchronously [AHASH] at this point.

export
    Export partial state of the transformation. This function dumps the
    entire state of the ongoing transformation into a provided block of
    data so it can be \ ``import``\  'ed back later on. This is useful in case
    you want to save partial result of the transformation after
    processing certain amount of data and reload this partial result
    multiple times later on for multiple re-use. No data processing
    happens at this point.

import
    Import partial state of the transformation. This function loads the
    entire state of the ongoing transformation from a provided block of
    data so the transformation can continue from this point onward. No
    data processing happens at this point.

setkey
    Set optional key used by the hashing algorithm. Intended to push
    optional key used by the hashing algorithm from upper layers into
    the driver. This function can store the key in the transformation
    context or can outright program it into the hardware. In the former
    case, one must be careful to program the key into the hardware at
    appropriate time and one must be careful that .\ :c:func:`setkey`\  can be
    called multiple times during the existence of the transformation
    object. Not  all hashing algorithms do implement this function as it
    is only needed for keyed message digests. SHAx/MDx/CRCx do NOT
    implement this function. HMAC(MDx)/HMAC(SHAx)/CMAC(AES) do implement
    this function. This function must be called before any other of the
    \ ``init``\ , \ ``update``\ , \ ``final``\ , \ ``finup``\ , \ ``digest``\  is called. No data
    processing happens at this point.

halg
    see struct hash_alg_common

.. _`shash_alg`:

struct shash_alg
================

.. c:type:: struct shash_alg

    synchronous message digest definition

.. _`shash_alg.definition`:

Definition
----------

.. code-block:: c

    struct shash_alg {
        int (*init)(struct shash_desc *desc);
        int (*update)(struct shash_desc *desc, const u8 *data,unsigned int len);
        int (*final)(struct shash_desc *desc, u8 *out);
        int (*finup)(struct shash_desc *desc, const u8 *data,unsigned int len, u8 *out);
        int (*digest)(struct shash_desc *desc, const u8 *data,unsigned int len, u8 *out);
        int (*export)(struct shash_desc *desc, void *out);
        int (*import)(struct shash_desc *desc, const void *in);
        int (*setkey)(struct crypto_shash *tfm, const u8 *key,unsigned int keylen);
        unsigned int descsize;
        unsigned int digestsize;
        unsigned int statesize;
        struct crypto_alg base;
    }

.. _`shash_alg.members`:

Members
-------

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

.. _`crypto_alloc_ahash`:

crypto_alloc_ahash
==================

.. c:function:: struct crypto_ahash *crypto_alloc_ahash(const char *alg_name, u32 type, u32 mask)

    allocate ahash cipher handle

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        ahash cipher

    :param u32 type:
        specifies the type of the cipher

    :param u32 mask:
        specifies the mask for the cipher

.. _`crypto_alloc_ahash.description`:

Description
-----------

Allocate a cipher handle for an ahash. The returned struct
crypto_ahash is the cipher handle that is required for any subsequent
API invocation for that ahash.

.. _`crypto_alloc_ahash.return`:

Return
------

allocated cipher handle in case of success; \ :c:func:`IS_ERR`\  is true in case
of an error, \ :c:func:`PTR_ERR`\  returns the error code.

.. _`crypto_free_ahash`:

crypto_free_ahash
=================

.. c:function:: void crypto_free_ahash(struct crypto_ahash *tfm)

    zeroize and free the ahash handle

    :param struct crypto_ahash \*tfm:
        cipher handle to be freed

.. _`crypto_has_ahash`:

crypto_has_ahash
================

.. c:function:: int crypto_has_ahash(const char *alg_name, u32 type, u32 mask)

    Search for the availability of an ahash.

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        ahash

    :param u32 type:
        specifies the type of the ahash

    :param u32 mask:
        specifies the mask for the ahash

.. _`crypto_has_ahash.return`:

Return
------

true when the ahash is known to the kernel crypto API; false
otherwise

.. _`crypto_ahash_blocksize`:

crypto_ahash_blocksize
======================

.. c:function:: unsigned int crypto_ahash_blocksize(struct crypto_ahash *tfm)

    obtain block size for cipher

    :param struct crypto_ahash \*tfm:
        cipher handle

.. _`crypto_ahash_blocksize.description`:

Description
-----------

The block size for the message digest cipher referenced with the cipher
handle is returned.

.. _`crypto_ahash_blocksize.return`:

Return
------

block size of cipher

.. _`crypto_ahash_digestsize`:

crypto_ahash_digestsize
=======================

.. c:function:: unsigned int crypto_ahash_digestsize(struct crypto_ahash *tfm)

    obtain message digest size

    :param struct crypto_ahash \*tfm:
        cipher handle

.. _`crypto_ahash_digestsize.description`:

Description
-----------

The size for the message digest created by the message digest cipher
referenced with the cipher handle is returned.

.. _`crypto_ahash_digestsize.return`:

Return
------

message digest size of cipher

.. _`crypto_ahash_reqtfm`:

crypto_ahash_reqtfm
===================

.. c:function:: struct crypto_ahash *crypto_ahash_reqtfm(struct ahash_request *req)

    obtain cipher handle from request

    :param struct ahash_request \*req:
        asynchronous request handle that contains the reference to the ahash
        cipher handle

.. _`crypto_ahash_reqtfm.description`:

Description
-----------

Return the ahash cipher handle that is registered with the asynchronous
request handle ahash_request.

.. _`crypto_ahash_reqtfm.return`:

Return
------

ahash cipher handle

.. _`crypto_ahash_reqsize`:

crypto_ahash_reqsize
====================

.. c:function:: unsigned int crypto_ahash_reqsize(struct crypto_ahash *tfm)

    obtain size of the request data structure

    :param struct crypto_ahash \*tfm:
        cipher handle

.. _`crypto_ahash_reqsize.description`:

Description
-----------

Return the size of the ahash state size. With the crypto_ahash_export
function, the caller can export the state into a buffer whose size is
defined with this function.

.. _`crypto_ahash_reqsize.return`:

Return
------

size of the ahash state

.. _`crypto_ahash_setkey`:

crypto_ahash_setkey
===================

.. c:function:: int crypto_ahash_setkey(struct crypto_ahash *tfm, const u8 *key, unsigned int keylen)

    set key for cipher handle

    :param struct crypto_ahash \*tfm:
        cipher handle

    :param const u8 \*key:
        buffer holding the key

    :param unsigned int keylen:
        length of the key in bytes

.. _`crypto_ahash_setkey.description`:

Description
-----------

The caller provided key is set for the ahash cipher. The cipher
handle must point to a keyed hash in order for this function to succeed.

.. _`crypto_ahash_setkey.return`:

Return
------

0 if the setting of the key was successful; < 0 if an error occurred

.. _`crypto_ahash_finup`:

crypto_ahash_finup
==================

.. c:function:: int crypto_ahash_finup(struct ahash_request *req)

    update and finalize message digest

    :param struct ahash_request \*req:
        reference to the ahash_request handle that holds all information
        needed to perform the cipher operation

.. _`crypto_ahash_finup.description`:

Description
-----------

This function is a "short-hand" for the function calls of
crypto_ahash_update and crypto_shash_final. The parameters have the same
meaning as discussed for those separate functions.

.. _`crypto_ahash_finup.return`:

Return
------

0 if the message digest creation was successful; < 0 if an error
occurred

.. _`crypto_ahash_final`:

crypto_ahash_final
==================

.. c:function:: int crypto_ahash_final(struct ahash_request *req)

    calculate message digest

    :param struct ahash_request \*req:
        reference to the ahash_request handle that holds all information
        needed to perform the cipher operation

.. _`crypto_ahash_final.description`:

Description
-----------

Finalize the message digest operation and create the message digest
based on all data added to the cipher handle. The message digest is placed
into the output buffer registered with the ahash_request handle.

.. _`crypto_ahash_final.return`:

Return
------

0 if the message digest creation was successful; < 0 if an error
occurred

.. _`crypto_ahash_digest`:

crypto_ahash_digest
===================

.. c:function:: int crypto_ahash_digest(struct ahash_request *req)

    calculate message digest for a buffer

    :param struct ahash_request \*req:
        reference to the ahash_request handle that holds all information
        needed to perform the cipher operation

.. _`crypto_ahash_digest.description`:

Description
-----------

This function is a "short-hand" for the function calls of crypto_ahash_init,
crypto_ahash_update and crypto_ahash_final. The parameters have the same
meaning as discussed for those separate three functions.

.. _`crypto_ahash_digest.return`:

Return
------

0 if the message digest creation was successful; < 0 if an error
occurred

.. _`crypto_ahash_export`:

crypto_ahash_export
===================

.. c:function:: int crypto_ahash_export(struct ahash_request *req, void *out)

    extract current message digest state

    :param struct ahash_request \*req:
        reference to the ahash_request handle whose state is exported

    :param void \*out:
        output buffer of sufficient size that can hold the hash state

.. _`crypto_ahash_export.description`:

Description
-----------

This function exports the hash state of the ahash_request handle into the
caller-allocated output buffer out which must have sufficient size (e.g. by
calling crypto_ahash_reqsize).

.. _`crypto_ahash_export.return`:

Return
------

0 if the export was successful; < 0 if an error occurred

.. _`crypto_ahash_import`:

crypto_ahash_import
===================

.. c:function:: int crypto_ahash_import(struct ahash_request *req, const void *in)

    import message digest state

    :param struct ahash_request \*req:
        reference to ahash_request handle the state is imported into

    :param const void \*in:
        buffer holding the state

.. _`crypto_ahash_import.description`:

Description
-----------

This function imports the hash state into the ahash_request handle from the
input buffer. That buffer should have been generated with the
crypto_ahash_export function.

.. _`crypto_ahash_import.return`:

Return
------

0 if the import was successful; < 0 if an error occurred

.. _`crypto_ahash_init`:

crypto_ahash_init
=================

.. c:function:: int crypto_ahash_init(struct ahash_request *req)

    (re)initialize message digest handle

    :param struct ahash_request \*req:
        ahash_request handle that already is initialized with all necessary
        data using the ahash_request\_\* API functions

.. _`crypto_ahash_init.description`:

Description
-----------

The call (re-)initializes the message digest referenced by the ahash_request
handle. Any potentially existing state created by previous operations is
discarded.

.. _`crypto_ahash_init.return`:

Return
------

0 if the message digest initialization was successful; < 0 if an
error occurred

.. _`crypto_ahash_update`:

crypto_ahash_update
===================

.. c:function:: int crypto_ahash_update(struct ahash_request *req)

    add data to message digest for processing

    :param struct ahash_request \*req:
        ahash_request handle that was previously initialized with the
        crypto_ahash_init call.

.. _`crypto_ahash_update.description`:

Description
-----------

Updates the message digest state of the \ :c:type:`struct ahash_request <ahash_request>` handle. The input data
is pointed to by the scatter/gather list registered in the \ :c:type:`struct ahash_request <ahash_request>`
handle

.. _`crypto_ahash_update.return`:

Return
------

0 if the message digest update was successful; < 0 if an error
occurred

.. _`ahash_request_set_tfm`:

ahash_request_set_tfm
=====================

.. c:function:: void ahash_request_set_tfm(struct ahash_request *req, struct crypto_ahash *tfm)

    update cipher handle reference in request

    :param struct ahash_request \*req:
        request handle to be modified

    :param struct crypto_ahash \*tfm:
        cipher handle that shall be added to the request handle

.. _`ahash_request_set_tfm.description`:

Description
-----------

Allow the caller to replace the existing ahash handle in the request
data structure with a different one.

.. _`ahash_request_alloc`:

ahash_request_alloc
===================

.. c:function:: struct ahash_request *ahash_request_alloc(struct crypto_ahash *tfm, gfp_t gfp)

    allocate request data structure

    :param struct crypto_ahash \*tfm:
        cipher handle to be registered with the request

    :param gfp_t gfp:
        memory allocation flag that is handed to kmalloc by the API call.

.. _`ahash_request_alloc.description`:

Description
-----------

Allocate the request data structure that must be used with the ahash
message digest API calls. During
the allocation, the provided ahash handle
is registered in the request data structure.

.. _`ahash_request_alloc.return`:

Return
------

allocated request handle in case of success, or NULL if out of memory

.. _`ahash_request_free`:

ahash_request_free
==================

.. c:function:: void ahash_request_free(struct ahash_request *req)

    zeroize and free the request data structure

    :param struct ahash_request \*req:
        request data structure cipher handle to be freed

.. _`ahash_request_set_callback`:

ahash_request_set_callback
==========================

.. c:function:: void ahash_request_set_callback(struct ahash_request *req, u32 flags, crypto_completion_t compl, void *data)

    set asynchronous callback function

    :param struct ahash_request \*req:
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
        \ :c:type:`struct crypto_async_request <crypto_async_request>` data structure provided to the callback function.

.. _`ahash_request_set_callback.description`:

Description
-----------

This function allows setting the callback function that is triggered once
the cipher operation completes.

The callback function is registered with the \ :c:type:`struct ahash_request <ahash_request>` handle and
must comply with the following template

void callback_function(struct crypto_async_request \*req, int error)

.. _`ahash_request_set_crypt`:

ahash_request_set_crypt
=======================

.. c:function:: void ahash_request_set_crypt(struct ahash_request *req, struct scatterlist *src, u8 *result, unsigned int nbytes)

    set data buffers

    :param struct ahash_request \*req:
        ahash_request handle to be updated

    :param struct scatterlist \*src:
        source scatter/gather list

    :param u8 \*result:
        buffer that is filled with the message digest -- the caller must
        ensure that the buffer has sufficient space by, for example, calling
        \ :c:func:`crypto_ahash_digestsize`\ 

    :param unsigned int nbytes:
        number of bytes to process from the source scatter/gather list

.. _`ahash_request_set_crypt.description`:

Description
-----------

By using this call, the caller references the source scatter/gather list.
The source scatter/gather list points to the data the message digest is to
be calculated for.

.. _`crypto_alloc_shash`:

crypto_alloc_shash
==================

.. c:function:: struct crypto_shash *crypto_alloc_shash(const char *alg_name, u32 type, u32 mask)

    allocate message digest handle

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        message digest cipher

    :param u32 type:
        specifies the type of the cipher

    :param u32 mask:
        specifies the mask for the cipher

.. _`crypto_alloc_shash.description`:

Description
-----------

Allocate a cipher handle for a message digest. The returned \ :c:type:`struct crypto_shash <crypto_shash>`\  is the cipher handle that is required for any subsequent
API invocation for that message digest.

.. _`crypto_alloc_shash.return`:

Return
------

allocated cipher handle in case of success; \ :c:func:`IS_ERR`\  is true in case
of an error, \ :c:func:`PTR_ERR`\  returns the error code.

.. _`crypto_free_shash`:

crypto_free_shash
=================

.. c:function:: void crypto_free_shash(struct crypto_shash *tfm)

    zeroize and free the message digest handle

    :param struct crypto_shash \*tfm:
        cipher handle to be freed

.. _`crypto_shash_blocksize`:

crypto_shash_blocksize
======================

.. c:function:: unsigned int crypto_shash_blocksize(struct crypto_shash *tfm)

    obtain block size for cipher

    :param struct crypto_shash \*tfm:
        cipher handle

.. _`crypto_shash_blocksize.description`:

Description
-----------

The block size for the message digest cipher referenced with the cipher
handle is returned.

.. _`crypto_shash_blocksize.return`:

Return
------

block size of cipher

.. _`crypto_shash_digestsize`:

crypto_shash_digestsize
=======================

.. c:function:: unsigned int crypto_shash_digestsize(struct crypto_shash *tfm)

    obtain message digest size

    :param struct crypto_shash \*tfm:
        cipher handle

.. _`crypto_shash_digestsize.description`:

Description
-----------

The size for the message digest created by the message digest cipher
referenced with the cipher handle is returned.

.. _`crypto_shash_digestsize.return`:

Return
------

digest size of cipher

.. _`crypto_shash_descsize`:

crypto_shash_descsize
=====================

.. c:function:: unsigned int crypto_shash_descsize(struct crypto_shash *tfm)

    obtain the operational state size

    :param struct crypto_shash \*tfm:
        cipher handle

.. _`crypto_shash_descsize.description`:

Description
-----------

The size of the operational state the cipher needs during operation is
returned for the hash referenced with the cipher handle. This size is
required to calculate the memory requirements to allow the caller allocating
sufficient memory for operational state.

The operational state is defined with struct shash_desc where the size of
that data structure is to be calculated as
sizeof(struct shash_desc) + crypto_shash_descsize(alg)

.. _`crypto_shash_descsize.return`:

Return
------

size of the operational state

.. _`crypto_shash_setkey`:

crypto_shash_setkey
===================

.. c:function:: int crypto_shash_setkey(struct crypto_shash *tfm, const u8 *key, unsigned int keylen)

    set key for message digest

    :param struct crypto_shash \*tfm:
        cipher handle

    :param const u8 \*key:
        buffer holding the key

    :param unsigned int keylen:
        length of the key in bytes

.. _`crypto_shash_setkey.description`:

Description
-----------

The caller provided key is set for the keyed message digest cipher. The
cipher handle must point to a keyed message digest cipher in order for this
function to succeed.

.. _`crypto_shash_setkey.return`:

Return
------

0 if the setting of the key was successful; < 0 if an error occurred

.. _`crypto_shash_digest`:

crypto_shash_digest
===================

.. c:function:: int crypto_shash_digest(struct shash_desc *desc, const u8 *data, unsigned int len, u8 *out)

    calculate message digest for buffer

    :param struct shash_desc \*desc:
        see \ :c:func:`crypto_shash_final`\ 

    :param const u8 \*data:
        see \ :c:func:`crypto_shash_update`\ 

    :param unsigned int len:
        see \ :c:func:`crypto_shash_update`\ 

    :param u8 \*out:
        see \ :c:func:`crypto_shash_final`\ 

.. _`crypto_shash_digest.description`:

Description
-----------

This function is a "short-hand" for the function calls of crypto_shash_init,
crypto_shash_update and crypto_shash_final. The parameters have the same
meaning as discussed for those separate three functions.

.. _`crypto_shash_digest.return`:

Return
------

0 if the message digest creation was successful; < 0 if an error
occurred

.. _`crypto_shash_export`:

crypto_shash_export
===================

.. c:function:: int crypto_shash_export(struct shash_desc *desc, void *out)

    extract operational state for message digest

    :param struct shash_desc \*desc:
        reference to the operational state handle whose state is exported

    :param void \*out:
        output buffer of sufficient size that can hold the hash state

.. _`crypto_shash_export.description`:

Description
-----------

This function exports the hash state of the operational state handle into the
caller-allocated output buffer out which must have sufficient size (e.g. by
calling crypto_shash_descsize).

.. _`crypto_shash_export.return`:

Return
------

0 if the export creation was successful; < 0 if an error occurred

.. _`crypto_shash_import`:

crypto_shash_import
===================

.. c:function:: int crypto_shash_import(struct shash_desc *desc, const void *in)

    import operational state

    :param struct shash_desc \*desc:
        reference to the operational state handle the state imported into

    :param const void \*in:
        buffer holding the state

.. _`crypto_shash_import.description`:

Description
-----------

This function imports the hash state into the operational state handle from
the input buffer. That buffer should have been generated with the
crypto_ahash_export function.

.. _`crypto_shash_import.return`:

Return
------

0 if the import was successful; < 0 if an error occurred

.. _`crypto_shash_init`:

crypto_shash_init
=================

.. c:function:: int crypto_shash_init(struct shash_desc *desc)

    (re)initialize message digest

    :param struct shash_desc \*desc:
        operational state handle that is already filled

.. _`crypto_shash_init.description`:

Description
-----------

The call (re-)initializes the message digest referenced by the
operational state handle. Any potentially existing state created by
previous operations is discarded.

.. _`crypto_shash_init.return`:

Return
------

0 if the message digest initialization was successful; < 0 if an
error occurred

.. _`crypto_shash_update`:

crypto_shash_update
===================

.. c:function:: int crypto_shash_update(struct shash_desc *desc, const u8 *data, unsigned int len)

    add data to message digest for processing

    :param struct shash_desc \*desc:
        operational state handle that is already initialized

    :param const u8 \*data:
        input data to be added to the message digest

    :param unsigned int len:
        length of the input data

.. _`crypto_shash_update.description`:

Description
-----------

Updates the message digest state of the operational state handle.

.. _`crypto_shash_update.return`:

Return
------

0 if the message digest update was successful; < 0 if an error
occurred

.. _`crypto_shash_final`:

crypto_shash_final
==================

.. c:function:: int crypto_shash_final(struct shash_desc *desc, u8 *out)

    calculate message digest

    :param struct shash_desc \*desc:
        operational state handle that is already filled with data

    :param u8 \*out:
        output buffer filled with the message digest

.. _`crypto_shash_final.description`:

Description
-----------

Finalize the message digest operation and create the message digest
based on all data added to the cipher handle. The message digest is placed
into the output buffer. The caller must ensure that the output buffer is
large enough by using crypto_shash_digestsize.

.. _`crypto_shash_final.return`:

Return
------

0 if the message digest creation was successful; < 0 if an error
occurred

.. _`crypto_shash_finup`:

crypto_shash_finup
==================

.. c:function:: int crypto_shash_finup(struct shash_desc *desc, const u8 *data, unsigned int len, u8 *out)

    calculate message digest of buffer

    :param struct shash_desc \*desc:
        see \ :c:func:`crypto_shash_final`\ 

    :param const u8 \*data:
        see \ :c:func:`crypto_shash_update`\ 

    :param unsigned int len:
        see \ :c:func:`crypto_shash_update`\ 

    :param u8 \*out:
        see \ :c:func:`crypto_shash_final`\ 

.. _`crypto_shash_finup.description`:

Description
-----------

This function is a "short-hand" for the function calls of
crypto_shash_update and crypto_shash_final. The parameters have the same
meaning as discussed for those separate functions.

.. _`crypto_shash_finup.return`:

Return
------

0 if the message digest creation was successful; < 0 if an error
occurred

.. This file was automatic generated / don't edit.

