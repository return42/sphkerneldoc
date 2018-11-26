.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libfc/fc_lport.c

.. _`fc_bsg_info`:

struct fc_bsg_info
==================

.. c:type:: struct fc_bsg_info

    FC Passthrough managemet structure

.. _`fc_bsg_info.definition`:

Definition
----------

.. code-block:: c

    struct fc_bsg_info {
        struct bsg_job *job;
        struct fc_lport *lport;
        u16 rsp_code;
        struct scatterlist *sg;
        u32 nents;
        size_t offset;
    }

.. _`fc_bsg_info.members`:

Members
-------

job
    The passthrough job

lport
    The local port to pass through a command

rsp_code
    The expected response code

sg
    job->reply_payload.sg_list

nents
    job->reply_payload.sg_cnt

offset
    The offset into the response data

.. _`fc_frame_drop`:

fc_frame_drop
=============

.. c:function:: int fc_frame_drop(struct fc_lport *lport, struct fc_frame *fp)

    Dummy frame handler

    :param lport:
        The local port the frame was received on
    :type lport: struct fc_lport \*

    :param fp:
        The received frame
    :type fp: struct fc_frame \*

.. _`fc_lport_rport_callback`:

fc_lport_rport_callback
=======================

.. c:function:: void fc_lport_rport_callback(struct fc_lport *lport, struct fc_rport_priv *rdata, enum fc_rport_event event)

    Event handler for rport events

    :param lport:
        The lport which is receiving the event
    :type lport: struct fc_lport \*

    :param rdata:
        private remote port data
    :type rdata: struct fc_rport_priv \*

    :param event:
        The event that occurred
    :type event: enum fc_rport_event

.. _`fc_lport_rport_callback.locking-note`:

Locking Note
------------

The rport lock should not be held when calling
this function.

.. _`fc_lport_state`:

fc_lport_state
==============

.. c:function:: const char *fc_lport_state(struct fc_lport *lport)

    Return a string which represents the lport's state

    :param lport:
        The lport whose state is to converted to a string
    :type lport: struct fc_lport \*

.. _`fc_lport_ptp_setup`:

fc_lport_ptp_setup
==================

.. c:function:: void fc_lport_ptp_setup(struct fc_lport *lport, u32 remote_fid, u64 remote_wwpn, u64 remote_wwnn)

    Create an rport for point-to-point mode

    :param lport:
        The lport to attach the ptp rport to
    :type lport: struct fc_lport \*

    :param remote_fid:
        The FID of the ptp rport
    :type remote_fid: u32

    :param remote_wwpn:
        The WWPN of the ptp rport
    :type remote_wwpn: u64

    :param remote_wwnn:
        The WWNN of the ptp rport
    :type remote_wwnn: u64

.. _`fc_get_host_port_state`:

fc_get_host_port_state
======================

.. c:function:: void fc_get_host_port_state(struct Scsi_Host *shost)

    Return the port state of the given Scsi_Host

    :param shost:
        The SCSI host whose port state is to be determined
    :type shost: struct Scsi_Host \*

.. _`fc_get_host_speed`:

fc_get_host_speed
=================

.. c:function:: void fc_get_host_speed(struct Scsi_Host *shost)

    Return the speed of the given Scsi_Host

    :param shost:
        The SCSI host whose port speed is to be determined
    :type shost: struct Scsi_Host \*

.. _`fc_get_host_stats`:

fc_get_host_stats
=================

.. c:function:: struct fc_host_statistics *fc_get_host_stats(struct Scsi_Host *shost)

    Return the Scsi_Host's statistics

    :param shost:
        The SCSI host whose statistics are to be returned
    :type shost: struct Scsi_Host \*

.. _`fc_lport_flogi_fill`:

fc_lport_flogi_fill
===================

.. c:function:: void fc_lport_flogi_fill(struct fc_lport *lport, struct fc_els_flogi *flogi, unsigned int op)

    Fill in FLOGI command for request

    :param lport:
        The local port the FLOGI is for
    :type lport: struct fc_lport \*

    :param flogi:
        The FLOGI command
    :type flogi: struct fc_els_flogi \*

    :param op:
        The opcode
    :type op: unsigned int

.. _`fc_lport_add_fc4_type`:

fc_lport_add_fc4_type
=====================

.. c:function:: void fc_lport_add_fc4_type(struct fc_lport *lport, enum fc_fh_type type)

    Add a supported FC-4 type to a local port

    :param lport:
        The local port to add a new FC-4 type to
    :type lport: struct fc_lport \*

    :param type:
        The new FC-4 type
    :type type: enum fc_fh_type

