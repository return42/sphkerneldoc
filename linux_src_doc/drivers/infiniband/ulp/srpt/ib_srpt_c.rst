.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/srpt/ib_srpt.c

.. _`srpt_event_handler`:

srpt_event_handler
==================

.. c:function:: void srpt_event_handler(struct ib_event_handler *handler, struct ib_event *event)

    asynchronous IB event callback function

    :param struct ib_event_handler \*handler:
        IB event handler registered by \ :c:func:`ib_register_event_handler`\ .

    :param struct ib_event \*event:
        Description of the event that occurred.

.. _`srpt_event_handler.description`:

Description
-----------

Callback function called by the InfiniBand core when an asynchronous IB
event occurs. This callback may occur in interrupt context. See also
section 11.5.2, Set Asynchronous Event Handler in the InfiniBand
Architecture Specification.

.. _`srpt_srq_event`:

srpt_srq_event
==============

.. c:function:: void srpt_srq_event(struct ib_event *event, void *ctx)

    SRQ event callback function

    :param struct ib_event \*event:
        Description of the event that occurred.

    :param void \*ctx:
        Context pointer specified at SRQ creation time.

.. _`srpt_qp_event`:

srpt_qp_event
=============

.. c:function:: void srpt_qp_event(struct ib_event *event, struct srpt_rdma_ch *ch)

    QP event callback function

    :param struct ib_event \*event:
        Description of the event that occurred.

    :param struct srpt_rdma_ch \*ch:
        SRPT RDMA channel.

.. _`srpt_set_ioc`:

srpt_set_ioc
============

.. c:function:: void srpt_set_ioc(u8 *c_list, u32 slot, u8 value)

    initialize a IOUnitInfo structure

    :param u8 \*c_list:
        controller list.

    :param u32 slot:
        one-based slot number.

    :param u8 value:
        four-bit value.

.. _`srpt_set_ioc.description`:

Description
-----------

Copies the lowest four bits of value in element slot of the array of four
bit elements called c_list (controller list). The index slot is one-based.

.. _`srpt_get_class_port_info`:

srpt_get_class_port_info
========================

.. c:function:: void srpt_get_class_port_info(struct ib_dm_mad *mad)

    copy ClassPortInfo to a management datagram

    :param struct ib_dm_mad \*mad:
        Datagram that will be sent as response to DM_ATTR_CLASS_PORT_INFO.

.. _`srpt_get_class_port_info.description`:

Description
-----------

See also section 16.3.3.1 ClassPortInfo in the InfiniBand Architecture
Specification.

.. _`srpt_get_iou`:

srpt_get_iou
============

.. c:function:: void srpt_get_iou(struct ib_dm_mad *mad)

    write IOUnitInfo to a management datagram

    :param struct ib_dm_mad \*mad:
        Datagram that will be sent as response to DM_ATTR_IOU_INFO.

.. _`srpt_get_iou.description`:

Description
-----------

See also section 16.3.3.3 IOUnitInfo in the InfiniBand Architecture
Specification. See also section B.7, table B.6 in the SRP r16a document.

.. _`srpt_get_ioc`:

srpt_get_ioc
============

.. c:function:: void srpt_get_ioc(struct srpt_port *sport, u32 slot, struct ib_dm_mad *mad)

    write IOControllerprofile to a management datagram

    :param struct srpt_port \*sport:
        HCA port through which the MAD has been received.

    :param u32 slot:
        Slot number specified in DM_ATTR_IOC_PROFILE query.

    :param struct ib_dm_mad \*mad:
        Datagram that will be sent as response to DM_ATTR_IOC_PROFILE.

.. _`srpt_get_ioc.description`:

Description
-----------

See also section 16.3.3.4 IOControllerProfile in the InfiniBand
Architecture Specification. See also section B.7, table B.7 in the SRP
r16a document.

.. _`srpt_get_svc_entries`:

srpt_get_svc_entries
====================

.. c:function:: void srpt_get_svc_entries(u64 ioc_guid, u16 slot, u8 hi, u8 lo, struct ib_dm_mad *mad)

    write ServiceEntries to a management datagram

    :param u64 ioc_guid:
        I/O controller GUID to use in reply.

    :param u16 slot:
        I/O controller number.

    :param u8 hi:
        End of the range of service entries to be specified in the reply.

    :param u8 lo:
        Start of the range of service entries to be specified in the reply..

    :param struct ib_dm_mad \*mad:
        Datagram that will be sent as response to DM_ATTR_SVC_ENTRIES.

