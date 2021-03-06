.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/akcipher.h

.. _`akcipher_request`:

struct akcipher_request
=======================

.. c:type:: struct akcipher_request

    public key request

.. _`akcipher_request.definition`:

Definition
----------

.. code-block:: c

    struct akcipher_request {
        struct crypto_async_request base;
        struct scatterlist *src;
        struct scatterlist *dst;
        unsigned int src_len;
        unsigned int dst_len;
        void *__ctx[] CRYPTO_MINALIGN_ATTR;
    }

.. _`akcipher_request.members`:

Members
-------

base
    Common attributes for async crypto requests

src
    Source data

dst
    Destination data

src_len
    Size of the input buffer

dst_len
    Size of the output buffer. It needs to be at least
    as big as the expected result depending on the operation
    After operation it will be updated with the actual size of the
    result.
    In case of error where the dst sgl size was insufficient,
    it will be updated to the size required for the operation.

__ctx
    Start of private context data

.. _`crypto_akcipher`:

struct crypto_akcipher
======================

.. c:type:: struct crypto_akcipher

    user-instantiated objects which encapsulate algorithms and core processing logic

.. _`crypto_akcipher.definition`:

Definition
----------

.. code-block:: c

    struct crypto_akcipher {
        struct crypto_tfm base;
    }

.. _`crypto_akcipher.members`:

Members
-------

base
    Common crypto API algorithm data structure

.. _`akcipher_alg`:

struct akcipher_alg
===================

.. c:type:: struct akcipher_alg

    generic public key algorithm

.. _`akcipher_alg.definition`:

Definition
----------

.. code-block:: c

    struct akcipher_alg {
        int (*sign)(struct akcipher_request *req);
        int (*verify)(struct akcipher_request *req);
        int (*encrypt)(struct akcipher_request *req);
        int (*decrypt)(struct akcipher_request *req);
        int (*set_pub_key)(struct crypto_akcipher *tfm, const void *key, unsigned int keylen);
        int (*set_priv_key)(struct crypto_akcipher *tfm, const void *key, unsigned int keylen);
        unsigned int (*max_size)(struct crypto_akcipher *tfm);
        int (*init)(struct crypto_akcipher *tfm);
        void (*exit)(struct crypto_akcipher *tfm);
        unsigned int reqsize;
        struct crypto_alg base;
    }

.. _`akcipher_alg.members`:

Members
-------

sign
    Function performs a sign operation as defined by public key
    algorithm. In case of error, where the dst_len was insufficient,
    the req->dst_len will be updated to the size required for the
    operation

verify
    Function performs a sign operation as defined by public key
    algorithm. In case of error, where the dst_len was insufficient,
    the req->dst_len will be updated to the size required for the
    operation

encrypt
    Function performs an encrypt operation as defined by public key
    algorithm. In case of error, where the dst_len was insufficient,
    the req->dst_len will be updated to the size required for the
    operation

decrypt
    Function performs a decrypt operation as defined by public key
    algorithm. In case of error, where the dst_len was insufficient,
    the req->dst_len will be updated to the size required for the
    operation

set_pub_key
    Function invokes the algorithm specific set public key
    function, which knows how to decode and interpret
    the BER encoded public key

set_priv_key
    Function invokes the algorithm specific set private key
    function, which knows how to decode and interpret
    the BER encoded private key

max_size
    Function returns dest buffer size required for a given key.

init
    Initialize the cryptographic transformation object.
    This function is used to initialize the cryptographic
    transformation object. This function is called only once at
    the instantiation time, right after the transformation context
    was allocated. In case the cryptographic hardware has some
    special requirements which need to be handled by software, this
    function shall check for the precise requirement of the
    transformation and put any software fallbacks in place.

exit
    Deinitialize the cryptographic transformation object. This is a
    counterpart to \ ``init``\ , used to remove various changes set in
    \ ``init``\ .

reqsize
    Request context size required by algorithm implementation