.. _`fc_lport_recv_rlir_req`:

fc_lport_recv_rlir_req
======================

.. c:function:: void fc_lport_recv_rlir_req(struct fc_lport *lport, struct fc_frame *fp)

    Handle received Registered Link Incident Report.

    :param lport:
        Fibre Channel local port receiving the RLIR
    :type lport: struct fc_lport \*

    :param fp:
        The RLIR request frame
    :type fp: struct fc_frame \*

.. _`fc_lport_recv_echo_req`:

fc_lport_recv_echo_req
======================

.. c:function:: void fc_lport_recv_echo_req(struct fc_lport *lport, struct fc_frame *in_fp)

    Handle received ECHO request

    :param lport:
        The local port receiving the ECHO
    :type lport: struct fc_lport \*

    :param in_fp:
        *undescribed*
    :type in_fp: struct fc_frame \*

.. _`fc_lport_recv_rnid_req`:

fc_lport_recv_rnid_req
======================

.. c:function:: void fc_lport_recv_rnid_req(struct fc_lport *lport, struct fc_frame *in_fp)

    Handle received Request Node ID data request

    :param lport:
        The local port receiving the RNID
    :type lport: struct fc_lport \*

    :param in_fp:
        *undescribed*
    :type in_fp: struct fc_frame \*

.. _`fc_lport_recv_logo_req`:

fc_lport_recv_logo_req
======================

.. c:function:: void fc_lport_recv_logo_req(struct fc_lport *lport, struct fc_frame *fp)

    Handle received fabric LOGO request

    :param lport:
        The local port receiving the LOGO
    :type lport: struct fc_lport \*

    :param fp:
        The LOGO request frame
    :type fp: struct fc_frame \*

.. _`fc_fabric_login`:

fc_fabric_login
===============

.. c:function:: int fc_fabric_login(struct fc_lport *lport)

    Start the lport state machine

    :param lport:
        The local port that should log into the fabric
    :type lport: struct fc_lport \*

.. _`fc_fabric_login.locking-note`:

Locking Note
------------

This function should not be called
with the lport lock held.

.. _`__fc_linkup`:

\__fc_linkup
============

.. c:function:: void __fc_linkup(struct fc_lport *lport)

    Handler for transport linkup events

    :param lport:
        The lport whose link is up
    :type lport: struct fc_lport \*

.. _`fc_linkup`:

fc_linkup
=========

.. c:function:: void fc_linkup(struct fc_lport *lport)

    Handler for transport linkup events

    :param lport:
        The local port whose link is up
    :type lport: struct fc_lport \*

.. _`__fc_linkdown`:

\__fc_linkdown
==============

.. c:function:: void __fc_linkdown(struct fc_lport *lport)

    Handler for transport linkdown events

    :param lport:
        The lport whose link is down
    :type lport: struct fc_lport \*

.. _`fc_linkdown`:

fc_linkdown
===========

.. c:function:: void fc_linkdown(struct fc_lport *lport)

    Handler for transport linkdown events

    :param lport:
        The local port whose link is down
    :type lport: struct fc_lport \*

.. _`fc_fabric_logoff`:

fc_fabric_logoff
================

.. c:function:: int fc_fabric_logoff(struct fc_lport *lport)

    Logout of the fabric

    :param lport:
        The local port to logoff the fabric
    :type lport: struct fc_lport \*

.. _`fc_fabric_logoff.return-value`:

Return value
------------

0 for success, -1 for failure

.. _`fc_lport_destroy`:

fc_lport_destroy
================

.. c:function:: int fc_lport_destroy(struct fc_lport *lport)

    Unregister a fc_lport

    :param lport:
        The local port to unregister
    :type lport: struct fc_lport \*

.. _`fc_lport_destroy.note`:

Note
----

exit routine for fc_lport instance
clean-up all the allocated memory
and free up other system resources.

.. _`fc_set_mfs`:

fc_set_mfs
==========

.. c:function:: int fc_set_mfs(struct fc_lport *lport, u32 mfs)

    Set the maximum frame size for a local port

    :param lport:
        The local port to set the MFS for
    :type lport: struct fc_lport \*

    :param mfs:
        The new MFS
    :type mfs: u32

.. _`fc_lport_disc_callback`:

fc_lport_disc_callback
======================

.. c:function:: void fc_lport_disc_callback(struct fc_lport *lport, enum fc_disc_event event)

    Callback for discovery events

    :param lport:
        The local port receiving the event
    :type lport: struct fc_lport \*

    :param event:
        The discovery event
    :type event: enum fc_disc_event

