.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/kpp.h

.. _`kpp_request`:

struct kpp_request
==================

.. c:type:: struct kpp_request


.. _`kpp_request.definition`:

Definition
----------

.. code-block:: c

    struct kpp_request {
        struct crypto_async_request base;
        struct scatterlist *src;
        struct scatterlist *dst;
        unsigned int src_len;
        unsigned int dst_len;
        void  *__ctx[];
    }

.. _`kpp_request.members`:

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
    result. In case of error where the dst sgl size was insufficient,
    it will be updated to the size required for the operation.

__ctx
    Start of private context data

.. _`crypto_kpp`:

struct crypto_kpp
=================

.. c:type:: struct crypto_kpp

    user-instantiated object which encapsulate algorithms and core processing logic

.. _`crypto_kpp.definition`:

Definition
----------

.. code-block:: c

    struct crypto_kpp {
        struct crypto_tfm base;
    }

.. _`crypto_kpp.members`:

Members
-------

base
    Common crypto API algorithm data structure

.. _`kpp_alg`:

struct kpp_alg
==============

.. c:type:: struct kpp_alg

    generic key-agreement protocol primitives

.. _`kpp_alg.definition`:

Definition
----------

.. code-block:: c

    struct kpp_alg {
        int (*set_secret)(struct crypto_kpp *tfm, void *buffer,unsigned int len);
        int (*generate_public_key)(struct kpp_request *req);
        int (*compute_shared_secret)(struct kpp_request *req);
        int (*max_size)(struct crypto_kpp *tfm);
        int (*init)(struct crypto_kpp *tfm);
        void (*exit)(struct crypto_kpp *tfm);
        unsigned int reqsize;
        struct crypto_alg base;
    }

.. _`kpp_alg.members`:

Members
-------

set_secret
    Function invokes the protocol specific function to
    store the secret private key along with parameters.
    The implementation knows how to decode thie buffer

generate_public_key
    Function generate the public key to be sent to the
    counterpart. In case of error, where output is not big
    enough req->dst_len will be updated to the size
    required

compute_shared_secret
    Function compute the shared secret as defined by
    the algorithm. The result is given back to the user.
    In case of error, where output is not big enough,
    req->dst_len will be updated to the size required

max_size
    Function returns the size of the output buffer

init
    Initialize the object. This is called only once at
    instantiation time. In case the cryptographic hardware
    needs to be initialized. Software fallback should be
    put in place here.

exit
    Undo everything \ ``init``\  did.

reqsize
    Request context size required by algorithm
    implementation

base
    Common crypto API algorithm data structure

.. _`crypto_alloc_kpp`:

crypto_alloc_kpp
================

.. c:function:: struct crypto_kpp *crypto_alloc_kpp(const char *alg_name, u32 type, u32 mask)

    allocate KPP tfm handle

    :param const char \*alg_name:
        is the name of the kpp algorithm (e.g. "dh", "ecdh")

    :param u32 type:
        specifies the type of the algorithm

    :param u32 mask:
        specifies the mask for the algorithm

.. _`crypto_alloc_kpp.description`:

Description
-----------

Allocate a handle for kpp algorithm. The returned struct crypto_kpp
is requeried for any following API invocation

.. _`crypto_alloc_kpp.return`:

Return
------

allocated handle in case of success; \ :c:func:`IS_ERR`\  is true in case of
        an error, \ :c:func:`PTR_ERR`\  returns the error code.

.. _`crypto_free_kpp`:

crypto_free_kpp
===============

.. c:function:: void crypto_free_kpp(struct crypto_kpp *tfm)

    free KPP tfm handle

    :param struct crypto_kpp \*tfm:
        KPP tfm handle allocated with \ :c:func:`crypto_alloc_kpp`\ 

.. _`kpp_request_alloc`:

kpp_request_alloc
=================

.. c:function:: struct kpp_request *kpp_request_alloc(struct crypto_kpp *tfm, gfp_t gfp)

    allocates kpp request

    :param struct crypto_kpp \*tfm:
        KPP tfm handle allocated with \ :c:func:`crypto_alloc_kpp`\ 

    :param gfp_t gfp:
        allocation flags

.. _`kpp_request_alloc.return`:

Return
------

allocated handle in case of success or NULL in case of an error.

.. _`kpp_request_free`:

kpp_request_free
================

.. c:function:: void kpp_request_free(struct kpp_request *req)

    zeroize and free kpp request

    :param struct kpp_request \*req:
        request to free

