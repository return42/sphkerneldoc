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

.. _`rpcrdma_wc_receive`:

rpcrdma_wc_receive
==================

.. c:function:: void rpcrdma_wc_receive(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled Receive WC

    :param struct ib_cq \*cq:
        completion queue (ignored)

    :param struct ib_wc \*wc:
        completed WR

.. _`rpcrdma_ia_open`:

rpcrdma_ia_open
===============

.. c:function:: int rpcrdma_ia_open(struct rpcrdma_xprt *xprt, struct sockaddr *addr)

    Open and initialize an Interface Adapter.

    :param struct rpcrdma_xprt \*xprt:
        controlling transport

    :param struct sockaddr \*addr:
        IP address of remote peer

.. _`rpcrdma_ia_open.description`:

Description
-----------

Returns 0 on success, negative errno if an appropriate
Interface Adapter could not be found and opened.

.. _`rpcrdma_ia_remove`:

rpcrdma_ia_remove
=================

.. c:function:: void rpcrdma_ia_remove(struct rpcrdma_ia *ia)

    Handle device driver unload

    :param struct rpcrdma_ia \*ia:
        interface adapter being removed

.. _`rpcrdma_ia_remove.description`:

Description
-----------

Divest transport H/W resources associated with this adapter,
but allow it to be restored later.

.. _`rpcrdma_ia_close`:

rpcrdma_ia_close
================

.. c:function:: void rpcrdma_ia_close(struct rpcrdma_ia *ia)

    Clean up/close an IA.

    :param struct rpcrdma_ia \*ia:
        interface adapter to close

.. _`rpcrdma_alloc_regbuf`:

rpcrdma_alloc_regbuf
====================

.. c:function:: struct rpcrdma_regbuf *rpcrdma_alloc_regbuf(size_t size, enum dma_data_direction direction, gfp_t flags)

    allocate and DMA-map memory for SEND/RECV buffers

    :param size_t size:
        size of buffer to be allocated, in bytes

    :param enum dma_data_direction direction:
        direction of data movement

    :param gfp_t flags:
        GFP flags

.. _`rpcrdma_alloc_regbuf.description`:

Description
-----------

Returns an ERR_PTR, or a pointer to a regbuf, a buffer that
can be persistently DMA-mapped for I/O.

xprtrdma uses a regbuf for posting an outgoing RDMA SEND, or for
receiving the payload of RDMA RECV operations. During Long Calls
or Replies they may be registered externally via ro_map.

.. _`__rpcrdma_dma_map_regbuf`:

__rpcrdma_dma_map_regbuf
========================

.. c:function:: bool __rpcrdma_dma_map_regbuf(struct rpcrdma_ia *ia, struct rpcrdma_regbuf *rb)

    DMA-map a regbuf

    :param struct rpcrdma_ia \*ia:
        controlling rpcrdma_ia

    :param struct rpcrdma_regbuf \*rb:
        regbuf to be mapped

.. _`rpcrdma_free_regbuf`:

rpcrdma_free_regbuf
===================

.. c:function:: void rpcrdma_free_regbuf(struct rpcrdma_regbuf *rb)

    deregister and free registered buffer

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

