.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/svc_rdma_sendto.c

.. _`svc_rdma_send_ctxts_destroy`:

svc_rdma_send_ctxts_destroy
===========================

.. c:function:: void svc_rdma_send_ctxts_destroy(struct svcxprt_rdma *rdma)

    Release all send_ctxt's for an xprt

    :param rdma:
        svcxprt_rdma being torn down
    :type rdma: struct svcxprt_rdma \*

.. _`svc_rdma_send_ctxt_get`:

svc_rdma_send_ctxt_get
======================

.. c:function:: struct svc_rdma_send_ctxt *svc_rdma_send_ctxt_get(struct svcxprt_rdma *rdma)

    Get a free send_ctxt

    :param rdma:
        controlling svcxprt_rdma
    :type rdma: struct svcxprt_rdma \*

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

    :param rdma:
        controlling svcxprt_rdma
    :type rdma: struct svcxprt_rdma \*

    :param ctxt:
        object to return to the free list
    :type ctxt: struct svc_rdma_send_ctxt \*

.. _`svc_rdma_send_ctxt_put.description`:

Description
-----------

Pages left in sc_pages are DMA unmapped and released.

.. _`svc_rdma_wc_send`:

svc_rdma_wc_send
================

.. c:function:: void svc_rdma_wc_send(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled Send WC

    :param cq:
        Completion Queue context
    :type cq: struct ib_cq \*

    :param wc:
        Work Completion object
    :type wc: struct ib_wc \*

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

    :param rdma:
        transport on which to post the WR
    :type rdma: struct svcxprt_rdma \*

    :param wr:
        prepared Send WR to post
    :type wr: struct ib_send_wr \*

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

    :param rdma:
        controlling transport
    :type rdma: struct svcxprt_rdma \*

    :param ctxt:
        send_ctxt for the Send WR
    :type ctxt: struct svc_rdma_send_ctxt \*

    :param len:
        length of transport header
    :type len: unsigned int

.. _`svc_rdma_sendto`:

svc_rdma_sendto
===============

.. c:function:: int svc_rdma_sendto(struct svc_rqst *rqstp)

    Transmit an RPC reply

    :param rqstp:
        processed RPC request, reply XDR already in ::rq_res
    :type rqstp: struct svc_rqst \*

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

