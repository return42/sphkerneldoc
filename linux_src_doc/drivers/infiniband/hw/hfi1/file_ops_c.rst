.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/file_ops.c

.. _`manage_rcvq`:

manage_rcvq
===========

.. c:function:: int manage_rcvq(struct hfi1_ctxtdata *uctxt, u16 subctxt, int start_stop)

    manage a context's receive queue

    :param struct hfi1_ctxtdata \*uctxt:
        the context

    :param u16 subctxt:
        the sub-context

    :param int start_stop:
        action to carry out

.. _`manage_rcvq.description`:

Description
-----------

start_stop == 0 disables receive on the context, for use in queue
overflow conditions.  start_stop==1 re-enables, to be used to
re-init the software copy of the head register

.. This file was automatic generated / don't edit.

