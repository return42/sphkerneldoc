.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/fcoe/fcoe_ctlr.c

.. _`fcoe_ctlr_set_state`:

fcoe_ctlr_set_state
===================

.. c:function:: void fcoe_ctlr_set_state(struct fcoe_ctlr *fip, enum fip_state state)

    Set and do debug printing for the new FIP state.

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param enum fip_state state:
        The new state

.. _`fcoe_ctlr_mtu_valid`:

fcoe_ctlr_mtu_valid
===================

.. c:function:: int fcoe_ctlr_mtu_valid(const struct fcoe_fcf *fcf)

    Check if a FCF's MTU is valid

    :param const struct fcoe_fcf \*fcf:
        The FCF to check

.. _`fcoe_ctlr_mtu_valid.description`:

Description
-----------

Return non-zero if FCF fcoe_size has been validated.

.. _`fcoe_ctlr_fcf_usable`:

fcoe_ctlr_fcf_usable
====================

.. c:function:: int fcoe_ctlr_fcf_usable(struct fcoe_fcf *fcf)

    Check if a FCF is usable

    :param struct fcoe_fcf \*fcf:
        The FCF to check

.. _`fcoe_ctlr_fcf_usable.description`:

Description
-----------

Return non-zero if the FCF is usable.

.. _`fcoe_ctlr_map_dest`:

fcoe_ctlr_map_dest
==================

.. c:function:: void fcoe_ctlr_map_dest(struct fcoe_ctlr *fip)

    Set flag and OUI for mapping destination addresses

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

.. _`fcoe_ctlr_init`:

fcoe_ctlr_init
==============

.. c:function:: void fcoe_ctlr_init(struct fcoe_ctlr *fip, enum fip_state mode)

    Initialize the FCoE Controller instance

    :param struct fcoe_ctlr \*fip:
        The FCoE controller to initialize

    :param enum fip_state mode:
        *undescribed*

.. _`fcoe_sysfs_fcf_add`:

fcoe_sysfs_fcf_add
==================

.. c:function:: int fcoe_sysfs_fcf_add(struct fcoe_fcf *new)

    Add a fcoe_fcf{,_device} to a fcoe_ctlr{,_device}

    :param struct fcoe_fcf \*new:
        The newly discovered FCF

.. _`fcoe_sysfs_fcf_add.description`:

Description
-----------

Called with fip->ctlr_mutex held

.. _`fcoe_sysfs_fcf_del`:

fcoe_sysfs_fcf_del
==================

.. c:function:: void fcoe_sysfs_fcf_del(struct fcoe_fcf *new)

    Remove a fcoe_fcf{,_device} to a fcoe_ctlr{,_device}

    :param struct fcoe_fcf \*new:
        The FCF to be removed

.. _`fcoe_sysfs_fcf_del.description`:

Description
-----------

Called with fip->ctlr_mutex held

.. _`fcoe_ctlr_reset_fcfs`:

fcoe_ctlr_reset_fcfs
====================

.. c:function:: void fcoe_ctlr_reset_fcfs(struct fcoe_ctlr *fip)

    Reset and free all FCFs for a controller

    :param struct fcoe_ctlr \*fip:
        The FCoE controller whose FCFs are to be reset

.. _`fcoe_ctlr_reset_fcfs.description`:

Description
-----------

Called with \ :c:type:`struct fcoe_ctlr <fcoe_ctlr>`\  lock held.

.. _`fcoe_ctlr_destroy`:

fcoe_ctlr_destroy
=================

.. c:function:: void fcoe_ctlr_destroy(struct fcoe_ctlr *fip)

    Disable and tear down a FCoE controller

    :param struct fcoe_ctlr \*fip:
        The FCoE controller to tear down

.. _`fcoe_ctlr_destroy.description`:

Description
-----------

This is called by FCoE drivers before freeing the \ :c:type:`struct fcoe_ctlr <fcoe_ctlr>`\ .

The receive handler will have been deleted before this to guarantee
that no more recv_work will be scheduled.

The timer routine will simply return once we set FIP_ST_DISABLED.
This guarantees that no further timeouts or work will be scheduled.

.. _`fcoe_ctlr_announce`:

