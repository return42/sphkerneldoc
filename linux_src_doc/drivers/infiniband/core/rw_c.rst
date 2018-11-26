.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/rw.c

.. _`rdma_rw_ctx_init`:

rdma_rw_ctx_init
================

.. c:function:: int rdma_rw_ctx_init(struct rdma_rw_ctx *ctx, struct ib_qp *qp, u8 port_num, struct scatterlist *sg, u32 sg_cnt, u32 sg_offset, u64 remote_addr, u32 rkey, enum dma_data_direction dir)

    initialize a RDMA READ/WRITE context

    :param ctx:
        context to initialize
    :type ctx: struct rdma_rw_ctx \*

    :param qp:
        queue pair to operate on
    :type qp: struct ib_qp \*

    :param port_num:
        port num to which the connection is bound
    :type port_num: u8

    :param sg:
        scatterlist to READ/WRITE from/to
    :type sg: struct scatterlist \*

    :param sg_cnt:
        number of entries in \ ``sg``\ 
    :type sg_cnt: u32

    :param sg_offset:
        current byte offset into \ ``sg``\ 
    :type sg_offset: u32

    :param remote_addr:
        remote address to read/write (relative to \ ``rkey``\ )
    :type remote_addr: u64

    :param rkey:
        remote key to operate on
    :type rkey: u32

    :param dir:
        \ ``DMA_TO_DEVICE``\  for RDMA WRITE, \ ``DMA_FROM_DEVICE``\  for RDMA READ
    :type dir: enum dma_data_direction

.. _`rdma_rw_ctx_init.description`:

Description
-----------

Returns the number of WQEs that will be needed on the workqueue if
successful, or a negative error code.

.. _`rdma_rw_ctx_signature_init`:

rdma_rw_ctx_signature_init
==========================

.. c:function:: int rdma_rw_ctx_signature_init(struct rdma_rw_ctx *ctx, struct ib_qp *qp, u8 port_num, struct scatterlist *sg, u32 sg_cnt, struct scatterlist *prot_sg, u32 prot_sg_cnt, struct ib_sig_attrs *sig_attrs, u64 remote_addr, u32 rkey, enum dma_data_direction dir)

    initialize a RW context with signature offload

    :param ctx:
        context to initialize
    :type ctx: struct rdma_rw_ctx \*

    :param qp:
        queue pair to operate on
    :type qp: struct ib_qp \*

    :param port_num:
        port num to which the connection is bound
    :type port_num: u8

    :param sg:
        scatterlist to READ/WRITE from/to
    :type sg: struct scatterlist \*

    :param sg_cnt:
        number of entries in \ ``sg``\ 
    :type sg_cnt: u32

    :param prot_sg:
        scatterlist to READ/WRITE protection information from/to
    :type prot_sg: struct scatterlist \*

    :param prot_sg_cnt:
        number of entries in \ ``prot_sg``\ 
    :type prot_sg_cnt: u32

    :param sig_attrs:
        signature offloading algorithms
    :type sig_attrs: struct ib_sig_attrs \*

    :param remote_addr:
        remote address to read/write (relative to \ ``rkey``\ )
    :type remote_addr: u64

    :param rkey:
        remote key to operate on
    :type rkey: u32

    :param dir:
        \ ``DMA_TO_DEVICE``\  for RDMA WRITE, \ ``DMA_FROM_DEVICE``\  for RDMA READ
    :type dir: enum dma_data_direction

.. _`rdma_rw_ctx_signature_init.description`:

Description
-----------

Returns the number of WQEs that will be needed on the workqueue if
successful, or a negative error code.

.. _`rdma_rw_ctx_wrs`:

rdma_rw_ctx_wrs
===============

.. c:function:: struct ib_send_wr *rdma_rw_ctx_wrs(struct rdma_rw_ctx *ctx, struct ib_qp *qp, u8 port_num, struct ib_cqe *cqe, struct ib_send_wr *chain_wr)

    return chain of WRs for a RDMA READ or WRITE operation

    :param ctx:
        context to operate on
    :type ctx: struct rdma_rw_ctx \*

    :param qp:
        queue pair to operate on
    :type qp: struct ib_qp \*

    :param port_num:
        port num to which the connection is bound
    :type port_num: u8

    :param cqe:
        completion queue entry for the last WR
    :type cqe: struct ib_cqe \*

    :param chain_wr:
        WR to append to the posted chain
    :type chain_wr: struct ib_send_wr \*

.. _`rdma_rw_ctx_wrs.description`:

Description
-----------

