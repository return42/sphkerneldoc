.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/rpc_rdma.c

.. _`rpcrdma_unmap_sendctx`:

rpcrdma_unmap_sendctx
=====================

.. c:function:: void rpcrdma_unmap_sendctx(struct rpcrdma_sendctx *sc)

    DMA-unmap Send buffers

    :param sc:
        sendctx containing SGEs to unmap
    :type sc: struct rpcrdma_sendctx \*

.. _`rpcrdma_prepare_send_sges`:

rpcrdma_prepare_send_sges
=========================

.. c:function:: int rpcrdma_prepare_send_sges(struct rpcrdma_xprt *r_xprt, struct rpcrdma_req *req, u32 hdrlen, struct xdr_buf *xdr, enum rpcrdma_chunktype rtype)

    Construct SGEs for a Send WR

    :param r_xprt:
        controlling transport
    :type r_xprt: struct rpcrdma_xprt \*

    :param req:
        context of RPC Call being marshalled
    :type req: struct rpcrdma_req \*

    :param hdrlen:
        size of transport header, in bytes
    :type hdrlen: u32

    :param xdr:
        xdr_buf containing RPC Call
    :type xdr: struct xdr_buf \*

    :param rtype:
        chunk type being encoded
    :type rtype: enum rpcrdma_chunktype

.. _`rpcrdma_prepare_send_sges.description`:

Description
-----------

Returns 0 on success; otherwise a negative errno is returned.

.. _`rpcrdma_marshal_req`:

rpcrdma_marshal_req
===================

.. c:function:: int rpcrdma_marshal_req(struct rpcrdma_xprt *r_xprt, struct rpc_rqst *rqst)

    Marshal and send one RPC request

    :param r_xprt:
        controlling transport
    :type r_xprt: struct rpcrdma_xprt \*

    :param rqst:
        RPC request to be marshaled
    :type rqst: struct rpc_rqst \*

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
\ ``-EAGAIN``\  if the caller should call again with the same arguments,
\ ``-ENOBUFS``\  if the caller should call again after a delay,
\ ``-EMSGSIZE``\  if the transport header is too small,
\ ``-EIO``\  if a permanent problem occurred while marshaling.

.. _`rpcrdma_inline_fixup`:

rpcrdma_inline_fixup
====================

.. c:function:: unsigned long rpcrdma_inline_fixup(struct rpc_rqst *rqst, char *srcp, int copy_len, int pad)

    Scatter inline received data into rqst's iovecs

    :param rqst:
        controlling RPC request
    :type rqst: struct rpc_rqst \*

    :param srcp:
        points to RPC message payload in receive buffer
    :type srcp: char \*

    :param copy_len:
        remaining length of receive buffer content
    :type copy_len: int

    :param pad:
        Write chunk pad bytes needed (zero for pure inline)
    :type pad: int

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