base
    Common crypto API algorithm data structure

.. _`generic-public-key-api`:

Generic Public Key API
======================

The Public Key API is used with the algorithms of type
CRYPTO_ALG_TYPE_AKCIPHER (listed as type "akcipher" in /proc/crypto)

.. _`crypto_alloc_akcipher`:

crypto_alloc_akcipher
=====================

.. c:function:: struct crypto_akcipher *crypto_alloc_akcipher(const char *alg_name, u32 type, u32 mask)

    allocate AKCIPHER tfm handle

    :param alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        public key algorithm e.g. "rsa"
    :type alg_name: const char \*

    :param type:
        specifies the type of the algorithm
    :type type: u32

    :param mask:
        specifies the mask for the algorithm
    :type mask: u32

.. _`crypto_alloc_akcipher.description`:

Description
-----------

Allocate a handle for public key algorithm. The returned struct
crypto_akcipher is the handle that is required for any subsequent
API invocation for the public key operations.

.. _`crypto_alloc_akcipher.return`:

Return
------

allocated handle in case of success; \ :c:func:`IS_ERR`\  is true in case
        of an error, \ :c:func:`PTR_ERR`\  returns the error code.

.. _`crypto_free_akcipher`:

crypto_free_akcipher
====================

.. c:function:: void crypto_free_akcipher(struct crypto_akcipher *tfm)

    free AKCIPHER tfm handle

    :param tfm:
        AKCIPHER tfm handle allocated with \ :c:func:`crypto_alloc_akcipher`\ 
    :type tfm: struct crypto_akcipher \*

.. _`akcipher_request_alloc`:

akcipher_request_alloc
======================

.. c:function:: struct akcipher_request *akcipher_request_alloc(struct crypto_akcipher *tfm, gfp_t gfp)

    allocates public key request

    :param tfm:
        AKCIPHER tfm handle allocated with \ :c:func:`crypto_alloc_akcipher`\ 
    :type tfm: struct crypto_akcipher \*

    :param gfp:
        allocation flags
    :type gfp: gfp_t

.. _`akcipher_request_alloc.return`:

Return
------

allocated handle in case of success or NULL in case of an error.

.. _`akcipher_request_free`:

akcipher_request_free
=====================

.. c:function:: void akcipher_request_free(struct akcipher_request *req)

    zeroize and free public key request

    :param req:
        request to free
    :type req: struct akcipher_request \*

.. _`akcipher_request_set_callback`:

akcipher_request_set_callback
=============================

.. c:function:: void akcipher_request_set_callback(struct akcipher_request *req, u32 flgs, crypto_completion_t cmpl, void *data)

    Sets an asynchronous callback.

    :param req:
        request that the callback will be set for
    :type req: struct akcipher_request \*

    :param flgs:
        specify for instance if the operation may backlog
    :type flgs: u32

    :param cmpl:
        callback which will be called
    :type cmpl: crypto_completion_t

    :param data:
        private data used by the caller
    :type data: void \*

.. _`akcipher_request_set_callback.description`:

Description
-----------

Callback will be called when an asynchronous operation on a given
request is finished.

.. _`akcipher_request_set_crypt`:

akcipher_request_set_crypt
==========================

.. c:function:: void akcipher_request_set_crypt(struct akcipher_request *req, struct scatterlist *src, struct scatterlist *dst, unsigned int src_len, unsigned int dst_len)

    Sets request parameters

    :param req:
        public key request
    :type req: struct akcipher_request \*

    :param src:
        ptr to input scatter list
    :type src: struct scatterlist \*

    :param dst:
        ptr to output scatter list
    :type dst: struct scatterlist \*

    :param src_len:
        size of the src input scatter list to be processed
    :type src_len: unsigned int

    :param dst_len:
        size of the dst output scatter list
    :type dst_len: unsigned int

.. _`akcipher_request_set_crypt.description`:

Description
-----------

Sets parameters required by crypto operation

