.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libfc/fc_exch.c

.. _`fc_exch_pool`:

struct fc_exch_pool
===================

.. c:type:: struct fc_exch_pool

    Per cpu exchange pool

.. _`fc_exch_pool.definition`:

Definition
----------

.. code-block:: c

    struct fc_exch_pool {
        spinlock_t lock;
        struct list_head ex_list;
        u16 next_index;
        u16 total_exches;
        u16 left;
        u16 right;
    }

.. _`fc_exch_pool.members`:

Members
-------

lock
    Exch pool lock

ex_list
    List of exchanges

next_index
    Next possible free exchange index

total_exches
    Total allocated exchanges

left
    *undescribed*

right
    *undescribed*

.. _`fc_exch_pool.description`:

Description
-----------

This structure manages per cpu exchanges in array of exchange pointers.
This array is allocated followed by struct fc_exch_pool memory for
assigned range of exchanges to per cpu pool.

.. _`fc_exch_mgr`:

struct fc_exch_mgr
==================

.. c:type:: struct fc_exch_mgr

    The Exchange Manager (EM).

.. _`fc_exch_mgr.definition`:

Definition
----------

.. code-block:: c

    struct fc_exch_mgr {
        struct fc_exch_pool __percpu *pool;
        mempool_t *ep_pool;
        struct fc_lport *lport;
        enum fc_class class;
        struct kref kref;
        u16 min_xid;
        u16 max_xid;
        u16 pool_max_index;
        struct stats;
    }

.. _`fc_exch_mgr.members`:

Members
-------

pool
    Per cpu exch pool

ep_pool
    Reserved exchange pointers

lport
    *undescribed*

class
    Default class for new sequences

kref
    Reference counter

min_xid
    Minimum exchange ID

max_xid
    Maximum exchange ID

pool_max_index
    Max exch array index in exch pool

stats
    Statistics structure

.. _`fc_exch_mgr.description`:

Description
-----------

This structure is the center for creating exchanges and sequences.
It manages the allocation of exchange IDs.

.. _`fc_exch_mgr_anchor`:

struct fc_exch_mgr_anchor
=========================

.. c:type:: struct fc_exch_mgr_anchor

    primary structure for list of EMs

.. _`fc_exch_mgr_anchor.definition`:

Definition
----------

.. code-block:: c

    struct fc_exch_mgr_anchor {
        struct list_head ema_list;
        struct fc_exch_mgr *mp;
        bool (*match)(struct fc_frame *);
    }

.. _`fc_exch_mgr_anchor.members`:

Members
-------

ema_list
    Exchange Manager Anchor list

mp
    Exchange Manager associated with this anchor

match
    Routine to determine if this anchor's EM should be used

.. _`fc_exch_mgr_anchor.description`:

Description
-----------

When walking the list of anchors the match routine will be called
for each anchor to determine if that EM should be used. The last
anchor in the list will always match to handle any exchanges not
handled by other EMs. The non-default EMs would be added to the
anchor list by HW that provides offloads.

.. _`fc_exch_name_lookup`:

fc_exch_name_lookup
===================

.. c:function:: const char *fc_exch_name_lookup(unsigned int op, char **table, unsigned int max_index)

    Lookup name by opcode

    :param unsigned int op:
        Opcode to be looked up

    :param char \*\*table:
        Opcode/name table

    :param unsigned int max_index:
        Index not to be exceeded

.. _`fc_exch_name_lookup.description`:

Description
-----------

This routine is used to determine a human-readable string identifying
a R_CTL opcode.

.. _`fc_exch_rctl_name`:

fc_exch_rctl_name
=================

.. c:function:: const char *fc_exch_rctl_name(unsigned int op)

    Wrapper routine for \ :c:func:`fc_exch_name_lookup`\ 

    :param unsigned int op:
        The opcode to be looked up

.. _`fc_exch_hold`:

fc_exch_hold
============

.. c:function:: void fc_exch_hold(struct fc_exch *ep)

    Increment an exchange's reference count

    :param struct fc_exch \*ep:
        Echange to be held

.. _`fc_exch_setup_hdr`:

fc_exch_setup_hdr
=================

.. c:function:: void fc_exch_setup_hdr(struct fc_exch *ep, struct fc_frame *fp, u32 f_ctl)

    Initialize a FC header by initializing some fields and determine SOF and EOF.

    :param struct fc_exch \*ep:
        The exchange to that will use the header

    :param struct fc_frame \*fp:
        The frame whose header is to be modified

    :param u32 f_ctl:
        F_CTL bits that will be used for the frame header