.. _`srpt_get_svc_entries.description`:

Description
-----------

See also section 16.3.3.5 ServiceEntries in the InfiniBand Architecture
Specification. See also section B.7, table B.8 in the SRP r16a document.

.. _`srpt_mgmt_method_get`:

srpt_mgmt_method_get
====================

.. c:function:: void srpt_mgmt_method_get(struct srpt_port *sp, struct ib_mad *rq_mad, struct ib_dm_mad *rsp_mad)

    process a received management datagram

    :param struct srpt_port \*sp:
        HCA port through which the MAD has been received.

    :param struct ib_mad \*rq_mad:
        received MAD.

    :param struct ib_dm_mad \*rsp_mad:
        response MAD.

.. _`srpt_mad_send_handler`:

srpt_mad_send_handler
=====================

.. c:function:: void srpt_mad_send_handler(struct ib_mad_agent *mad_agent, struct ib_mad_send_wc *mad_wc)

    MAD send completion callback

    :param struct ib_mad_agent \*mad_agent:
        Return value of \ :c:func:`ib_register_mad_agent`\ .

    :param struct ib_mad_send_wc \*mad_wc:
        Work completion reporting that the MAD has been sent.

.. _`srpt_mad_recv_handler`:

srpt_mad_recv_handler
=====================

.. c:function:: void srpt_mad_recv_handler(struct ib_mad_agent *mad_agent, struct ib_mad_send_buf *send_buf, struct ib_mad_recv_wc *mad_wc)

    MAD reception callback function

    :param struct ib_mad_agent \*mad_agent:
        Return value of \ :c:func:`ib_register_mad_agent`\ .

    :param struct ib_mad_send_buf \*send_buf:
        Not used.

    :param struct ib_mad_recv_wc \*mad_wc:
        Work completion reporting that a MAD has been received.

.. _`srpt_refresh_port`:

srpt_refresh_port
=================

.. c:function:: int srpt_refresh_port(struct srpt_port *sport)

    configure a HCA port

    :param struct srpt_port \*sport:
        SRPT HCA port.

.. _`srpt_refresh_port.description`:

Description
-----------

Enable InfiniBand management datagram processing, update the cached sm_lid,
lid and gid values, and register a callback function for processing MADs
on the specified port.

.. _`srpt_refresh_port.note`:

Note
----

It is safe to call this function more than once for the same port.

.. _`srpt_unregister_mad_agent`:

srpt_unregister_mad_agent
=========================

.. c:function:: void srpt_unregister_mad_agent(struct srpt_device *sdev)

    unregister MAD callback functions

    :param struct srpt_device \*sdev:
        SRPT HCA pointer.

.. _`srpt_unregister_mad_agent.note`:

Note
----

It is safe to call this function more than once for the same device.

.. _`srpt_alloc_ioctx`:

srpt_alloc_ioctx
================

.. c:function:: struct srpt_ioctx *srpt_alloc_ioctx(struct srpt_device *sdev, int ioctx_size, int dma_size, enum dma_data_direction dir)

    allocate a SRPT I/O context structure

    :param struct srpt_device \*sdev:
        SRPT HCA pointer.

    :param int ioctx_size:
        I/O context size.

    :param int dma_size:
        Size of I/O context DMA buffer.

    :param enum dma_data_direction dir:
        DMA data direction.

.. _`srpt_free_ioctx`:

srpt_free_ioctx
===============

.. c:function:: void srpt_free_ioctx(struct srpt_device *sdev, struct srpt_ioctx *ioctx, int dma_size, enum dma_data_direction dir)

    free a SRPT I/O context structure

    :param struct srpt_device \*sdev:
        SRPT HCA pointer.

    :param struct srpt_ioctx \*ioctx:
        I/O context pointer.

    :param int dma_size:
        Size of I/O context DMA buffer.

    :param enum dma_data_direction dir:
        DMA data direction.

.. _`srpt_alloc_ioctx_ring`:

srpt_alloc_ioctx_ring
=====================