.. _`crypto_akcipher_maxsize`:

crypto_akcipher_maxsize
=======================

.. c:function:: unsigned int crypto_akcipher_maxsize(struct crypto_akcipher *tfm)

    Get len for output buffer

    :param tfm:
        AKCIPHER tfm handle allocated with \ :c:func:`crypto_alloc_akcipher`\ 
    :type tfm: struct crypto_akcipher \*

.. _`crypto_akcipher_maxsize.description`:

Description
-----------

Function returns the dest buffer size required for a given key.
Function assumes that the key is already set in the transformation. If this
function is called without a setkey or with a failed setkey, you will end up
in a NULL dereference.

.. _`crypto_akcipher_encrypt`:

crypto_akcipher_encrypt
=======================

.. c:function:: int crypto_akcipher_encrypt(struct akcipher_request *req)

    Invoke public key encrypt operation

    :param req:
        asymmetric key request
    :type req: struct akcipher_request \*

.. _`crypto_akcipher_encrypt.description`:

Description
-----------

Function invokes the specific public key encrypt operation for a given
public key algorithm

.. _`crypto_akcipher_encrypt.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_akcipher_decrypt`:

crypto_akcipher_decrypt
=======================

.. c:function:: int crypto_akcipher_decrypt(struct akcipher_request *req)

    Invoke public key decrypt operation

    :param req:
        asymmetric key request
    :type req: struct akcipher_request \*

.. _`crypto_akcipher_decrypt.description`:

Description
-----------

Function invokes the specific public key decrypt operation for a given
public key algorithm

.. _`crypto_akcipher_decrypt.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_akcipher_sign`:

crypto_akcipher_sign
====================

.. c:function:: int crypto_akcipher_sign(struct akcipher_request *req)

    Invoke public key sign operation

    :param req:
        asymmetric key request
    :type req: struct akcipher_request \*

.. _`crypto_akcipher_sign.description`:

Description
-----------

Function invokes the specific public key sign operation for a given
public key algorithm

.. _`crypto_akcipher_sign.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_akcipher_verify`:

crypto_akcipher_verify
======================

.. c:function:: int crypto_akcipher_verify(struct akcipher_request *req)

    Invoke public key verify operation

    :param req:
        asymmetric key request
    :type req: struct akcipher_request \*

.. _`crypto_akcipher_verify.description`:

Description
-----------

Function invokes the specific public key verify operation for a given
public key algorithm

.. _`crypto_akcipher_verify.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_akcipher_set_pub_key`:

crypto_akcipher_set_pub_key
===========================

.. c:function:: int crypto_akcipher_set_pub_key(struct crypto_akcipher *tfm, const void *key, unsigned int keylen)

    Invoke set public key operation

    :param tfm:
        tfm handle
    :type tfm: struct crypto_akcipher \*

    :param key:
        BER encoded public key
    :type key: const void \*

    :param keylen:
        length of the key
    :type keylen: unsigned int

.. _`crypto_akcipher_set_pub_key.description`:

Description
-----------

Function invokes the algorithm specific set key function, which knows
how to decode and interpret the encoded key

.. _`crypto_akcipher_set_pub_key.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_akcipher_set_priv_key`:

crypto_akcipher_set_priv_key
============================

.. c:function:: int crypto_akcipher_set_priv_key(struct crypto_akcipher *tfm, const void *key, unsigned int keylen)

    Invoke set private key operation

    :param tfm:
        tfm handle
    :type tfm: struct crypto_akcipher \*

    :param key:
        BER encoded private key
    :type key: const void \*

    :param keylen:
        length of the key
    :type keylen: unsigned int

.. _`crypto_akcipher_set_priv_key.description`:

Description
-----------

Function invokes the algorithm specific set key function, which knows
how to decode and interpret the encoded key

.. _`crypto_akcipher_set_priv_key.return`:

Return
------

zero on success; error code in case of error

.. This file was automatic generated / don't edit.

