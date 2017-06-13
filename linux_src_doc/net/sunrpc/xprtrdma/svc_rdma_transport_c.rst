.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/svc_rdma_transport.c

.. _`svc_rdma_wc_receive`:

svc_rdma_wc_receive
===================

.. c:function:: void svc_rdma_wc_receive(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled Receive WC

    :param struct ib_cq \*cq:
        completion queue

    :param struct ib_wc \*wc:
        completed WR

.. _`svc_rdma_wc_send`:

svc_rdma_wc_send
================

.. c:function:: void svc_rdma_wc_send(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled Send WC

    :param struct ib_cq \*cq:
        completion queue

    :param struct ib_wc \*wc:
        completed WR

.. _`svc_rdma_wc_reg`:

svc_rdma_wc_reg
===============

.. c:function:: void svc_rdma_wc_reg(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled FASTREG WC

    :param struct ib_cq \*cq:
        completion queue

    :param struct ib_wc \*wc:
        completed WR

.. _`svc_rdma_wc_read`:

svc_rdma_wc_read
================

.. c:function:: void svc_rdma_wc_read(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled Read WC

    :param struct ib_cq \*cq:
        completion queue

    :param struct ib_wc \*wc:
        completed WR

.. _`svc_rdma_wc_inv`:

svc_rdma_wc_inv
===============

.. c:function:: void svc_rdma_wc_inv(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for each polled LOCAL_INV WC

    :param struct ib_cq \*cq:
        completion queue

    :param struct ib_wc \*wc:
        completed WR

.. This file was automatic generated / don't edit.

