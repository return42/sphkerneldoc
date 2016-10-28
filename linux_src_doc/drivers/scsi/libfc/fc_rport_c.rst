.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libfc/fc_rport.c

.. _`fc_rport_lookup`:

fc_rport_lookup
===============

.. c:function:: struct fc_rport_priv *fc_rport_lookup(const struct fc_lport *lport, u32 port_id)

    Lookup a remote port by port_id

    :param const struct fc_lport \*lport:
        The local port to lookup the remote port on

    :param u32 port_id:
        The remote port ID to look up

.. _`fc_rport_lookup.description`:

Description
-----------

The caller must hold either disc_mutex or \ :c:func:`rcu_read_lock`\ .

.. _`fc_rport_create`:

fc_rport_create
===============

.. c:function:: struct fc_rport_priv *fc_rport_create(struct fc_lport *lport, u32 port_id)

    Create a new remote port

    :param struct fc_lport \*lport:
        The local port this remote port will be associated with

    :param u32 port_id:
        *undescribed*

.. _`fc_rport_create.description`:

Description
-----------

The remote port will start in the INIT state.

.. _`fc_rport_create.locking-note`:

Locking note
------------

must be called with the disc_mutex held.

.. _`fc_rport_destroy`:

fc_rport_destroy
================

.. c:function:: void fc_rport_destroy(struct kref *kref)

    Free a remote port after last reference is released

    :param struct kref \*kref:
        The remote port's kref

.. _`fc_rport_state`:

fc_rport_state
==============

.. c:function:: const char *fc_rport_state(struct fc_rport_priv *rdata)

    Return a string identifying the remote port's state

    :param struct fc_rport_priv \*rdata:
        The remote port

.. _`fc_set_rport_loss_tmo`:

fc_set_rport_loss_tmo
=====================

.. c:function:: void fc_set_rport_loss_tmo(struct fc_rport *rport, u32 timeout)

    Set the remote port loss timeout

    :param struct fc_rport \*rport:
        The remote port that gets a new timeout value

    :param u32 timeout:
        The new timeout value (in seconds)

.. _`fc_plogi_get_maxframe`:

fc_plogi_get_maxframe
=====================

.. c:function:: unsigned int fc_plogi_get_maxframe(struct fc_els_flogi *flp, unsigned int maxval)

    Get the maximum payload from the common service parameters in a FLOGI frame

    :param struct fc_els_flogi \*flp:
        The FLOGI or PLOGI payload

    :param unsigned int maxval:
        The maximum frame size upper limit; this may be less than what
        is in the service parameters

.. _`fc_rport_state_enter`:

fc_rport_state_enter
====================

.. c:function:: void fc_rport_state_enter(struct fc_rport_priv *rdata, enum fc_rport_state new)

    Change the state of a remote port

    :param struct fc_rport_priv \*rdata:
        The remote port whose state should change

    :param enum fc_rport_state new:
        The new state

.. _`fc_rport_state_enter.locking-note`:

Locking Note
------------

Called with the rport lock held

.. _`fc_rport_work`:

fc_rport_work
=============

.. c:function:: void fc_rport_work(struct work_struct *work)

    Handler for remote port events in the rport_event_queue

    :param struct work_struct \*work:
        Handle to the remote port being dequeued

.. _`fc_rport_login`:

fc_rport_login
==============

.. c:function:: int fc_rport_login(struct fc_rport_priv *rdata)

    Start the remote port login state machine

    :param struct fc_rport_priv \*rdata:
        The remote port to be logged in to

.. _`fc_rport_login.locking-note`:

Locking Note
------------

Called without the rport lock held. This
function will hold the rport lock, call an \_enter\_\*
function and then unlock the rport.

This indicates the intent to be logged into the remote port.
If it appears we are already logged in, ADISC is used to verify
the setup.

.. _`fc_rport_enter_delete`:

fc_rport_enter_delete
=====================

.. c:function:: void fc_rport_enter_delete(struct fc_rport_priv *rdata, enum fc_rport_event event)

    Schedule a remote port to be deleted

    :param struct fc_rport_priv \*rdata:
        The remote port to be deleted

    :param enum fc_rport_event event:
        The event to report as the reason for deletion

.. _`fc_rport_enter_delete.locking-note`:

Locking Note
------------