.. _`fc_exch_setup_hdr.the-fields-initialized-by-this-routine-are`:

The fields initialized by this routine are
------------------------------------------

fh_ox_id, fh_rx_id,
fh_seq_id, fh_seq_cnt and the SOF and EOF.

.. _`fc_exch_release`:

fc_exch_release
===============

.. c:function:: void fc_exch_release(struct fc_exch *ep)

    Decrement an exchange's reference count

    :param struct fc_exch \*ep:
        Exchange to be released

.. _`fc_exch_release.description`:

Description
-----------

If the reference count reaches zero and the exchange is complete,
it is freed.

.. _`fc_exch_timer_cancel`:

fc_exch_timer_cancel
====================

.. c:function:: void fc_exch_timer_cancel(struct fc_exch *ep)

    cancel exch timer

    :param struct fc_exch \*ep:
        The exchange whose timer to be canceled

.. _`fc_exch_timer_set_locked`:

fc_exch_timer_set_locked
========================

.. c:function:: void fc_exch_timer_set_locked(struct fc_exch *ep, unsigned int timer_msec)

    Start a timer for an exchange w/ the the exchange lock held

    :param struct fc_exch \*ep:
        The exchange whose timer will start

    :param unsigned int timer_msec:
        The timeout period

.. _`fc_exch_timer_set_locked.description`:

Description
-----------

Used for upper level protocols to time out the exchange.
The timer is cancelled when it fires or when the exchange completes.

.. _`fc_exch_timer_set`:

fc_exch_timer_set
=================

.. c:function:: void fc_exch_timer_set(struct fc_exch *ep, unsigned int timer_msec)

    Lock the exchange and set the timer

    :param struct fc_exch \*ep:
        The exchange whose timer will start

    :param unsigned int timer_msec:
        The timeout period

.. _`fc_exch_done_locked`:

fc_exch_done_locked
===================

.. c:function:: int fc_exch_done_locked(struct fc_exch *ep)

    Complete an exchange with the exchange lock held

    :param struct fc_exch \*ep:
        The exchange that is complete

.. _`fc_exch_done_locked.note`:

Note
----

May sleep if invoked from outside a response handler.

.. _`fc_exch_ptr_get`:

fc_exch_ptr_get
===============

.. c:function:: struct fc_exch *fc_exch_ptr_get(struct fc_exch_pool *pool, u16 index)

    Return an exchange from an exchange pool

    :param struct fc_exch_pool \*pool:
        Exchange Pool to get an exchange from

    :param u16 index:
        Index of the exchange within the pool

.. _`fc_exch_ptr_get.description`:

Description
-----------

Use the index to get an exchange from within an exchange pool. exches
will point to an array of exchange pointers. The index will select
the exchange within the array.

.. _`fc_exch_ptr_set`:

fc_exch_ptr_set
===============

.. c:function:: void fc_exch_ptr_set(struct fc_exch_pool *pool, u16 index, struct fc_exch *ep)

    Assign an exchange to a slot in an exchange pool

    :param struct fc_exch_pool \*pool:
        The pool to assign the exchange to

    :param u16 index:
        The index in the pool where the exchange will be assigned

    :param struct fc_exch \*ep:
        The exchange to assign to the pool

.. _`fc_exch_delete`:

fc_exch_delete
==============

.. c:function:: void fc_exch_delete(struct fc_exch *ep)

    Delete an exchange

    :param struct fc_exch \*ep:
        The exchange to be deleted

.. _`fc_seq_send`:

fc_seq_send
===========

.. c:function:: int fc_seq_send(struct fc_lport *lport, struct fc_seq *sp, struct fc_frame *fp)

    Send a frame using existing sequence/exchange pair

    :param struct fc_lport \*lport:
        The local port that the exchange will be sent on

    :param struct fc_seq \*sp:
        The sequence to be sent

    :param struct fc_frame \*fp:
        The frame to be sent on the exchange

.. _`fc_seq_send.note`:

Note
----

The frame will be freed either by a direct call to fc_frame_free(fp)
or indirectly by calling libfc_function_template.frame_send().

.. _`fc_seq_alloc`:

fc_seq_alloc
============