.. c:function:: struct srpt_ioctx **srpt_alloc_ioctx_ring(struct srpt_device *sdev, int ring_size, int ioctx_size, int dma_size, enum dma_data_direction dir)

    allocate a ring of SRPT I/O context structures

    :param struct srpt_device \*sdev:
        Device to allocate the I/O context ring for.

    :param int ring_size:
        Number of elements in the I/O context ring.

    :param int ioctx_size:
        I/O context size.

    :param int dma_size:
        DMA buffer size.

    :param enum dma_data_direction dir:
        DMA data direction.

.. _`srpt_free_ioctx_ring`:

srpt_free_ioctx_ring
====================

.. c:function:: void srpt_free_ioctx_ring(struct srpt_ioctx **ioctx_ring, struct srpt_device *sdev, int ring_size, int dma_size, enum dma_data_direction dir)

    free the ring of SRPT I/O context structures

    :param struct srpt_ioctx \*\*ioctx_ring:
        I/O context ring to be freed.

    :param struct srpt_device \*sdev:
        SRPT HCA pointer.

    :param int ring_size:
        Number of ring elements.

    :param int dma_size:
        Size of I/O context DMA buffer.

    :param enum dma_data_direction dir:
        DMA data direction.

.. _`srpt_set_cmd_state`:

srpt_set_cmd_state
==================

.. c:function:: enum srpt_command_state srpt_set_cmd_state(struct srpt_send_ioctx *ioctx, enum srpt_command_state new)

    set the state of a SCSI command

    :param struct srpt_send_ioctx \*ioctx:
        Send I/O context.

    :param enum srpt_command_state new:
        New I/O context state.

.. _`srpt_set_cmd_state.description`:

Description
-----------

Does not modify the state of aborted commands. Returns the previous command
state.

.. _`srpt_test_and_set_cmd_state`:

srpt_test_and_set_cmd_state
===========================

.. c:function:: bool srpt_test_and_set_cmd_state(struct srpt_send_ioctx *ioctx, enum srpt_command_state old, enum srpt_command_state new)

    test and set the state of a command

    :param struct srpt_send_ioctx \*ioctx:
        Send I/O context.

    :param enum srpt_command_state old:
        Current I/O context state.

    :param enum srpt_command_state new:
        New I/O context state.

.. _`srpt_test_and_set_cmd_state.description`:

Description
-----------

Returns true if and only if the previous command state was equal to 'old'.

.. _`srpt_post_recv`:

srpt_post_recv
==============

.. c:function:: int srpt_post_recv(struct srpt_device *sdev, struct srpt_rdma_ch *ch, struct srpt_recv_ioctx *ioctx)

    post an IB receive request

    :param struct srpt_device \*sdev:
        SRPT HCA pointer.

    :param struct srpt_rdma_ch \*ch:
        SRPT RDMA channel.

    :param struct srpt_recv_ioctx \*ioctx:
        Receive I/O context pointer.

.. _`srpt_zerolength_write`:

srpt_zerolength_write
=====================

.. c:function:: int srpt_zerolength_write(struct srpt_rdma_ch *ch)

    perform a zero-length RDMA write

    :param struct srpt_rdma_ch \*ch:
        SRPT RDMA channel.

.. _`srpt_zerolength_write.a-quote-from-the-infiniband-specification`:

A quote from the InfiniBand specification
-----------------------------------------

C9-88: For an HCA responder
using Reliable Connection service, for each zero-length RDMA READ or WRITE
request, the R_Key shall not be validated, even if the request includes
Immediate data.

.. _`srpt_get_desc_tbl`:

srpt_get_desc_tbl
=================

.. c:function:: int srpt_get_desc_tbl(struct srpt_send_ioctx *ioctx, struct srp_cmd *srp_cmd, enum dma_data_direction *dir, struct scatterlist **sg, unsigned *sg_cnt, u64 *data_len)

    parse the data descriptors of a SRP_CMD request

    :param struct srpt_send_ioctx \*ioctx:
        Pointer to the I/O context associated with the request.

    :param struct srp_cmd \*srp_cmd:
        Pointer to the SRP_CMD request data.

    :param enum dma_data_direction \*dir:
        Pointer to the variable to which the transfer direction will be
        written.

    :param struct scatterlist \*\*sg:
        [out] scatterlist allocated for the parsed SRP_CMD.

    :param unsigned \*sg_cnt:
        [out] length of \ ``sg``\ .

    :param u64 \*data_len:
        Pointer to the variable to which the total data length of all
        descriptors in the SRP_CMD request will be written.

