.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/interrupt.c

.. _`mei_irq_compl_handler`:

mei_irq_compl_handler
=====================

.. c:function:: void mei_irq_compl_handler(struct mei_device *dev, struct mei_cl_cb *compl_list)

    dispatch complete handlers for the completed callbacks

    :param struct mei_device \*dev:
        mei device

    :param struct mei_cl_cb \*compl_list:
        list of completed cbs

.. _`mei_cl_hbm_equal`:

mei_cl_hbm_equal
================

.. c:function:: int mei_cl_hbm_equal(struct mei_cl *cl, struct mei_msg_hdr *mei_hdr)

    check if hbm is addressed to the client

    :param struct mei_cl \*cl:
        host client

    :param struct mei_msg_hdr \*mei_hdr:
        header of mei client message

.. _`mei_cl_hbm_equal.return`:

Return
------

true if matches, false otherwise

.. _`mei_irq_discard_msg`:

mei_irq_discard_msg
===================

.. c:function:: void mei_irq_discard_msg(struct mei_device *dev, struct mei_msg_hdr *hdr)

    discard received message

    :param struct mei_device \*dev:
        mei device

    :param struct mei_msg_hdr \*hdr:
        message header

.. _`mei_cl_irq_read_msg`:

mei_cl_irq_read_msg
===================

.. c:function:: int mei_cl_irq_read_msg(struct mei_cl *cl, struct mei_msg_hdr *mei_hdr, struct mei_cl_cb *complete_list)

    process client message

    :param struct mei_cl \*cl:
        reading client

    :param struct mei_msg_hdr \*mei_hdr:
        header of mei client message

    :param struct mei_cl_cb \*complete_list:
        completion list

.. _`mei_cl_irq_read_msg.return`:

Return
------

always 0

.. _`mei_cl_irq_disconnect_rsp`:

mei_cl_irq_disconnect_rsp
=========================

.. c:function:: int mei_cl_irq_disconnect_rsp(struct mei_cl *cl, struct mei_cl_cb *cb, struct mei_cl_cb *cmpl_list)

    send disconnection response message

    :param struct mei_cl \*cl:
        client

    :param struct mei_cl_cb \*cb:
        callback block.

    :param struct mei_cl_cb \*cmpl_list:
        complete list.

.. _`mei_cl_irq_disconnect_rsp.return`:

Return
------

0, OK; otherwise, error.

.. _`mei_cl_irq_read`:

mei_cl_irq_read
===============

.. c:function:: int mei_cl_irq_read(struct mei_cl *cl, struct mei_cl_cb *cb, struct mei_cl_cb *cmpl_list)

    processes client read related operation from the interrupt thread context - request for flow control credits

    :param struct mei_cl \*cl:
        client

    :param struct mei_cl_cb \*cb:
        callback block.

    :param struct mei_cl_cb \*cmpl_list:
        complete list.

.. _`mei_cl_irq_read.return`:

Return
------

0, OK; otherwise, error.

.. _`mei_irq_read_handler`:

mei_irq_read_handler
====================

.. c:function:: int mei_irq_read_handler(struct mei_device *dev, struct mei_cl_cb *cmpl_list, s32 *slots)

    bottom half read routine after ISR to handle the read processing.

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl_cb \*cmpl_list:
        An instance of our list structure

    :param s32 \*slots:
        slots to read.

.. _`mei_irq_read_handler.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_irq_write_handler`:

mei_irq_write_handler
=====================

.. c:function:: int mei_irq_write_handler(struct mei_device *dev, struct mei_cl_cb *cmpl_list)

    dispatch write requests after irq received

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl_cb \*cmpl_list:
        An instance of our list structure

.. _`mei_irq_write_handler.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_connect_timeout`:

mei_connect_timeout
===================

.. c:function:: void mei_connect_timeout(struct mei_cl *cl)

    connect/disconnect timeouts

    :param struct mei_cl \*cl:
        host client

.. _`mei_schedule_stall_timer`:

mei_schedule_stall_timer
========================

.. c:function:: void mei_schedule_stall_timer(struct mei_device *dev)

    re-arm stall_timer work

    :param struct mei_device \*dev:
        the device structure

.. _`mei_schedule_stall_timer.description`:

Description
-----------

Schedule stall timer

.. _`mei_timer`:

mei_timer
=========

.. c:function:: void mei_timer(struct work_struct *work)

    timer function.

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. This file was automatic generated / don't edit.