.. c:function:: struct fc_seq *fc_seq_alloc(struct fc_exch *ep, u8 seq_id)

    Allocate a sequence for a given exchange

    :param struct fc_exch \*ep:
        The exchange to allocate a new sequence for

    :param u8 seq_id:
        The sequence ID to be used

.. _`fc_seq_alloc.description`:

Description
-----------

We don't support multiple originated sequences on the same exchange.
By implication, any previously originated sequence on this exchange
is complete, and we reallocate the same sequence.

.. _`fc_seq_start_next_locked`:

fc_seq_start_next_locked
========================

.. c:function:: struct fc_seq *fc_seq_start_next_locked(struct fc_seq *sp)

    Allocate a new sequence on the same exchange as the supplied sequence

    :param struct fc_seq \*sp:
        The sequence/exchange to get a new sequence for

.. _`fc_seq_start_next`:

fc_seq_start_next
=================

.. c:function:: struct fc_seq *fc_seq_start_next(struct fc_seq *sp)

    Lock the exchange and get a new sequence for a given sequence/exchange pair

    :param struct fc_seq \*sp:
        The sequence/exchange to get a new exchange for

.. _`fc_exch_abort_locked`:

fc_exch_abort_locked
====================

.. c:function:: int fc_exch_abort_locked(struct fc_exch *ep, unsigned int timer_msec)

    Abort an exchange

    :param struct fc_exch \*ep:
        The exchange to be aborted

    :param unsigned int timer_msec:
        The period of time to wait before aborting

.. _`fc_exch_abort_locked.description`:

Description
-----------

Abort an exchange and sequence. Generally called because of a
exchange timeout or an abort from the upper layer.

A timer_msec can be specified for abort timeout, if non-zero
timer_msec value is specified then exchange resp handler
will be called with timeout error if no response to abort.

.. _`fc_exch_abort_locked.locking-notes`:

Locking notes
-------------

Called with exch lock held

.. _`fc_exch_abort_locked.return-value`:

Return value
------------

0 on success else error code

.. _`fc_seq_exch_abort`:

fc_seq_exch_abort
=================

.. c:function:: int fc_seq_exch_abort(const struct fc_seq *req_sp, unsigned int timer_msec)

    Abort an exchange and sequence

    :param const struct fc_seq \*req_sp:
        The sequence to be aborted

    :param unsigned int timer_msec:
        The period of time to wait before aborting

.. _`fc_seq_exch_abort.description`:

Description
-----------

Generally called because of a timeout or an abort from the upper layer.

.. _`fc_seq_exch_abort.return-value`:

Return value
------------

0 on success else error code

.. _`fc_invoke_resp`:

fc_invoke_resp
==============

.. c:function:: bool fc_invoke_resp(struct fc_exch *ep, struct fc_seq *sp, struct fc_frame *fp)

    invoke ep->resp()

    :param struct fc_exch \*ep:
        *undescribed*

    :param struct fc_seq \*sp:
        *undescribed*

    :param struct fc_frame \*fp:
        *undescribed*

.. _`fc_invoke_resp.notes`:

Notes
-----

It is assumed that after initialization finished (this means the
first unlock of ex_lock after \ :c:func:`fc_exch_alloc`\ ) ep->resp and ep->arg are
modified only via \ :c:func:`fc_seq_set_resp`\ . This guarantees that none of these
two variables changes if ep->resp_active > 0.

If an \ :c:func:`fc_seq_set_resp`\  call is busy modifying ep->resp and ep->arg when
this function is invoked, the first \ :c:func:`spin_lock_bh`\  call in this function
will wait until \ :c:func:`fc_seq_set_resp`\  has finished modifying these variables.

Since \ :c:func:`fc_exch_done`\  invokes \ :c:func:`fc_seq_set_resp`\  it is guaranteed that that
ep->resp() won't be invoked after \ :c:func:`fc_exch_done`\  has returned.

The response handler itself may invoke \ :c:func:`fc_exch_done`\ , which will clear the
ep->resp pointer.

.. _`fc_invoke_resp.return-value`:

Return value
------------

Returns true if and only if ep->resp has been invoked.

.. _`fc_exch_timeout`:

fc_exch_timeout
===============

.. c:function:: void fc_exch_timeout(struct work_struct *work)

    Handle exchange timer expiration

    :param struct work_struct \*work:
        The work_struct identifying the exchange that timed out

