.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/transport.c

.. _`xprt_rdma_connect_worker`:

xprt_rdma_connect_worker
========================

.. c:function:: void xprt_rdma_connect_worker(struct work_struct *work)

    establish connection in the background

    :param work:
        worker thread context
    :type work: struct work_struct \*

.. _`xprt_rdma_connect_worker.description`:

Description
-----------

Requester holds the xprt's send lock to prevent activity on this
transport while a fresh connection is being established. RPC tasks
sleep on the xprt's pending queue waiting for connect to complete.

.. _`xprt_rdma_inject_disconnect`:

xprt_rdma_inject_disconnect
===========================

.. c:function:: void xprt_rdma_inject_disconnect(struct rpc_xprt *xprt)

    inject a connection fault

    :param xprt:
        transport context
    :type xprt: struct rpc_xprt \*

.. _`xprt_rdma_inject_disconnect.description`:

Description
-----------

If \ ``xprt``\  is connected, disconnect it to simulate spurious connection
loss.

.. _`xprt_rdma_destroy`:

xprt_rdma_destroy
=================

.. c:function:: void xprt_rdma_destroy(struct rpc_xprt *xprt)

    Full tear down of transport

    :param xprt:
        doomed transport context
    :type xprt: struct rpc_xprt \*

.. _`xprt_rdma_destroy.description`:

Description
-----------

Caller guarantees there will be no more calls to us with
this \ ``xprt``\ .

.. _`xprt_setup_rdma`:

xprt_setup_rdma
===============

.. c:function:: struct rpc_xprt *xprt_setup_rdma(struct xprt_create *args)

    Set up transport to use RDMA

    :param args:
        rpc transport arguments
    :type args: struct xprt_create \*

.. _`xprt_rdma_close`:

xprt_rdma_close
===============

.. c:function:: void xprt_rdma_close(struct rpc_xprt *xprt)

    close a transport connection

    :param xprt:
        transport context
    :type xprt: struct rpc_xprt \*

.. _`xprt_rdma_close.description`:

Description
-----------

Called during transport shutdown, reconnect, or device removal.
Caller holds \ ``xprt``\ 's send lock to prevent activity on this
transport while the connection is torn down.

.. _`xprt_rdma_set_port`:

xprt_rdma_set_port
==================

.. c:function:: void xprt_rdma_set_port(struct rpc_xprt *xprt, u16 port)

    update server port with rpcbind result

    :param xprt:
        controlling RPC transport
    :type xprt: struct rpc_xprt \*

    :param port:
        new port value
    :type port: u16

.. _`xprt_rdma_set_port.description`:

Description
-----------

Transport connect status is unchanged.

.. _`xprt_rdma_timer`:

xprt_rdma_timer
===============

.. c:function:: void xprt_rdma_timer(struct rpc_xprt *xprt, struct rpc_task *task)

    invoked when an RPC times out

    :param xprt:
        controlling RPC transport
    :type xprt: struct rpc_xprt \*

    :param task:
        RPC task that timed out
    :type task: struct rpc_task \*

.. _`xprt_rdma_timer.description`:

Description
-----------

Invoked when the transport is still connected, but an RPC
retransmit timeout occurs.

Since RDMA connections don't have a keep-alive, forcibly
disconnect and retry to connect. This drives full
detection of the network path, and retransmissions of
all pending RPCs.

.. _`xprt_rdma_connect`:

xprt_rdma_connect
=================

.. c:function:: void xprt_rdma_connect(struct rpc_xprt *xprt, struct rpc_task *task)

    try to establish a transport connection

    :param xprt:
        transport state
    :type xprt: struct rpc_xprt \*

    :param task:
        RPC scheduler context
    :type task: struct rpc_task \*

.. _`xprt_rdma_alloc_slot`:

xprt_rdma_alloc_slot
====================

.. c:function:: void xprt_rdma_alloc_slot(struct rpc_xprt *xprt, struct rpc_task *task)

    allocate an rpc_rqst

    :param xprt:
        controlling RPC transport
    :type xprt: struct rpc_xprt \*

    :param task:
        RPC task requesting a fresh rpc_rqst
    :type task: struct rpc_task \*

.. _`xprt_rdma_alloc_slot.tk_status-values`:

tk_status values
----------------

\ ``0``\  if task->tk_rqstp points to a fresh rpc_rqst
\ ``-EAGAIN``\  if no rpc_rqst is available; queued on backlog

.. _`xprt_rdma_free_slot`:

xprt_rdma_free_slot
===================

.. c:function:: void xprt_rdma_free_slot(struct rpc_xprt *xprt, struct rpc_rqst *rqst)

    release an rpc_rqst

    :param xprt:
        controlling RPC transport
    :type xprt: struct rpc_xprt \*

    :param rqst:
        rpc_rqst to release
    :type rqst: struct rpc_rqst \*

.. _`xprt_rdma_allocate`:

xprt_rdma_allocate
==================

.. c:function:: int xprt_rdma_allocate(struct rpc_task *task)

    allocate transport resources for an RPC

    :param task:
        RPC task
    :type task: struct rpc_task \*

.. _`xprt_rdma_allocate.return-values`:

Return values
-------------

0:    Success; rq_buffer points to RPC buffer to use

.. _`xprt_rdma_allocate.enomem`:

ENOMEM
------

Out of memory, call again later

.. _`xprt_rdma_allocate.eio`:

EIO
---

A permanent error occurred, do not retry

.. _`xprt_rdma_free`:

xprt_rdma_free
==============

.. c:function:: void xprt_rdma_free(struct rpc_task *task)

    release resources allocated by xprt_rdma_allocate

    :param task:
        RPC task
    :type task: struct rpc_task \*

.. _`xprt_rdma_free.description`:

Description
-----------

Caller guarantees rqst->rq_buffer is non-NULL.

.. _`xprt_rdma_send_request`:

xprt_rdma_send_request
======================

.. c:function:: int xprt_rdma_send_request(struct rpc_rqst *rqst)

    marshal and send an RPC request

    :param rqst:
        RPC message in rq_snd_buf
    :type rqst: struct rpc_rqst \*

.. _`xprt_rdma_send_request.description`:

Description
-----------

Caller holds the transport's write lock.

.. _`xprt_rdma_send_request.return`:

Return
------

\ ``0``\  if the RPC message has been sent
\ ``-ENOTCONN``\  if the caller should reconnect and call again
\ ``-EAGAIN``\  if the caller should call again
\ ``-ENOBUFS``\  if the caller should call again after a delay
\ ``-EIO``\  if a permanent error occurred and the request was not
sent. Do not try to send this message again.

.. This file was automatic generated / don't edit.