.. _`srpt_get_desc_tbl.description`:

Description
-----------

This function initializes ioctx->nrbuf and ioctx->r_bufs.

Returns -EINVAL when the SRP_CMD request contains inconsistent descriptors;
-ENOMEM when memory allocation fails and zero upon success.

.. _`srpt_init_ch_qp`:

srpt_init_ch_qp
===============

.. c:function:: int srpt_init_ch_qp(struct srpt_rdma_ch *ch, struct ib_qp *qp)

    initialize queue pair attributes

    :param struct srpt_rdma_ch \*ch:
        SRPT RDMA channel.

    :param struct ib_qp \*qp:
        Queue pair pointer.

.. _`srpt_init_ch_qp.description`:

Description
-----------

Initialized the attributes of queue pair 'qp' by allowing local write,
remote read and remote write. Also transitions 'qp' to state IB_QPS_INIT.

.. _`srpt_ch_qp_rtr`:

srpt_ch_qp_rtr
==============

.. c:function:: int srpt_ch_qp_rtr(struct srpt_rdma_ch *ch, struct ib_qp *qp)

    change the state of a channel to 'ready to receive' (RTR)

    :param struct srpt_rdma_ch \*ch:
        channel of the queue pair.

    :param struct ib_qp \*qp:
        queue pair to change the state of.

.. _`srpt_ch_qp_rtr.description`:

Description
-----------

Returns zero upon success and a negative value upon failure.

.. _`srpt_ch_qp_rtr.note`:

Note
----

currently a struct ib_qp_attr takes 136 bytes on a 64-bit system.
If this structure ever becomes larger, it might be necessary to allocate
it dynamically instead of on the stack.

.. _`srpt_ch_qp_rts`:

srpt_ch_qp_rts
==============

.. c:function:: int srpt_ch_qp_rts(struct srpt_rdma_ch *ch, struct ib_qp *qp)

    change the state of a channel to 'ready to send' (RTS)

    :param struct srpt_rdma_ch \*ch:
        channel of the queue pair.

    :param struct ib_qp \*qp:
        queue pair to change the state of.

.. _`srpt_ch_qp_rts.description`:

Description
-----------

Returns zero upon success and a negative value upon failure.

.. _`srpt_ch_qp_rts.note`:

Note
----

currently a struct ib_qp_attr takes 136 bytes on a 64-bit system.
If this structure ever becomes larger, it might be necessary to allocate
it dynamically instead of on the stack.

.. _`srpt_ch_qp_err`:

srpt_ch_qp_err
==============

.. c:function:: int srpt_ch_qp_err(struct srpt_rdma_ch *ch)

    set the channel queue pair state to 'error'

    :param struct srpt_rdma_ch \*ch:
        SRPT RDMA channel.

.. _`srpt_get_send_ioctx`:

srpt_get_send_ioctx
===================

.. c:function:: struct srpt_send_ioctx *srpt_get_send_ioctx(struct srpt_rdma_ch *ch)

    obtain an I/O context for sending to the initiator

    :param struct srpt_rdma_ch \*ch:
        SRPT RDMA channel.

.. _`srpt_abort_cmd`:

srpt_abort_cmd
==============

.. c:function:: int srpt_abort_cmd(struct srpt_send_ioctx *ioctx)

    abort a SCSI command

    :param struct srpt_send_ioctx \*ioctx:
        I/O context associated with the SCSI command.

.. _`srpt_rdma_read_done`:

srpt_rdma_read_done
===================

.. c:function:: void srpt_rdma_read_done(struct ib_cq *cq, struct ib_wc *wc)

    RDMA read completion callback

    :param struct ib_cq \*cq:
        Completion queue.

    :param struct ib_wc \*wc:
        Work completion.

.. _`srpt_rdma_read_done.xxx`:

XXX
---

what is now target_execute_cmd used to be asynchronous, and unmapping
the data that has been transferred via IB RDMA had to be postponed until the
\ :c:func:`check_stop_free`\  callback.  None of this is necessary anymore and needs to
be cleaned up.

.. _`srpt_build_cmd_rsp`:

srpt_build_cmd_rsp
==================

