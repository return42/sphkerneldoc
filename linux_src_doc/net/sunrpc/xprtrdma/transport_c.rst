.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/transport.c

.. _`xprt_setup_rdma`:

xprt_setup_rdma
===============

.. c:function:: struct rpc_xprt *xprt_setup_rdma(struct xprt_create *args)

    Set up transport to use RDMA

    :param struct xprt_create \*args:
        rpc transport arguments

.. _`xprt_rdma_close`:

xprt_rdma_close
===============

.. c:function:: void xprt_rdma_close(struct rpc_xprt *xprt)

    Close down RDMA connection

    :param struct rpc_xprt \*xprt:
        generic transport to be closed

.. _`xprt_rdma_close.description`:

Description
-----------

Called during transport shutdown reconnect, or device
removal. Caller holds the transport's write lock.

.. _`xprt_rdma_set_port`:

xprt_rdma_set_port
==================

.. c:function:: void xprt_rdma_set_port(struct rpc_xprt *xprt, u16 port)

    update server port with rpcbind result

    :param struct rpc_xprt \*xprt:
        controlling RPC transport

    :param u16 port:
        new port value

.. _`xprt_rdma_set_port.description`:

Description
-----------

Transport connect status is unchanged.

.. _`xprt_rdma_timer`:

xprt_rdma_timer
===============

.. c:function:: void xprt_rdma_timer(struct rpc_xprt *xprt, struct rpc_task *task)

    invoked when an RPC times out

    :param struct rpc_xprt \*xprt:
        controlling RPC transport

    :param struct rpc_task \*task:
        RPC task that timed out

.. _`xprt_rdma_timer.description`:

Description
-----------

Invoked when the transport is still connected, but an RPC
retransmit timeout occurs.

Since RDMA connections don't have a keep-alive, forcibly
disconnect and retry to connect. This drives full
detection of the network path, and retransmissions of
all pending RPCs.

.. _`xprt_rdma_allocate`:

xprt_rdma_allocate
==================

.. c:function:: int xprt_rdma_allocate(struct rpc_task *task)

    allocate transport resources for an RPC

    :param struct rpc_task \*task:
        RPC task

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

The RDMA allocate/free functions need the task structure as a place
to hide the struct rpcrdma_req, which is necessary for the actual
send/recv sequence.

xprt_rdma_allocate provides buffers that are already mapped for
DMA, and a local DMA lkey is provided for each.

.. _`xprt_rdma_free`:

xprt_rdma_free
==============

.. c:function:: void xprt_rdma_free(struct rpc_task *task)

    release resources allocated by xprt_rdma_allocate

    :param struct rpc_task \*task:
        RPC task

.. _`xprt_rdma_free.description`:

Description
-----------

Caller guarantees rqst->rq_buffer is non-NULL.

.. _`xprt_rdma_send_request`:

xprt_rdma_send_request
======================

.. c:function:: int xprt_rdma_send_request(struct rpc_task *task)

    marshal and send an RPC request

    :param struct rpc_task \*task:
        RPC task with an RPC message in rq_snd_buf

.. _`xprt_rdma_send_request.description`:

Description
-----------

Caller holds the transport's write lock.

.. _`xprt_rdma_send_request.return`:

Return
------

\ ``0``\  if the RPC message has been sent
\ ``-ENOTCONN``\  if the caller should reconnect and call again
\ ``-ENOBUFS``\  if the caller should call again later
\ ``-EIO``\  if a permanent error occurred and the request was not
sent. Do not try to send this message again.

.. This file was automatic generated / don't edit.

