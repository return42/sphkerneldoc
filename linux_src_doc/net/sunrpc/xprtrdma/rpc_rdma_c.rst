.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/rpc_rdma.c

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

