.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/rpc_rdma.c

.. _`rpcrdma_unmap_sendctx`:

rpcrdma_unmap_sendctx
=====================

.. c:function:: void rpcrdma_unmap_sendctx(struct rpcrdma_sendctx *sc)

    DMA-unmap Send buffers

    :param struct rpcrdma_sendctx \*sc:
        sendctx containing SGEs to unmap

.. _`rpcrdma_prepare_send_sges`:

rpcrdma_prepare_send_sges
=========================

.. c:function:: int rpcrdma_prepare_send_sges(struct rpcrdma_xprt *r_xprt, struct rpcrdma_req *req, u32 hdrlen, struct xdr_buf *xdr, enum rpcrdma_chunktype rtype)

    Construct SGEs for a Send WR

    :param struct rpcrdma_xprt \*r_xprt:
        controlling transport

    :param struct rpcrdma_req \*req:
        context of RPC Call being marshalled

    :param u32 hdrlen:
        size of transport header, in bytes

    :param struct xdr_buf \*xdr:
        xdr_buf containing RPC Call

    :param enum rpcrdma_chunktype rtype:
        chunk type being encoded

.. _`rpcrdma_prepare_send_sges.description`:

Description
-----------

Returns 0 on success; otherwise a negative errno is returned.

.. _`rpcrdma_marshal_req`:

rpcrdma_marshal_req
===================

.. c:function:: int rpcrdma_marshal_req(struct rpcrdma_xprt *r_xprt, struct rpc_rqst *rqst)

    Marshal and send one RPC request

    :param struct rpcrdma_xprt \*r_xprt:
        controlling transport

    :param struct rpc_rqst \*rqst:
        RPC request to be marshaled

.. _`rpcrdma_marshal_req.description`:

Description
-----------

For the RPC in "rqst", this function:
- Chooses the transfer mode (eg., RDMA_MSG or RDMA_NOMSG)
- Registers Read, Write, and Reply chunks
- Constructs the transport header
- Posts a Send WR to send the transport header and request

.. _`rpcrdma_marshal_req.return`:

Return
------

\ ``0``\  if the RPC was sent successfully,
\ ``-ENOTCONN``\  if the connection was lost,
\ ``-EAGAIN``\  if not enough pages are available for on-demand reply buffer,
\ ``-ENOBUFS``\  if no MRs are available to register chunks,
\ ``-EMSGSIZE``\  if the transport header is too small,
\ ``-EIO``\  if a permanent problem occurred while marshaling.

.. _`rpcrdma_inline_fixup`:

rpcrdma_inline_fixup
====================

.. c:function:: unsigned long rpcrdma_inline_fixup(struct rpc_rqst *rqst, char *srcp, int copy_len, int pad)

    Scatter inline received data into rqst's iovecs

    :param struct rpc_rqst \*rqst:
        controlling RPC request

    :param char \*srcp:
        points to RPC message payload in receive buffer

    :param int copy_len:
        remaining length of receive buffer content

    :param int pad:
        Write chunk pad bytes needed (zero for pure inline)

.. _`rpcrdma_inline_fixup.description`:

Description
-----------

The upper layer has set the maximum number of bytes it can
receive in each component of rq_rcv_buf. These values are set in
the head.iov_len, page_len, tail.iov_len, and buflen fields.

Unlike the TCP equivalent (xdr_partial_copy_from_skb), in
many cases this function simply updates iov_base pointers in
rq_rcv_buf to point directly to the received reply data, to
avoid copying reply data.

Returns the count of bytes which had to be memcopied.

.. This file was automatic generated / don't edit.

