.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/verbs.c

.. _`rpcrdma_disconnect_worker`:

rpcrdma_disconnect_worker
=========================

.. c:function:: void rpcrdma_disconnect_worker(struct work_struct *work)

    Force a disconnect

    :param work:
        endpoint to be disconnected
    :type work: struct work_struct \*

.. _`rpcrdma_disconnect_worker.description`:

Description
-----------

Provider callbacks can possibly run in an IRQ context. This function
is invoked in a worker thread to guarantee that disconnect wake-up
calls are always done in process context.

.. _`rpcrdma_qp_event_handler`:

rpcrdma_qp_event_handler
========================

.. c:function:: void rpcrdma_qp_event_handler(struct ib_event *event, void *context)

    Handle one QP event (error notification)

    :param event:
        details of the event
    :type event: struct ib_event \*

    :param context:
        ep that owns QP where event occurred
    :type context: void \*

.. _`rpcrdma_qp_event_handler.description`:

Description
-----------

Called from the RDMA provider (device driver) possibly in an interrupt
context.

.. _`rpcrdma_wc_send`:

rpcrdma_wc_send
===============

.. c:function:: void rpcrdma_wc_send(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled Send WC

    :param cq:
        completion queue (ignored)
    :type cq: struct ib_cq \*

    :param wc:
        completed WR
    :type wc: struct ib_wc \*

.. _`rpcrdma_wc_receive`:

rpcrdma_wc_receive
==================

.. c:function:: void rpcrdma_wc_receive(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled Receive WC

    :param cq:
        completion queue (ignored)
    :type cq: struct ib_cq \*

    :param wc:
        completed WR
    :type wc: struct ib_wc \*

.. _`rpcrdma_cm_event_handler`:

rpcrdma_cm_event_handler
========================

.. c:function:: int rpcrdma_cm_event_handler(struct rdma_cm_id *id, struct rdma_cm_event *event)

    Handle RDMA CM events

    :param id:
        rdma_cm_id on which an event has occurred
    :type id: struct rdma_cm_id \*

    :param event:
        details of the event
    :type event: struct rdma_cm_event \*

.. _`rpcrdma_cm_event_handler.description`:

Description
-----------

Called with \ ``id``\ 's mutex held. Returns 1 if caller should
destroy \ ``id``\ , otherwise 0.

.. _`rpcrdma_ia_open`:

rpcrdma_ia_open
===============

.. c:function:: int rpcrdma_ia_open(struct rpcrdma_xprt *xprt)

    Open and initialize an Interface Adapter.

    :param xprt:
        transport with IA to (re)initialize
    :type xprt: struct rpcrdma_xprt \*

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

    :param ia:
        interface adapter being removed
    :type ia: struct rpcrdma_ia \*

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

    :param ia:
        interface adapter to close
    :type ia: struct rpcrdma_ia \*

.. _`rpcrdma_sendctx_get_locked`:

rpcrdma_sendctx_get_locked
==========================

.. c:function:: struct rpcrdma_sendctx *rpcrdma_sendctx_get_locked(struct rpcrdma_buffer *buf)

    Acquire a send context

    :param buf:
        transport buffers from which to acquire an unused context
    :type buf: struct rpcrdma_buffer \*

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

    :param sc:
        send context to release
    :type sc: struct rpcrdma_sendctx \*

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

    :param r_xprt:
        controlling transport
    :type r_xprt: struct rpcrdma_xprt \*

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

    :param mr:
        object to release
    :type mr: struct rpcrdma_mr \*

.. _`rpcrdma_mr_unmap_and_put`:

rpcrdma_mr_unmap_and_put
========================

.. c:function:: void rpcrdma_mr_unmap_and_put(struct rpcrdma_mr *mr)

    DMA unmap an MR and release it

    :param mr:
        object to release
    :type mr: struct rpcrdma_mr \*

.. _`rpcrdma_buffer_get`:

rpcrdma_buffer_get
==================

.. c:function:: struct rpcrdma_req *rpcrdma_buffer_get(struct rpcrdma_buffer *buffers)

    Get a request buffer

    :param buffers:
        Buffer pool from which to obtain a buffer
    :type buffers: struct rpcrdma_buffer \*

.. _`rpcrdma_buffer_get.description`:

Description
-----------

Returns a fresh rpcrdma_req, or NULL if none are available.

.. _`rpcrdma_buffer_put`:

rpcrdma_buffer_put
==================

.. c:function:: void rpcrdma_buffer_put(struct rpcrdma_req *req)

    Put request/reply buffers back into pool

    :param req:
        object to return
    :type req: struct rpcrdma_req \*

.. _`rpcrdma_alloc_regbuf`:

rpcrdma_alloc_regbuf
====================

.. c:function:: struct rpcrdma_regbuf *rpcrdma_alloc_regbuf(size_t size, enum dma_data_direction direction, gfp_t flags)

    allocate and DMA-map memory for SEND/RECV buffers

    :param size:
        size of buffer to be allocated, in bytes
    :type size: size_t

    :param direction:
        direction of data movement
    :type direction: enum dma_data_direction

    :param flags:
        GFP flags
    :type flags: gfp_t

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

    :param ia:
        controlling rpcrdma_ia
    :type ia: struct rpcrdma_ia \*

    :param rb:
        regbuf to be mapped
    :type rb: struct rpcrdma_regbuf \*

.. _`rpcrdma_free_regbuf`:

rpcrdma_free_regbuf
===================

.. c:function:: void rpcrdma_free_regbuf(struct rpcrdma_regbuf *rb)

    deregister and free registered buffer

    :param rb:
        regbuf to be deregistered and freed
    :type rb: struct rpcrdma_regbuf \*

.. _`rpcrdma_post_recvs`:

rpcrdma_post_recvs
==================

.. c:function:: void rpcrdma_post_recvs(struct rpcrdma_xprt *r_xprt, bool temp)

    Maybe post some Receive buffers

    :param r_xprt:
        controlling transport
    :type r_xprt: struct rpcrdma_xprt \*

    :param temp:
        when true, allocate temp rpcrdma_rep objects
    :type temp: bool

.. This file was automatic generated / don't edit.

