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

.. _`xprt_rdma_send_request.return-values`:

Return values
-------------

0:    The request has been sent

.. _`xprt_rdma_send_request.enotconn`:

ENOTCONN
--------

Caller needs to invoke connect logic then call again

.. _`xprt_rdma_send_request.enobufs`:

ENOBUFS
-------

Call again later to send the request

.. _`xprt_rdma_send_request.eio`:

EIO
---

A permanent error occurred. The request was not sent,
and don't try it again

send_request invokes the meat of RPC RDMA. It must do the following:

1.  Marshal the RPC request into an RPC RDMA request, which means
putting a header in front of data, and creating IOVs for RDMA
from those in the request.
2.  In marshaling, detect opportunities for RDMA, and use them.
3.  Post a recv message to set up asynch completion, then send
the request (rpcrdma_ep_post).
4.  No partial sends are possible in the RPC-RDMA protocol (as in UDP).

.. This file was automatic generated / don't edit.

