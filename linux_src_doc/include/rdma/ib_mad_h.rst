.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/ib_mad.h

.. _`ib_get_cpi_resp_time`:

ib_get_cpi_resp_time
====================

.. c:function:: u8 ib_get_cpi_resp_time(struct ib_class_port_info *cpi)

    Returns the resp_time value from cap_mask2_resp_time in ib_class_port_info.

    :param cpi:
        A struct ib_class_port_info mad.
    :type cpi: struct ib_class_port_info \*

.. _`ib_set_cpi_resp_time`:

ib_set_cpi_resp_time
====================

.. c:function:: void ib_set_cpi_resp_time(struct ib_class_port_info *cpi, u8 rtime)

    Sets the response time in an ib_class_port_info mad.

    :param cpi:
        A struct ib_class_port_info.
    :type cpi: struct ib_class_port_info \*

    :param rtime:
        The response time to set.
    :type rtime: u8

.. _`ib_get_cpi_capmask2`:

ib_get_cpi_capmask2
===================

.. c:function:: u32 ib_get_cpi_capmask2(struct ib_class_port_info *cpi)

    Returns the capmask2 value from cap_mask2_resp_time in ib_class_port_info.

    :param cpi:
        A struct ib_class_port_info mad.
    :type cpi: struct ib_class_port_info \*

.. _`ib_set_cpi_capmask2`:

ib_set_cpi_capmask2
===================

.. c:function:: void ib_set_cpi_capmask2(struct ib_class_port_info *cpi, u32 capmask2)

    Sets the capmask2 in an ib_class_port_info mad.

    :param cpi:
        A struct ib_class_port_info.
    :type cpi: struct ib_class_port_info \*

    :param capmask2:
        The capmask2 to set.
    :type capmask2: u32

.. _`opa_get_cpi_capmask2`:

opa_get_cpi_capmask2
====================

.. c:function:: u32 opa_get_cpi_capmask2(struct opa_class_port_info *cpi)

    Returns the capmask2 value from cap_mask2_resp_time in ib_class_port_info.

    :param cpi:
        A struct opa_class_port_info mad.
    :type cpi: struct opa_class_port_info \*

.. _`ib_response_mad`:

ib_response_mad
===============

.. c:function:: int ib_response_mad(const struct ib_mad_hdr *hdr)

    Returns if the specified MAD has been generated in response to a sent request or trap.

    :param hdr:
        *undescribed*
    :type hdr: const struct ib_mad_hdr \*

.. _`ib_get_rmpp_resptime`:

ib_get_rmpp_resptime
====================

.. c:function:: u8 ib_get_rmpp_resptime(struct ib_rmpp_hdr *rmpp_hdr)

    Returns the RMPP response time.

    :param rmpp_hdr:
        An RMPP header.
    :type rmpp_hdr: struct ib_rmpp_hdr \*

.. _`ib_get_rmpp_flags`:

ib_get_rmpp_flags
=================

.. c:function:: u8 ib_get_rmpp_flags(struct ib_rmpp_hdr *rmpp_hdr)

    Returns the RMPP flags.

    :param rmpp_hdr:
        An RMPP header.
    :type rmpp_hdr: struct ib_rmpp_hdr \*

.. _`ib_set_rmpp_resptime`:

ib_set_rmpp_resptime
====================

.. c:function:: void ib_set_rmpp_resptime(struct ib_rmpp_hdr *rmpp_hdr, u8 rtime)

    Sets the response time in an RMPP header.

    :param rmpp_hdr:
        An RMPP header.
    :type rmpp_hdr: struct ib_rmpp_hdr \*

    :param rtime:
        The response time to set.
    :type rtime: u8

.. _`ib_set_rmpp_flags`:

ib_set_rmpp_flags
=================

.. c:function:: void ib_set_rmpp_flags(struct ib_rmpp_hdr *rmpp_hdr, u8 flags)

    Sets the flags in an RMPP header.

    :param rmpp_hdr:
        An RMPP header.
    :type rmpp_hdr: struct ib_rmpp_hdr \*

    :param flags:
        The flags to set.
    :type flags: u8

.. _`ib_mad_send_handler`:

ib_mad_send_handler
===================

.. c:function:: void ib_mad_send_handler(struct ib_mad_agent *mad_agent, struct ib_mad_send_wc *mad_send_wc)

    callback handler for a sent MAD.

    :param mad_agent:
        MAD agent that sent the MAD.
    :type mad_agent: struct ib_mad_agent \*

    :param mad_send_wc:
        Send work completion information on the sent MAD.
    :type mad_send_wc: struct ib_mad_send_wc \*

.. _`ib_mad_snoop_handler`:

ib_mad_snoop_handler
====================

