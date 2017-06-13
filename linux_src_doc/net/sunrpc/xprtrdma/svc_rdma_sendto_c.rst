.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/svc_rdma_sendto.c

.. _`svc_rdma_map_reply_hdr`:

svc_rdma_map_reply_hdr
======================

.. c:function:: int svc_rdma_map_reply_hdr(struct svcxprt_rdma *rdma, struct svc_rdma_op_ctxt *ctxt, __be32 *rdma_resp, unsigned int len)

    DMA map the transport header buffer

    :param struct svcxprt_rdma \*rdma:
        controlling transport

    :param struct svc_rdma_op_ctxt \*ctxt:
        op_ctxt for the Send WR

    :param __be32 \*rdma_resp:
        buffer containing transport header

    :param unsigned int len:
        length of transport header

.. _`svc_rdma_map_reply_hdr.return`:

Return
------

%0 if the header is DMA mapped,
\ ``-EIO``\  if DMA mapping failed.

.. _`svc_rdma_post_send_wr`:

svc_rdma_post_send_wr
=====================

.. c:function:: int svc_rdma_post_send_wr(struct svcxprt_rdma *rdma, struct svc_rdma_op_ctxt *ctxt, int num_sge, u32 inv_rkey)

    Set up and post one Send Work Request

    :param struct svcxprt_rdma \*rdma:
        controlling transport

    :param struct svc_rdma_op_ctxt \*ctxt:
        op_ctxt for transmitting the Send WR

    :param int num_sge:
        number of SGEs to send

    :param u32 inv_rkey:
        R_key argument to Send With Invalidate, or zero

.. _`svc_rdma_post_send_wr.return`:

Return
------

%0 if the Send\* was posted successfully,
\ ``-ENOTCONN``\  if the connection was lost or dropped,
\ ``-EINVAL``\  if there was a problem with the Send we built,
\ ``-ENOMEM``\  if ib_post_send failed.

.. _`svc_rdma_sendto`:

svc_rdma_sendto
===============

.. c:function:: int svc_rdma_sendto(struct svc_rqst *rqstp)

    Transmit an RPC reply

    :param struct svc_rqst \*rqstp:
        processed RPC request, reply XDR already in ::rq_res

.. _`svc_rdma_sendto.description`:

Description
-----------

Any resources still associated with \ ``rqstp``\  are released upon return.
If no reply message was possible, the connection is closed.

.. _`svc_rdma_sendto.return`:

Return
------

%0 if an RPC reply has been successfully posted,
\ ``-ENOMEM``\  if a resource shortage occurred (connection is lost),
\ ``-ENOTCONN``\  if posting failed (connection is lost).

.. This file was automatic generated / don't edit.