fcoe_ctlr_announce
==================

.. c:function:: void fcoe_ctlr_announce(struct fcoe_ctlr *fip)

    announce new FCF selection

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

.. _`fcoe_ctlr_announce.description`:

Description
-----------

Also sets the destination MAC for FCoE and control packets

Called with neither ctlr_mutex nor ctlr_lock held.

.. _`fcoe_ctlr_fcoe_size`:

fcoe_ctlr_fcoe_size
===================

.. c:function:: u32 fcoe_ctlr_fcoe_size(struct fcoe_ctlr *fip)

    Return the maximum FCoE size required for VN_Port

    :param struct fcoe_ctlr \*fip:
        The FCoE controller to get the maximum FCoE size from

.. _`fcoe_ctlr_fcoe_size.description`:

Description
-----------

Returns the maximum packet size including the FCoE header and trailer,
but not including any Ethernet or VLAN headers.

.. _`fcoe_ctlr_solicit`:

fcoe_ctlr_solicit
=================

.. c:function:: void fcoe_ctlr_solicit(struct fcoe_ctlr *fip, struct fcoe_fcf *fcf)

    Send a FIP solicitation

    :param struct fcoe_ctlr \*fip:
        The FCoE controller to send the solicitation on

    :param struct fcoe_fcf \*fcf:
        The destination FCF (if NULL, a multicast solicitation is sent)

.. _`fcoe_ctlr_link_up`:

fcoe_ctlr_link_up
=================

.. c:function:: void fcoe_ctlr_link_up(struct fcoe_ctlr *fip)

    Start FCoE controller

    :param struct fcoe_ctlr \*fip:
        The FCoE controller to start

.. _`fcoe_ctlr_link_up.description`:

Description
-----------

Called from the LLD when the network link is ready.

.. _`fcoe_ctlr_reset`:

fcoe_ctlr_reset
===============

.. c:function:: void fcoe_ctlr_reset(struct fcoe_ctlr *fip)

    Reset a FCoE controller

    :param struct fcoe_ctlr \*fip:
        The FCoE controller to reset

.. _`fcoe_ctlr_link_down`:

fcoe_ctlr_link_down
===================

.. c:function:: int fcoe_ctlr_link_down(struct fcoe_ctlr *fip)

    Stop a FCoE controller

    :param struct fcoe_ctlr \*fip:
        The FCoE controller to be stopped

.. _`fcoe_ctlr_link_down.description`:

Description
-----------

Returns non-zero if the link was up and now isn't.

Called from the LLD when the network link is not ready.
There may be multiple calls while the link is down.

.. _`fcoe_ctlr_send_keep_alive`:

fcoe_ctlr_send_keep_alive
=========================

.. c:function:: void fcoe_ctlr_send_keep_alive(struct fcoe_ctlr *fip, struct fc_lport *lport, int ports, u8 *sa)

    Send a keep-alive to the selected FCF

    :param struct fcoe_ctlr \*fip:
        The FCoE controller to send the FKA on

    :param struct fc_lport \*lport:
        libfc fc_lport to send from

    :param int ports:
        0 for controller keep-alive, 1 for port keep-alive

    :param u8 \*sa:
        The source MAC address

.. _`fcoe_ctlr_send_keep_alive.description`:

Description
-----------

A controller keep-alive is sent every fka_period (typically 8 seconds).
The source MAC is the native MAC address.

A port keep-alive is sent every 90 seconds while logged in.
The source MAC is the assigned mapped source address.
The destination is the FCF's F-port.

.. _`fcoe_ctlr_encaps`:

fcoe_ctlr_encaps
================

.. c:function:: int fcoe_ctlr_encaps(struct fcoe_ctlr *fip, struct fc_lport *lport, u8 dtype, struct sk_buff *skb, u32 d_id)

    Encapsulate an ELS frame for FIP, without sending it

    :param struct fcoe_ctlr \*fip:
        The FCoE controller for the ELS frame

    :param struct fc_lport \*lport:
        *undescribed*

    :param u8 dtype:
        The FIP descriptor type for the frame

    :param struct sk_buff \*skb:
        The FCoE ELS frame including FC header but no FCoE headers

    :param u32 d_id:
        The destination port ID.