Called with the rport lock held.

Allow state change into DELETE only once.

Call queue_work only if there's no event already pending.
Set the new event so that the old pending event will not occur.
Since we have the mutex, even if \ :c:func:`fc_rport_work`\  is already started,
it'll see the new event.

.. _`fc_rport_logoff`:

fc_rport_logoff
===============

.. c:function:: int fc_rport_logoff(struct fc_rport_priv *rdata)

    Logoff and remove a remote port

    :param struct fc_rport_priv \*rdata:
        The remote port to be logged off of

.. _`fc_rport_logoff.locking-note`:

Locking Note
------------

Called without the rport lock held. This
function will hold the rport lock, call an \_enter\_\*
function and then unlock the rport.

.. _`fc_rport_enter_ready`:

fc_rport_enter_ready
====================

.. c:function:: void fc_rport_enter_ready(struct fc_rport_priv *rdata)

    Transition to the RPORT_ST_READY state

    :param struct fc_rport_priv \*rdata:
        The remote port that is ready

.. _`fc_rport_enter_ready.locking-note`:

Locking Note
------------

The rport lock is expected to be held before calling
this routine.

.. _`fc_rport_timeout`:

fc_rport_timeout
================

.. c:function:: void fc_rport_timeout(struct work_struct *work)

    Handler for the retry_work timer

    :param struct work_struct \*work:
        Handle to the remote port that has timed out

.. _`fc_rport_timeout.locking-note`:

Locking Note
------------

Called without the rport lock held. This
function will hold the rport lock, call an \_enter\_\*
function and then unlock the rport.

.. _`fc_rport_error`:

fc_rport_error
==============

.. c:function:: void fc_rport_error(struct fc_rport_priv *rdata, struct fc_frame *fp)

    Error handler, called once retries have been exhausted

    :param struct fc_rport_priv \*rdata:
        The remote port the error is happened on

    :param struct fc_frame \*fp:
        The error code encapsulated in a frame pointer

.. _`fc_rport_error.locking-note`:

Locking Note
------------

The rport lock is expected to be held before
calling this routine

.. _`fc_rport_error_retry`:

fc_rport_error_retry
====================

.. c:function:: void fc_rport_error_retry(struct fc_rport_priv *rdata, struct fc_frame *fp)

    Handler for remote port state retries

    :param struct fc_rport_priv \*rdata:
        The remote port whose state is to be retried

    :param struct fc_frame \*fp:
        The error code encapsulated in a frame pointer

.. _`fc_rport_error_retry.description`:

Description
-----------

If the error was an exchange timeout retry immediately,
otherwise wait for E_D_TOV.

.. _`fc_rport_error_retry.locking-note`:

Locking Note
------------

The rport lock is expected to be held before
calling this routine

.. _`fc_rport_login_complete`:

fc_rport_login_complete
=======================

.. c:function:: int fc_rport_login_complete(struct fc_rport_priv *rdata, struct fc_frame *fp)

    Handle parameters and completion of p-mp login.

    :param struct fc_rport_priv \*rdata:
        The remote port which we logged into or which logged into us.

    :param struct fc_frame \*fp:
        The FLOGI or PLOGI request or response frame

.. _`fc_rport_login_complete.description`:

Description
-----------

Returns non-zero error if a problem is detected with the frame.
Does not free the frame.

This is only used in point-to-multipoint mode for FIP currently.

.. _`fc_rport_flogi_resp`:

fc_rport_flogi_resp
===================

.. c:function:: void fc_rport_flogi_resp(struct fc_seq *sp, struct fc_frame *fp, void *rp_arg)

    Handle response to FLOGI request for p-mp mode

    :param struct fc_seq \*sp:
        The sequence that the FLOGI was on

    :param struct fc_frame \*fp:
        The FLOGI response frame

    :param void \*rp_arg:
        The remote port that received the FLOGI response

.. _`fc_rport_enter_flogi`:

fc_rport_enter_flogi
====================

.. c:function:: void fc_rport_enter_flogi(struct fc_rport_priv *rdata)

    Send a FLOGI request to the remote port for p-mp

    :param struct fc_rport_priv \*rdata:
        The remote port to send a FLOGI to

.. _`fc_rport_enter_flogi.locking-note`:

Locking Note
------------