.. _`fc_exch_em_alloc`:

fc_exch_em_alloc
================

.. c:function:: struct fc_exch *fc_exch_em_alloc(struct fc_lport *lport, struct fc_exch_mgr *mp)

    Allocate an exchange from a specified EM.

    :param struct fc_lport \*lport:
        The local port that the exchange is for

    :param struct fc_exch_mgr \*mp:
        The exchange manager that will allocate the exchange

.. _`fc_exch_em_alloc.description`:

Description
-----------

Returns pointer to allocated fc_exch with exch lock held.

.. _`fc_exch_alloc`:

fc_exch_alloc
=============

.. c:function:: struct fc_exch *fc_exch_alloc(struct fc_lport *lport, struct fc_frame *fp)

    Allocate an exchange from an EM on a local port's list of EMs.

    :param struct fc_lport \*lport:
        The local port that will own the exchange

    :param struct fc_frame \*fp:
        The FC frame that the exchange will be for

.. _`fc_exch_alloc.description`:

Description
-----------

This function walks the list of exchange manager(EM)
anchors to select an EM for a new exchange allocation. The
EM is selected when a NULL match function pointer is encountered
or when a call to a match function returns true.

.. _`fc_exch_find`:

fc_exch_find
============

.. c:function:: struct fc_exch *fc_exch_find(struct fc_exch_mgr *mp, u16 xid)

    Lookup and hold an exchange

    :param struct fc_exch_mgr \*mp:
        The exchange manager to lookup the exchange from

    :param u16 xid:
        The XID of the exchange to look up

.. _`fc_exch_done`:

fc_exch_done
============

.. c:function:: void fc_exch_done(struct fc_seq *sp)

    Indicate that an exchange/sequence tuple is complete and the memory allocated for the related objects may be freed.

    :param struct fc_seq \*sp:
        The sequence that has completed

.. _`fc_exch_done.note`:

Note
----

May sleep if invoked from outside a response handler.

.. _`fc_exch_resp`:

fc_exch_resp
============

.. c:function:: struct fc_exch *fc_exch_resp(struct fc_lport *lport, struct fc_exch_mgr *mp, struct fc_frame *fp)

    Allocate a new exchange for a response frame

    :param struct fc_lport \*lport:
        The local port that the exchange was for

    :param struct fc_exch_mgr \*mp:
        The exchange manager to allocate the exchange from

    :param struct fc_frame \*fp:
        The response frame

.. _`fc_exch_resp.description`:

Description
-----------

Sets the responder ID in the frame header.

.. _`fc_seq_lookup_recip`:

fc_seq_lookup_recip
===================

.. c:function:: enum fc_pf_rjt_reason fc_seq_lookup_recip(struct fc_lport *lport, struct fc_exch_mgr *mp, struct fc_frame *fp)

    Find a sequence where the other end originated the sequence

    :param struct fc_lport \*lport:
        The local port that the frame was sent to

    :param struct fc_exch_mgr \*mp:
        The Exchange Manager to lookup the exchange from

    :param struct fc_frame \*fp:
        The frame associated with the sequence we're looking for

.. _`fc_seq_lookup_recip.description`:

Description
-----------

If fc_pf_rjt_reason is FC_RJT_NONE then this function will have a hold
on the ep that should be released by the caller.

.. _`fc_seq_lookup_orig`:

fc_seq_lookup_orig
==================

.. c:function:: struct fc_seq *fc_seq_lookup_orig(struct fc_exch_mgr *mp, struct fc_frame *fp)

    Find a sequence where this end originated the sequence

    :param struct fc_exch_mgr \*mp:
        The Exchange Manager to lookup the exchange from

    :param struct fc_frame \*fp:
        The frame associated with the sequence we're looking for

.. _`fc_seq_lookup_orig.description`:

Description
-----------

Does not hold the sequence for the caller.

.. _`fc_exch_set_addr`:

fc_exch_set_addr
================

.. c:function:: void fc_exch_set_addr(struct fc_exch *ep, u32 orig_id, u32 resp_id)

    Set the source and destination IDs for an exchange

    :param struct fc_exch \*ep:
        The exchange to set the addresses for

    :param u32 orig_id:
        The originator's ID

    :param u32 resp_id:
        The responder's ID

.. _`fc_exch_set_addr.description`:

Description
-----------