.. c:function:: void ib_mad_snoop_handler(struct ib_mad_agent *mad_agent, struct ib_mad_send_buf *send_buf, struct ib_mad_send_wc *mad_send_wc)

    Callback handler for snooping sent MADs.

    :param mad_agent:
        MAD agent that snooped the MAD.
    :type mad_agent: struct ib_mad_agent \*

    :param send_buf:
        send MAD data buffer.
    :type send_buf: struct ib_mad_send_buf \*

    :param mad_send_wc:
        Work completion information on the sent MAD.  Valid
        only for snooping that occurs on a send completion.
    :type mad_send_wc: struct ib_mad_send_wc \*

.. _`ib_mad_snoop_handler.description`:

Description
-----------

Clients snooping MADs should not modify data referenced by the \ ``send_buf``\ 
or \ ``mad_send_wc``\ .

.. _`ib_mad_recv_handler`:

ib_mad_recv_handler
===================

.. c:function:: void ib_mad_recv_handler(struct ib_mad_agent *mad_agent, struct ib_mad_send_buf *send_buf, struct ib_mad_recv_wc *mad_recv_wc)

    callback handler for a received MAD.

    :param mad_agent:
        MAD agent requesting the received MAD.
    :type mad_agent: struct ib_mad_agent \*

    :param send_buf:
        Send buffer if found, else NULL
    :type send_buf: struct ib_mad_send_buf \*

    :param mad_recv_wc:
        Received work completion information on the received MAD.
    :type mad_recv_wc: struct ib_mad_recv_wc \*

.. _`ib_mad_recv_handler.description`:

Description
-----------

MADs received in response to a send request operation will be handed to
the user before the send operation completes.  All data buffers given
to registered agents through this routine are owned by the receiving
client, except for snooping agents.  Clients snooping MADs should not
modify the data referenced by \ ``mad_recv_wc``\ .

.. _`ib_register_mad_agent`:

ib_register_mad_agent
=====================

.. c:function:: struct ib_mad_agent *ib_register_mad_agent(struct ib_device *device, u8 port_num, enum ib_qp_type qp_type, struct ib_mad_reg_req *mad_reg_req, u8 rmpp_version, ib_mad_send_handler send_handler, ib_mad_recv_handler recv_handler, void *context, u32 registration_flags)

    Register to send/receive MADs.

    :param device:
        The device to register with.
    :type device: struct ib_device \*

    :param port_num:
        The port on the specified device to use.
    :type port_num: u8

    :param qp_type:
        Specifies which QP to access.  Must be either
        IB_QPT_SMI or IB_QPT_GSI.
    :type qp_type: enum ib_qp_type

    :param mad_reg_req:
        Specifies which unsolicited MADs should be received
        by the caller.  This parameter may be NULL if the caller only
        wishes to receive solicited responses.
    :type mad_reg_req: struct ib_mad_reg_req \*

    :param rmpp_version:
        If set, indicates that the client will send
        and receive MADs that contain the RMPP header for the given version.
        If set to 0, indicates that RMPP is not used by this client.
    :type rmpp_version: u8

    :param send_handler:
        The completion callback routine invoked after a send
        request has completed.
    :type send_handler: ib_mad_send_handler

    :param recv_handler:
        The completion callback routine invoked for a received
        MAD.
    :type recv_handler: ib_mad_recv_handler

    :param context:
        User specified context associated with the registration.
    :type context: void \*

    :param registration_flags:
        Registration flags to set for this agent
    :type registration_flags: u32

.. _`ib_register_mad_snoop`:

ib_register_mad_snoop
=====================

.. c:function:: struct ib_mad_agent *ib_register_mad_snoop(struct ib_device *device, u8 port_num, enum ib_qp_type qp_type, int mad_snoop_flags, ib_mad_snoop_handler snoop_handler, ib_mad_recv_handler recv_handler, void *context)

    Register to snoop sent and received MADs.

    :param device:
        The device to register with.
    :type device: struct ib_device \*

    :param port_num:
        The port on the specified device to use.
    :type port_num: u8

    :param qp_type:
        Specifies which QP traffic to snoop.  Must be either
        IB_QPT_SMI or IB_QPT_GSI.
    :type qp_type: enum ib_qp_type

    :param mad_snoop_flags:
        Specifies information where snooping occurs.
    :type mad_snoop_flags: int

    :param snoop_handler:
        *undescribed*
    :type snoop_handler: ib_mad_snoop_handler

    :param recv_handler:
        The callback routine invoked for a snooped receive.
    :type recv_handler: ib_mad_recv_handler

    :param context:
        User specified context associated with the registration.
    :type context: void \*

.. _`ib_unregister_mad_agent`:

ib_unregister_mad_agent
=======================

.. c:function:: void ib_unregister_mad_agent(struct ib_mad_agent *mad_agent)

    Unregisters a client from using MAD services.

    :param mad_agent:
        Corresponding MAD registration request to deregister.
    :type mad_agent: struct ib_mad_agent \*