.. c:function:: int srpt_build_cmd_rsp(struct srpt_rdma_ch *ch, struct srpt_send_ioctx *ioctx, u64 tag, int status)

    build a SRP_RSP response

    :param struct srpt_rdma_ch \*ch:
        RDMA channel through which the request has been received.

    :param struct srpt_send_ioctx \*ioctx:
        I/O context associated with the SRP_CMD request. The response will
        be built in the buffer ioctx->buf points at and hence this function will
        overwrite the request data.

    :param u64 tag:
        tag of the request for which this response is being generated.

    :param int status:
        value for the STATUS field of the SRP_RSP information unit.

.. _`srpt_build_cmd_rsp.description`:

Description
-----------

Returns the size in bytes of the SRP_RSP response.

An SRP_RSP response contains a SCSI status or service response. See also
section 6.9 in the SRP r16a document for the format of an SRP_RSP
response. See also SPC-2 for more information about sense data.

.. _`srpt_build_tskmgmt_rsp`:

srpt_build_tskmgmt_rsp
======================

.. c:function:: int srpt_build_tskmgmt_rsp(struct srpt_rdma_ch *ch, struct srpt_send_ioctx *ioctx, u8 rsp_code, u64 tag)

    build a task management response

    :param struct srpt_rdma_ch \*ch:
        RDMA channel through which the request has been received.

    :param struct srpt_send_ioctx \*ioctx:
        I/O context in which the SRP_RSP response will be built.

    :param u8 rsp_code:
        RSP_CODE that will be stored in the response.

    :param u64 tag:
        Tag of the request for which this response is being generated.

.. _`srpt_build_tskmgmt_rsp.description`:

Description
-----------

Returns the size in bytes of the SRP_RSP response.

An SRP_RSP response contains a SCSI status or service response. See also
section 6.9 in the SRP r16a document for the format of an SRP_RSP
response.

.. _`srpt_handle_cmd`:

srpt_handle_cmd
===============

.. c:function:: void srpt_handle_cmd(struct srpt_rdma_ch *ch, struct srpt_recv_ioctx *recv_ioctx, struct srpt_send_ioctx *send_ioctx)

    process a SRP_CMD information unit

    :param struct srpt_rdma_ch \*ch:
        SRPT RDMA channel.

    :param struct srpt_recv_ioctx \*recv_ioctx:
        Receive I/O context.

    :param struct srpt_send_ioctx \*send_ioctx:
        Send I/O context.

.. _`srpt_handle_tsk_mgmt`:

srpt_handle_tsk_mgmt
====================

.. c:function:: void srpt_handle_tsk_mgmt(struct srpt_rdma_ch *ch, struct srpt_recv_ioctx *recv_ioctx, struct srpt_send_ioctx *send_ioctx)

    process a SRP_TSK_MGMT information unit

    :param struct srpt_rdma_ch \*ch:
        SRPT RDMA channel.

    :param struct srpt_recv_ioctx \*recv_ioctx:
        Receive I/O context.

    :param struct srpt_send_ioctx \*send_ioctx:
        Send I/O context.

.. _`srpt_handle_tsk_mgmt.description`:

Description
-----------

Returns 0 if and only if the request will be processed by the target core.

For more information about SRP_TSK_MGMT information units, see also section
6.7 in the SRP r16a document.

.. _`srpt_handle_new_iu`:

srpt_handle_new_iu
==================

.. c:function:: bool srpt_handle_new_iu(struct srpt_rdma_ch *ch, struct srpt_recv_ioctx *recv_ioctx)

    process a newly received information unit

    :param struct srpt_rdma_ch \*ch:
        RDMA channel through which the information unit has been received.

    :param struct srpt_recv_ioctx \*recv_ioctx:
        Receive I/O context associated with the information unit.

.. _`srpt_send_done`:

srpt_send_done
==============

.. c:function:: void srpt_send_done(struct ib_cq *cq, struct ib_wc *wc)

    send completion callback

    :param struct ib_cq \*cq:
        Completion queue.

    :param struct ib_wc \*wc:
        Work completion.

.. _`srpt_send_done.note`:

Note
----

