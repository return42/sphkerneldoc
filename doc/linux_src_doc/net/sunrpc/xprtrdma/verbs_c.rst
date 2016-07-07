.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/verbs.c

.. _`rpcrdma_wc_send`:

rpcrdma_wc_send
===============

.. c:function:: void rpcrdma_wc_send(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled Send WC

    :param struct ib_cq \*cq:
        completion queue (ignored)

    :param struct ib_wc \*wc:
        completed WR

.. _`rpcrdma_receive_wc`:

rpcrdma_receive_wc
==================

.. c:function:: void rpcrdma_receive_wc(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled Receive WC

    :param struct ib_cq \*cq:
        completion queue (ignored)

    :param struct ib_wc \*wc:
        completed WR

.. _`rpcrdma_alloc_regbuf`:

rpcrdma_alloc_regbuf
====================

.. c:function:: struct rpcrdma_regbuf *rpcrdma_alloc_regbuf(struct rpcrdma_ia *ia, size_t size, gfp_t flags)

    kmalloc and register memory for SEND/RECV buffers

    :param struct rpcrdma_ia \*ia:
        controlling rpcrdma_ia

    :param size_t size:
        size of buffer to be allocated, in bytes

    :param gfp_t flags:
        GFP flags

.. _`rpcrdma_alloc_regbuf.description`:

Description
-----------

Returns pointer to private header of an area of internally
registered memory, or an ERR_PTR. The registered buffer follows
the end of the private header.

xprtrdma uses a regbuf for posting an outgoing RDMA SEND, or for
receiving the payload of RDMA RECV operations. regbufs are not
used for RDMA READ/WRITE operations, thus are registered only for
LOCAL access.

.. _`rpcrdma_free_regbuf`:

rpcrdma_free_regbuf
===================

.. c:function:: void rpcrdma_free_regbuf(struct rpcrdma_ia *ia, struct rpcrdma_regbuf *rb)

    deregister and free registered buffer

    :param struct rpcrdma_ia \*ia:
        controlling rpcrdma_ia

    :param struct rpcrdma_regbuf \*rb:
        regbuf to be deregistered and freed

.. _`rpcrdma_ep_post_extra_recv`:

rpcrdma_ep_post_extra_recv
==========================

.. c:function:: int rpcrdma_ep_post_extra_recv(struct rpcrdma_xprt *r_xprt, unsigned int count)

    Post buffers for incoming backchannel requests

    :param struct rpcrdma_xprt \*r_xprt:
        transport associated with these backchannel resources

    :param unsigned int count:
        *undescribed*

.. _`rpcrdma_ep_post_extra_recv.description`:

Description
-----------

Returns zero if all requested buffers were posted, or a negative errno.

.. This file was automatic generated / don't edit.