.. _`fc_lport_enter_ready`:

fc_lport_enter_ready
====================

.. c:function:: void fc_lport_enter_ready(struct fc_lport *lport)

    Enter the ready state and start discovery

    :param lport:
        The local port that is ready
    :type lport: struct fc_lport \*

.. _`fc_lport_set_port_id`:

fc_lport_set_port_id
====================

.. c:function:: void fc_lport_set_port_id(struct fc_lport *lport, u32 port_id, struct fc_frame *fp)

    set the local port Port ID

    :param lport:
        The local port which will have its Port ID set.
    :type lport: struct fc_lport \*

    :param port_id:
        The new port ID.
    :type port_id: u32

    :param fp:
        The frame containing the incoming request, or NULL.
    :type fp: struct fc_frame \*

.. _`fc_lport_set_local_id`:

fc_lport_set_local_id
=====================

.. c:function:: void fc_lport_set_local_id(struct fc_lport *lport, u32 port_id)

    set the local port Port ID for point-to-multipoint

    :param lport:
        The local port which will have its Port ID set.
    :type lport: struct fc_lport \*

    :param port_id:
        The new port ID.
    :type port_id: u32

.. _`fc_lport_set_local_id.description`:

Description
-----------

Called by the lower-level driver when transport sets the local port_id.
This is used in VN_port to VN_port mode for FCoE, and causes FLOGI and
discovery to be skipped.

.. _`fc_lport_recv_flogi_req`:

fc_lport_recv_flogi_req
=======================

.. c:function:: void fc_lport_recv_flogi_req(struct fc_lport *lport, struct fc_frame *rx_fp)

    Receive a FLOGI request

    :param lport:
        The local port that received the request
    :type lport: struct fc_lport \*

    :param rx_fp:
        The FLOGI frame
    :type rx_fp: struct fc_frame \*

.. _`fc_lport_recv_flogi_req.description`:

Description
-----------

A received FLOGI request indicates a point-to-point connection.
Accept it with the common service parameters indicating our N port.
Set up to do a PLOGI if we have the higher-number WWPN.

.. _`fc_lport_recv_els_req`:

fc_lport_recv_els_req
=====================

.. c:function:: void fc_lport_recv_els_req(struct fc_lport *lport, struct fc_frame *fp)

    The generic lport ELS request handler

    :param lport:
        The local port that received the request
    :type lport: struct fc_lport \*

    :param fp:
        The request frame
    :type fp: struct fc_frame \*

.. _`fc_lport_recv_els_req.description`:

Description
-----------

This function will see if the lport handles the request or
if an rport should handle the request.

.. _`fc_lport_recv_els_req.locking-note`:

Locking Note
------------

This function should not be called with the lport
lock held because it will grab the lock.

.. _`fc_lport_recv`:

fc_lport_recv
=============

.. c:function:: void fc_lport_recv(struct fc_lport *lport, struct fc_frame *fp)

    The generic lport request handler

    :param lport:
        The lport that received the request
    :type lport: struct fc_lport \*

    :param fp:
        The frame the request is in
    :type fp: struct fc_frame \*

.. _`fc_lport_recv.locking-note`:

Locking Note
------------

This function should not be called with the lport
lock held because it may grab the lock.

.. _`fc_lport_reset`:

fc_lport_reset
==============

.. c:function:: int fc_lport_reset(struct fc_lport *lport)

    Reset a local port

    :param lport:
        The local port which should be reset
    :type lport: struct fc_lport \*

.. _`fc_lport_reset.locking-note`:

Locking Note
------------

This functions should not be called with the
lport lock held.

.. _`fc_lport_reset_locked`:

fc_lport_reset_locked
=====================

.. c:function:: void fc_lport_reset_locked(struct fc_lport *lport)

    Reset the local port w/ the lport lock held

    :param lport:
        The local port to be reset
    :type lport: struct fc_lport \*

.. _`fc_lport_enter_reset`:

fc_lport_enter_reset
====================

.. c:function:: void fc_lport_enter_reset(struct fc_lport *lport)

    Reset the local port

    :param lport:
        The local port to be reset
    :type lport: struct fc_lport \*

.. _`fc_lport_enter_disabled`:

fc_lport_enter_disabled
=======================

.. c:function:: void fc_lport_enter_disabled(struct fc_lport *lport)

    Disable the local port

    :param lport:
        The local port to be reset
    :type lport: struct fc_lport \*

.. _`fc_lport_error`:

fc_lport_error
==============

.. c:function:: void fc_lport_error(struct fc_lport *lport, struct fc_frame *fp)

    Handler for any errors

    :param lport:
        The local port that the error was on
    :type lport: struct fc_lport \*

    :param fp:
        The error code encoded in a frame pointer
    :type fp: struct fc_frame \*

.. _`fc_lport_error.description`:

Description
-----------

If the error was caused by a resource allocation failure
then wait for half a second and retry, otherwise retry
after the e_d_tov time.

.. _`fc_lport_ns_resp`:

fc_lport_ns_resp
================

.. c:function:: void fc_lport_ns_resp(struct fc_seq *sp, struct fc_frame *fp, void *lp_arg)

    Handle response to a name server registration exchange

    :param sp:
        current sequence in exchange
    :type sp: struct fc_seq \*

    :param fp:
        response frame
    :type fp: struct fc_frame \*

    :param lp_arg:
        Fibre Channel host port instance
    :type lp_arg: void \*

.. _`fc_lport_ns_resp.locking-note`:

Locking Note
------------

This function will be called without the lport lock
held, but it will lock, call an \_enter\_\* function or \ :c:func:`fc_lport_error`\ 
and then unlock the lport.

.. _`fc_lport_ms_resp`:

fc_lport_ms_resp
================

.. c:function:: void fc_lport_ms_resp(struct fc_seq *sp, struct fc_frame *fp, void *lp_arg)

    Handle response to a management server exchange

    :param sp:
        current sequence in exchange
    :type sp: struct fc_seq \*

    :param fp:
        response frame
    :type fp: struct fc_frame \*

    :param lp_arg:
        Fibre Channel host port instance
    :type lp_arg: void \*

.. _`fc_lport_ms_resp.locking-note`:

Locking Note
------------

This function will be called without the lport lock
held, but it will lock, call an \_enter\_\* function or \ :c:func:`fc_lport_error`\ 
and then unlock the lport.

.. _`fc_lport_scr_resp`:

fc_lport_scr_resp
=================

.. c:function:: void fc_lport_scr_resp(struct fc_seq *sp, struct fc_frame *fp, void *lp_arg)

    Handle response to State Change Register (SCR) request

    :param sp:
        current sequence in SCR exchange
    :type sp: struct fc_seq \*

    :param fp:
        response frame
    :type fp: struct fc_frame \*

    :param lp_arg:
        Fibre Channel lport port instance that sent the registration request
    :type lp_arg: void \*

.. _`fc_lport_scr_resp.locking-note`:

Locking Note
------------

This function will be called without the lport lock
held, but it will lock, call an \_enter\_\* function or fc_lport_error
and then unlock the lport.

.. _`fc_lport_enter_scr`:

fc_lport_enter_scr
==================

.. c:function:: void fc_lport_enter_scr(struct fc_lport *lport)

    Send a SCR (State Change Register) request

    :param lport:
        The local port to register for state changes
    :type lport: struct fc_lport \*

.. _`fc_lport_enter_ns`:

fc_lport_enter_ns
=================

.. c:function:: void fc_lport_enter_ns(struct fc_lport *lport, enum fc_lport_state state)

    register some object with the name server

    :param lport:
        Fibre Channel local port to register
    :type lport: struct fc_lport \*

    :param state:
        *undescribed*
    :type state: enum fc_lport_state

.. _`fc_lport_enter_dns`:

fc_lport_enter_dns
==================

.. c:function:: void fc_lport_enter_dns(struct fc_lport *lport)

    Create a fc_rport for the name server

    :param lport:
        The local port requesting a remote port for the name server
    :type lport: struct fc_lport \*

.. _`fc_lport_enter_ms`:

fc_lport_enter_ms
=================

.. c:function:: void fc_lport_enter_ms(struct fc_lport *lport, enum fc_lport_state state)

    management server commands

    :param lport:
        Fibre Channel local port to register
    :type lport: struct fc_lport \*

    :param state:
        *undescribed*
    :type state: enum fc_lport_state

.. _`fc_lport_enter_fdmi`:

fc_lport_enter_fdmi
===================

.. c:function:: void fc_lport_enter_fdmi(struct fc_lport *lport)

    Create a fc_rport for the management server

    :param lport:
        The local port requesting a remote port for the management server
    :type lport: struct fc_lport \*

.. _`fc_lport_timeout`:

fc_lport_timeout
================

.. c:function:: void fc_lport_timeout(struct work_struct *work)

    Handler for the retry_work timer

    :param work:
        The work struct of the local port
    :type work: struct work_struct \*