Although this has not yet been observed during tests, at least in
theory it is possible that the \ :c:func:`srpt_get_send_ioctx`\  call invoked by
\ :c:func:`srpt_handle_new_iu`\  fails. This is possible because the req_lim_delta
value in each response is set to one, and it is possible that this response
makes the initiator send a new request before the send completion for that
response has been processed. This could e.g. happen if the call to
\ :c:func:`srpt_put_send_iotcx`\  is delayed because of a higher priority interrupt or
if IB retransmission causes generation of the send completion to be
delayed. Incoming information units for which \ :c:func:`srpt_get_send_ioctx`\  fails
are queued on cmd_wait_list. The code below processes these delayed
requests one at a time.

.. _`srpt_create_ch_ib`:

srpt_create_ch_ib
=================

.. c:function:: int srpt_create_ch_ib(struct srpt_rdma_ch *ch)

    create receive and send completion queues

    :param struct srpt_rdma_ch \*ch:
        SRPT RDMA channel.

.. _`srpt_close_ch`:

srpt_close_ch
=============

.. c:function:: bool srpt_close_ch(struct srpt_rdma_ch *ch)

    close a RDMA channel

    :param struct srpt_rdma_ch \*ch:
        SRPT RDMA channel.

.. _`srpt_close_ch.description`:

Description
-----------

Make sure all resources associated with the channel will be deallocated at
an appropriate time.

Returns true if and only if the channel state has been modified into
CH_DRAINING.

.. _`srpt_cm_req_recv`:

srpt_cm_req_recv
================

.. c:function:: int srpt_cm_req_recv(struct srpt_device *const sdev, struct ib_cm_id *ib_cm_id, struct rdma_cm_id *rdma_cm_id, u8 port_num, __be16 pkey, const struct srp_login_req *req, const char *src_addr)

    process the event IB_CM_REQ_RECEIVED

    :param struct srpt_device \*const sdev:
        HCA through which the login request was received.

    :param struct ib_cm_id \*ib_cm_id:
        IB/CM connection identifier in case of IB/CM.

    :param struct rdma_cm_id \*rdma_cm_id:
        RDMA/CM connection identifier in case of RDMA/CM.

    :param u8 port_num:
        Port through which the REQ message was received.

    :param __be16 pkey:
        P_Key of the incoming connection.

    :param const struct srp_login_req \*req:
        SRP login request.

    :param const char \*src_addr:
        GID (IB/CM) or IP address (RDMA/CM) of the port that submitted
        the login request.

.. _`srpt_cm_req_recv.description`:

Description
-----------

Ownership of the cm_id is transferred to the target session if this
function returns zero. Otherwise the caller remains the owner of cm_id.

.. _`srpt_cm_rtu_recv`:

srpt_cm_rtu_recv
================

.. c:function:: void srpt_cm_rtu_recv(struct srpt_rdma_ch *ch)

    process an IB_CM_RTU_RECEIVED or USER_ESTABLISHED event

    :param struct srpt_rdma_ch \*ch:
        SRPT RDMA channel.

.. _`srpt_cm_rtu_recv.description`:

Description
-----------

An RTU (ready to use) message indicates that the connection has been
established and that the recipient may begin transmitting.

.. _`srpt_cm_handler`:

srpt_cm_handler
===============

.. c:function:: int srpt_cm_handler(struct ib_cm_id *cm_id, struct ib_cm_event *event)

    IB connection manager callback function

    :param struct ib_cm_id \*cm_id:
        IB/CM connection identifier.

    :param struct ib_cm_event \*event:
        IB/CM event.

.. _`srpt_cm_handler.description`:

Description
-----------

A non-zero return value will cause the caller destroy the CM ID.

.. _`srpt_cm_handler.note`:

Note
----

\ :c:func:`srpt_cm_handler`\  must only return a non-zero value when transferring
ownership of the cm_id to a channel by \ :c:func:`srpt_cm_req_recv`\  failed. Returning
a non-zero value in any other case will trigger a race with the
\ :c:func:`ib_destroy_cm_id`\  call in \ :c:func:`srpt_release_channel`\ .

.. _`srpt_queue_response`:

srpt_queue_response
===================

.. c:function:: void srpt_queue_response(struct se_cmd *cmd)

    transmit the response to a SCSI command

    :param struct se_cmd \*cmd:
        SCSI target command.

.. _`srpt_queue_response.description`:

Description
-----------

Callback function called by the TCM core. Must not block since it can be
invoked on the context of the IB completion handler.

.. _`srpt_release_sport`:

srpt_release_sport
==================

.. c:function:: int srpt_release_sport(struct srpt_port *sport)

    disable login and wait for associated channels

    :param struct srpt_port \*sport:
        SRPT HCA port.

.. _`srpt_add_one`:

srpt_add_one
============

.. c:function:: void srpt_add_one(struct ib_device *device)

    InfiniBand device addition callback function

    :param struct ib_device \*device:
        Describes a HCA.

.. _`srpt_remove_one`:

srpt_remove_one
===============

.. c:function:: void srpt_remove_one(struct ib_device *device, void *client_data)

    InfiniBand device removal callback function

    :param struct ib_device \*device:
        Describes a HCA.

    :param void \*client_data:
        The value passed as the third argument to \ :c:func:`ib_set_client_data`\ .

.. _`srpt_close_session`:

srpt_close_session
==================

.. c:function:: void srpt_close_session(struct se_session *se_sess)

    forcibly close a session

    :param struct se_session \*se_sess:
        SCSI target session.

.. _`srpt_close_session.description`:

Description
-----------

Callback function invoked by the TCM core to clean up sessions associated
with a node ACL when the user invokes
rmdir /sys/kernel/config/target/$driver/$port/$tpg/acls/$i_port_id

.. _`srpt_sess_get_index`:

srpt_sess_get_index
===================

.. c:function:: u32 srpt_sess_get_index(struct se_session *se_sess)

    return the value of scsiAttIntrPortIndex (SCSI-MIB)

    :param struct se_session \*se_sess:
        SCSI target session.

.. _`srpt_sess_get_index.description`:

Description
-----------

A quote from RFC 4455 (SCSI-MIB) about this MIB object:
This object represents an arbitrary integer used to uniquely identify a
particular attached remote initiator port to a particular SCSI target port
within a particular SCSI target device within a particular SCSI instance.

.. _`srpt_parse_i_port_id`:

srpt_parse_i_port_id
====================

.. c:function:: int srpt_parse_i_port_id(u8 i_port_id, const char *name)

    parse an initiator port ID

    :param u8 i_port_id:
        Binary 128-bit port ID.

    :param const char \*name:
        ASCII representation of a 128-bit initiator port ID.

.. _`srpt_make_tpg`:

srpt_make_tpg
=============

.. c:function:: struct se_portal_group *srpt_make_tpg(struct se_wwn *wwn, struct config_group *group, const char *name)

    configfs callback invoked for mkdir /sys/kernel/config/target/$driver/$port/$tpg

    :param struct se_wwn \*wwn:
        Corresponds to \ ``$driver``\ /$port.

    :param struct config_group \*group:
        Not used.

    :param const char \*name:
        \ ``$tpg``\ .

.. _`srpt_drop_tpg`:

srpt_drop_tpg
=============

.. c:function:: void srpt_drop_tpg(struct se_portal_group *tpg)

    configfs callback invoked for rmdir /sys/kernel/config/target/$driver/$port/$tpg

    :param struct se_portal_group \*tpg:
        Target portal group to deregister.

.. _`srpt_make_tport`:

srpt_make_tport
===============

.. c:function:: struct se_wwn *srpt_make_tport(struct target_fabric_configfs *tf, struct config_group *group, const char *name)

    configfs callback invoked for mkdir /sys/kernel/config/target/$driver/$port

    :param struct target_fabric_configfs \*tf:
        Not used.

    :param struct config_group \*group:
        Not used.

    :param const char \*name:
        \ ``$port``\ .

.. _`srpt_drop_tport`:

srpt_drop_tport
===============

.. c:function:: void srpt_drop_tport(struct se_wwn *wwn)

    configfs callback invoked for rmdir /sys/kernel/config/target/$driver/$port

    :param struct se_wwn \*wwn:
        \ ``$port``\ .

.. _`srpt_init_module`:

srpt_init_module
================

.. c:function:: int srpt_init_module( void)

    kernel module initialization

    :param  void:
        no arguments

.. _`srpt_init_module.note`:

Note
----

Since \ :c:func:`ib_register_client`\  registers callback functions, and since at
least one of these callback functions (srpt_add_one()) calls target core
functions, this driver must be registered with the target core before
\ :c:func:`ib_register_client`\  is called.

.. This file was automatic generated / don't edit.

