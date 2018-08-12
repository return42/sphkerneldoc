.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/svc_rdma_sendto.c

.. _`svc_rdma_send_ctxts_destroy`:

svc_rdma_send_ctxts_destroy
===========================

.. c:function:: void svc_rdma_send_ctxts_destroy(struct svcxprt_rdma *rdma)

    Release all send_ctxt's for an xprt

    :param struct svcxprt_rdma \*rdma:
        svcxprt_rdma being torn down

.. _`svc_rdma_send_ctxt_get`:

svc_rdma_send_ctxt_get
======================

.. c:function:: struct svc_rdma_send_ctxt *svc_rdma_send_ctxt_get(struct svcxprt_rdma *rdma)

    Get a free send_ctxt

    :param struct svcxprt_rdma \*rdma:
        controlling svcxprt_rdma

.. _`svc_rdma_send_ctxt_get.description`:

Description
-----------

Returns a ready-to-use send_ctxt, or NULL if none are
available and a fresh one cannot be allocated.

.. _`svc_rdma_send_ctxt_put`:

svc_rdma_send_ctxt_put
======================

.. c:function:: void svc_rdma_send_ctxt_put(struct svcxprt_rdma *rdma, struct svc_rdma_send_ctxt *ctxt)

    Return send_ctxt to free list

    :param struct svcxprt_rdma \*rdma:
        controlling svcxprt_rdma

    :param struct svc_rdma_send_ctxt \*ctxt:
        object to return to the free list

.. _`svc_rdma_send_ctxt_put.description`:

Description
-----------

Pages left in sc_pages are DMA unmapped and released.

.. _`svc_rdma_wc_send`:

svc_rdma_wc_send
================

.. c:function:: void svc_rdma_wc_send(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled Send WC

    :param struct ib_cq \*cq:
        Completion Queue context

    :param struct ib_wc \*wc:
        Work Completion object

.. _`svc_rdma_wc_send.description`:

Description
-----------

NB: The svc_xprt/svcxprt_rdma is pinned whenever it's possible that
the Send completion handler could be running.

.. _`svc_rdma_send`:

svc_rdma_send
=============

.. c:function:: int svc_rdma_send(struct svcxprt_rdma *rdma, struct ib_send_wr *wr)

    Post a single Send WR

    :param struct svcxprt_rdma \*rdma:
        transport on which to post the WR

    :param struct ib_send_wr \*wr:
        prepared Send WR to post

.. _`svc_rdma_send.description`:

Description
-----------

Returns zero the Send WR was posted successfully. Otherwise, a
negative errno is returned.

.. _`svc_rdma_sync_reply_hdr`:

svc_rdma_sync_reply_hdr
=======================

.. c:function:: void svc_rdma_sync_reply_hdr(struct svcxprt_rdma *rdma, struct svc_rdma_send_ctxt *ctxt, unsigned int len)

    DMA sync the transport header buffer

    :param struct svcxprt_rdma \*rdma:
        controlling transport

    :param struct svc_rdma_send_ctxt \*ctxt:
        send_ctxt for the Send WR

    :param unsigned int len:
        length of transport header

.. _`svc_rdma_sendto`:

svc_rdma_sendto
===============

.. c:function:: int svc_rdma_sendto(struct svc_rqst *rqstp)

    Transmit an RPC reply

    :param struct svc_rqst \*rqstp:
        processed RPC request, reply XDR already in ::rq_res

.. _`svc_rdma_sendto.description`:

Description
-----------

Any resources still associated with \ ``rqstp``\  are released upon return.
If no reply message was possible, the connection is closed.

.. _`svc_rdma_sendto.return`:

Return
------

\ ``0``\  if an RPC reply has been successfully posted,
\ ``-ENOMEM``\  if a resource shortage occurred (connection is lost),
\ ``-ENOTCONN``\  if posting failed (connection is lost).

.. This file was automatic generated / don't edit.