The rport lock is expected to be held before calling
this routine.

.. _`fc_rport_recv_flogi_req`:

fc_rport_recv_flogi_req
=======================

.. c:function:: void fc_rport_recv_flogi_req(struct fc_lport *lport, struct fc_frame *rx_fp)

    Handle Fabric Login (FLOGI) request in p-mp mode

    :param struct fc_lport \*lport:
        The local port that received the PLOGI request

    :param struct fc_frame \*rx_fp:
        The PLOGI request frame

.. _`fc_rport_plogi_resp`:

fc_rport_plogi_resp
===================

.. c:function:: void fc_rport_plogi_resp(struct fc_seq *sp, struct fc_frame *fp, void *rdata_arg)

    Handler for ELS PLOGI responses

    :param struct fc_seq \*sp:
        The sequence the PLOGI is on

    :param struct fc_frame \*fp:
        The PLOGI response frame

    :param void \*rdata_arg:
        The remote port that sent the PLOGI response

.. _`fc_rport_plogi_resp.locking-note`:

Locking Note
------------

This function will be called without the rport lock
held, but it will lock, call an \_enter\_\* function or fc_rport_error
and then unlock the rport.

.. _`fc_rport_enter_plogi`:

fc_rport_enter_plogi
====================

.. c:function:: void fc_rport_enter_plogi(struct fc_rport_priv *rdata)

    Send Port Login (PLOGI) request

    :param struct fc_rport_priv \*rdata:
        The remote port to send a PLOGI to

.. _`fc_rport_enter_plogi.locking-note`:

Locking Note
------------

The rport lock is expected to be held before calling
this routine.

.. _`fc_rport_prli_resp`:

fc_rport_prli_resp
==================

.. c:function:: void fc_rport_prli_resp(struct fc_seq *sp, struct fc_frame *fp, void *rdata_arg)

    Process Login (PRLI) response handler

    :param struct fc_seq \*sp:
        The sequence the PRLI response was on

    :param struct fc_frame \*fp:
        The PRLI response frame

    :param void \*rdata_arg:
        The remote port that sent the PRLI response

.. _`fc_rport_prli_resp.locking-note`:

Locking Note
------------

This function will be called without the rport lock
held, but it will lock, call an \_enter\_\* function or fc_rport_error
and then unlock the rport.

.. _`fc_rport_enter_prli`:

fc_rport_enter_prli
===================

.. c:function:: void fc_rport_enter_prli(struct fc_rport_priv *rdata)

    Send Process Login (PRLI) request

    :param struct fc_rport_priv \*rdata:
        The remote port to send the PRLI request to

.. _`fc_rport_enter_prli.locking-note`:

Locking Note
------------

The rport lock is expected to be held before calling
this routine.

.. _`fc_rport_rtv_resp`:

fc_rport_rtv_resp
=================

.. c:function:: void fc_rport_rtv_resp(struct fc_seq *sp, struct fc_frame *fp, void *rdata_arg)

    Handler for Request Timeout Value (RTV) responses

    :param struct fc_seq \*sp:
        The sequence the RTV was on

    :param struct fc_frame \*fp:
        The RTV response frame

    :param void \*rdata_arg:
        The remote port that sent the RTV response

.. _`fc_rport_rtv_resp.description`:

Description
-----------

Many targets don't seem to support this.

.. _`fc_rport_rtv_resp.locking-note`:

Locking Note
------------

This function will be called without the rport lock
held, but it will lock, call an \_enter\_\* function or fc_rport_error
and then unlock the rport.

.. _`fc_rport_enter_rtv`:

fc_rport_enter_rtv
==================

.. c:function:: void fc_rport_enter_rtv(struct fc_rport_priv *rdata)

    Send Request Timeout Value (RTV) request

    :param struct fc_rport_priv \*rdata:
        The remote port to send the RTV request to

.. _`fc_rport_enter_rtv.locking-note`:

Locking Note
------------

The rport lock is expected to be held before calling
this routine.

.. _`fc_rport_logo_resp`:

fc_rport_logo_resp
==================

.. c:function:: void fc_rport_logo_resp(struct fc_seq *sp, struct fc_frame *fp, void *lport_arg)

    Handler for logout (LOGO) responses

    :param struct fc_seq \*sp:
        The sequence the LOGO was on

    :param struct fc_frame \*fp:
        The LOGO response frame

    :param void \*lport_arg:
        The local port

