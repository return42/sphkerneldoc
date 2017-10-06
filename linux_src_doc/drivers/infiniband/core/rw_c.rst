.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/rw.c

.. _`rdma_rw_ctx_init`:

rdma_rw_ctx_init
================

.. c:function:: int rdma_rw_ctx_init(struct rdma_rw_ctx *ctx, struct ib_qp *qp, u8 port_num, struct scatterlist *sg, u32 sg_cnt, u32 sg_offset, u64 remote_addr, u32 rkey, enum dma_data_direction dir)

    initialize a RDMA READ/WRITE context

    :param struct rdma_rw_ctx \*ctx:
        context to initialize

    :param struct ib_qp \*qp:
        queue pair to operate on

    :param u8 port_num:
        port num to which the connection is bound

    :param struct scatterlist \*sg:
        scatterlist to READ/WRITE from/to

    :param u32 sg_cnt:
        number of entries in \ ``sg``\ 

    :param u32 sg_offset:
        current byte offset into \ ``sg``\ 

    :param u64 remote_addr:
        remote address to read/write (relative to \ ``rkey``\ )

    :param u32 rkey:
        remote key to operate on

    :param enum dma_data_direction dir:
        %DMA_TO_DEVICE for RDMA WRITE, \ ``DMA_FROM_DEVICE``\  for RDMA READ

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

    :param struct rdma_rw_ctx \*ctx:
        context to initialize

    :param struct ib_qp \*qp:
        queue pair to operate on

    :param u8 port_num:
        port num to which the connection is bound

    :param struct scatterlist \*sg:
        scatterlist to READ/WRITE from/to

    :param u32 sg_cnt:
        number of entries in \ ``sg``\ 

    :param struct scatterlist \*prot_sg:
        scatterlist to READ/WRITE protection information from/to

    :param u32 prot_sg_cnt:
        number of entries in \ ``prot_sg``\ 

    :param struct ib_sig_attrs \*sig_attrs:
        signature offloading algorithms

    :param u64 remote_addr:
        remote address to read/write (relative to \ ``rkey``\ )

    :param u32 rkey:
        remote key to operate on

    :param enum dma_data_direction dir:
        %DMA_TO_DEVICE for RDMA WRITE, \ ``DMA_FROM_DEVICE``\  for RDMA READ

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

    :param struct rdma_rw_ctx \*ctx:
        context to operate on

    :param struct ib_qp \*qp:
        queue pair to operate on

    :param u8 port_num:
        port num to which the connection is bound

    :param struct ib_cqe \*cqe:
        completion queue entry for the last WR

    :param struct ib_send_wr \*chain_wr:
        WR to append to the posted chain

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

    :param struct rdma_rw_ctx \*ctx:
        context to operate on

    :param struct ib_qp \*qp:
        queue pair to operate on

    :param u8 port_num:
        port num to which the connection is bound

    :param struct ib_cqe \*cqe:
        completion queue entry for the last WR

    :param struct ib_send_wr \*chain_wr:
        WR to append to the posted chain

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

    :param struct rdma_rw_ctx \*ctx:
        context to release

    :param struct ib_qp \*qp:
        queue pair to operate on

    :param u8 port_num:
        port num to which the connection is bound

    :param struct scatterlist \*sg:
        scatterlist that was used for the READ/WRITE

    :param u32 sg_cnt:
        number of entries in \ ``sg``\ 

    :param enum dma_data_direction dir:
        %DMA_TO_DEVICE for RDMA WRITE, \ ``DMA_FROM_DEVICE``\  for RDMA READ

.. _`rdma_rw_ctx_destroy_signature`:

rdma_rw_ctx_destroy_signature
=============================

.. c:function:: void rdma_rw_ctx_destroy_signature(struct rdma_rw_ctx *ctx, struct ib_qp *qp, u8 port_num, struct scatterlist *sg, u32 sg_cnt, struct scatterlist *prot_sg, u32 prot_sg_cnt, enum dma_data_direction dir)

    release all resources allocated by rdma_rw_ctx_init_signature

    :param struct rdma_rw_ctx \*ctx:
        context to release

    :param struct ib_qp \*qp:
        queue pair to operate on

    :param u8 port_num:
        port num to which the connection is bound

    :param struct scatterlist \*sg:
        scatterlist that was used for the READ/WRITE

    :param u32 sg_cnt:
        number of entries in \ ``sg``\ 

    :param struct scatterlist \*prot_sg:
        scatterlist that was used for the READ/WRITE of the PI

    :param u32 prot_sg_cnt:
        number of entries in \ ``prot_sg``\ 

    :param enum dma_data_direction dir:
        %DMA_TO_DEVICE for RDMA WRITE, \ ``DMA_FROM_DEVICE``\  for RDMA READ

.. _`rdma_rw_mr_factor`:

rdma_rw_mr_factor
=================

.. c:function:: unsigned int rdma_rw_mr_factor(struct ib_device *device, u8 port_num, unsigned int maxpages)

    return number of MRs required for a payload

    :param struct ib_device \*device:
        device handling the connection

    :param u8 port_num:
        port num to which the connection is bound

    :param unsigned int maxpages:
        maximum payload pages per rdma_rw_ctx

.. _`rdma_rw_mr_factor.description`:

Description
-----------

Returns the number of MRs the device requires to move \ ``maxpayload``\ 
bytes. The returned value is used during transport creation to
compute max_rdma_ctxts and the size of the transport's Send and
Send Completion Queues.

.. This file was automatic generated / don't edit.