.. _`fcoe_ctlr_encaps.description`:

Description
-----------

Returns non-zero error code on failure.

The caller must check that the length is a multiple of 4.

The \ ``skb``\  must have enough headroom (28 bytes) and tailroom (8 bytes).
Headroom includes the FIP encapsulation description, FIP header, and
Ethernet header.  The tailroom is for the FIP MAC descriptor.

.. _`fcoe_ctlr_els_send`:

fcoe_ctlr_els_send
==================

.. c:function:: int fcoe_ctlr_els_send(struct fcoe_ctlr *fip, struct fc_lport *lport, struct sk_buff *skb)

    Send an ELS frame encapsulated by FIP if appropriate.

    :param struct fcoe_ctlr \*fip:
        FCoE controller.

    :param struct fc_lport \*lport:
        libfc fc_lport to send from

    :param struct sk_buff \*skb:
        FCoE ELS frame including FC header but no FCoE headers.

.. _`fcoe_ctlr_els_send.description`:

Description
-----------

Returns a non-zero error code if the frame should not be sent.
Returns zero if the caller should send the frame with FCoE encapsulation.

The caller must check that the length is a multiple of 4.
The SKB must have enough headroom (28 bytes) and tailroom (8 bytes).
The the skb must also be an fc_frame.

This is called from the lower-level driver with spinlocks held,
so we must not take a mutex here.

.. _`fcoe_ctlr_age_fcfs`:

fcoe_ctlr_age_fcfs
==================

.. c:function:: unsigned long fcoe_ctlr_age_fcfs(struct fcoe_ctlr *fip)

    Reset and free all old FCFs for a controller

    :param struct fcoe_ctlr \*fip:
        The FCoE controller to free FCFs on

.. _`fcoe_ctlr_age_fcfs.description`:

Description
-----------

Called with lock held and preemption disabled.

An FCF is considered old if we have missed two advertisements.
That is, there have been no valid advertisement from it for 2.5
times its keep-alive period.

In addition, determine the time when an FCF selection can occur.

Also, increment the MissDiscAdvCount when no advertisement is received
for the corresponding FCF for 1.5 \* FKA_ADV_PERIOD (FC-BB-5 LESB).

Returns the time in jiffies for the next call.

.. _`fcoe_ctlr_parse_adv`:

fcoe_ctlr_parse_adv
===================

.. c:function:: int fcoe_ctlr_parse_adv(struct fcoe_ctlr *fip, struct sk_buff *skb, struct fcoe_fcf *fcf)

    Decode a FIP advertisement into a new FCF entry

    :param struct fcoe_ctlr \*fip:
        The FCoE controller receiving the advertisement

    :param struct sk_buff \*skb:
        The received FIP advertisement frame

    :param struct fcoe_fcf \*fcf:
        The resulting FCF entry

.. _`fcoe_ctlr_parse_adv.description`:

Description
-----------

Returns zero on a valid parsed advertisement,
otherwise returns non zero value.

.. _`fcoe_ctlr_recv_adv`:

fcoe_ctlr_recv_adv
==================

.. c:function:: void fcoe_ctlr_recv_adv(struct fcoe_ctlr *fip, struct sk_buff *skb)

    Handle an incoming advertisement

    :param struct fcoe_ctlr \*fip:
        The FCoE controller receiving the advertisement

    :param struct sk_buff \*skb:
        The received FIP packet

.. _`fcoe_ctlr_recv_els`:

fcoe_ctlr_recv_els
==================

.. c:function:: void fcoe_ctlr_recv_els(struct fcoe_ctlr *fip, struct sk_buff *skb)

    Handle an incoming FIP encapsulated ELS frame

    :param struct fcoe_ctlr \*fip:
        The FCoE controller which received the packet

    :param struct sk_buff \*skb:
        The received FIP packet

.. _`fcoe_ctlr_recv_clr_vlink`:

fcoe_ctlr_recv_clr_vlink
========================

.. c:function:: void fcoe_ctlr_recv_clr_vlink(struct fcoe_ctlr *fip, struct sk_buff *skb)

    Handle an incoming link reset frame

    :param struct fcoe_ctlr \*fip:
        The FCoE controller that received the frame

    :param struct sk_buff \*skb:
        *undescribed*

