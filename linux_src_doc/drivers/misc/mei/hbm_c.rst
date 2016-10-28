.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/hbm.c

.. _`mei_cl_conn_status_to_errno`:

mei_cl_conn_status_to_errno
===========================

.. c:function:: int mei_cl_conn_status_to_errno(enum mei_cl_connect_status status)

    convert client connect response status to error code

    :param enum mei_cl_connect_status status:
        client connect response status

.. _`mei_cl_conn_status_to_errno.return`:

Return
------

corresponding error code

.. _`mei_hbm_idle`:

mei_hbm_idle
============

.. c:function:: void mei_hbm_idle(struct mei_device *dev)

    set hbm to idle state

    :param struct mei_device \*dev:
        the device structure

.. _`mei_hbm_reset`:

mei_hbm_reset
=============

.. c:function:: void mei_hbm_reset(struct mei_device *dev)

    reset hbm counters and book keeping data structurs

    :param struct mei_device \*dev:
        the device structure

.. _`mei_hbm_hdr`:

mei_hbm_hdr
===========

.. c:function:: void mei_hbm_hdr(struct mei_msg_hdr *hdr, size_t length)

    construct hbm header

    :param struct mei_msg_hdr \*hdr:
        hbm header

    :param size_t length:
        payload length

.. _`mei_hbm_cl_hdr`:

mei_hbm_cl_hdr
==============

.. c:function:: void mei_hbm_cl_hdr(struct mei_cl *cl, u8 hbm_cmd, void *buf, size_t len)

    construct client hbm header

    :param struct mei_cl \*cl:
        client

    :param u8 hbm_cmd:
        host bus message command

    :param void \*buf:
        buffer for cl header

    :param size_t len:
        buffer length

.. _`mei_hbm_cl_write`:

mei_hbm_cl_write
================

.. c:function:: int mei_hbm_cl_write(struct mei_device *dev, struct mei_cl *cl, u8 hbm_cmd, size_t len)

    write simple hbm client message

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl \*cl:
        client

    :param u8 hbm_cmd:
        host bus message command

    :param size_t len:
        buffer length

.. _`mei_hbm_cl_write.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_hbm_cl_addr_equal`:

mei_hbm_cl_addr_equal
=====================

.. c:function:: bool mei_hbm_cl_addr_equal(struct mei_cl *cl, struct mei_hbm_cl_cmd *cmd)

    check if the client's and the message address match

    :param struct mei_cl \*cl:
        client

    :param struct mei_hbm_cl_cmd \*cmd:
        hbm client message

.. _`mei_hbm_cl_addr_equal.return`:

Return
------

true if addresses are the same

.. _`mei_hbm_cl_find_by_cmd`:

mei_hbm_cl_find_by_cmd
======================

.. c:function:: struct mei_cl *mei_hbm_cl_find_by_cmd(struct mei_device *dev, void *buf)

    find recipient client

    :param struct mei_device \*dev:
        the device structure

    :param void \*buf:
        a buffer with hbm cl command

.. _`mei_hbm_cl_find_by_cmd.return`:

Return
------

the recipient client or NULL if not found

.. _`mei_hbm_start_wait`:

mei_hbm_start_wait
==================

.. c:function:: int mei_hbm_start_wait(struct mei_device *dev)

    wait for start response message.

    :param struct mei_device \*dev:
        the device structure

.. _`mei_hbm_start_wait.return`:

Return
------

0 on success and < 0 on failure

.. _`mei_hbm_start_req`:

mei_hbm_start_req
=================

.. c:function:: int mei_hbm_start_req(struct mei_device *dev)

    sends start request message.

    :param struct mei_device \*dev:
        the device structure

.. _`mei_hbm_start_req.return`:

Return
------

0 on success and < 0 on failure

.. _`mei_hbm_enum_clients_req`:

mei_hbm_enum_clients_req
========================

.. c:function:: int mei_hbm_enum_clients_req(struct mei_device *dev)

    sends enumeration client request message.

    :param struct mei_device \*dev:
        the device structure

.. _`mei_hbm_enum_clients_req.return`:

Return
------

0 on success and < 0 on failure

.. _`mei_hbm_me_cl_add`:

mei_hbm_me_cl_add
=================

.. c:function:: int mei_hbm_me_cl_add(struct mei_device *dev, struct hbm_props_response *res)

    add new me client to the list

    :param struct mei_device \*dev:
        the device structure

    :param struct hbm_props_response \*res:
        hbm property response

.. _`mei_hbm_me_cl_add.return`:

Return
------

0 on success and -ENOMEM on allocation failure

.. _`mei_hbm_add_cl_resp`:

mei_hbm_add_cl_resp
===================

.. c:function:: int mei_hbm_add_cl_resp(struct mei_device *dev, u8 addr, u8 status)

    send response to fw on client add request

    :param struct mei_device \*dev:
        the device structure

    :param u8 addr:
        me address

    :param u8 status:
        response status

.. _`mei_hbm_add_cl_resp.return`:

Return
------

0 on success and < 0 on failure

