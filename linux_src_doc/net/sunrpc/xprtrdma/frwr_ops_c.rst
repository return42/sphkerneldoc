.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/frwr_ops.c

.. _`frwr_wc_fastreg`:

frwr_wc_fastreg
===============

.. c:function:: void frwr_wc_fastreg(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for a flushed FastReg WC

    :param struct ib_cq \*cq:
        completion queue (ignored)

    :param struct ib_wc \*wc:
        completed WR

.. _`frwr_wc_localinv`:

frwr_wc_localinv
================

.. c:function:: void frwr_wc_localinv(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for a flushed LocalInv WC

    :param struct ib_cq \*cq:
        completion queue (ignored)

    :param struct ib_wc \*wc:
        completed WR

.. _`frwr_wc_localinv_wake`:

frwr_wc_localinv_wake
=====================

.. c:function:: void frwr_wc_localinv_wake(struct ib_cq *cq, struct ib_wc *wc)

    Invoked by RDMA provider for a signaled LocalInv WC

    :param struct ib_cq \*cq:
        completion queue (ignored)

    :param struct ib_wc \*wc:
        completed WR

.. _`frwr_wc_localinv_wake.description`:

Description
-----------

Awaken anyone waiting for an MR to finish being fenced.

.. This file was automatic generated / don't edit.