.. _`fcoe_ctlr_recv_clr_vlink.description`:

Description
-----------

There may be multiple VN_Port descriptors.
The overall length has already been checked.

.. _`fcoe_ctlr_recv`:

fcoe_ctlr_recv
==============

.. c:function:: void fcoe_ctlr_recv(struct fcoe_ctlr *fip, struct sk_buff *skb)

    Receive a FIP packet

    :param struct fcoe_ctlr \*fip:
        The FCoE controller that received the packet

    :param struct sk_buff \*skb:
        The received FIP packet

.. _`fcoe_ctlr_recv.description`:

Description
-----------

This may be called from either NET_RX_SOFTIRQ or IRQ.

.. _`fcoe_ctlr_recv_handler`:

fcoe_ctlr_recv_handler
======================

.. c:function:: int fcoe_ctlr_recv_handler(struct fcoe_ctlr *fip, struct sk_buff *skb)

    Receive a FIP frame

    :param struct fcoe_ctlr \*fip:
        The FCoE controller that received the frame

    :param struct sk_buff \*skb:
        The received FIP frame

.. _`fcoe_ctlr_recv_handler.description`:

Description
-----------

Returns non-zero if the frame is dropped.

.. _`fcoe_ctlr_select`:

fcoe_ctlr_select
================

.. c:function:: struct fcoe_fcf *fcoe_ctlr_select(struct fcoe_ctlr *fip)

    Select the best FCF (if possible)

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

.. _`fcoe_ctlr_select.description`:

Description
-----------

Returns the selected FCF, or NULL if none are usable.

If there are conflicting advertisements, no FCF can be chosen.

If there is already a selected FCF, this will choose a better one or
an equivalent one that hasn't already been sent a FLOGI.

Called with lock held.

.. _`fcoe_ctlr_flogi_send_locked`:

fcoe_ctlr_flogi_send_locked
===========================

.. c:function:: int fcoe_ctlr_flogi_send_locked(struct fcoe_ctlr *fip)

    send FIP-encapsulated FLOGI to current FCF

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

.. _`fcoe_ctlr_flogi_send_locked.description`:

Description
-----------

Returns non-zero error if it could not be sent.

Called with ctlr_mutex and ctlr_lock held.
Caller must verify that fip->sel_fcf is not NULL.

.. _`fcoe_ctlr_flogi_retry`:

fcoe_ctlr_flogi_retry
=====================

.. c:function:: int fcoe_ctlr_flogi_retry(struct fcoe_ctlr *fip)

    resend FLOGI request to a new FCF if possible

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

.. _`fcoe_ctlr_flogi_retry.description`:

Description
-----------

Returns non-zero error code if there's no FLOGI request to retry or
no alternate FCF available.

.. _`fcoe_ctlr_flogi_send`:

fcoe_ctlr_flogi_send
====================

.. c:function:: void fcoe_ctlr_flogi_send(struct fcoe_ctlr *fip)

    Handle sending of FIP FLOGI.

    :param struct fcoe_ctlr \*fip:
        The FCoE controller that timed out

.. _`fcoe_ctlr_flogi_send.description`:

Description
-----------

Done here because \ :c:func:`fcoe_ctlr_els_send`\  can't get mutex.

Called with ctlr_mutex held.  The caller must not hold ctlr_lock.

.. _`fcoe_ctlr_timeout`:

fcoe_ctlr_timeout
=================

.. c:function:: void fcoe_ctlr_timeout(unsigned long arg)

    FIP timeout handler

    :param unsigned long arg:
        The FCoE controller that timed out

.. _`fcoe_ctlr_timer_work`:

fcoe_ctlr_timer_work
====================

.. c:function:: void fcoe_ctlr_timer_work(struct work_struct *work)

    Worker thread function for timer work

    :param struct work_struct \*work:
        Handle to a FCoE controller

.. _`fcoe_ctlr_timer_work.description`:

Description
-----------

Ages FCFs.  Triggers FCF selection if possible.
Sends keep-alives and resets.

.. _`fcoe_ctlr_recv_work`:

