.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp/hbm.c

.. _`ishtp_hbm_fw_cl_allocate`:

ishtp_hbm_fw_cl_allocate
========================

.. c:function:: void ishtp_hbm_fw_cl_allocate(struct ishtp_device *dev)

    Allocate FW clients

    :param struct ishtp_device \*dev:
        ISHTP device instance

.. _`ishtp_hbm_fw_cl_allocate.description`:

Description
-----------

Allocates storage for fw clients

.. _`ishtp_hbm_cl_hdr`:

ishtp_hbm_cl_hdr
================

.. c:function:: void ishtp_hbm_cl_hdr(struct ishtp_cl *cl, uint8_t hbm_cmd, void *buf, size_t len)

    construct client hbm header

    :param struct ishtp_cl \*cl:
        client

    :param uint8_t hbm_cmd:
        host bus message command

    :param void \*buf:
        buffer for cl header

    :param size_t len:
        buffer length

.. _`ishtp_hbm_cl_hdr.description`:

Description
-----------

Initialize HBM buffer

.. _`ishtp_hbm_cl_addr_equal`:

ishtp_hbm_cl_addr_equal
=======================

.. c:function:: bool ishtp_hbm_cl_addr_equal(struct ishtp_cl *cl, void *buf)

    Compare client address

    :param struct ishtp_cl \*cl:
        client

    :param void \*buf:
        Client command buffer

.. _`ishtp_hbm_cl_addr_equal.description`:

Description
-----------

Compare client address with the address in command buffer

.. _`ishtp_hbm_cl_addr_equal.return`:

Return
------

True if they have the same address

.. _`ishtp_hbm_start_wait`:

ishtp_hbm_start_wait
====================

.. c:function:: int ishtp_hbm_start_wait(struct ishtp_device *dev)

    Wait for HBM start message

    :param struct ishtp_device \*dev:
        ISHTP device instance

.. _`ishtp_hbm_start_wait.description`:

Description
-----------

Wait for HBM start message from firmware

.. _`ishtp_hbm_start_wait.return`:

Return
------

0 if HBM start is/was received else timeout error

.. _`ishtp_hbm_start_req`:

ishtp_hbm_start_req
===================

.. c:function:: int ishtp_hbm_start_req(struct ishtp_device *dev)

    Send HBM start message

    :param struct ishtp_device \*dev:
        ISHTP device instance

.. _`ishtp_hbm_start_req.description`:

Description
-----------

Send HBM start message to firmware

.. _`ishtp_hbm_start_req.return`:

Return
------

0 if success else error code

.. _`ishtp_hbm_enum_clients_req`:

ishtp_hbm_enum_clients_req
==========================

.. c:function:: void ishtp_hbm_enum_clients_req(struct ishtp_device *dev)

    Send client enum req

    :param struct ishtp_device \*dev:
        ISHTP device instance

.. _`ishtp_hbm_enum_clients_req.description`:

Description
-----------

Send enumeration client request message

.. _`ishtp_hbm_enum_clients_req.return`:

Return
------

0 if success else error code

.. _`ishtp_hbm_prop_req`:

ishtp_hbm_prop_req
==================

.. c:function:: int ishtp_hbm_prop_req(struct ishtp_device *dev)

    Request property

    :param struct ishtp_device \*dev:
        ISHTP device instance

.. _`ishtp_hbm_prop_req.description`:

Description
-----------

Request property for a single client

.. _`ishtp_hbm_prop_req.return`:

Return
------

0 if success else error code

.. _`ishtp_hbm_stop_req`:

ishtp_hbm_stop_req
==================

.. c:function:: void ishtp_hbm_stop_req(struct ishtp_device *dev)

    Send HBM stop

    :param struct ishtp_device \*dev:
        ISHTP device instance

.. _`ishtp_hbm_stop_req.description`:

Description
-----------

Send stop request message

.. _`ishtp_hbm_cl_flow_control_req`:

ishtp_hbm_cl_flow_control_req
=============================

.. c:function:: int ishtp_hbm_cl_flow_control_req(struct ishtp_device *dev, struct ishtp_cl *cl)

    Send flow control request

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct ishtp_cl \*cl:
        ISHTP client instance

.. _`ishtp_hbm_cl_flow_control_req.description`:

Description
-----------

Send flow control request

.. _`ishtp_hbm_cl_flow_control_req.return`:

Return
------

0 if success else error code

.. _`ishtp_hbm_cl_disconnect_req`:

ishtp_hbm_cl_disconnect_req
===========================

.. c:function:: int ishtp_hbm_cl_disconnect_req(struct ishtp_device *dev, struct ishtp_cl *cl)

    Send disconnect request

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct ishtp_cl \*cl:
        ISHTP client instance

.. _`ishtp_hbm_cl_disconnect_req.description`:

Description
-----------

Send disconnect message to fw

.. _`ishtp_hbm_cl_disconnect_req.return`:

Return
------

0 if success else error code

.. _`ishtp_hbm_cl_disconnect_res`:

ishtp_hbm_cl_disconnect_res
===========================

.. c:function:: void ishtp_hbm_cl_disconnect_res(struct ishtp_device *dev, struct hbm_client_connect_response *rs)

    Get disconnect response

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct hbm_client_connect_response \*rs:
        Response message

.. _`ishtp_hbm_cl_disconnect_res.description`:

Description
-----------

Received disconnect response from fw

.. _`ishtp_hbm_cl_connect_req`:

ishtp_hbm_cl_connect_req
========================