Note this must be done before the first sequence of the exchange is sent.

.. _`fc_seq_els_rsp_send`:

fc_seq_els_rsp_send
===================

.. c:function:: void fc_seq_els_rsp_send(struct fc_frame *fp, enum fc_els_cmd els_cmd, struct fc_seq_els_data *els_data)

    Send an ELS response using information from the existing sequence/exchange.

    :param struct fc_frame \*fp:
        The received frame

    :param enum fc_els_cmd els_cmd:
        The ELS command to be sent

    :param struct fc_seq_els_data \*els_data:
        The ELS data to be sent

.. _`fc_seq_els_rsp_send.description`:

Description
-----------

The received frame is not freed.

.. _`fc_seq_send_last`:

fc_seq_send_last
================

.. c:function:: void fc_seq_send_last(struct fc_seq *sp, struct fc_frame *fp, enum fc_rctl rctl, enum fc_fh_type fh_type)

    Send a sequence that is the last in the exchange

    :param struct fc_seq \*sp:
        The sequence that is to be sent

    :param struct fc_frame \*fp:
        The frame that will be sent on the sequence

    :param enum fc_rctl rctl:
        The R_CTL information to be sent

    :param enum fc_fh_type fh_type:
        The frame header type

.. _`fc_seq_send_ack`:

fc_seq_send_ack
===============

.. c:function:: void fc_seq_send_ack(struct fc_seq *sp, const struct fc_frame *rx_fp)

    Send an acknowledgement that we've received a frame

    :param struct fc_seq \*sp:
        The sequence to send the ACK on

    :param const struct fc_frame \*rx_fp:
        The received frame that is being acknoledged

.. _`fc_seq_send_ack.description`:

Description
-----------

Send ACK_1 (or equiv.) indicating we received something.

.. _`fc_exch_send_ba_rjt`:

fc_exch_send_ba_rjt
===================

.. c:function:: void fc_exch_send_ba_rjt(struct fc_frame *rx_fp, enum fc_ba_rjt_reason reason, enum fc_ba_rjt_explan explan)

    Send BLS Reject

    :param struct fc_frame \*rx_fp:
        The frame being rejected

    :param enum fc_ba_rjt_reason reason:
        The reason the frame is being rejected

    :param enum fc_ba_rjt_explan explan:
        The explanation for the rejection

.. _`fc_exch_send_ba_rjt.description`:

Description
-----------

This is for rejecting BA_ABTS only.

.. _`fc_exch_recv_abts`:

fc_exch_recv_abts
=================

.. c:function:: void fc_exch_recv_abts(struct fc_exch *ep, struct fc_frame *rx_fp)

    Handle an incoming ABTS

    :param struct fc_exch \*ep:
        The exchange the abort was on

    :param struct fc_frame \*rx_fp:
        The ABTS frame

.. _`fc_exch_recv_abts.description`:

Description
-----------

This would be for target mode usually, but could be due to lost
FCP transfer ready, confirm or RRQ. We always handle this as an
exchange abort, ignoring the parameter.

.. _`fc_seq_assign`:

fc_seq_assign
=============

.. c:function:: struct fc_seq *fc_seq_assign(struct fc_lport *lport, struct fc_frame *fp)

    Assign exchange and sequence for incoming request

    :param struct fc_lport \*lport:
        The local port that received the request

    :param struct fc_frame \*fp:
        The request frame

.. _`fc_seq_assign.description`:

Description
-----------

On success, the sequence pointer will be returned and also in fr_seq(@fp).
A reference will be held on the exchange/sequence for the caller, which
must call \ :c:func:`fc_seq_release`\ .

.. _`fc_seq_release`:

fc_seq_release
==============

.. c:function:: void fc_seq_release(struct fc_seq *sp)

    Release the hold

    :param struct fc_seq \*sp:
        The sequence.

.. _`fc_exch_recv_req`:

fc_exch_recv_req
================

.. c:function:: void fc_exch_recv_req(struct fc_lport *lport, struct fc_exch_mgr *mp, struct fc_frame *fp)

    Handler for an incoming request

    :param struct fc_lport \*lport:
        The local port that received the request

    :param struct fc_exch_mgr \*mp:
        The EM that the exchange is on

    :param struct fc_frame \*fp:
        The request frame

.. _`fc_exch_recv_req.description`:

Description
-----------

