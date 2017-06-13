.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/acompress.h

.. _`acomp_req`:

struct acomp_req
================

.. c:type:: struct acomp_req

    asynchronous (de)compression request

.. _`acomp_req.definition`:

Definition
----------

.. code-block:: c

    struct acomp_req {
        struct crypto_async_request base;
        struct scatterlist *src;
        struct scatterlist *dst;
        unsigned int slen;
        unsigned int dlen;
        u32 flags;
        void  *__ctx;
    }

.. _`acomp_req.members`:

Members
-------

base
    Common attributes for asynchronous crypto requests

src
    Source Data

dst
    Destination data

slen
    Size of the input buffer

dlen
    Size of the output buffer and number of bytes produced

flags
    Internal flags

__ctx
    Start of private context data

.. _`crypto_acomp`:

struct crypto_acomp
===================

.. c:type:: struct crypto_acomp

    user-instantiated objects which encapsulate algorithms and core processing logic

.. _`crypto_acomp.definition`:

Definition
----------

.. code-block:: c

    struct crypto_acomp {
        int (*compress)(struct acomp_req *req);
        int (*decompress)(struct acomp_req *req);
        void (*dst_free)(struct scatterlist *dst);
        unsigned int reqsize;
        struct crypto_tfm base;
    }

.. _`crypto_acomp.members`:

Members
-------

compress
    Function performs a compress operation

decompress
    Function performs a de-compress operation

dst_free
    Frees destination buffer if allocated inside the
    algorithm

reqsize
    Context size for (de)compression requests

base
    Common crypto API algorithm data structure

.. _`acomp_alg`:

struct acomp_alg
================

.. c:type:: struct acomp_alg

    asynchronous compression algorithm

.. _`acomp_alg.definition`:

Definition
----------

.. code-block:: c

    struct acomp_alg {
        int (*compress)(struct acomp_req *req);
        int (*decompress)(struct acomp_req *req);
        void (*dst_free)(struct scatterlist *dst);
        int (*init)(struct crypto_acomp *tfm);
        void (*exit)(struct crypto_acomp *tfm);
        unsigned int reqsize;
        struct crypto_alg base;
    }

.. _`acomp_alg.members`:

Members
-------

compress
    Function performs a compress operation

decompress
    Function performs a de-compress operation

dst_free
    Frees destination buffer if allocated inside the algorithm

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
    Context size for (de)compression requests

base
    Common crypto API algorithm data structure

.. _`crypto_alloc_acomp`:

crypto_alloc_acomp
==================

.. c:function:: struct crypto_acomp *crypto_alloc_acomp(const char *alg_name, u32 type, u32 mask)

    - allocate ACOMPRESS tfm handle

    :param const char \*alg_name:
        is the cra_name / name or cra_driver_name / driver name of the
        compression algorithm e.g. "deflate"

    :param u32 type:
        specifies the type of the algorithm

    :param u32 mask:
        specifies the mask for the algorithm

.. _`crypto_alloc_acomp.description`:

Description
-----------

Allocate a handle for a compression algorithm. The returned struct
crypto_acomp is the handle that is required for any subsequent
API invocation for the compression operations.

.. _`crypto_alloc_acomp.return`:

Return
------

allocated handle in case of success; \ :c:func:`IS_ERR`\  is true in case
of an error, \ :c:func:`PTR_ERR`\  returns the error code.

.. _`crypto_free_acomp`:

crypto_free_acomp
=================

.. c:function:: void crypto_free_acomp(struct crypto_acomp *tfm)

    - free ACOMPRESS tfm handle

    :param struct crypto_acomp \*tfm:
        ACOMPRESS tfm handle allocated with \ :c:func:`crypto_alloc_acomp`\ 

.. _`acomp_request_alloc`:

acomp_request_alloc
===================

.. c:function:: struct acomp_req *acomp_request_alloc(struct crypto_acomp *tfm)

    - allocates asynchronous (de)compression request

    :param struct crypto_acomp \*tfm:
        ACOMPRESS tfm handle allocated with \ :c:func:`crypto_alloc_acomp`\ 

.. _`acomp_request_alloc.return`:

Return
------

allocated handle in case of success or NULL in case of an error

.. _`acomp_request_free`:

acomp_request_free
==================

.. c:function:: void acomp_request_free(struct acomp_req *req)

    - zeroize and free asynchronous (de)compression request as well as the output buffer if allocated inside the algorithm

    :param struct acomp_req \*req:
        request to free

.. _`acomp_request_set_callback`:

acomp_request_set_callback
==========================

.. c:function:: void acomp_request_set_callback(struct acomp_req *req, u32 flgs, crypto_completion_t cmpl, void *data)

    - Sets an asynchronous callback

    :param struct acomp_req \*req:
        request that the callback will be set for

    :param u32 flgs:
        specify for instance if the operation may backlog

    :param crypto_completion_t cmpl:
        *undescribed*

    :param void \*data:
        private data used by the caller

.. _`acomp_request_set_callback.description`:

Description
-----------

Callback will be called when an asynchronous operation on a given
request is finished.

.. _`acomp_request_set_params`:

acomp_request_set_params
========================

.. c:function:: void acomp_request_set_params(struct acomp_req *req, struct scatterlist *src, struct scatterlist *dst, unsigned int slen, unsigned int dlen)

    - Sets request parameters

    :param struct acomp_req \*req:
        asynchronous compress request

    :param struct scatterlist \*src:
        pointer to input buffer scatterlist

    :param struct scatterlist \*dst:
        pointer to output buffer scatterlist. If this is NULL, the
        acomp layer will allocate the output memory

    :param unsigned int slen:
        size of the input buffer

    :param unsigned int dlen:
        size of the output buffer. If dst is NULL, this can be used by
        the user to specify the maximum amount of memory to allocate

.. _`acomp_request_set_params.description`:

Description
-----------

Sets parameters required by an acomp operation

.. _`crypto_acomp_compress`:

crypto_acomp_compress
=====================

.. c:function:: int crypto_acomp_compress(struct acomp_req *req)

    - Invoke asynchronous compress operation

    :param struct acomp_req \*req:
        asynchronous compress request

.. _`crypto_acomp_compress.description`:

Description
-----------

Function invokes the asynchronous compress operation

.. _`crypto_acomp_compress.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_acomp_decompress`:

crypto_acomp_decompress
=======================

.. c:function:: int crypto_acomp_decompress(struct acomp_req *req)

    - Invoke asynchronous decompress operation

    :param struct acomp_req \*req:
        asynchronous compress request

.. _`crypto_acomp_decompress.description`:

Description
-----------

Function invokes the asynchronous decompress operation

.. _`crypto_acomp_decompress.return`:

Return
------

zero on success; error code in case of error

.. This file was automatic generated / don't edit.