.. _`mei_hbm_fw_add_cl_req`:

mei_hbm_fw_add_cl_req
=====================

.. c:function:: int mei_hbm_fw_add_cl_req(struct mei_device *dev, struct hbm_add_client_request *req)

    request from the fw to add a client

    :param struct mei_device \*dev:
        the device structure

    :param struct hbm_add_client_request \*req:
        add client request

.. _`mei_hbm_fw_add_cl_req.return`:

Return
------

0 on success and < 0 on failure

.. _`mei_hbm_cl_notify_req`:

mei_hbm_cl_notify_req
=====================

.. c:function:: int mei_hbm_cl_notify_req(struct mei_device *dev, struct mei_cl *cl, u8 start)

    send notification request

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl \*cl:
        a client to disconnect from

    :param u8 start:
        true for start false for stop

.. _`mei_hbm_cl_notify_req.return`:

Return
------

0 on success and -EIO on write failure

.. _`notify_res_to_fop`:

notify_res_to_fop
=================

.. c:function:: enum mei_cb_file_ops notify_res_to_fop(struct mei_hbm_cl_cmd *cmd)

    convert notification response to the proper notification FOP

    :param struct mei_hbm_cl_cmd \*cmd:
        client notification start response command

.. _`notify_res_to_fop.return`:

Return
------

MEI_FOP_NOTIFY_START or MEI_FOP_NOTIFY_STOP;

.. _`mei_hbm_cl_notify_start_res`:

mei_hbm_cl_notify_start_res
===========================

.. c:function:: void mei_hbm_cl_notify_start_res(struct mei_device *dev, struct mei_cl *cl, struct mei_hbm_cl_cmd *cmd)

    update the client state according notify start response

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl \*cl:
        mei host client

    :param struct mei_hbm_cl_cmd \*cmd:
        client notification start response command

.. _`mei_hbm_cl_notify_stop_res`:

mei_hbm_cl_notify_stop_res
==========================

.. c:function:: void mei_hbm_cl_notify_stop_res(struct mei_device *dev, struct mei_cl *cl, struct mei_hbm_cl_cmd *cmd)

    update the client state according notify stop response

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl \*cl:
        mei host client

    :param struct mei_hbm_cl_cmd \*cmd:
        client notification stop response command

.. _`mei_hbm_cl_notify`:

mei_hbm_cl_notify
=================

.. c:function:: void mei_hbm_cl_notify(struct mei_device *dev, struct mei_hbm_cl_cmd *cmd)

    signal notification event

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_hbm_cl_cmd \*cmd:
        notification client message

.. _`mei_hbm_prop_req`:

mei_hbm_prop_req
================

.. c:function:: int mei_hbm_prop_req(struct mei_device *dev, unsigned long start_idx)

    request property for a single client

    :param struct mei_device \*dev:
        the device structure

    :param unsigned long start_idx:
        client index to start search

.. _`mei_hbm_prop_req.return`:

Return
------

0 on success and < 0 on failure

.. _`mei_hbm_pg`:

mei_hbm_pg
==========

.. c:function:: int mei_hbm_pg(struct mei_device *dev, u8 pg_cmd)

    sends pg command

    :param struct mei_device \*dev:
        the device structure

    :param u8 pg_cmd:
        the pg command code

.. _`mei_hbm_pg.return`:

Return
------

-EIO on write failure
-EOPNOTSUPP if the operation is not supported by the protocol

.. _`mei_hbm_stop_req`:

mei_hbm_stop_req
================

.. c:function:: int mei_hbm_stop_req(struct mei_device *dev)

    send stop request message

    :param struct mei_device \*dev:
        mei device

.. _`mei_hbm_stop_req.return`:

Return
------

-EIO on write failure

.. _`mei_hbm_cl_flow_control_req`:

mei_hbm_cl_flow_control_req
===========================

.. c:function:: int mei_hbm_cl_flow_control_req(struct mei_device *dev, struct mei_cl *cl)

    sends flow control request.

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl \*cl:
        client info

.. _`mei_hbm_cl_flow_control_req.return`:

Return
------

-EIO on write failure

.. _`mei_hbm_add_single_flow_creds`:

mei_hbm_add_single_flow_creds
=============================

.. c:function:: int mei_hbm_add_single_flow_creds(struct mei_device *dev, struct hbm_flow_control *flow)

    adds single buffer credentials.

    :param struct mei_device \*dev:
        the device structure

    :param struct hbm_flow_control \*flow:
        flow control.

.. _`mei_hbm_add_single_flow_creds.return`:

Return
------

0 on success, < 0 otherwise

.. _`mei_hbm_cl_flow_control_res`:

mei_hbm_cl_flow_control_res
===========================

.. c:function:: void mei_hbm_cl_flow_control_res(struct mei_device *dev, struct hbm_flow_control *flow_control)

    flow control response from me

    :param struct mei_device \*dev:
        the device structure

    :param struct hbm_flow_control \*flow_control:
        flow control response bus message

.. _`mei_hbm_cl_disconnect_req`:

mei_hbm_cl_disconnect_req
=========================

