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

.. c:function:: int rpcrdma_ia_open(struct rpcrdma_xprt *xprt)

    Open and initialize an Interface Adapter.

    :param struct rpcrdma_xprt \*xprt:
        transport with IA to (re)initialize

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

.. _`rpcrdma_sendctx_get_locked`:

rpcrdma_sendctx_get_locked
==========================

.. c:function:: struct rpcrdma_sendctx *rpcrdma_sendctx_get_locked(struct rpcrdma_buffer *buf)

    Acquire a send context

    :param struct rpcrdma_buffer \*buf:
        transport buffers from which to acquire an unused context

.. _`rpcrdma_sendctx_get_locked.description`:

Description
-----------

Returns pointer to a free send completion context; or NULL if
the queue is empty.

.. _`rpcrdma_sendctx_get_locked.usage`:

Usage
-----

Called to acquire an SGE array before preparing a Send WR.

The caller serializes calls to this function (per rpcrdma_buffer),
and provides an effective memory barrier that flushes the new value
of rb_sc_head.

.. _`rpcrdma_sendctx_put_locked`:

rpcrdma_sendctx_put_locked
==========================

.. c:function:: void rpcrdma_sendctx_put_locked(struct rpcrdma_sendctx *sc)

    Release a send context

    :param struct rpcrdma_sendctx \*sc:
        send context to release

.. _`rpcrdma_sendctx_put_locked.usage`:

Usage
-----

Called from Send completion to return a sendctxt
to the queue.

The caller serializes calls to this function (per rpcrdma_buffer).

.. _`rpcrdma_mr_get`:

rpcrdma_mr_get
==============

.. c:function:: struct rpcrdma_mr *rpcrdma_mr_get(struct rpcrdma_xprt *r_xprt)

    Allocate an rpcrdma_mr object

    :param struct rpcrdma_xprt \*r_xprt:
        controlling transport

.. _`rpcrdma_mr_get.description`:

Description
-----------

Returns an initialized rpcrdma_mr or NULL if no free
rpcrdma_mr objects are available.

.. _`rpcrdma_mr_put`:

rpcrdma_mr_put
==============

.. c:function:: void rpcrdma_mr_put(struct rpcrdma_mr *mr)

    Release an rpcrdma_mr object

    :param struct rpcrdma_mr \*mr:
        object to release

.. _`rpcrdma_mr_unmap_and_put`:

rpcrdma_mr_unmap_and_put
========================

.. c:function:: void rpcrdma_mr_unmap_and_put(struct rpcrdma_mr *mr)

    DMA unmap an MR and release it

    :param struct rpcrdma_mr \*mr:
        object to release

.. _`rpcrdma_buffer_get`:

rpcrdma_buffer_get
==================

.. c:function:: struct rpcrdma_req *rpcrdma_buffer_get(struct rpcrdma_buffer *buffers)

    Get a request buffer

    :param struct rpcrdma_buffer \*buffers:
        Buffer pool from which to obtain a buffer

.. _`rpcrdma_buffer_get.description`:

Description
-----------

Returns a fresh rpcrdma_req, or NULL if none are available.

.. _`rpcrdma_buffer_put`:

rpcrdma_buffer_put
==================

.. c:function:: void rpcrdma_buffer_put(struct rpcrdma_req *req)

    Put request/reply buffers back into pool

    :param struct rpcrdma_req \*req:
        object to return

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

\__rpcrdma_dma_map_regbuf
=========================

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

.. _`rpcrdma_post_recvs`:

rpcrdma_post_recvs
==================

.. c:function:: void rpcrdma_post_recvs(struct rpcrdma_xprt *r_xprt, bool temp)

    Maybe post some Receive buffers

    :param struct rpcrdma_xprt \*r_xprt:
        controlling transport

    :param bool temp:
        when true, allocate temp rpcrdma_rep objects

.. This file was automatic generated / don't edit.