.. _`kpp_request_set_callback`:

kpp_request_set_callback
========================

.. c:function:: void kpp_request_set_callback(struct kpp_request *req, u32 flgs, crypto_completion_t cmpl, void *data)

    Sets an asynchronous callback.

    :param struct kpp_request \*req:
        request that the callback will be set for

    :param u32 flgs:
        specify for instance if the operation may backlog

    :param crypto_completion_t cmpl:
        callback which will be called

    :param void \*data:
        private data used by the caller

.. _`kpp_request_set_callback.description`:

Description
-----------

Callback will be called when an asynchronous operation on a given
request is finished.

.. _`kpp_request_set_input`:

kpp_request_set_input
=====================

.. c:function:: void kpp_request_set_input(struct kpp_request *req, struct scatterlist *input, unsigned int input_len)

    Sets input buffer

    :param struct kpp_request \*req:
        kpp request

    :param struct scatterlist \*input:
        ptr to input scatter list

    :param unsigned int input_len:
        size of the input scatter list

.. _`kpp_request_set_input.description`:

Description
-----------

Sets parameters required by generate_public_key

.. _`kpp_request_set_output`:

kpp_request_set_output
======================

.. c:function:: void kpp_request_set_output(struct kpp_request *req, struct scatterlist *output, unsigned int output_len)

    Sets output buffer

    :param struct kpp_request \*req:
        kpp request

    :param struct scatterlist \*output:
        ptr to output scatter list

    :param unsigned int output_len:
        size of the output scatter list

.. _`kpp_request_set_output.description`:

Description
-----------

Sets parameters required by kpp operation

.. _`kpp_secret`:

struct kpp_secret
=================

.. c:type:: struct kpp_secret

    small header for packing secret buffer

.. _`kpp_secret.definition`:

Definition
----------

.. code-block:: c

    struct kpp_secret {
        unsigned short type;
        unsigned short len;
    }

.. _`kpp_secret.members`:

Members
-------

type
    define type of secret. Each kpp type will define its own

len
    specify the len of the secret, include the header, that
    follows the struct

.. _`crypto_kpp_set_secret`:

crypto_kpp_set_secret
=====================

.. c:function:: int crypto_kpp_set_secret(struct crypto_kpp *tfm, void *buffer, unsigned int len)

    Invoke kpp operation

    :param struct crypto_kpp \*tfm:
        tfm handle

    :param void \*buffer:
        Buffer holding the packet representation of the private
        key. The structure of the packet key depends on the particular
        KPP implementation. Packing and unpacking helpers are provided
        for ECDH and DH (see the respective header files for those
        implementations).

    :param unsigned int len:
        Length of the packet private key buffer.

.. _`crypto_kpp_set_secret.description`:

Description
-----------

Function invokes the specific kpp operation for a given alg.

.. _`crypto_kpp_set_secret.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_kpp_generate_public_key`:

crypto_kpp_generate_public_key
==============================

.. c:function:: int crypto_kpp_generate_public_key(struct kpp_request *req)

    Invoke kpp operation

    :param struct kpp_request \*req:
        kpp key request

.. _`crypto_kpp_generate_public_key.description`:

Description
-----------

Function invokes the specific kpp operation for generating the public part
for a given kpp algorithm.

To generate a private key, the caller should use a random number generator.
The output of the requested length serves as the private key.

.. _`crypto_kpp_generate_public_key.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_kpp_compute_shared_secret`:

crypto_kpp_compute_shared_secret
================================

.. c:function:: int crypto_kpp_compute_shared_secret(struct kpp_request *req)

    Invoke kpp operation

    :param struct kpp_request \*req:
        kpp key request

.. _`crypto_kpp_compute_shared_secret.description`:

Description
-----------

Function invokes the specific kpp operation for computing the shared secret
for a given kpp algorithm.

.. _`crypto_kpp_compute_shared_secret.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_kpp_maxsize`:

crypto_kpp_maxsize
==================

.. c:function:: int crypto_kpp_maxsize(struct crypto_kpp *tfm)

    Get len for output buffer

    :param struct crypto_kpp \*tfm:
        KPP tfm handle allocated with \ :c:func:`crypto_alloc_kpp`\ 

.. _`crypto_kpp_maxsize.description`:

Description
-----------

Function returns the output buffer size required

.. _`crypto_kpp_maxsize.return`:

Return
------

minimum len for output buffer or error code if key hasn't been set

.. This file was automatic generated / don't edit.