This is used when the other end is originating the exchange
and the sequence.

.. _`fc_exch_recv_seq_resp`:

fc_exch_recv_seq_resp
=====================

.. c:function:: void fc_exch_recv_seq_resp(struct fc_exch_mgr *mp, struct fc_frame *fp)

    Handler for an incoming response where the other end is the originator of the sequence that is a response to our initial exchange

    :param struct fc_exch_mgr \*mp:
        The EM that the exchange is on

    :param struct fc_frame \*fp:
        The response frame

.. _`fc_exch_recv_resp`:

fc_exch_recv_resp
=================

.. c:function:: void fc_exch_recv_resp(struct fc_exch_mgr *mp, struct fc_frame *fp)

    Handler for a sequence where other end is responding to our sequence

    :param struct fc_exch_mgr \*mp:
        The EM that the exchange is on

    :param struct fc_frame \*fp:
        The response frame

.. _`fc_exch_abts_resp`:

fc_exch_abts_resp
=================

.. c:function:: void fc_exch_abts_resp(struct fc_exch *ep, struct fc_frame *fp)

    Handler for a response to an ABT

    :param struct fc_exch \*ep:
        The exchange that the frame is on

    :param struct fc_frame \*fp:
        The response frame

.. _`fc_exch_abts_resp.description`:

Description
-----------

This response would be to an ABTS cancelling an exchange or sequence.
The response can be either BA_ACC or BA_RJT

.. _`fc_exch_recv_bls`:

fc_exch_recv_bls
================

.. c:function:: void fc_exch_recv_bls(struct fc_exch_mgr *mp, struct fc_frame *fp)

    Handler for a BLS sequence

    :param struct fc_exch_mgr \*mp:
        The EM that the exchange is on

    :param struct fc_frame \*fp:
        The request frame

.. _`fc_exch_recv_bls.description`:

Description
-----------

The BLS frame is always a sequence initiated by the remote side.
We may be either the originator or recipient of the exchange.

.. _`fc_seq_ls_acc`:

fc_seq_ls_acc
=============

.. c:function:: void fc_seq_ls_acc(struct fc_frame *rx_fp)

    Accept sequence with LS_ACC

    :param struct fc_frame \*rx_fp:
        The received frame, not freed here.

.. _`fc_seq_ls_acc.description`:

Description
-----------

If this fails due to allocation or transmit congestion, assume the
originator will repeat the sequence.

.. _`fc_seq_ls_rjt`:

fc_seq_ls_rjt
=============

.. c:function:: void fc_seq_ls_rjt(struct fc_frame *rx_fp, enum fc_els_rjt_reason reason, enum fc_els_rjt_explan explan)

    Reject a sequence with ELS LS_RJT

    :param struct fc_frame \*rx_fp:
        The received frame, not freed here.

    :param enum fc_els_rjt_reason reason:
        The reason the sequence is being rejected

    :param enum fc_els_rjt_explan explan:
        The explanation for the rejection

.. _`fc_seq_ls_rjt.description`:

Description
-----------

If this fails due to allocation or transmit congestion, assume the
originator will repeat the sequence.

.. _`fc_exch_reset`:

fc_exch_reset
=============

.. c:function:: void fc_exch_reset(struct fc_exch *ep)

    Reset an exchange

    :param struct fc_exch \*ep:
        The exchange to be reset

.. _`fc_exch_reset.note`:

Note
----

May sleep if invoked from outside a response handler.

.. _`fc_exch_pool_reset`:

fc_exch_pool_reset
==================

.. c:function:: void fc_exch_pool_reset(struct fc_lport *lport, struct fc_exch_pool *pool, u32 sid, u32 did)

    Reset a per cpu exchange pool

    :param struct fc_lport \*lport:
        The local port that the exchange pool is on

    :param struct fc_exch_pool \*pool:
        The exchange pool to be reset

    :param u32 sid:
        The source ID

    :param u32 did:
        The destination ID

.. _`fc_exch_pool_reset.description`:

Description
-----------

Resets a per cpu exches pool, releasing all of its sequences
and exchanges. If sid is non-zero then reset only exchanges
we sourced from the local port's FID. If did is non-zero then
only reset exchanges destined for the local port's FID.

.. _`fc_exch_mgr_reset`:

fc_exch_mgr_reset
=================

