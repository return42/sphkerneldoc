.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/af_alg.c

.. _`af_alg_alloc_tsgl`:

af_alg_alloc_tsgl
=================

.. c:function:: int af_alg_alloc_tsgl(struct sock *sk)

    allocate the TX SGL

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`af_alg_alloc_tsgl.description`:

Description
-----------

\ ``sk``\  socket of connection to user space

.. _`af_alg_count_tsgl`:

af_alg_count_tsgl
=================

.. c:function:: unsigned int af_alg_count_tsgl(struct sock *sk, size_t bytes, size_t offset)

    Count number of TX SG entries

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param bytes:
        *undescribed*
    :type bytes: size_t

    :param offset:
        *undescribed*
    :type offset: size_t

.. _`af_alg_count_tsgl.description`:

Description
-----------

The counting starts from the beginning of the SGL to \ ``bytes``\ . If
an offset is provided, the counting of the SG entries starts at the offset.

\ ``sk``\  socket of connection to user space
\ ``bytes``\  Count the number of SG entries holding given number of bytes.
\ ``offset``\  Start the counting of SG entries from the given offset.
\ ``return``\  Number of TX SG entries found given the constraints

.. _`af_alg_pull_tsgl`:

af_alg_pull_tsgl
================

.. c:function:: void af_alg_pull_tsgl(struct sock *sk, size_t used, struct scatterlist *dst, size_t dst_offset)

    Release the specified buffers from TX SGL

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param used:
        *undescribed*
    :type used: size_t

    :param dst:
        *undescribed*
    :type dst: struct scatterlist \*

    :param dst_offset:
        *undescribed*
    :type dst_offset: size_t

.. _`af_alg_pull_tsgl.description`:

Description
-----------

If \ ``dst``\  is non-null, reassign the pages to dst. The caller must release
the pages. If \ ``dst_offset``\  is given only reassign the pages to \ ``dst``\  starting
at the \ ``dst_offset``\  (byte). The caller must ensure that \ ``dst``\  is large
enough (e.g. by using af_alg_count_tsgl with the same offset).

\ ``sk``\  socket of connection to user space
\ ``used``\  Number of bytes to pull from TX SGL
\ ``dst``\  If non-NULL, buffer is reassigned to dst SGL instead of releasing. The
caller must release the buffers in dst.
\ ``dst_offset``\  Reassign the TX SGL from given offset. All buffers before
reaching the offset is released.

.. _`af_alg_free_areq_sgls`:

af_alg_free_areq_sgls
=====================

.. c:function:: void af_alg_free_areq_sgls(struct af_alg_async_req *areq)

    Release TX and RX SGLs of the request

    :param areq:
        *undescribed*
    :type areq: struct af_alg_async_req \*

.. _`af_alg_free_areq_sgls.description`:

Description
-----------

\ ``areq``\  Request holding the TX and RX SGL

.. _`af_alg_wait_for_wmem`:

af_alg_wait_for_wmem
====================

.. c:function:: int af_alg_wait_for_wmem(struct sock *sk, unsigned int flags)

    wait for availability of writable memory

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param flags:
        *undescribed*
    :type flags: unsigned int

.. _`af_alg_wait_for_wmem.description`:

Description
-----------

\ ``sk``\  socket of connection to user space
\ ``flags``\  If MSG_DONTWAIT is set, then only report if function would sleep
\ ``return``\  0 when writable memory is available, < 0 upon error

.. _`af_alg_wmem_wakeup`:

af_alg_wmem_wakeup
==================

.. c:function:: void af_alg_wmem_wakeup(struct sock *sk)

    wakeup caller when writable memory is available

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`af_alg_wmem_wakeup.description`:

Description
-----------

\ ``sk``\  socket of connection to user space

.. _`af_alg_wait_for_data`:

af_alg_wait_for_data
====================

.. c:function:: int af_alg_wait_for_data(struct sock *sk, unsigned flags)

    wait for availability of TX data

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param flags:
        *undescribed*
    :type flags: unsigned

.. _`af_alg_wait_for_data.description`:

Description
-----------

\ ``sk``\  socket of connection to user space
\ ``flags``\  If MSG_DONTWAIT is set, then only report if function would sleep
\ ``return``\  0 when writable memory is available, < 0 upon error

.. _`af_alg_data_wakeup`:

af_alg_data_wakeup
==================

.. c:function:: void af_alg_data_wakeup(struct sock *sk)

    wakeup caller when new data can be sent to kernel

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`af_alg_data_wakeup.description`:

Description
-----------

\ ``sk``\  socket of connection to user space