fcoe_ctlr_recv_work
===================

.. c:function:: void fcoe_ctlr_recv_work(struct work_struct *recv_work)

    Worker thread function for receiving FIP frames

    :param struct work_struct \*recv_work:
        Handle to a FCoE controller

.. _`fcoe_ctlr_recv_flogi`:

fcoe_ctlr_recv_flogi
====================

.. c:function:: int fcoe_ctlr_recv_flogi(struct fcoe_ctlr *fip, struct fc_lport *lport, struct fc_frame *fp)

    Snoop pre-FIP receipt of FLOGI response

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_frame \*fp:
        The FC frame to snoop

.. _`fcoe_ctlr_recv_flogi.description`:

Description
-----------

Snoop potential response to FLOGI or even incoming FLOGI.

The caller has checked that we are waiting for login as indicated
by fip->flogi_oxid != FC_XID_UNKNOWN.

The caller is responsible for freeing the frame.
Fill in the granted_mac address.

Return non-zero if the frame should not be delivered to libfc.

.. _`fcoe_wwn_from_mac`:

fcoe_wwn_from_mac
=================

.. c:function:: u64 fcoe_wwn_from_mac(unsigned char mac, unsigned int scheme, unsigned int port)

    Converts a 48-bit IEEE MAC address to a 64-bit FC WWN

    :param unsigned char mac:
        The MAC address to convert

    :param unsigned int scheme:
        The scheme to use when converting

    :param unsigned int port:
        The port indicator for converting

.. _`fcoe_wwn_from_mac.return`:

Return
------

u64 fc world wide name

.. _`fcoe_ctlr_rport`:

fcoe_ctlr_rport
===============

.. c:function:: struct fcoe_rport *fcoe_ctlr_rport(struct fc_rport_priv *rdata)

    return the fcoe_rport for a given fc_rport_priv

    :param struct fc_rport_priv \*rdata:
        libfc remote port

.. _`fcoe_ctlr_vn_send`:

fcoe_ctlr_vn_send
=================

.. c:function:: void fcoe_ctlr_vn_send(struct fcoe_ctlr *fip, enum fip_vn2vn_subcode sub, const u8 *dest, size_t min_len)

    Send a FIP VN2VN Probe Request or Reply.

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param enum fip_vn2vn_subcode sub:
        sub-opcode for probe request, reply, or advertisement.

    :param const u8 \*dest:
        The destination Ethernet MAC address

    :param size_t min_len:
        minimum size of the Ethernet payload to be sent

.. _`fcoe_ctlr_vn_rport_callback`:

fcoe_ctlr_vn_rport_callback
===========================

.. c:function:: void fcoe_ctlr_vn_rport_callback(struct fc_lport *lport, struct fc_rport_priv *rdata, enum fc_rport_event event)

    Event handler for rport events.

    :param struct fc_lport \*lport:
        The lport which is receiving the event

    :param struct fc_rport_priv \*rdata:
        remote port private data

    :param enum fc_rport_event event:
        The event that occurred

.. _`fcoe_ctlr_vn_rport_callback.locking-note`:

Locking Note
------------

The rport lock must not be held when calling this function.

.. _`fcoe_ctlr_disc_stop_locked`:

fcoe_ctlr_disc_stop_locked
==========================

.. c:function:: void fcoe_ctlr_disc_stop_locked(struct fc_lport *lport)

    stop discovery in VN2VN mode

    :param struct fc_lport \*lport:
        *undescribed*

.. _`fcoe_ctlr_disc_stop_locked.description`:

Description
-----------

Called with ctlr_mutex held.

.. _`fcoe_ctlr_disc_stop`:

fcoe_ctlr_disc_stop
===================

.. c:function:: void fcoe_ctlr_disc_stop(struct fc_lport *lport)

    stop discovery in VN2VN mode

    :param struct fc_lport \*lport:
        *undescribed*

.. _`fcoe_ctlr_disc_stop.description`:

Description
-----------

Called through the local port template for discovery.
Called without the ctlr_mutex held.

.. _`fcoe_ctlr_disc_stop_final`:

fcoe_ctlr_disc_stop_final
=========================