.. c:function:: void fc_exch_mgr_reset(struct fc_lport *lport, u32 sid, u32 did)

    Reset all EMs of a local port

    :param struct fc_lport \*lport:
        The local port whose EMs are to be reset

    :param u32 sid:
        The source ID

    :param u32 did:
        The destination ID

.. _`fc_exch_mgr_reset.description`:

Description
-----------

Reset all EMs associated with a given local port. Release all
sequences and exchanges. If sid is non-zero then reset only the
exchanges sent from the local port's FID. If did is non-zero then
reset only exchanges destined for the local port's FID.

.. _`fc_exch_lookup`:

fc_exch_lookup
==============

.. c:function:: struct fc_exch *fc_exch_lookup(struct fc_lport *lport, u32 xid)

    find an exchange

    :param struct fc_lport \*lport:
        The local port

    :param u32 xid:
        The exchange ID

.. _`fc_exch_lookup.description`:

Description
-----------

Returns exchange pointer with hold for caller, or NULL if not found.

.. _`fc_exch_els_rec`:

fc_exch_els_rec
===============

.. c:function:: void fc_exch_els_rec(struct fc_frame *rfp)

    Handler for ELS REC (Read Exchange Concise) requests

    :param struct fc_frame \*rfp:
        The REC frame, not freed here.

.. _`fc_exch_els_rec.description`:

Description
-----------

Note that the requesting port may be different than the S_ID in the request.

.. _`fc_exch_rrq_resp`:

fc_exch_rrq_resp
================

.. c:function:: void fc_exch_rrq_resp(struct fc_seq *sp, struct fc_frame *fp, void *arg)

    Handler for RRQ responses

    :param struct fc_seq \*sp:
        The sequence that the RRQ is on

    :param struct fc_frame \*fp:
        The RRQ frame

    :param void \*arg:
        The exchange that the RRQ is on

.. _`fc_exch_rrq_resp.todo`:

TODO
----

fix error handler.

.. _`fc_exch_seq_send`:

fc_exch_seq_send
================

.. c:function:: struct fc_seq *fc_exch_seq_send(struct fc_lport *lport, struct fc_frame *fp, void (*resp)(struct fc_seq *, struct fc_frame *fp, void *arg), void (*destructor)(struct fc_seq *, void *), void *arg, u32 timer_msec)

    Send a frame using a new exchange and sequence

    :param struct fc_lport \*lport:
        The local port to send the frame on

    :param struct fc_frame \*fp:
        The frame to be sent

    :param void (\*resp)(struct fc_seq \*, struct fc_frame \*fp, void \*arg):
        The response handler for this request

    :param void (\*destructor)(struct fc_seq \*, void \*):
        The destructor for the exchange

    :param void \*arg:
        The argument to be passed to the response handler

    :param u32 timer_msec:
        The timeout period for the exchange

.. _`fc_exch_seq_send.description`:

Description
-----------

The exchange response handler is set in this routine to \ :c:func:`resp`\ 
function pointer. It can be called in two scenarios: if a timeout
occurs or if a response frame is received for the exchange. The
fc_frame pointer in response handler will also indicate timeout
as error using IS_ERR related macros.

The exchange destructor handler is also set in this routine.
The destructor handler is invoked by EM layer when exchange
is about to free, this can be used by caller to free its
resources along with exchange free.

The arg is passed back to resp and destructor handler.

The timeout value (in msec) for an exchange is set if non zero
timer_msec argument is specified. The timer is canceled when
it fires or when the exchange is done. The exchange timeout handler
is registered by EM layer.

The frame pointer with some of the header's fields must be
filled before calling this routine, those fields are:

- routing control
- FC port did
- FC port sid
- FC header type
- frame control
- parameter or relative offset

.. _`fc_exch_rrq`:

fc_exch_rrq
===========

.. c:function:: void fc_exch_rrq(struct fc_exch *ep)

    Send an ELS RRQ (Reinstate Recovery Qualifier) command

    :param struct fc_exch \*ep:
        The exchange to send the RRQ on

.. _`fc_exch_rrq.description`:

Description
-----------

This tells the remote port to stop blocking the use of
the exchange and the seq_cnt range.

.. _`fc_exch_els_rrq`:

fc_exch_els_rrq
===============

.. c:function:: void fc_exch_els_rrq(struct fc_frame *fp)

    Handler for ELS RRQ (Reset Recovery Qualifier) requests

    :param struct fc_frame \*fp:
        The RRQ frame, not freed here.