.. c:function:: int ishtp_hbm_cl_connect_req(struct ishtp_device *dev, struct ishtp_cl *cl)

    Send connect request

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_hbm_cl_connect_req.description`:

Description
-----------

Send connection request to specific fw client

.. _`ishtp_hbm_cl_connect_req.return`:

Return
------

0 if success else error code

.. _`ishtp_hbm_cl_connect_res`:

ishtp_hbm_cl_connect_res
========================

.. c:function:: void ishtp_hbm_cl_connect_res(struct ishtp_device *dev, struct hbm_client_connect_response *rs)

    Get connect response

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct hbm_client_connect_response \*rs:
        Response message

.. _`ishtp_hbm_cl_connect_res.description`:

Description
-----------

Received connect response from fw

.. _`ishtp_hbm_fw_disconnect_req`:

ishtp_hbm_fw_disconnect_req
===========================

.. c:function:: void ishtp_hbm_fw_disconnect_req(struct ishtp_device *dev, struct hbm_client_connect_request *disconnect_req)

    Receive disconnect request

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct hbm_client_connect_request \*disconnect_req:
        disconnect request structure

.. _`ishtp_hbm_fw_disconnect_req.description`:

Description
-----------

Disconnect request bus message from the fw. Send diconnect response.

.. _`ishtp_hbm_dma_xfer_ack`:

ishtp_hbm_dma_xfer_ack
======================

.. c:function:: void ishtp_hbm_dma_xfer_ack(struct ishtp_device *dev, struct dma_xfer_hbm *dma_xfer)

    Receive transfer ACK

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct dma_xfer_hbm \*dma_xfer:
        HBM transfer message

.. _`ishtp_hbm_dma_xfer_ack.description`:

Description
-----------

Receive ack for ISHTP-over-DMA client message

.. _`ishtp_hbm_dma_xfer`:

ishtp_hbm_dma_xfer
==================

.. c:function:: void ishtp_hbm_dma_xfer(struct ishtp_device *dev, struct dma_xfer_hbm *dma_xfer)

    Receive DMA transfer message

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct dma_xfer_hbm \*dma_xfer:
        HBM transfer message

.. _`ishtp_hbm_dma_xfer.description`:

Description
-----------

Receive ISHTP-over-DMA client message

.. _`ishtp_hbm_dispatch`:

ishtp_hbm_dispatch
==================

.. c:function:: void ishtp_hbm_dispatch(struct ishtp_device *dev, struct ishtp_bus_message *hdr)

    HBM dispatch function

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct ishtp_bus_message \*hdr:
        bus message

.. _`ishtp_hbm_dispatch.description`:

Description
-----------

Bottom half read routine after ISR to handle the read bus message cmd
processing

.. _`bh_hbm_work_fn`:

bh_hbm_work_fn
==============

.. c:function:: void bh_hbm_work_fn(struct work_struct *work)

    HBM work function

    :param struct work_struct \*work:
        work struct

.. _`bh_hbm_work_fn.description`:

Description
-----------

Bottom half processing work function (instead of thread handler)
for processing hbm messages

.. _`recv_hbm`:

recv_hbm
========

.. c:function:: void recv_hbm(struct ishtp_device *dev, struct ishtp_msg_hdr *ishtp_hdr)

    Receive HBM message

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct ishtp_msg_hdr \*ishtp_hdr:
        received bus message

.. _`recv_hbm.description`:

Description
-----------

Receive and process ISHTP bus messages in ISR context. This will schedule
work function to process message

.. _`recv_fixed_cl_msg`:

recv_fixed_cl_msg
=================

.. c:function:: void recv_fixed_cl_msg(struct ishtp_device *dev, struct ishtp_msg_hdr *ishtp_hdr)

    Receive fixed client message

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct ishtp_msg_hdr \*ishtp_hdr:
        received bus message

.. _`recv_fixed_cl_msg.description`:

Description
-----------

Receive and process ISHTP fixed client messages (address == 0)
in ISR context

.. _`fix_cl_hdr`:

fix_cl_hdr
==========

.. c:function:: void fix_cl_hdr(struct ishtp_msg_hdr *hdr, size_t length, uint8_t cl_addr)

    Initialize fixed client header

    :param struct ishtp_msg_hdr \*hdr:
        message header

    :param size_t length:
        length of message

    :param uint8_t cl_addr:
        Client address

.. _`fix_cl_hdr.description`:

Description
-----------

Initialize message header for fixed client

.. _`ishtp_send_suspend`:

ishtp_send_suspend
==================

.. c:function:: void ishtp_send_suspend(struct ishtp_device *dev)

    Send suspend message to FW

    :param struct ishtp_device \*dev:
        ISHTP device instance

.. _`ishtp_send_suspend.description`:

Description
-----------

Send suspend message to FW. This is useful for system freeze (non S3) case

.. _`ishtp_send_resume`:

ishtp_send_resume
=================

.. c:function:: void ishtp_send_resume(struct ishtp_device *dev)

    Send resume message to FW

    :param struct ishtp_device \*dev:
        ISHTP device instance

.. _`ishtp_send_resume.description`:

Description
-----------

Send resume message to FW. This is useful for system freeze (non S3) case

.. _`ishtp_query_subscribers`:

ishtp_query_subscribers
=======================

.. c:function:: void ishtp_query_subscribers(struct ishtp_device *dev)

    Send query subscribers message

    :param struct ishtp_device \*dev:
        ISHTP device instance

.. _`ishtp_query_subscribers.description`:

Description
-----------

Send message to query subscribers

.. This file was automatic generated / don't edit.