.. c:function:: void fcoe_ctlr_disc_stop_final(struct fc_lport *lport)

    stop discovery for shutdown in VN2VN mode

    :param struct fc_lport \*lport:
        *undescribed*

.. _`fcoe_ctlr_disc_stop_final.description`:

Description
-----------

Called through the local port template for discovery.
Called without the ctlr_mutex held.

.. _`fcoe_ctlr_vn_restart`:

fcoe_ctlr_vn_restart
====================

.. c:function:: void fcoe_ctlr_vn_restart(struct fcoe_ctlr *fip)

    VN2VN probe restart with new port_id

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

.. _`fcoe_ctlr_vn_restart.description`:

Description
-----------

Called with fcoe_ctlr lock held.

.. _`fcoe_ctlr_vn_start`:

fcoe_ctlr_vn_start
==================

.. c:function:: void fcoe_ctlr_vn_start(struct fcoe_ctlr *fip)

    Start in VN2VN mode

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

.. _`fcoe_ctlr_vn_start.description`:

Description
-----------

Called with fcoe_ctlr lock held.

.. _`fcoe_ctlr_vn_parse`:

fcoe_ctlr_vn_parse
==================

.. c:function:: int fcoe_ctlr_vn_parse(struct fcoe_ctlr *fip, struct sk_buff *skb, struct fc_rport_priv *rdata)

    parse probe request or response

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param struct sk_buff \*skb:
        incoming packet

    :param struct fc_rport_priv \*rdata:
        buffer for resulting parsed VN entry plus fcoe_rport

.. _`fcoe_ctlr_vn_parse.description`:

Description
-----------

Returns non-zero error number on error.
Does not consume the packet.

.. _`fcoe_ctlr_vn_send_claim`:

fcoe_ctlr_vn_send_claim
=======================

.. c:function:: void fcoe_ctlr_vn_send_claim(struct fcoe_ctlr *fip)

    send multicast FIP VN2VN Claim Notification.

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

.. _`fcoe_ctlr_vn_send_claim.description`:

Description
-----------

Called with ctlr_mutex held.

.. _`fcoe_ctlr_vn_probe_req`:

fcoe_ctlr_vn_probe_req
======================

.. c:function:: void fcoe_ctlr_vn_probe_req(struct fcoe_ctlr *fip, struct fc_rport_priv *rdata)

    handle incoming VN2VN probe request.

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param struct fc_rport_priv \*rdata:
        parsed remote port with frport from the probe request

.. _`fcoe_ctlr_vn_probe_req.description`:

Description
-----------

Called with ctlr_mutex held.

.. _`fcoe_ctlr_vn_probe_reply`:

fcoe_ctlr_vn_probe_reply
========================

.. c:function:: void fcoe_ctlr_vn_probe_reply(struct fcoe_ctlr *fip, struct fc_rport_priv *rdata)

    handle incoming VN2VN probe reply.

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param struct fc_rport_priv \*rdata:
        parsed remote port with frport from the probe request

.. _`fcoe_ctlr_vn_probe_reply.description`:

Description
-----------

Called with ctlr_mutex held.

.. _`fcoe_ctlr_vn_add`:

fcoe_ctlr_vn_add
================

.. c:function:: void fcoe_ctlr_vn_add(struct fcoe_ctlr *fip, struct fc_rport_priv *new)

    Add a VN2VN entry to the list, based on a claim reply.

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param struct fc_rport_priv \*new:
        newly-parsed remote port with frport as a template for new rdata

.. _`fcoe_ctlr_vn_add.description`:

Description
-----------

Called with ctlr_mutex held.

.. _`fcoe_ctlr_vn_lookup`:

fcoe_ctlr_vn_lookup
===================

.. c:function:: int fcoe_ctlr_vn_lookup(struct fcoe_ctlr *fip, u32 port_id, u8 *mac)

    Find VN remote port's MAC address

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param u32 port_id:
        The port_id of the remote VN_node

    :param u8 \*mac:
        buffer which will hold the VN_NODE destination MAC address, if found.

.. _`fcoe_ctlr_vn_lookup.description`:

Description
-----------

Returns non-zero error if no remote port found.