.. _`fc_rport_enter_logo`:

fc_rport_enter_logo
===================

.. c:function:: void fc_rport_enter_logo(struct fc_rport_priv *rdata)

    Send a logout (LOGO) request

    :param struct fc_rport_priv \*rdata:
        The remote port to send the LOGO request to

.. _`fc_rport_enter_logo.locking-note`:

Locking Note
------------

The rport lock is expected to be held before calling
this routine.

.. _`fc_rport_adisc_resp`:

fc_rport_adisc_resp
===================

.. c:function:: void fc_rport_adisc_resp(struct fc_seq *sp, struct fc_frame *fp, void *rdata_arg)

    Handler for Address Discovery (ADISC) responses

    :param struct fc_seq \*sp:
        The sequence the ADISC response was on

    :param struct fc_frame \*fp:
        The ADISC response frame

    :param void \*rdata_arg:
        The remote port that sent the ADISC response

.. _`fc_rport_adisc_resp.locking-note`:

Locking Note
------------

This function will be called without the rport lock
held, but it will lock, call an \_enter\_\* function or fc_rport_error
and then unlock the rport.

.. _`fc_rport_enter_adisc`:

fc_rport_enter_adisc
====================

.. c:function:: void fc_rport_enter_adisc(struct fc_rport_priv *rdata)

    Send Address Discover (ADISC) request

    :param struct fc_rport_priv \*rdata:
        The remote port to send the ADISC request to

.. _`fc_rport_enter_adisc.locking-note`:

Locking Note
------------

The rport lock is expected to be held before calling
this routine.

.. _`fc_rport_recv_adisc_req`:

fc_rport_recv_adisc_req
=======================

.. c:function:: void fc_rport_recv_adisc_req(struct fc_rport_priv *rdata, struct fc_frame *in_fp)

    Handler for Address Discovery (ADISC) requests

    :param struct fc_rport_priv \*rdata:
        The remote port that sent the ADISC request

    :param struct fc_frame \*in_fp:
        The ADISC request frame

.. _`fc_rport_recv_adisc_req.locking-note`:

Locking Note
------------

Called with the lport and rport locks held.

.. _`fc_rport_recv_rls_req`:

fc_rport_recv_rls_req
=====================

.. c:function:: void fc_rport_recv_rls_req(struct fc_rport_priv *rdata, struct fc_frame *rx_fp)

    Handle received Read Link Status request

    :param struct fc_rport_priv \*rdata:
        The remote port that sent the RLS request

    :param struct fc_frame \*rx_fp:
        The PRLI request frame

.. _`fc_rport_recv_rls_req.locking-note`:

Locking Note
------------

The rport lock is expected to be held before calling
this function.

.. _`fc_rport_recv_els_req`:

fc_rport_recv_els_req
=====================

.. c:function:: void fc_rport_recv_els_req(struct fc_lport *lport, struct fc_frame *fp)

    Handler for validated ELS requests

    :param struct fc_lport \*lport:
        The local port that received the ELS request

    :param struct fc_frame \*fp:
        The ELS request frame

.. _`fc_rport_recv_els_req.description`:

Description
-----------

Handle incoming ELS requests that require port login.
The ELS opcode has already been validated by the caller.

.. _`fc_rport_recv_els_req.locking-note`:

Locking Note
------------

Called with the lport lock held.

.. _`fc_rport_recv_req`:

fc_rport_recv_req
=================

.. c:function:: void fc_rport_recv_req(struct fc_lport *lport, struct fc_frame *fp)

    Handler for requests

    :param struct fc_lport \*lport:
        The local port that received the request

    :param struct fc_frame \*fp:
        The request frame

.. _`fc_rport_recv_req.locking-note`:

Locking Note
------------

Called with the lport lock held.

.. _`fc_rport_recv_plogi_req`:

fc_rport_recv_plogi_req
=======================

.. c:function:: void fc_rport_recv_plogi_req(struct fc_lport *lport, struct fc_frame *rx_fp)

    Handler for Port Login (PLOGI) requests

    :param struct fc_lport \*lport:
        The local port that received the PLOGI request

    :param struct fc_frame \*rx_fp:
        The PLOGI request frame