.. _`fc_exch_update_stats`:

fc_exch_update_stats
====================

.. c:function:: void fc_exch_update_stats(struct fc_lport *lport)

    update exches stats to lport

    :param struct fc_lport \*lport:
        The local port to update exchange manager stats

.. _`fc_exch_mgr_add`:

fc_exch_mgr_add
===============

.. c:function:: struct fc_exch_mgr_anchor *fc_exch_mgr_add(struct fc_lport *lport, struct fc_exch_mgr *mp, bool (*match)(struct fc_frame *))

    Add an exchange manager to a local port's list of EMs

    :param struct fc_lport \*lport:
        The local port to add the exchange manager to

    :param struct fc_exch_mgr \*mp:
        The exchange manager to be added to the local port

    :param bool (\*match)(struct fc_frame \*):
        The match routine that indicates when this EM should be used

.. _`fc_exch_mgr_destroy`:

fc_exch_mgr_destroy
===================

.. c:function:: void fc_exch_mgr_destroy(struct kref *kref)

    Destroy an exchange manager

    :param struct kref \*kref:
        The reference to the EM to be destroyed

.. _`fc_exch_mgr_del`:

fc_exch_mgr_del
===============

.. c:function:: void fc_exch_mgr_del(struct fc_exch_mgr_anchor *ema)

    Delete an EM from a local port's list

    :param struct fc_exch_mgr_anchor \*ema:
        The exchange manager anchor identifying the EM to be deleted

.. _`fc_exch_mgr_list_clone`:

fc_exch_mgr_list_clone
======================

.. c:function:: int fc_exch_mgr_list_clone(struct fc_lport *src, struct fc_lport *dst)

    Share all exchange manager objects

    :param struct fc_lport \*src:
        Source lport to clone exchange managers from

    :param struct fc_lport \*dst:
        New lport that takes references to all the exchange managers

.. _`fc_exch_mgr_alloc`:

fc_exch_mgr_alloc
=================

.. c:function:: struct fc_exch_mgr *fc_exch_mgr_alloc(struct fc_lport *lport, enum fc_class class, u16 min_xid, u16 max_xid, bool (*match)(struct fc_frame *))

    Allocate an exchange manager

    :param struct fc_lport \*lport:
        The local port that the new EM will be associated with

    :param enum fc_class class:
        The default FC class for new exchanges

    :param u16 min_xid:
        The minimum XID for exchanges from the new EM

    :param u16 max_xid:
        The maximum XID for exchanges from the new EM

    :param bool (\*match)(struct fc_frame \*):
        The match routine for the new EM

.. _`fc_exch_mgr_free`:

fc_exch_mgr_free
================

.. c:function:: void fc_exch_mgr_free(struct fc_lport *lport)

    Free all exchange managers on a local port

    :param struct fc_lport \*lport:
        The local port whose EMs are to be freed

.. _`fc_find_ema`:

fc_find_ema
===========

.. c:function:: struct fc_exch_mgr_anchor *fc_find_ema(u32 f_ctl, struct fc_lport *lport, struct fc_frame_header *fh)

    Lookup and return appropriate Exchange Manager Anchor depending upon 'xid'.

    :param u32 f_ctl:
        f_ctl

    :param struct fc_lport \*lport:
        The local port the frame was received on

    :param struct fc_frame_header \*fh:
        The received frame header

.. _`fc_exch_recv`:

fc_exch_recv
============

.. c:function:: void fc_exch_recv(struct fc_lport *lport, struct fc_frame *fp)

    Handler for received frames

    :param struct fc_lport \*lport:
        The local port the frame was received on

    :param struct fc_frame \*fp:
        The received frame

.. _`fc_exch_init`:

fc_exch_init
============

.. c:function:: int fc_exch_init(struct fc_lport *lport)

    Initialize the exchange layer for a local port

    :param struct fc_lport \*lport:
        The local port to initialize the exchange layer for

.. _`fc_setup_exch_mgr`:

fc_setup_exch_mgr
=================

.. c:function:: int fc_setup_exch_mgr( void)

    Setup an exchange manager

    :param  void:
        no arguments

.. _`fc_destroy_exch_mgr`:

fc_destroy_exch_mgr
===================

.. c:function:: void fc_destroy_exch_mgr( void)

    Destroy an exchange manager

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