.. _`af_alg_sendmsg`:

af_alg_sendmsg
==============

.. c:function:: int af_alg_sendmsg(struct socket *sock, struct msghdr *msg, size_t size, unsigned int ivsize)

    implementation of sendmsg system call handler

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param msg:
        *undescribed*
    :type msg: struct msghdr \*

    :param size:
        *undescribed*
    :type size: size_t

    :param ivsize:
        *undescribed*
    :type ivsize: unsigned int

.. _`af_alg_sendmsg.description`:

Description
-----------

The sendmsg system call handler obtains the user data and stores it
in ctx->tsgl_list. This implies allocation of the required numbers of
struct af_alg_tsgl.

In addition, the ctx is filled with the information sent via CMSG.

\ ``sock``\  socket of connection to user space
\ ``msg``\  message from user space
\ ``size``\  size of message from user space
\ ``ivsize``\  the size of the IV for the cipher operation to verify that the
user-space-provided IV has the right size
\ ``return``\  the number of copied data upon success, < 0 upon error

.. _`af_alg_sendpage`:

af_alg_sendpage
===============

.. c:function:: ssize_t af_alg_sendpage(struct socket *sock, struct page *page, int offset, size_t size, int flags)

    sendpage system call handler

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param page:
        *undescribed*
    :type page: struct page \*

    :param offset:
        *undescribed*
    :type offset: int

    :param size:
        *undescribed*
    :type size: size_t

    :param flags:
        *undescribed*
    :type flags: int

.. _`af_alg_sendpage.description`:

Description
-----------

This is a generic implementation of sendpage to fill ctx->tsgl_list.

.. _`af_alg_free_resources`:

af_alg_free_resources
=====================

.. c:function:: void af_alg_free_resources(struct af_alg_async_req *areq)

    release resources required for crypto request

    :param areq:
        *undescribed*
    :type areq: struct af_alg_async_req \*

.. _`af_alg_async_cb`:

af_alg_async_cb
===============

.. c:function:: void af_alg_async_cb(struct crypto_async_request *_req, int err)

    AIO callback handler

    :param _req:
        *undescribed*
    :type _req: struct crypto_async_request \*

    :param err:
        *undescribed*
    :type err: int

.. _`af_alg_async_cb.description`:

Description
-----------

This handler cleans up the struct af_alg_async_req upon completion of the
AIO operation.

The number of bytes to be generated with the AIO operation must be set
in areq->outlen before the AIO callback handler is invoked.

.. _`af_alg_poll`:

af_alg_poll
===========

.. c:function:: __poll_t af_alg_poll(struct file *file, struct socket *sock, poll_table *wait)

    poll system call handler

    :param file:
        *undescribed*
    :type file: struct file \*

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param wait:
        *undescribed*
    :type wait: poll_table \*

.. _`af_alg_alloc_areq`:

af_alg_alloc_areq
=================

.. c:function:: struct af_alg_async_req *af_alg_alloc_areq(struct sock *sk, unsigned int areqlen)

    allocate struct af_alg_async_req

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param areqlen:
        *undescribed*
    :type areqlen: unsigned int

.. _`af_alg_alloc_areq.description`:

Description
-----------

\ ``sk``\  socket of connection to user space
\ ``areqlen``\  size of struct af_alg_async_req + crypto\_\*\_reqsize
\ ``return``\  allocated data structure or ERR_PTR upon error

.. _`af_alg_get_rsgl`:

af_alg_get_rsgl
===============

.. c:function:: int af_alg_get_rsgl(struct sock *sk, struct msghdr *msg, int flags, struct af_alg_async_req *areq, size_t maxsize, size_t *outlen)

    create the RX SGL for the output data from the crypto operation

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param msg:
        *undescribed*
    :type msg: struct msghdr \*

    :param flags:
        *undescribed*
    :type flags: int

    :param areq:
        *undescribed*
    :type areq: struct af_alg_async_req \*

    :param maxsize:
        *undescribed*
    :type maxsize: size_t

    :param outlen:
        *undescribed*
    :type outlen: size_t \*

.. _`af_alg_get_rsgl.description`:

Description
-----------

\ ``sk``\  socket of connection to user space
\ ``msg``\  user space message
\ ``flags``\  flags used to invoke recvmsg with
\ ``areq``\  instance of the cryptographic request that will hold the RX SGL
\ ``maxsize``\  maximum number of bytes to be pulled from user space
\ ``outlen``\  number of bytes in the RX SGL
\ ``return``\  0 on success, < 0 upon error

.. This file was automatic generated / don't edit.