.. _`ib_unregister_mad_agent.description`:

Description
-----------

After invoking this routine, MAD services are no longer usable by the
client on the associated QP.

.. _`ib_post_send_mad`:

ib_post_send_mad
================

.. c:function:: int ib_post_send_mad(struct ib_mad_send_buf *send_buf, struct ib_mad_send_buf **bad_send_buf)

    Posts MAD(s) to the send queue of the QP associated with the registered client.

    :param send_buf:
        Specifies the information needed to send the MAD(s).
    :type send_buf: struct ib_mad_send_buf \*

    :param bad_send_buf:
        Specifies the MAD on which an error was encountered.  This
        parameter is optional if only a single MAD is posted.
    :type bad_send_buf: struct ib_mad_send_buf \*\*

.. _`ib_post_send_mad.description`:

Description
-----------

Sent MADs are not guaranteed to complete in the order that they were posted.

If the MAD requires RMPP, the data buffer should contain a single copy
of the common MAD, RMPP, and class specific headers, followed by the class
defined data.  If the class defined data would not divide evenly into
RMPP segments, then space must be allocated at the end of the referenced
buffer for any required padding.  To indicate the amount of class defined
data being transferred, the paylen_newwin field in the RMPP header should
be set to the size of the class specific header plus the amount of class
defined data being transferred.  The paylen_newwin field should be
specified in network-byte order.

.. _`ib_free_recv_mad`:

ib_free_recv_mad
================

.. c:function:: void ib_free_recv_mad(struct ib_mad_recv_wc *mad_recv_wc)

    Returns data buffers used to receive a MAD.

    :param mad_recv_wc:
        Work completion information for a received MAD.
    :type mad_recv_wc: struct ib_mad_recv_wc \*

.. _`ib_free_recv_mad.description`:

Description
-----------

Clients receiving MADs through their ib_mad_recv_handler must call this
routine to return the work completion buffers to the access layer.

.. _`ib_cancel_mad`:

ib_cancel_mad
=============

.. c:function:: void ib_cancel_mad(struct ib_mad_agent *mad_agent, struct ib_mad_send_buf *send_buf)

    Cancels an outstanding send MAD operation.

    :param mad_agent:
        Specifies the registration associated with sent MAD.
    :type mad_agent: struct ib_mad_agent \*

    :param send_buf:
        Indicates the MAD to cancel.
    :type send_buf: struct ib_mad_send_buf \*

.. _`ib_cancel_mad.description`:

Description
-----------

MADs will be returned to the user through the corresponding
ib_mad_send_handler.

.. _`ib_modify_mad`:

ib_modify_mad
=============

.. c:function:: int ib_modify_mad(struct ib_mad_agent *mad_agent, struct ib_mad_send_buf *send_buf, u32 timeout_ms)

    Modifies an outstanding send MAD operation.

    :param mad_agent:
        Specifies the registration associated with sent MAD.
    :type mad_agent: struct ib_mad_agent \*

    :param send_buf:
        Indicates the MAD to modify.
    :type send_buf: struct ib_mad_send_buf \*

    :param timeout_ms:
        New timeout value for sent MAD.
    :type timeout_ms: u32

.. _`ib_modify_mad.description`:

Description
-----------

This call will reset the timeout value for a sent MAD to the specified
value.

.. _`ib_redirect_mad_qp`:

ib_redirect_mad_qp
==================

.. c:function:: struct ib_mad_agent *ib_redirect_mad_qp(struct ib_qp *qp, u8 rmpp_version, ib_mad_send_handler send_handler, ib_mad_recv_handler recv_handler, void *context)

    Registers a QP for MAD services.

    :param qp:
        Reference to a QP that requires MAD services.
    :type qp: struct ib_qp \*

    :param rmpp_version:
        If set, indicates that the client will send
        and receive MADs that contain the RMPP header for the given version.
        If set to 0, indicates that RMPP is not used by this client.
    :type rmpp_version: u8

    :param send_handler:
        The completion callback routine invoked after a send
        request has completed.
    :type send_handler: ib_mad_send_handler

    :param recv_handler:
        The completion callback routine invoked for a received
        MAD.
    :type recv_handler: ib_mad_recv_handler

    :param context:
        User specified context associated with the registration.
    :type context: void \*

.. _`ib_redirect_mad_qp.description`:

Description
-----------

Use of this call allows clients to use MAD services, such as RMPP,
on user-owned QPs.  After calling this routine, users may send
MADs on the specified QP by calling ib_mad_post_send.

.. _`ib_process_mad_wc`:

ib_process_mad_wc
=================

