.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_mgmt.c

.. _`hinic_register_mgmt_msg_cb`:

hinic_register_mgmt_msg_cb
==========================

.. c:function:: void hinic_register_mgmt_msg_cb(struct hinic_pf_to_mgmt *pf_to_mgmt, enum hinic_mod_type mod, void *handle, void (*callback)(void *handle, u8 cmd, void *buf_in, u16 in_size, void *buf_out, u16 *out_size))

    register msg handler for a msg from a module

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param mod:
        module in the chip that this handler will handle its messages
    :type mod: enum hinic_mod_type

    :param handle:
        private data for the callback
    :type handle: void \*

    :param void (\*callback)(void \*handle, u8 cmd, void \*buf_in, u16 in_size, void \*buf_out, u16 \*out_size):
        the handler that will handle messages

.. _`hinic_unregister_mgmt_msg_cb`:

hinic_unregister_mgmt_msg_cb
============================

.. c:function:: void hinic_unregister_mgmt_msg_cb(struct hinic_pf_to_mgmt *pf_to_mgmt, enum hinic_mod_type mod)

    unregister msg handler for a msg from a module

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param mod:
        module in the chip that this handler handles its messages
    :type mod: enum hinic_mod_type

.. _`prepare_header`:

prepare_header
==============

.. c:function:: u64 prepare_header(struct hinic_pf_to_mgmt *pf_to_mgmt, u16 msg_len, enum hinic_mod_type mod, enum msg_ack_type ack_type, enum mgmt_direction_type direction, u16 cmd, u16 msg_id)

    prepare the header of the message

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param msg_len:
        the length of the message
    :type msg_len: u16

    :param mod:
        module in the chip that will get the message
    :type mod: enum hinic_mod_type

    :param ack_type:
        ask for response
    :type ack_type: enum msg_ack_type

    :param direction:
        the direction of the message
    :type direction: enum mgmt_direction_type

    :param cmd:
        command of the message
    :type cmd: u16

    :param msg_id:
        message id
    :type msg_id: u16

.. _`prepare_header.description`:

Description
-----------

Return the prepared header value

.. _`prepare_mgmt_cmd`:

prepare_mgmt_cmd
================

.. c:function:: void prepare_mgmt_cmd(u8 *mgmt_cmd, u64 *header, u8 *msg, u16 msg_len)

    prepare the mgmt command

    :param mgmt_cmd:
        pointer to the command to prepare
    :type mgmt_cmd: u8 \*

    :param header:
        pointer of the header for the message
    :type header: u64 \*

    :param msg:
        the data of the message
    :type msg: u8 \*

    :param msg_len:
        the length of the message
    :type msg_len: u16

.. _`mgmt_msg_len`:

mgmt_msg_len
============

.. c:function:: u16 mgmt_msg_len(u16 msg_data_len)

    calculate the total message length

    :param msg_data_len:
        the length of the message data
    :type msg_data_len: u16

.. _`mgmt_msg_len.description`:

Description
-----------

Return the total message length

.. _`send_msg_to_mgmt`:

send_msg_to_mgmt
================

.. c:function:: int send_msg_to_mgmt(struct hinic_pf_to_mgmt *pf_to_mgmt, enum hinic_mod_type mod, u8 cmd, u8 *data, u16 data_len, enum msg_ack_type ack_type, enum mgmt_direction_type direction, u16 resp_msg_id)

    send message to mgmt by API CMD

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param mod:
        module in the chip that will get the message
    :type mod: enum hinic_mod_type

    :param cmd:
        command of the message
    :type cmd: u8

    :param data:
        the msg data
    :type data: u8 \*

    :param data_len:
        the msg data length
    :type data_len: u16

    :param ack_type:
        ask for response
    :type ack_type: enum msg_ack_type

    :param direction:
        the direction of the original message
    :type direction: enum mgmt_direction_type

    :param resp_msg_id:
        msg id to response for
    :type resp_msg_id: u16

.. _`send_msg_to_mgmt.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`msg_to_mgmt_sync`:

msg_to_mgmt_sync
================

.. c:function:: int msg_to_mgmt_sync(struct hinic_pf_to_mgmt *pf_to_mgmt, enum hinic_mod_type mod, u8 cmd, u8 *buf_in, u16 in_size, u8 *buf_out, u16 *out_size, enum mgmt_direction_type direction, u16 resp_msg_id)

    send sync message to mgmt

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param mod:
        module in the chip that will get the message
    :type mod: enum hinic_mod_type

    :param cmd:
        command of the message
    :type cmd: u8

    :param buf_in:
        the msg data
    :type buf_in: u8 \*

    :param in_size:
        the msg data length
    :type in_size: u16

    :param buf_out:
        response
    :type buf_out: u8 \*

    :param out_size:
        response length
    :type out_size: u16 \*

    :param direction:
        the direction of the original message
    :type direction: enum mgmt_direction_type

    :param resp_msg_id:
        msg id to response for
    :type resp_msg_id: u16

.. _`msg_to_mgmt_sync.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`msg_to_mgmt_async`:

msg_to_mgmt_async
=================

.. c:function:: int msg_to_mgmt_async(struct hinic_pf_to_mgmt *pf_to_mgmt, enum hinic_mod_type mod, u8 cmd, u8 *buf_in, u16 in_size, enum mgmt_direction_type direction, u16 resp_msg_id)

    send message to mgmt without response

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param mod:
        module in the chip that will get the message
    :type mod: enum hinic_mod_type

    :param cmd:
        command of the message
    :type cmd: u8

    :param buf_in:
        the msg data
    :type buf_in: u8 \*

    :param in_size:
        the msg data length
    :type in_size: u16

    :param direction:
        the direction of the original message
    :type direction: enum mgmt_direction_type

    :param resp_msg_id:
        msg id to response for
    :type resp_msg_id: u16

.. _`msg_to_mgmt_async.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_msg_to_mgmt`:

hinic_msg_to_mgmt
=================

.. c:function:: int hinic_msg_to_mgmt(struct hinic_pf_to_mgmt *pf_to_mgmt, enum hinic_mod_type mod, u8 cmd, void *buf_in, u16 in_size, void *buf_out, u16 *out_size, enum hinic_mgmt_msg_type sync)

    send message to mgmt

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param mod:
        module in the chip that will get the message
    :type mod: enum hinic_mod_type

    :param cmd:
        command of the message
    :type cmd: u8

    :param buf_in:
        the msg data
    :type buf_in: void \*

    :param in_size:
        the msg data length
    :type in_size: u16

    :param buf_out:
        response
    :type buf_out: void \*

    :param out_size:
        returned response length
    :type out_size: u16 \*

    :param sync:
        sync msg or async msg
    :type sync: enum hinic_mgmt_msg_type

.. _`hinic_msg_to_mgmt.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`mgmt_recv_msg_handler`:

mgmt_recv_msg_handler
=====================

.. c:function:: void mgmt_recv_msg_handler(struct hinic_pf_to_mgmt *pf_to_mgmt, struct hinic_recv_msg *recv_msg)

    handler for message from mgmt cpu

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param recv_msg:
        received message details
    :type recv_msg: struct hinic_recv_msg \*

.. _`mgmt_resp_msg_handler`:

mgmt_resp_msg_handler
=====================

.. c:function:: void mgmt_resp_msg_handler(struct hinic_pf_to_mgmt *pf_to_mgmt, struct hinic_recv_msg *recv_msg)

    handler for a response message from mgmt cpu

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param recv_msg:
        received message details
    :type recv_msg: struct hinic_recv_msg \*

.. _`recv_mgmt_msg_handler`:

recv_mgmt_msg_handler
=====================

.. c:function:: void recv_mgmt_msg_handler(struct hinic_pf_to_mgmt *pf_to_mgmt, u64 *header, struct hinic_recv_msg *recv_msg)

    handler for a message from mgmt cpu

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param header:
        the header of the message
    :type header: u64 \*

    :param recv_msg:
        received message details
    :type recv_msg: struct hinic_recv_msg \*

.. _`mgmt_msg_aeqe_handler`:

mgmt_msg_aeqe_handler
=====================

.. c:function:: void mgmt_msg_aeqe_handler(void *handle, void *data, u8 size)

    handler for a mgmt message event

    :param handle:
        PF to MGMT channel
    :type handle: void \*

    :param data:
        the header of the message
    :type data: void \*

    :param size:
        unused
    :type size: u8

.. _`alloc_recv_msg`:

alloc_recv_msg
==============

.. c:function:: int alloc_recv_msg(struct hinic_pf_to_mgmt *pf_to_mgmt, struct hinic_recv_msg *recv_msg)

    allocate receive message memory

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param recv_msg:
        pointer that will hold the allocated data
    :type recv_msg: struct hinic_recv_msg \*

.. _`alloc_recv_msg.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`alloc_msg_buf`:

alloc_msg_buf
=============

.. c:function:: int alloc_msg_buf(struct hinic_pf_to_mgmt *pf_to_mgmt)

    allocate all the message buffers of PF to MGMT channel

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

.. _`alloc_msg_buf.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_pf_to_mgmt_init`:

hinic_pf_to_mgmt_init
=====================

.. c:function:: int hinic_pf_to_mgmt_init(struct hinic_pf_to_mgmt *pf_to_mgmt, struct hinic_hwif *hwif)

    initialize PF to MGMT channel

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

    :param hwif:
        HW interface the PF to MGMT will use for accessing HW
    :type hwif: struct hinic_hwif \*

.. _`hinic_pf_to_mgmt_init.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_pf_to_mgmt_free`:

hinic_pf_to_mgmt_free
=====================

.. c:function:: void hinic_pf_to_mgmt_free(struct hinic_pf_to_mgmt *pf_to_mgmt)

    free PF to MGMT channel

    :param pf_to_mgmt:
        PF to MGMT channel
    :type pf_to_mgmt: struct hinic_pf_to_mgmt \*

.. This file was automatic generated / don't edit.

