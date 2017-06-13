.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/svc_rdma_rw.c

.. _`svc_rdma_destroy_rw_ctxts`:

svc_rdma_destroy_rw_ctxts
=========================

.. c:function:: void svc_rdma_destroy_rw_ctxts(struct svcxprt_rdma *rdma)

    Free accumulated R/W contexts

    :param struct svcxprt_rdma \*rdma:
        transport about to be destroyed

.. _`svc_rdma_write_done`:

svc_rdma_write_done
===================

.. c:function:: void svc_rdma_write_done(struct ib_cq *cq, struct ib_wc *wc)

    Write chunk completion

    :param struct ib_cq \*cq:
        controlling Completion Queue

    :param struct ib_wc \*wc:
        Work Completion

.. _`svc_rdma_write_done.description`:

Description
-----------

Pages under I/O are freed by a subsequent Send completion.

.. _`svc_rdma_send_write_chunk`:

svc_rdma_send_write_chunk
=========================

.. c:function:: int svc_rdma_send_write_chunk(struct svcxprt_rdma *rdma, __be32 *wr_ch, struct xdr_buf *xdr)

    Write all segments in a Write chunk

    :param struct svcxprt_rdma \*rdma:
        controlling RDMA transport

    :param __be32 \*wr_ch:
        Write chunk provided by client

    :param struct xdr_buf \*xdr:
        xdr_buf containing the data payload

.. _`svc_rdma_send_write_chunk.description`:

Description
-----------

Returns a non-negative number of bytes the chunk consumed, or
\ ``-E2BIG``\  if the payload was larger than the Write chunk,
\ ``-ENOMEM``\  if rdma_rw context pool was exhausted,
\ ``-ENOTCONN``\  if posting failed (connection is lost),
\ ``-EIO``\  if rdma_rw initialization failed (DMA mapping, etc).

.. _`svc_rdma_send_reply_chunk`:

svc_rdma_send_reply_chunk
=========================

.. c:function:: int svc_rdma_send_reply_chunk(struct svcxprt_rdma *rdma, __be32 *rp_ch, bool writelist, struct xdr_buf *xdr)

    Write all segments in the Reply chunk

    :param struct svcxprt_rdma \*rdma:
        controlling RDMA transport

    :param __be32 \*rp_ch:
        Reply chunk provided by client

    :param bool writelist:
        true if client provided a Write list

    :param struct xdr_buf \*xdr:
        xdr_buf containing an RPC Reply

.. _`svc_rdma_send_reply_chunk.description`:

Description
-----------

Returns a non-negative number of bytes the chunk consumed, or
\ ``-E2BIG``\  if the payload was larger than the Reply chunk,
\ ``-ENOMEM``\  if rdma_rw context pool was exhausted,
\ ``-ENOTCONN``\  if posting failed (connection is lost),
\ ``-EIO``\  if rdma_rw initialization failed (DMA mapping, etc).

.. This file was automatic generated / don't edit.