.. c:function:: int ib_process_mad_wc(struct ib_mad_agent *mad_agent, struct ib_wc *wc)

    Processes a work completion associated with a MAD sent or received on a redirected QP.

    :param mad_agent:
        Specifies the registered MAD service using the redirected QP.
    :type mad_agent: struct ib_mad_agent \*

    :param wc:
        References a work completion associated with a sent or received
        MAD segment.
    :type wc: struct ib_wc \*

.. _`ib_process_mad_wc.description`:

Description
-----------

This routine is used to complete or continue processing on a MAD request.
If the work completion is associated with a send operation, calling
this routine is required to continue an RMPP transfer or to wait for a
corresponding response, if it is a request.  If the work completion is
associated with a receive operation, calling this routine is required to
process an inbound or outbound RMPP transfer, or to match a response MAD
with its corresponding request.

.. _`ib_create_send_mad`:

ib_create_send_mad
==================

.. c:function:: struct ib_mad_send_buf *ib_create_send_mad(struct ib_mad_agent *mad_agent, u32 remote_qpn, u16 pkey_index, int rmpp_active, int hdr_len, int data_len, gfp_t gfp_mask, u8 base_version)

    Allocate and initialize a data buffer and work request for sending a MAD.

    :param mad_agent:
        Specifies the registered MAD service to associate with the MAD.
    :type mad_agent: struct ib_mad_agent \*

    :param remote_qpn:
        Specifies the QPN of the receiving node.
    :type remote_qpn: u32

    :param pkey_index:
        Specifies which PKey the MAD will be sent using.  This field
        is valid only if the remote_qpn is QP 1.
    :type pkey_index: u16

    :param rmpp_active:
        Indicates if the send will enable RMPP.
    :type rmpp_active: int

    :param hdr_len:
        Indicates the size of the data header of the MAD.  This length
        should include the common MAD header, RMPP header, plus any class
        specific header.
    :type hdr_len: int

    :param data_len:
        Indicates the size of any user-transferred data.  The call will
        automatically adjust the allocated buffer size to account for any
        additional padding that may be necessary.
    :type data_len: int

    :param gfp_mask:
        GFP mask used for the memory allocation.
    :type gfp_mask: gfp_t

    :param base_version:
        Base Version of this MAD
    :type base_version: u8

.. _`ib_create_send_mad.description`:

Description
-----------

This routine allocates a MAD for sending.  The returned MAD send buffer
will reference a data buffer usable for sending a MAD, along
with an initialized work request structure.  Users may modify the returned
MAD data buffer before posting the send.

The returned MAD header, class specific headers, and any padding will be
cleared.  Users are responsible for initializing the common MAD header,
any class specific header, and MAD data area.
If \ ``rmpp_active``\  is set, the RMPP header will be initialized for sending.

.. _`ib_is_mad_class_rmpp`:

ib_is_mad_class_rmpp
====================

.. c:function:: int ib_is_mad_class_rmpp(u8 mgmt_class)

    returns whether given management class supports RMPP.

    :param mgmt_class:
        management class
    :type mgmt_class: u8

.. _`ib_is_mad_class_rmpp.description`:

Description
-----------

This routine returns whether the management class supports RMPP.

.. _`ib_get_mad_data_offset`:

ib_get_mad_data_offset
======================

.. c:function:: int ib_get_mad_data_offset(u8 mgmt_class)

    returns the data offset for a given management class.

    :param mgmt_class:
        management class
    :type mgmt_class: u8

.. _`ib_get_mad_data_offset.description`:

Description
-----------

This routine returns the data offset in the MAD for the management
class requested.

.. _`ib_get_rmpp_segment`:

ib_get_rmpp_segment
===================

.. c:function:: void *ib_get_rmpp_segment(struct ib_mad_send_buf *send_buf, int seg_num)

    returns the data buffer for a given RMPP segment.

    :param send_buf:
        Previously allocated send data buffer.
    :type send_buf: struct ib_mad_send_buf \*

    :param seg_num:
        number of segment to return
    :type seg_num: int

.. _`ib_get_rmpp_segment.description`:

Description
-----------

This routine returns a pointer to the data buffer of an RMPP MAD.
Users must provide synchronization to \ ``send_buf``\  around this call.

.. _`ib_free_send_mad`:

ib_free_send_mad
================

.. c:function:: void ib_free_send_mad(struct ib_mad_send_buf *send_buf)

    Returns data buffers used to send a MAD.

    :param send_buf:
        Previously allocated send data buffer.
    :type send_buf: struct ib_mad_send_buf \*

.. _`ib_mad_kernel_rmpp_agent`:

ib_mad_kernel_rmpp_agent
========================

.. c:function:: int ib_mad_kernel_rmpp_agent(const struct ib_mad_agent *agent)

    Returns if the agent is performing RMPP.

    :param agent:
        the agent in question
    :type agent: const struct ib_mad_agent \*

.. This file was automatic generated / don't edit.