.. _`fcoe_ctlr_vn_claim_notify`:

fcoe_ctlr_vn_claim_notify
=========================

.. c:function:: void fcoe_ctlr_vn_claim_notify(struct fcoe_ctlr *fip, struct fc_rport_priv *new)

    handle received FIP VN2VN Claim Notification

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param struct fc_rport_priv \*new:
        newly-parsed remote port with frport as a template for new rdata

.. _`fcoe_ctlr_vn_claim_notify.description`:

Description
-----------

Called with ctlr_mutex held.

.. _`fcoe_ctlr_vn_claim_resp`:

fcoe_ctlr_vn_claim_resp
=======================

.. c:function:: void fcoe_ctlr_vn_claim_resp(struct fcoe_ctlr *fip, struct fc_rport_priv *new)

    handle received Claim Response

    :param struct fcoe_ctlr \*fip:
        The FCoE controller that received the frame

    :param struct fc_rport_priv \*new:
        newly-parsed remote port with frport from the Claim Response

.. _`fcoe_ctlr_vn_claim_resp.description`:

Description
-----------

Called with ctlr_mutex held.

.. _`fcoe_ctlr_vn_beacon`:

fcoe_ctlr_vn_beacon
===================

.. c:function:: void fcoe_ctlr_vn_beacon(struct fcoe_ctlr *fip, struct fc_rport_priv *new)

    handle received beacon.

    :param struct fcoe_ctlr \*fip:
        The FCoE controller that received the frame

    :param struct fc_rport_priv \*new:
        newly-parsed remote port with frport from the Beacon

.. _`fcoe_ctlr_vn_beacon.description`:

Description
-----------

Called with ctlr_mutex held.

.. _`fcoe_ctlr_vn_age`:

fcoe_ctlr_vn_age
================

.. c:function:: unsigned long fcoe_ctlr_vn_age(struct fcoe_ctlr *fip)

    Check for VN_ports without recent beacons

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

.. _`fcoe_ctlr_vn_age.description`:

Description
-----------

Called with ctlr_mutex held.
Called only in state FIP_ST_VNMP_UP.
Returns the soonest time for next age-out or a time far in the future.

.. _`fcoe_ctlr_vn_recv`:

fcoe_ctlr_vn_recv
=================

.. c:function:: int fcoe_ctlr_vn_recv(struct fcoe_ctlr *fip, struct sk_buff *skb)

    Receive a FIP frame

    :param struct fcoe_ctlr \*fip:
        The FCoE controller that received the frame

    :param struct sk_buff \*skb:
        The received FIP frame

.. _`fcoe_ctlr_vn_recv.description`:

Description
-----------

Returns non-zero if the frame is dropped.
Always consumes the frame.

.. _`fcoe_ctlr_vlan_parse`:

fcoe_ctlr_vlan_parse
====================

.. c:function:: int fcoe_ctlr_vlan_parse(struct fcoe_ctlr *fip, struct sk_buff *skb, struct fc_rport_priv *rdata)

    parse vlan discovery request or response

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param struct sk_buff \*skb:
        incoming packet

    :param struct fc_rport_priv \*rdata:
        buffer for resulting parsed VLAN entry plus fcoe_rport

.. _`fcoe_ctlr_vlan_parse.description`:

Description
-----------

Returns non-zero error number on error.
Does not consume the packet.

.. _`fcoe_ctlr_vlan_send`:

fcoe_ctlr_vlan_send
===================

.. c:function:: void fcoe_ctlr_vlan_send(struct fcoe_ctlr *fip, enum fip_vlan_subcode sub, const u8 *dest)

    Send a FIP VLAN Notification

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param enum fip_vlan_subcode sub:
        sub-opcode for vlan notification or vn2vn vlan notification

    :param const u8 \*dest:
        The destination Ethernet MAC address

.. _`fcoe_ctlr_vlan_disc_reply`:

fcoe_ctlr_vlan_disc_reply
=========================

.. c:function:: void fcoe_ctlr_vlan_disc_reply(struct fcoe_ctlr *fip, struct fc_rport_priv *rdata)

    send FIP VLAN Discovery Notification.

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

    :param struct fc_rport_priv \*rdata:
        *undescribed*

