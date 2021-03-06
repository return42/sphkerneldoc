.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/if_alg.h

.. _`af_alg_async_req`:

struct af_alg_async_req
=======================

.. c:type:: struct af_alg_async_req

    definition of crypto request

.. _`af_alg_async_req.definition`:

Definition
----------

.. code-block:: c

    struct af_alg_async_req {
        struct kiocb *iocb;
        struct sock *sk;
        struct af_alg_rsgl first_rsgl;
        struct af_alg_rsgl *last_rsgl;
        struct list_head rsgl_list;
        struct scatterlist *tsgl;
        unsigned int tsgl_entries;
        unsigned int outlen;
        unsigned int areqlen;
        union {
            struct aead_request aead_req;
            struct skcipher_request skcipher_req;
        } cra_u;
    }

.. _`af_alg_async_req.members`:

Members
-------

iocb
    IOCB for AIO operations

sk
    Socket the request is associated with

first_rsgl
    First RX SG

last_rsgl
    Pointer to last RX SG

rsgl_list
    Track RX SGs

tsgl
    Private, per request TX SGL of buffers to process

tsgl_entries
    Number of entries in priv. TX SGL

outlen
    Number of output bytes generated by crypto op

areqlen
    Length of this data structure

cra_u
    Cipher request

.. _`af_alg_ctx`:

struct af_alg_ctx
=================

.. c:type:: struct af_alg_ctx

    definition of the crypto context

.. _`af_alg_ctx.definition`:

Definition
----------

.. code-block:: c

    struct af_alg_ctx {
        struct list_head tsgl_list;
        void *iv;
        size_t aead_assoclen;
        struct crypto_wait wait;
        size_t used;
        atomic_t rcvused;
        bool more;
        bool merge;
        bool enc;
        unsigned int len;
    }

.. _`af_alg_ctx.members`:

Members
-------

tsgl_list
    Link to TX SGL

iv
    IV for cipher operation

aead_assoclen
    Length of AAD for AEAD cipher operations

wait
    *undescribed*

used
    TX bytes sent to kernel. This variable is used to
    ensure that user space cannot cause the kernel
    to allocate too much memory in sendmsg operation.

rcvused
    Total RX bytes to be filled by kernel. This variable
    is used to ensure user space cannot cause the kernel
    to allocate too much memory in a recvmsg operation.

more
    More data to be expected from user space?

merge
    Shall new data from user space be merged into existing
    SG?

enc
    Cryptographic operation to be performed when
    recvmsg is invoked.

len
    Length of memory allocated for this data structure.

.. _`af_alg_ctx.description`:

Description
-----------

The crypto context tracks the input data during the lifetime of an AF_ALG
socket.

.. _`af_alg_sndbuf`:

af_alg_sndbuf
=============

.. c:function:: int af_alg_sndbuf(struct sock *sk)

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`af_alg_sndbuf.description`:

Description
-----------

\ ``sk``\  socket of connection to user space
\ ``return``\  number of bytes still available

.. _`af_alg_writable`:

af_alg_writable
===============

.. c:function:: bool af_alg_writable(struct sock *sk)

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`af_alg_writable.description`:

Description
-----------

\ ``sk``\  socket of connection to user space
\ ``return``\  true => writable, false => not writable

.. _`af_alg_rcvbuf`:

af_alg_rcvbuf
=============

.. c:function:: int af_alg_rcvbuf(struct sock *sk)

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`af_alg_rcvbuf.description`:

Description
-----------

\ ``sk``\  socket of connection to user space
\ ``return``\  number of bytes still available

.. _`af_alg_readable`:

af_alg_readable
===============

.. c:function:: bool af_alg_readable(struct sock *sk)

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`af_alg_readable.description`:

Description
-----------

\ ``sk``\  socket of connection to user space
\ ``return``\  true => writable, false => not writable

.. This file was automatic generated / don't edit.

