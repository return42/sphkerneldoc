.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/user_sdma.c

.. _`hfi1_user_sdma_process_request`:

hfi1_user_sdma_process_request
==============================

.. c:function:: int hfi1_user_sdma_process_request(struct hfi1_filedata *fd, struct iovec *iovec, unsigned long dim, unsigned long *count)

    Process and start a user sdma request

    :param fd:
        valid file descriptor
    :type fd: struct hfi1_filedata \*

    :param iovec:
        array of io vectors to process
    :type iovec: struct iovec \*

    :param dim:
        overall iovec array size
    :type dim: unsigned long

    :param count:
        number of io vector array entries processed
    :type count: unsigned long \*

.. _`user_sdma_txreq_cb`:

user_sdma_txreq_cb
==================

.. c:function:: void user_sdma_txreq_cb(struct sdma_txreq *txreq, int status)

    SDMA tx request completion callback.

    :param txreq:
        valid sdma tx request
    :type txreq: struct sdma_txreq \*

    :param status:
        success/failure of request
    :type status: int

.. _`user_sdma_txreq_cb.description`:

Description
-----------

Called when the SDMA progress state machine gets notification that
the SDMA descriptors for this tx request have been processed by the
DMA engine. Called in interrupt context.
Only do work on completed sequences.

.. This file was automatic generated / don't edit.