.. _`fcoe_ctlr_vlan_disc_reply.description`:

Description
-----------

Called with ctlr_mutex held.

.. _`fcoe_ctlr_vlan_recv`:

fcoe_ctlr_vlan_recv
===================

.. c:function:: int fcoe_ctlr_vlan_recv(struct fcoe_ctlr *fip, struct sk_buff *skb)

    vlan request receive handler for VN2VN mode.

    :param struct fcoe_ctlr \*fip:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`fcoe_ctlr_disc_recv`:

fcoe_ctlr_disc_recv
===================

.. c:function:: void fcoe_ctlr_disc_recv(struct fc_lport *lport, struct fc_frame *fp)

    discovery receive handler for VN2VN mode.

    :param struct fc_lport \*lport:
        The local port

    :param struct fc_frame \*fp:
        The received frame

.. _`fcoe_ctlr_disc_recv.description`:

Description
-----------

This should never be called since we don't see RSCNs or other
fabric-generated ELSes.

.. _`fcoe_ctlr_disc_start`:

fcoe_ctlr_disc_start
====================

.. c:function:: void fcoe_ctlr_disc_start(void (*callback)(struct fc_lport *, enum fc_disc_event), struct fc_lport *lport)

    start discovery for VN2VN mode.

    :param void (\*callback)(struct fc_lport \*, enum fc_disc_event):
        *undescribed*

    :param struct fc_lport \*lport:
        *undescribed*

.. _`fcoe_ctlr_disc_start.description`:

Description
-----------

This sets a flag indicating that remote ports should be created
and started for the peers we discover.  We use the disc_callback
pointer as that flag.  Peers already discovered are created here.

The lport lock is held during this call. The callback must be done
later, without holding either the lport or discovery locks.
The fcoe_ctlr lock may also be held during this call.

.. _`fcoe_ctlr_vn_disc`:

fcoe_ctlr_vn_disc
=================

.. c:function:: void fcoe_ctlr_vn_disc(struct fcoe_ctlr *fip)

    report FIP VN_port discovery results after claim state.

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

.. _`fcoe_ctlr_vn_disc.description`:

Description
-----------

Starts the FLOGI and PLOGI login process to each discovered rport for which
we've received at least one beacon.
Performs the discovery complete callback.

.. _`fcoe_ctlr_vn_timeout`:

fcoe_ctlr_vn_timeout
====================

.. c:function:: void fcoe_ctlr_vn_timeout(struct fcoe_ctlr *fip)

    timer work function for VN2VN mode.

    :param struct fcoe_ctlr \*fip:
        The FCoE controller

.. _`fcoe_ctlr_mode_set`:

fcoe_ctlr_mode_set
==================

.. c:function:: void fcoe_ctlr_mode_set(struct fc_lport *lport, struct fcoe_ctlr *fip, enum fip_mode fip_mode)

    Set or reset the ctlr's mode

    :param struct fc_lport \*lport:
        The local port to be (re)configured

    :param struct fcoe_ctlr \*fip:
        The FCoE controller whose mode is changing

    :param enum fip_mode fip_mode:
        The new fip mode

.. _`fcoe_ctlr_mode_set.description`:

Description
-----------

Note that the we shouldn't be changing the libfc discovery settings
(fc_disc_config) while an lport is going through the libfc state
machine. The mode can only be changed when a fcoe_ctlr device is
disabled, so that should ensure that this routine is only called
when nothing is happening.

.. _`fcoe_libfc_config`:

fcoe_libfc_config
=================

.. c:function:: int fcoe_libfc_config(struct fc_lport *lport, struct fcoe_ctlr *fip, const struct libfc_function_template *tt, int init_fcp)

    Sets up libfc related properties for local port

    :param struct fc_lport \*lport:
        The local port to configure libfc for

    :param struct fcoe_ctlr \*fip:
        The FCoE controller in use by the local port

    :param const struct libfc_function_template \*tt:
        The libfc function template

    :param int init_fcp:
        If non-zero, the FCP portion of libfc should be initialized

.. _`fcoe_libfc_config.description`:

Description
-----------

Returns : 0 for success

.. This file was automatic generated / don't edit.