.. _`fc_lport_logo_resp`:

fc_lport_logo_resp
==================

.. c:function:: void fc_lport_logo_resp(struct fc_seq *sp, struct fc_frame *fp, void *lp_arg)

    Handle response to LOGO request

    :param sp:
        The sequence that the LOGO was on
    :type sp: struct fc_seq \*

    :param fp:
        The LOGO frame
    :type fp: struct fc_frame \*

    :param lp_arg:
        The lport port that received the LOGO request
    :type lp_arg: void \*

.. _`fc_lport_logo_resp.locking-note`:

Locking Note
------------

This function will be called without the lport lock
held, but it will lock, call an \_enter\_\* function or \ :c:func:`fc_lport_error`\ 
and then unlock the lport.

.. _`fc_lport_enter_logo`:

fc_lport_enter_logo
===================

.. c:function:: void fc_lport_enter_logo(struct fc_lport *lport)

    Logout of the fabric

    :param lport:
        The local port to be logged out
    :type lport: struct fc_lport \*

.. _`fc_lport_flogi_resp`:

fc_lport_flogi_resp
===================

.. c:function:: void fc_lport_flogi_resp(struct fc_seq *sp, struct fc_frame *fp, void *lp_arg)

    Handle response to FLOGI request

    :param sp:
        The sequence that the FLOGI was on
    :type sp: struct fc_seq \*

    :param fp:
        The FLOGI response frame
    :type fp: struct fc_frame \*

    :param lp_arg:
        The lport port that received the FLOGI response
    :type lp_arg: void \*

.. _`fc_lport_flogi_resp.locking-note`:

Locking Note
------------

This function will be called without the lport lock
held, but it will lock, call an \_enter\_\* function or \ :c:func:`fc_lport_error`\ 
and then unlock the lport.

.. _`fc_lport_enter_flogi`:

fc_lport_enter_flogi
====================

.. c:function:: void fc_lport_enter_flogi(struct fc_lport *lport)

    Send a FLOGI request to the fabric manager

    :param lport:
        Fibre Channel local port to be logged in to the fabric
    :type lport: struct fc_lport \*

.. _`fc_lport_config`:

fc_lport_config
===============

.. c:function:: int fc_lport_config(struct fc_lport *lport)

    Configure a fc_lport

    :param lport:
        The local port to be configured
    :type lport: struct fc_lport \*

.. _`fc_lport_init`:

fc_lport_init
=============

.. c:function:: int fc_lport_init(struct fc_lport *lport)

    Initialize the lport layer for a local port

    :param lport:
        The local port to initialize the exchange layer for
    :type lport: struct fc_lport \*

.. _`fc_lport_bsg_resp`:

fc_lport_bsg_resp
=================

.. c:function:: void fc_lport_bsg_resp(struct fc_seq *sp, struct fc_frame *fp, void *info_arg)

    The common response handler for FC Passthrough requests

    :param sp:
        The sequence for the FC Passthrough response
    :type sp: struct fc_seq \*

    :param fp:
        The response frame
    :type fp: struct fc_frame \*

    :param info_arg:
        The BSG info that the response is for
    :type info_arg: void \*

.. _`fc_lport_els_request`:

fc_lport_els_request
====================

.. c:function:: int fc_lport_els_request(struct bsg_job *job, struct fc_lport *lport, u32 did, u32 tov)

    Send ELS passthrough request

    :param job:
        The BSG Passthrough job
    :type job: struct bsg_job \*

    :param lport:
        The local port sending the request
    :type lport: struct fc_lport \*

    :param did:
        The destination port id
    :type did: u32

    :param tov:
        *undescribed*
    :type tov: u32

.. _`fc_lport_ct_request`:

fc_lport_ct_request
===================

.. c:function:: int fc_lport_ct_request(struct bsg_job *job, struct fc_lport *lport, u32 did, u32 tov)

    Send CT Passthrough request

    :param job:
        The BSG Passthrough job
    :type job: struct bsg_job \*

    :param lport:
        The local port sending the request
    :type lport: struct fc_lport \*

    :param did:
        The destination FC-ID
    :type did: u32

    :param tov:
        The timeout period to wait for the response
    :type tov: u32

.. _`fc_lport_bsg_request`:

fc_lport_bsg_request
====================

.. c:function:: int fc_lport_bsg_request(struct bsg_job *job)

    The common entry point for sending FC Passthrough requests

    :param job:
        The BSG passthrough job
    :type job: struct bsg_job \*

.. This file was automatic generated / don't edit.