Return the WR chain for the set of RDMA READ/WRITE operations described by
\ ``ctx``\ , as well as any memory registration operations needed.  If \ ``chain_wr``\ 
is non-NULL the WR it points to will be appended to the chain of WRs posted.
If \ ``chain_wr``\  is not set \ ``cqe``\  must be set so that the caller gets a
completion notification.

.. _`rdma_rw_ctx_post`:

rdma_rw_ctx_post
================

.. c:function:: int rdma_rw_ctx_post(struct rdma_rw_ctx *ctx, struct ib_qp *qp, u8 port_num, struct ib_cqe *cqe, struct ib_send_wr *chain_wr)

    post a RDMA READ or RDMA WRITE operation

    :param ctx:
        context to operate on
    :type ctx: struct rdma_rw_ctx \*

    :param qp:
        queue pair to operate on
    :type qp: struct ib_qp \*

    :param port_num:
        port num to which the connection is bound
    :type port_num: u8

    :param cqe:
        completion queue entry for the last WR
    :type cqe: struct ib_cqe \*

    :param chain_wr:
        WR to append to the posted chain
    :type chain_wr: struct ib_send_wr \*

.. _`rdma_rw_ctx_post.description`:

Description
-----------

Post the set of RDMA READ/WRITE operations described by \ ``ctx``\ , as well as
any memory registration operations needed.  If \ ``chain_wr``\  is non-NULL the
WR it points to will be appended to the chain of WRs posted.  If \ ``chain_wr``\ 
is not set \ ``cqe``\  must be set so that the caller gets a completion
notification.

.. _`rdma_rw_ctx_destroy`:

rdma_rw_ctx_destroy
===================

.. c:function:: void rdma_rw_ctx_destroy(struct rdma_rw_ctx *ctx, struct ib_qp *qp, u8 port_num, struct scatterlist *sg, u32 sg_cnt, enum dma_data_direction dir)

    release all resources allocated by rdma_rw_ctx_init

    :param ctx:
        context to release
    :type ctx: struct rdma_rw_ctx \*

    :param qp:
        queue pair to operate on
    :type qp: struct ib_qp \*

    :param port_num:
        port num to which the connection is bound
    :type port_num: u8

    :param sg:
        scatterlist that was used for the READ/WRITE
    :type sg: struct scatterlist \*

    :param sg_cnt:
        number of entries in \ ``sg``\ 
    :type sg_cnt: u32

    :param dir:
        \ ``DMA_TO_DEVICE``\  for RDMA WRITE, \ ``DMA_FROM_DEVICE``\  for RDMA READ
    :type dir: enum dma_data_direction

.. _`rdma_rw_ctx_destroy_signature`:

rdma_rw_ctx_destroy_signature
=============================

.. c:function:: void rdma_rw_ctx_destroy_signature(struct rdma_rw_ctx *ctx, struct ib_qp *qp, u8 port_num, struct scatterlist *sg, u32 sg_cnt, struct scatterlist *prot_sg, u32 prot_sg_cnt, enum dma_data_direction dir)

    release all resources allocated by rdma_rw_ctx_init_signature

    :param ctx:
        context to release
    :type ctx: struct rdma_rw_ctx \*

    :param qp:
        queue pair to operate on
    :type qp: struct ib_qp \*

    :param port_num:
        port num to which the connection is bound
    :type port_num: u8

    :param sg:
        scatterlist that was used for the READ/WRITE
    :type sg: struct scatterlist \*

    :param sg_cnt:
        number of entries in \ ``sg``\ 
    :type sg_cnt: u32

    :param prot_sg:
        scatterlist that was used for the READ/WRITE of the PI
    :type prot_sg: struct scatterlist \*

    :param prot_sg_cnt:
        number of entries in \ ``prot_sg``\ 
    :type prot_sg_cnt: u32

    :param dir:
        \ ``DMA_TO_DEVICE``\  for RDMA WRITE, \ ``DMA_FROM_DEVICE``\  for RDMA READ
    :type dir: enum dma_data_direction

.. _`rdma_rw_mr_factor`:

rdma_rw_mr_factor
=================

.. c:function:: unsigned int rdma_rw_mr_factor(struct ib_device *device, u8 port_num, unsigned int maxpages)

    return number of MRs required for a payload

    :param device:
        device handling the connection
    :type device: struct ib_device \*

    :param port_num:
        port num to which the connection is bound
    :type port_num: u8

    :param maxpages:
        maximum payload pages per rdma_rw_ctx
    :type maxpages: unsigned int

.. _`rdma_rw_mr_factor.description`:

Description
-----------

Returns the number of MRs the device requires to move \ ``maxpayload``\ 
bytes. The returned value is used during transport creation to
compute max_rdma_ctxts and the size of the transport's Send and
Send Completion Queues.

.. This file was automatic generated / don't edit.

