.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/svc_rdma_recvfrom.c

.. _`svc_rdma_recv_ctxts_destroy`:

svc_rdma_recv_ctxts_destroy
===========================

.. c:function:: void svc_rdma_recv_ctxts_destroy(struct svcxprt_rdma *rdma)

    Release all recv_ctxt's for an xprt

    :param struct svcxprt_rdma \*rdma:
        svcxprt_rdma being torn down

.. _`svc_rdma_recv_ctxt_put`:

svc_rdma_recv_ctxt_put
======================

.. c:function:: void svc_rdma_recv_ctxt_put(struct svcxprt_rdma *rdma, struct svc_rdma_recv_ctxt *ctxt)

    Return recv_ctxt to free list

    :param struct svcxprt_rdma \*rdma:
        controlling svcxprt_rdma

    :param struct svc_rdma_recv_ctxt \*ctxt:
        object to return to the free list

.. _`svc_rdma_post_recvs`:

svc_rdma_post_recvs
===================

.. c:function:: bool svc_rdma_post_recvs(struct svcxprt_rdma *rdma)

    Post initial set of Recv WRs

    :param struct svcxprt_rdma \*rdma:
        fresh svcxprt_rdma

.. _`svc_rdma_post_recvs.description`:

Description
-----------

Returns true if successful, otherwise false.

.. _`svc_rdma_wc_receive`:

svc_rdma_wc_receive
===================

.. c:function:: void svc_rdma_wc_receive(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled Receive WC

    :param struct ib_cq \*cq:
        Completion Queue context

    :param struct ib_wc \*wc:
        Work Completion object

.. _`svc_rdma_wc_receive.description`:

Description
-----------

NB: The svc_xprt/svcxprt_rdma is pinned whenever it's possible that
the Receive completion handler could be running.

.. _`svc_rdma_flush_recv_queues`:

svc_rdma_flush_recv_queues
==========================

.. c:function:: void svc_rdma_flush_recv_queues(struct svcxprt_rdma *rdma)

    Drain pending Receive work

    :param struct svcxprt_rdma \*rdma:
        svcxprt_rdma being shut down

.. _`svc_rdma_recvfrom`:

svc_rdma_recvfrom
=================

.. c:function:: int svc_rdma_recvfrom(struct svc_rqst *rqstp)

    Receive an RPC call

    :param struct svc_rqst \*rqstp:
        request structure into which to receive an RPC Call

.. _`svc_rdma_recvfrom.return`:

Return
------

The positive number of bytes in the RPC Call message,
\ ``0``\  if there were no Calls ready to return,
\ ``-EINVAL``\  if the Read chunk data is too large,
\ ``-ENOMEM``\  if rdma_rw context pool was exhausted,
\ ``-ENOTCONN``\  if posting failed (connection is lost),
\ ``-EIO``\  if rdma_rw initialization failed (DMA mapping, etc).

Called in a loop when XPT_DATA is set. XPT_DATA is cleared only
when there are no remaining ctxt's to process.

The next ctxt is removed from the "receive" lists.

- If the ctxt completes a Read, then finish assembling the Call
message and return the number of bytes in the message.

- If the ctxt completes a Receive, then construct the Call
message from the contents of the Receive buffer.

- If there are no Read chunks in this message, then finish
assembling the Call message and return the number of bytes
in the message.

- If there are Read chunks in this message, post Read WRs to
pull that payload and return 0.

.. This file was automatic generated / don't edit.

