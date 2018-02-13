.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/svc_rdma_backchannel.c

.. _`svc_rdma_handle_bc_reply`:

svc_rdma_handle_bc_reply
========================

.. c:function:: int svc_rdma_handle_bc_reply(struct rpc_xprt *xprt, __be32 *rdma_resp, struct xdr_buf *rcvbuf)

    Process incoming backchannel reply

    :param struct rpc_xprt \*xprt:
        controlling backchannel transport

    :param __be32 \*rdma_resp:
        pointer to incoming transport header

    :param struct xdr_buf \*rcvbuf:
        XDR buffer into which to decode the reply

.. _`svc_rdma_handle_bc_reply.return`:

Return
------

\ ``0``\  if \ ``rcvbuf``\  is filled in, xprt_complete_rqst called,
\ ``-EAGAIN``\  if server should call ->recvfrom again.

.. This file was automatic generated / don't edit.