.. _`fc_rport_recv_plogi_req.locking-note`:

Locking Note
------------

The rport lock is held before calling this function.

.. _`fc_rport_recv_prli_req`:

fc_rport_recv_prli_req
======================

.. c:function:: void fc_rport_recv_prli_req(struct fc_rport_priv *rdata, struct fc_frame *rx_fp)

    Handler for process login (PRLI) requests

    :param struct fc_rport_priv \*rdata:
        The remote port that sent the PRLI request

    :param struct fc_frame \*rx_fp:
        The PRLI request frame

.. _`fc_rport_recv_prli_req.locking-note`:

Locking Note
------------

The rport lock is expected to be held before calling
this function.

.. _`fc_rport_recv_prlo_req`:

fc_rport_recv_prlo_req
======================

.. c:function:: void fc_rport_recv_prlo_req(struct fc_rport_priv *rdata, struct fc_frame *rx_fp)

    Handler for process logout (PRLO) requests

    :param struct fc_rport_priv \*rdata:
        The remote port that sent the PRLO request

    :param struct fc_frame \*rx_fp:
        The PRLO request frame

.. _`fc_rport_recv_prlo_req.locking-note`:

Locking Note
------------

The rport lock is expected to be held before calling
this function.

.. _`fc_rport_recv_logo_req`:

fc_rport_recv_logo_req
======================

.. c:function:: void fc_rport_recv_logo_req(struct fc_lport *lport, struct fc_frame *fp)

    Handler for logout (LOGO) requests

    :param struct fc_lport \*lport:
        The local port that received the LOGO request

    :param struct fc_frame \*fp:
        The LOGO request frame

.. _`fc_rport_recv_logo_req.locking-note`:

Locking Note
------------

The rport lock is expected to be held before calling
this function.

.. _`fc_rport_flush_queue`:

fc_rport_flush_queue
====================

.. c:function:: void fc_rport_flush_queue( void)

    Flush the rport_event_queue

    :param  void:
        no arguments

.. _`fc_rport_init`:

fc_rport_init
=============

.. c:function:: int fc_rport_init(struct fc_lport *lport)

    Initialize the remote port layer for a local port

    :param struct fc_lport \*lport:
        The local port to initialize the remote port layer for

.. _`fc_rport_fcp_prli`:

fc_rport_fcp_prli
=================

.. c:function:: int fc_rport_fcp_prli(struct fc_rport_priv *rdata, u32 spp_len, const struct fc_els_spp *rspp, struct fc_els_spp *spp)

    Handle incoming PRLI for the FCP initiator.

    :param struct fc_rport_priv \*rdata:
        remote port private

    :param u32 spp_len:
        service parameter page length

    :param const struct fc_els_spp \*rspp:
        received service parameter page

    :param struct fc_els_spp \*spp:
        response service parameter page

.. _`fc_rport_fcp_prli.description`:

Description
-----------

Returns the value for the response code to be placed in spp_flags;
Returns 0 if not an initiator.

.. _`fc_rport_t0_prli`:

fc_rport_t0_prli
================

.. c:function:: int fc_rport_t0_prli(struct fc_rport_priv *rdata, u32 spp_len, const struct fc_els_spp *rspp, struct fc_els_spp *spp)

    Handle incoming PRLI parameters for type 0

    :param struct fc_rport_priv \*rdata:
        remote port private

    :param u32 spp_len:
        service parameter page length

    :param const struct fc_els_spp \*rspp:
        received service parameter page

    :param struct fc_els_spp \*spp:
        response service parameter page

.. _`fc_setup_rport`:

fc_setup_rport
==============

.. c:function:: int fc_setup_rport( void)

    Initialize the rport_event_queue

    :param  void:
        no arguments

.. _`fc_destroy_rport`:

fc_destroy_rport
================

.. c:function:: void fc_destroy_rport( void)

    Destroy the rport_event_queue

    :param  void:
        no arguments

.. _`fc_rport_terminate_io`:

fc_rport_terminate_io
=====================

.. c:function:: void fc_rport_terminate_io(struct fc_rport *rport)

    Stop all outstanding I/O on a remote port

    :param struct fc_rport \*rport:
        The remote port whose I/O should be terminated

.. This file was automatic generated / don't edit.