.. c:function:: int mei_hbm_cl_disconnect_req(struct mei_device *dev, struct mei_cl *cl)

    sends disconnect message to fw.

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl \*cl:
        a client to disconnect from

.. _`mei_hbm_cl_disconnect_req.return`:

Return
------

-EIO on write failure

.. _`mei_hbm_cl_disconnect_rsp`:

mei_hbm_cl_disconnect_rsp
=========================

.. c:function:: int mei_hbm_cl_disconnect_rsp(struct mei_device *dev, struct mei_cl *cl)

    sends disconnect respose to the FW

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl \*cl:
        a client to disconnect from

.. _`mei_hbm_cl_disconnect_rsp.return`:

Return
------

-EIO on write failure

.. _`mei_hbm_cl_disconnect_res`:

mei_hbm_cl_disconnect_res
=========================

.. c:function:: void mei_hbm_cl_disconnect_res(struct mei_device *dev, struct mei_cl *cl, struct mei_hbm_cl_cmd *cmd)

    update the client state according disconnect response

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl \*cl:
        mei host client

    :param struct mei_hbm_cl_cmd \*cmd:
        disconnect client response host bus message

.. _`mei_hbm_cl_connect_req`:

mei_hbm_cl_connect_req
======================

.. c:function:: int mei_hbm_cl_connect_req(struct mei_device *dev, struct mei_cl *cl)

    send connection request to specific me client

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl \*cl:
        a client to connect to

.. _`mei_hbm_cl_connect_req.return`:

Return
------

-EIO on write failure

.. _`mei_hbm_cl_connect_res`:

mei_hbm_cl_connect_res
======================

.. c:function:: void mei_hbm_cl_connect_res(struct mei_device *dev, struct mei_cl *cl, struct mei_hbm_cl_cmd *cmd)

    update the client state according connection response

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_cl \*cl:
        mei host client

    :param struct mei_hbm_cl_cmd \*cmd:
        connect client response host bus message

.. _`mei_hbm_cl_res`:

mei_hbm_cl_res
==============

.. c:function:: void mei_hbm_cl_res(struct mei_device *dev, struct mei_hbm_cl_cmd *rs, enum mei_cb_file_ops fop_type)

    process hbm response received on behalf an client

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_hbm_cl_cmd \*rs:
        hbm client message

    :param enum mei_cb_file_ops fop_type:
        file operation type

.. _`mei_hbm_fw_disconnect_req`:

mei_hbm_fw_disconnect_req
=========================

.. c:function:: int mei_hbm_fw_disconnect_req(struct mei_device *dev, struct hbm_client_connect_request *disconnect_req)

    disconnect request initiated by ME firmware host sends disconnect response

    :param struct mei_device \*dev:
        the device structure.

    :param struct hbm_client_connect_request \*disconnect_req:
        disconnect request bus message from the me

.. _`mei_hbm_fw_disconnect_req.return`:

Return
------

-ENOMEM on allocation failure

.. _`mei_hbm_pg_enter_res`:

mei_hbm_pg_enter_res
====================

.. c:function:: int mei_hbm_pg_enter_res(struct mei_device *dev)

    PG enter response received

    :param struct mei_device \*dev:
        the device structure.

.. _`mei_hbm_pg_enter_res.return`:

Return
------

0 on success, -EPROTO on state mismatch

.. _`mei_hbm_pg_resume`:

mei_hbm_pg_resume
=================

.. c:function:: void mei_hbm_pg_resume(struct mei_device *dev)

    process with PG resume

    :param struct mei_device \*dev:
        the device structure.

.. _`mei_hbm_pg_exit_res`:

mei_hbm_pg_exit_res
===================

.. c:function:: int mei_hbm_pg_exit_res(struct mei_device *dev)

    PG exit response received

    :param struct mei_device \*dev:
        the device structure.

.. _`mei_hbm_pg_exit_res.return`:

Return
------

0 on success, -EPROTO on state mismatch

.. _`mei_hbm_config_features`:

mei_hbm_config_features
=======================

.. c:function:: void mei_hbm_config_features(struct mei_device *dev)

    check what hbm features and commands are supported by the fw

    :param struct mei_device \*dev:
        the device structure

.. _`mei_hbm_version_is_supported`:

mei_hbm_version_is_supported
============================

.. c:function:: bool mei_hbm_version_is_supported(struct mei_device *dev)

    checks whether the driver can support the hbm version of the device

    :param struct mei_device \*dev:
        the device structure

.. _`mei_hbm_version_is_supported.return`:

Return
------

true if driver can support hbm version of the device

.. _`mei_hbm_dispatch`:

mei_hbm_dispatch
================

.. c:function:: int mei_hbm_dispatch(struct mei_device *dev, struct mei_msg_hdr *hdr)

    bottom half read routine after ISR to handle the read bus message cmd processing.

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_msg_hdr \*hdr:
        header of bus message

.. _`mei_hbm_dispatch.return`:

Return
------

0 on success and < 0 on failure

.. This file was automatic generated / don't edit.

