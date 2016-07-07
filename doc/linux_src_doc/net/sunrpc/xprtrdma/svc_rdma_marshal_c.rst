.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/svc_rdma_marshal.c

.. _`svc_rdma_xdr_decode_req`:

svc_rdma_xdr_decode_req
=======================

.. c:function:: int svc_rdma_xdr_decode_req(struct xdr_buf *rq_arg)

    Parse incoming RPC-over-RDMA header

    :param struct xdr_buf \*rq_arg:
        Receive buffer

.. _`svc_rdma_xdr_decode_req.description`:

Description
-----------

On entry, xdr->head[0].iov_base points to first byte in the
RPC-over-RDMA header.

On successful exit, head[0] points to first byte past the
RPC-over-RDMA header. For RDMA_MSG, this is the RPC message.
The length of the RPC-over-RDMA header is returned.

.. This file was automatic generated / don't edit.

