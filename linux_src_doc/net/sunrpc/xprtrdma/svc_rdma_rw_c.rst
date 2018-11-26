.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/svc_rdma_rw.c

.. _`svc_rdma_destroy_rw_ctxts`:

svc_rdma_destroy_rw_ctxts
=========================

.. c:function:: void svc_rdma_destroy_rw_ctxts(struct svcxprt_rdma *rdma)

    Free accumulated R/W contexts

    :param rdma:
        transport about to be destroyed
    :type rdma: struct svcxprt_rdma \*

.. _`svc_rdma_write_done`:

svc_rdma_write_done
===================

.. c:function:: void svc_rdma_write_done(struct ib_cq *cq, struct ib_wc *wc)

    Write chunk completion

    :param cq:
        controlling Completion Queue
    :type cq: struct ib_cq \*

    :param wc:
        Work Completion
    :type wc: struct ib_wc \*

.. _`svc_rdma_write_done.description`:

Description
-----------

Pages under I/O are freed by a subsequent Send completion.

.. _`svc_rdma_wc_read_done`:

svc_rdma_wc_read_done
=====================

.. c:function:: void svc_rdma_wc_read_done(struct ib_cq *cq, struct ib_wc *wc)

    Handle completion of an RDMA Read ctx

    :param cq:
        controlling Completion Queue
    :type cq: struct ib_cq \*

    :param wc:
        Work Completion
    :type wc: struct ib_wc \*

.. _`svc_rdma_send_write_chunk`:

svc_rdma_send_write_chunk
=========================

.. c:function:: int svc_rdma_send_write_chunk(struct svcxprt_rdma *rdma, __be32 *wr_ch, struct xdr_buf *xdr)

    Write all segments in a Write chunk

    :param rdma:
        controlling RDMA transport
    :type rdma: struct svcxprt_rdma \*

    :param wr_ch:
        Write chunk provided by client
    :type wr_ch: __be32 \*

    :param xdr:
        xdr_buf containing the data payload
    :type xdr: struct xdr_buf \*

.. _`svc_rdma_send_write_chunk.description`:

Description
-----------

Returns a non-negative number of bytes the chunk consumed, or
\ ``-E2BIG``\  if the payload was larger than the Write chunk,
\ ``-EINVAL``\  if client provided too many segments,
\ ``-ENOMEM``\  if rdma_rw context pool was exhausted,
\ ``-ENOTCONN``\  if posting failed (connection is lost),
\ ``-EIO``\  if rdma_rw initialization failed (DMA mapping, etc).

.. _`svc_rdma_send_reply_chunk`:

svc_rdma_send_reply_chunk
=========================

.. c:function:: int svc_rdma_send_reply_chunk(struct svcxprt_rdma *rdma, __be32 *rp_ch, bool writelist, struct xdr_buf *xdr)

    Write all segments in the Reply chunk

    :param rdma:
        controlling RDMA transport
    :type rdma: struct svcxprt_rdma \*

    :param rp_ch:
        Reply chunk provided by client
    :type rp_ch: __be32 \*

    :param writelist:
        true if client provided a Write list
    :type writelist: bool

    :param xdr:
        xdr_buf containing an RPC Reply
    :type xdr: struct xdr_buf \*

.. _`svc_rdma_send_reply_chunk.description`:

Description
-----------

Returns a non-negative number of bytes the chunk consumed, or
\ ``-E2BIG``\  if the payload was larger than the Reply chunk,
\ ``-EINVAL``\  if client provided too many segments,
\ ``-ENOMEM``\  if rdma_rw context pool was exhausted,
\ ``-ENOTCONN``\  if posting failed (connection is lost),
\ ``-EIO``\  if rdma_rw initialization failed (DMA mapping, etc).

.. _`svc_rdma_recv_read_chunk`:

svc_rdma_recv_read_chunk
========================

.. c:function:: int svc_rdma_recv_read_chunk(struct svcxprt_rdma *rdma, struct svc_rqst *rqstp, struct svc_rdma_recv_ctxt *head, __be32 *p)

    Pull a Read chunk from the client

    :param rdma:
        controlling RDMA transport
    :type rdma: struct svcxprt_rdma \*

    :param rqstp:
        set of pages to use as Read sink buffers
    :type rqstp: struct svc_rqst \*

    :param head:
        pages under I/O collect here
    :type head: struct svc_rdma_recv_ctxt \*

    :param p:
        pointer to start of Read chunk
    :type p: __be32 \*

.. _`svc_rdma_recv_read_chunk.return`:

Return
------

\ ``0``\  if all needed RDMA Reads were posted successfully,
\ ``-EINVAL``\  if client provided too many segments,
\ ``-ENOMEM``\  if rdma_rw context pool was exhausted,
\ ``-ENOTCONN``\  if posting failed (connection is lost),
\ ``-EIO``\  if rdma_rw initialization failed (DMA mapping, etc).

.. _`svc_rdma_recv_read_chunk.assumptions`:

Assumptions
-----------

- All Read segments in \ ``p``\  have the same Position value.

.. This file was automatic generated / don't edit.

