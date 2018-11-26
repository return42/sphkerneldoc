.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp/hbm.c

.. _`ishtp_hbm_fw_cl_allocate`:

ishtp_hbm_fw_cl_allocate
========================

.. c:function:: void ishtp_hbm_fw_cl_allocate(struct ishtp_device *dev)

    Allocate FW clients

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

.. _`ishtp_hbm_fw_cl_allocate.description`:

Description
-----------

Allocates storage for fw clients

.. _`ishtp_hbm_cl_hdr`:

ishtp_hbm_cl_hdr
================

.. c:function:: void ishtp_hbm_cl_hdr(struct ishtp_cl *cl, uint8_t hbm_cmd, void *buf, size_t len)

    construct client hbm header

    :param cl:
        client
    :type cl: struct ishtp_cl \*

    :param hbm_cmd:
        host bus message command
    :type hbm_cmd: uint8_t

    :param buf:
        buffer for cl header
    :type buf: void \*

    :param len:
        buffer length
    :type len: size_t

.. _`ishtp_hbm_cl_hdr.description`:

Description
-----------

Initialize HBM buffer

.. _`ishtp_hbm_cl_addr_equal`:

ishtp_hbm_cl_addr_equal
=======================

.. c:function:: bool ishtp_hbm_cl_addr_equal(struct ishtp_cl *cl, void *buf)

    Compare client address

    :param cl:
        client
    :type cl: struct ishtp_cl \*

    :param buf:
        Client command buffer
    :type buf: void \*

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

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

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

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

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

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

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

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

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

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

.. _`ishtp_hbm_stop_req.description`:

Description
-----------

Send stop request message

.. _`ishtp_hbm_cl_flow_control_req`:

ishtp_hbm_cl_flow_control_req
=============================

.. c:function:: int ishtp_hbm_cl_flow_control_req(struct ishtp_device *dev, struct ishtp_cl *cl)

    Send flow control request

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

    :param cl:
        ISHTP client instance
    :type cl: struct ishtp_cl \*

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

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

    :param cl:
        ISHTP client instance
    :type cl: struct ishtp_cl \*

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

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

    :param rs:
        Response message
    :type rs: struct hbm_client_connect_response \*

.. _`ishtp_hbm_cl_disconnect_res.description`:

Description
-----------

Received disconnect response from fw

.. _`ishtp_hbm_cl_connect_req`:

ishtp_hbm_cl_connect_req
========================

.. c:function:: int ishtp_hbm_cl_connect_req(struct ishtp_device *dev, struct ishtp_cl *cl)

    Send connect request

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

    :param cl:
        client device instance
    :type cl: struct ishtp_cl \*

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

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

    :param rs:
        Response message
    :type rs: struct hbm_client_connect_response \*

.. _`ishtp_hbm_cl_connect_res.description`:

Description
-----------

Received connect response from fw

.. _`ishtp_hbm_fw_disconnect_req`:

ishtp_hbm_fw_disconnect_req
===========================

.. c:function:: void ishtp_hbm_fw_disconnect_req(struct ishtp_device *dev, struct hbm_client_connect_request *disconnect_req)

    Receive disconnect request

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

    :param disconnect_req:
        disconnect request structure
    :type disconnect_req: struct hbm_client_connect_request \*

.. _`ishtp_hbm_fw_disconnect_req.description`:

Description
-----------

Disconnect request bus message from the fw. Send diconnect response.

.. _`ishtp_hbm_dma_xfer_ack`:

ishtp_hbm_dma_xfer_ack
======================

.. c:function:: void ishtp_hbm_dma_xfer_ack(struct ishtp_device *dev, struct dma_xfer_hbm *dma_xfer)

    Receive transfer ACK

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

    :param dma_xfer:
        HBM transfer message
    :type dma_xfer: struct dma_xfer_hbm \*

.. _`ishtp_hbm_dma_xfer_ack.description`:

Description
-----------

Receive ack for ISHTP-over-DMA client message

.. _`ishtp_hbm_dma_xfer`:

ishtp_hbm_dma_xfer
==================

.. c:function:: void ishtp_hbm_dma_xfer(struct ishtp_device *dev, struct dma_xfer_hbm *dma_xfer)

    Receive DMA transfer message

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

    :param dma_xfer:
        HBM transfer message
    :type dma_xfer: struct dma_xfer_hbm \*

.. _`ishtp_hbm_dma_xfer.description`:

Description
-----------

Receive ISHTP-over-DMA client message

.. _`ishtp_hbm_dispatch`:

ishtp_hbm_dispatch
==================

.. c:function:: void ishtp_hbm_dispatch(struct ishtp_device *dev, struct ishtp_bus_message *hdr)

    HBM dispatch function

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

    :param hdr:
        bus message
    :type hdr: struct ishtp_bus_message \*

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

    :param work:
        work struct
    :type work: struct work_struct \*

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

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

    :param ishtp_hdr:
        received bus message
    :type ishtp_hdr: struct ishtp_msg_hdr \*

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

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

    :param ishtp_hdr:
        received bus message
    :type ishtp_hdr: struct ishtp_msg_hdr \*

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

    :param hdr:
        message header
    :type hdr: struct ishtp_msg_hdr \*

    :param length:
        length of message
    :type length: size_t

    :param cl_addr:
        Client address
    :type cl_addr: uint8_t

.. _`fix_cl_hdr.description`:

Description
-----------

Initialize message header for fixed client

.. _`ishtp_send_suspend`:

ishtp_send_suspend
==================

.. c:function:: void ishtp_send_suspend(struct ishtp_device *dev)

    Send suspend message to FW

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

.. _`ishtp_send_suspend.description`:

Description
-----------

Send suspend message to FW. This is useful for system freeze (non S3) case

.. _`ishtp_send_resume`:

ishtp_send_resume
=================

.. c:function:: void ishtp_send_resume(struct ishtp_device *dev)

    Send resume message to FW

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

.. _`ishtp_send_resume.description`:

Description
-----------

Send resume message to FW. This is useful for system freeze (non S3) case

.. _`ishtp_query_subscribers`:

ishtp_query_subscribers
=======================

.. c:function:: void ishtp_query_subscribers(struct ishtp_device *dev)

    Send query subscribers message

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

.. _`ishtp_query_subscribers.description`:

Description
-----------

Send message to query subscribers

.. This file was automatic generated / don't edit.

