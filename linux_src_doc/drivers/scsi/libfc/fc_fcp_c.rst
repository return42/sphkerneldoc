.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libfc/fc_fcp.c

.. _`fc_fcp_internal`:

struct fc_fcp_internal
======================

.. c:type:: struct fc_fcp_internal

    FCP layer internal data

.. _`fc_fcp_internal.definition`:

Definition
----------

.. code-block:: c

    struct fc_fcp_internal {
        mempool_t *scsi_pkt_pool;
        spinlock_t scsi_queue_lock;
        struct list_head scsi_pkt_queue;
        unsigned long last_can_queue_ramp_down_time;
        unsigned long last_can_queue_ramp_up_time;
        int max_can_queue;
    }

.. _`fc_fcp_internal.members`:

Members
-------

scsi_pkt_pool
    Memory pool to draw FCP packets from

scsi_queue_lock
    Protects the scsi_pkt_queue

scsi_pkt_queue
    Current FCP packets

last_can_queue_ramp_down_time
    ramp down time

last_can_queue_ramp_up_time
    ramp up time

max_can_queue
    max can_queue size

.. _`fc_fcp_pkt_alloc`:

fc_fcp_pkt_alloc
================

.. c:function:: struct fc_fcp_pkt *fc_fcp_pkt_alloc(struct fc_lport *lport, gfp_t gfp)

    Allocate a fcp_pkt

    :param lport:
        The local port that the FCP packet is for
    :type lport: struct fc_lport \*

    :param gfp:
        GFP flags for allocation
    :type gfp: gfp_t

.. _`fc_fcp_pkt_alloc.return-value`:

Return value
------------

fcp_pkt structure or null on allocation failure.

.. _`fc_fcp_pkt_alloc.context`:

Context
-------

Can be called from process context, no lock is required.

.. _`fc_fcp_pkt_release`:

fc_fcp_pkt_release
==================

.. c:function:: void fc_fcp_pkt_release(struct fc_fcp_pkt *fsp)

    Release hold on a fcp_pkt

    :param fsp:
        The FCP packet to be released
    :type fsp: struct fc_fcp_pkt \*

.. _`fc_fcp_pkt_release.context`:

Context
-------

Can be called from process or interrupt context,
no lock is required.

.. _`fc_fcp_pkt_hold`:

fc_fcp_pkt_hold
===============

.. c:function:: void fc_fcp_pkt_hold(struct fc_fcp_pkt *fsp)

    Hold a fcp_pkt

    :param fsp:
        The FCP packet to be held
    :type fsp: struct fc_fcp_pkt \*

.. _`fc_fcp_pkt_destroy`:

fc_fcp_pkt_destroy
==================

.. c:function:: void fc_fcp_pkt_destroy(struct fc_seq *seq, void *fsp)

    Release hold on a fcp_pkt

    :param seq:
        The sequence that the FCP packet is on (required by destructor API)
    :type seq: struct fc_seq \*

    :param fsp:
        The FCP packet to be released
    :type fsp: void \*

.. _`fc_fcp_pkt_destroy.description`:

Description
-----------

This routine is called by a destructor callback in the \ :c:func:`fc_exch_seq_send`\ 
routine of the libfc Transport Template. The 'struct fc_seq' is a required
argument even though it is not used by this routine.

.. _`fc_fcp_pkt_destroy.context`:

Context
-------

No locking required.

.. _`fc_fcp_lock_pkt`:

fc_fcp_lock_pkt
===============

.. c:function:: int fc_fcp_lock_pkt(struct fc_fcp_pkt *fsp)

    Lock a fcp_pkt and increase its reference count

    :param fsp:
        The FCP packet to be locked and incremented
    :type fsp: struct fc_fcp_pkt \*

.. _`fc_fcp_lock_pkt.description`:

Description
-----------

We should only return error if we return a command to SCSI-ml before
getting a response. This can happen in cases where we send a abort, but
do not wait for the response and the abort and command can be passing
each other on the wire/network-layer.

.. _`fc_fcp_lock_pkt.note`:

Note
----

this function locks the packet and gets a reference to allow
callers to call the completion function while the lock is held and
not have to worry about the packets refcount.

.. _`fc_fcp_lock_pkt.todo`:

TODO
----

Maybe we should just have callers grab/release the lock and
have a function that they call to verify the fsp and grab a ref if
needed.

.. _`fc_fcp_unlock_pkt`:

fc_fcp_unlock_pkt
=================

.. c:function:: void fc_fcp_unlock_pkt(struct fc_fcp_pkt *fsp)

    Release a fcp_pkt's lock and decrement its reference count

    :param fsp:
        The FCP packet to be unlocked and decremented
    :type fsp: struct fc_fcp_pkt \*

.. _`fc_fcp_timer_set`:

fc_fcp_timer_set
================

.. c:function:: void fc_fcp_timer_set(struct fc_fcp_pkt *fsp, unsigned long delay)

    Start a timer for a fcp_pkt

    :param fsp:
        The FCP packet to start a timer for
    :type fsp: struct fc_fcp_pkt \*

    :param delay:
        The timeout period in jiffies
    :type delay: unsigned long

.. _`fc_fcp_send_abort`:

fc_fcp_send_abort
=================

.. c:function:: int fc_fcp_send_abort(struct fc_fcp_pkt *fsp)

    Send an abort for exchanges associated with a fcp_pkt

    :param fsp:
        The FCP packet to abort exchanges on
    :type fsp: struct fc_fcp_pkt \*

.. _`fc_fcp_retry_cmd`:

fc_fcp_retry_cmd
================

.. c:function:: void fc_fcp_retry_cmd(struct fc_fcp_pkt *fsp, int status_code)

    Retry a fcp_pkt

    :param fsp:
        The FCP packet to be retried
    :type fsp: struct fc_fcp_pkt \*

    :param status_code:
        *undescribed*
    :type status_code: int

.. _`fc_fcp_retry_cmd.description`:

Description
-----------

Sets the status code to be FC_ERROR and then calls
\ :c:func:`fc_fcp_complete_locked`\  which in turn calls \ :c:func:`fc_io_compl`\ .
\ :c:func:`fc_io_compl`\  will notify the SCSI-ml that the I/O is done.
The SCSI-ml will retry the command.

.. _`fc_fcp_ddp_setup`:

fc_fcp_ddp_setup
================

.. c:function:: void fc_fcp_ddp_setup(struct fc_fcp_pkt *fsp, u16 xid)

    Calls a LLD's ddp_setup routine to set up DDP context

    :param fsp:
        The FCP packet that will manage the DDP frames
    :type fsp: struct fc_fcp_pkt \*

    :param xid:
        The XID that will be used for the DDP exchange
    :type xid: u16

.. _`fc_fcp_ddp_done`:

fc_fcp_ddp_done
===============

.. c:function:: void fc_fcp_ddp_done(struct fc_fcp_pkt *fsp)

    Calls a LLD's ddp_done routine to release any DDP related resources for a fcp_pkt

    :param fsp:
        The FCP packet that DDP had been used on
    :type fsp: struct fc_fcp_pkt \*

.. _`fc_fcp_can_queue_ramp_up`:

fc_fcp_can_queue_ramp_up
========================

.. c:function:: void fc_fcp_can_queue_ramp_up(struct fc_lport *lport)

    increases can_queue

    :param lport:
        lport to ramp up can_queue
    :type lport: struct fc_lport \*

.. _`fc_fcp_can_queue_ramp_down`:

fc_fcp_can_queue_ramp_down
==========================

.. c:function:: bool fc_fcp_can_queue_ramp_down(struct fc_lport *lport)

    reduces can_queue

    :param lport:
        lport to reduce can_queue
    :type lport: struct fc_lport \*

.. _`fc_fcp_can_queue_ramp_down.description`:

Description
-----------

If we are getting memory allocation failures, then we may
be trying to execute too many commands. We let the running
commands complete or timeout, then try again with a reduced
can_queue. Eventually we will hit the point where we run
on all reserved structs.

.. _`get_fsp_rec_tov`:

get_fsp_rec_tov
===============

.. c:function:: unsigned int get_fsp_rec_tov(struct fc_fcp_pkt *fsp)

    Helper function to get REC_TOV

    :param fsp:
        the FCP packet
    :type fsp: struct fc_fcp_pkt \*

.. _`get_fsp_rec_tov.description`:

Description
-----------

Returns rec tov in jiffies as rpriv->e_d_tov + 1 second

.. _`fc_fcp_recv_data`:

fc_fcp_recv_data
================

.. c:function:: void fc_fcp_recv_data(struct fc_fcp_pkt *fsp, struct fc_frame *fp)

    Handler for receiving SCSI-FCP data from a target

    :param fsp:
        The FCP packet the data is on
    :type fsp: struct fc_fcp_pkt \*

    :param fp:
        The data frame
    :type fp: struct fc_frame \*

.. _`fc_fcp_send_data`:

fc_fcp_send_data
================

.. c:function:: int fc_fcp_send_data(struct fc_fcp_pkt *fsp, struct fc_seq *seq, size_t offset, size_t seq_blen)

    Send SCSI data to a target

    :param fsp:
        The FCP packet the data is on
    :type fsp: struct fc_fcp_pkt \*

    :param seq:
        *undescribed*
    :type seq: struct fc_seq \*

    :param offset:
        The starting offset for this data request
    :type offset: size_t

    :param seq_blen:
        The burst length for this data request
    :type seq_blen: size_t

.. _`fc_fcp_send_data.description`:

Description
-----------

Called after receiving a Transfer Ready data descriptor.
If the LLD is capable of sequence offload then send down the
seq_blen amount of data in single frame, otherwise send
multiple frames of the maximum frame payload supported by
the target port.

.. _`fc_fcp_abts_resp`:

fc_fcp_abts_resp
================

.. c:function:: void fc_fcp_abts_resp(struct fc_fcp_pkt *fsp, struct fc_frame *fp)

    Receive an ABTS response

    :param fsp:
        The FCP packet that is being aborted
    :type fsp: struct fc_fcp_pkt \*

    :param fp:
        The response frame
    :type fp: struct fc_frame \*

.. _`fc_fcp_recv`:

fc_fcp_recv
===========

.. c:function:: void fc_fcp_recv(struct fc_seq *seq, struct fc_frame *fp, void *arg)

    Receive an FCP frame

    :param seq:
        The sequence the frame is on
    :type seq: struct fc_seq \*

    :param fp:
        The received frame
    :type fp: struct fc_frame \*

    :param arg:
        The related FCP packet
    :type arg: void \*

.. _`fc_fcp_recv.context`:

Context
-------

Called from Soft IRQ context. Can not be called
holding the FCP packet list lock.

.. _`fc_fcp_resp`:

fc_fcp_resp
===========

.. c:function:: void fc_fcp_resp(struct fc_fcp_pkt *fsp, struct fc_frame *fp)

    Handler for FCP responses

    :param fsp:
        The FCP packet the response is for
    :type fsp: struct fc_fcp_pkt \*

    :param fp:
        The response frame
    :type fp: struct fc_frame \*

.. _`fc_fcp_complete_locked`:

fc_fcp_complete_locked
======================

.. c:function:: void fc_fcp_complete_locked(struct fc_fcp_pkt *fsp)

    Complete processing of a fcp_pkt with the fcp_pkt lock held

    :param fsp:
        The FCP packet to be completed
    :type fsp: struct fc_fcp_pkt \*

.. _`fc_fcp_complete_locked.description`:

Description
-----------

This function may sleep if a timer is pending. The packet lock must be
held, and the host lock must not be held.

.. _`fc_fcp_cleanup_cmd`:

fc_fcp_cleanup_cmd
==================

.. c:function:: void fc_fcp_cleanup_cmd(struct fc_fcp_pkt *fsp, int error)

    Cancel the active exchange on a fcp_pkt

    :param fsp:
        The FCP packet whose exchanges should be canceled
    :type fsp: struct fc_fcp_pkt \*

    :param error:
        The reason for the cancellation
    :type error: int

.. _`fc_fcp_cleanup_each_cmd`:

fc_fcp_cleanup_each_cmd
=======================

.. c:function:: void fc_fcp_cleanup_each_cmd(struct fc_lport *lport, unsigned int id, unsigned int lun, int error)

    Cancel all exchanges on a local port

    :param lport:
        The local port whose exchanges should be canceled
    :type lport: struct fc_lport \*

    :param id:
        The target's ID
    :type id: unsigned int

    :param lun:
        The LUN
    :type lun: unsigned int

    :param error:
        The reason for cancellation
    :type error: int

.. _`fc_fcp_cleanup_each_cmd.description`:

Description
-----------

If lun or id is -1, they are ignored.

.. _`fc_fcp_abort_io`:

fc_fcp_abort_io
===============

.. c:function:: void fc_fcp_abort_io(struct fc_lport *lport)

    Abort all FCP-SCSI exchanges on a local port

    :param lport:
        The local port whose exchanges are to be aborted
    :type lport: struct fc_lport \*

.. _`fc_fcp_pkt_send`:

fc_fcp_pkt_send
===============

.. c:function:: int fc_fcp_pkt_send(struct fc_lport *lport, struct fc_fcp_pkt *fsp)

    Send a fcp_pkt

    :param lport:
        The local port to send the FCP packet on
    :type lport: struct fc_lport \*

    :param fsp:
        The FCP packet to send
    :type fsp: struct fc_fcp_pkt \*

.. _`fc_fcp_pkt_send.return`:

Return
------

Zero for success and -1 for failure

.. _`fc_fcp_pkt_send.locks`:

Locks
-----

Called without locks held

.. _`fc_fcp_cmd_send`:

fc_fcp_cmd_send
===============

.. c:function:: int fc_fcp_cmd_send(struct fc_lport *lport, struct fc_fcp_pkt *fsp, void (*resp)(struct fc_seq *, struct fc_frame *fp, void *arg))

    Send a FCP command

    :param lport:
        The local port to send the command on
    :type lport: struct fc_lport \*

    :param fsp:
        The FCP packet the command is on
    :type fsp: struct fc_fcp_pkt \*

    :param void (\*resp)(struct fc_seq \*, struct fc_frame \*fp, void \*arg):
        The handler for the response

.. _`fc_fcp_error`:

fc_fcp_error
============

.. c:function:: void fc_fcp_error(struct fc_fcp_pkt *fsp, struct fc_frame *fp)

    Handler for FCP layer errors

    :param fsp:
        The FCP packet the error is on
    :type fsp: struct fc_fcp_pkt \*

    :param fp:
        The frame that has errored
    :type fp: struct fc_frame \*

.. _`fc_fcp_pkt_abort`:

fc_fcp_pkt_abort
================

.. c:function:: int fc_fcp_pkt_abort(struct fc_fcp_pkt *fsp)

    Abort a fcp_pkt

    :param fsp:
        The FCP packet to abort on
    :type fsp: struct fc_fcp_pkt \*

.. _`fc_fcp_pkt_abort.description`:

Description
-----------

Called to send an abort and then wait for abort completion

.. _`fc_lun_reset_send`:

fc_lun_reset_send
=================

.. c:function:: void fc_lun_reset_send(struct timer_list *t)

    Send LUN reset command

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`fc_lun_reset`:

fc_lun_reset
============

.. c:function:: int fc_lun_reset(struct fc_lport *lport, struct fc_fcp_pkt *fsp, unsigned int id, unsigned int lun)

    Send a LUN RESET command to a device and wait for the reply

    :param lport:
        The local port to sent the command on
    :type lport: struct fc_lport \*

    :param fsp:
        The FCP packet that identifies the LUN to be reset
    :type fsp: struct fc_fcp_pkt \*

    :param id:
        The SCSI command ID
    :type id: unsigned int

    :param lun:
        The LUN ID to be reset
    :type lun: unsigned int

.. _`fc_tm_done`:

fc_tm_done
==========

.. c:function:: void fc_tm_done(struct fc_seq *seq, struct fc_frame *fp, void *arg)

    Task Management response handler

    :param seq:
        The sequence that the response is on
    :type seq: struct fc_seq \*

    :param fp:
        The response frame
    :type fp: struct fc_frame \*

    :param arg:
        The FCP packet the response is for
    :type arg: void \*

.. _`fc_fcp_cleanup`:

fc_fcp_cleanup
==============

.. c:function:: void fc_fcp_cleanup(struct fc_lport *lport)

    Cleanup all FCP exchanges on a local port

    :param lport:
        The local port to be cleaned up
    :type lport: struct fc_lport \*

.. _`fc_fcp_timeout`:

fc_fcp_timeout
==============

.. c:function:: void fc_fcp_timeout(struct timer_list *t)

    Handler for fcp_pkt timeouts

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`fc_fcp_timeout.description`:

Description
-----------

If REC is supported then just issue it and return. The REC exchange will
complete or time out and recovery can continue at that point. Otherwise,
if the response has been received without all the data it has been
ER_TIMEOUT since the response was received. If the response has not been
received we see if data was received recently. If it has been then we
continue waiting, otherwise, we abort the command.

.. _`fc_fcp_rec`:

fc_fcp_rec
==========

.. c:function:: void fc_fcp_rec(struct fc_fcp_pkt *fsp)

    Send a REC ELS request

    :param fsp:
        The FCP packet to send the REC request on
    :type fsp: struct fc_fcp_pkt \*

.. _`fc_fcp_rec_resp`:

fc_fcp_rec_resp
===============

.. c:function:: void fc_fcp_rec_resp(struct fc_seq *seq, struct fc_frame *fp, void *arg)

    Handler for REC ELS responses

    :param seq:
        The sequence the response is on
    :type seq: struct fc_seq \*

    :param fp:
        The response frame
    :type fp: struct fc_frame \*

    :param arg:
        The FCP packet the response is on
    :type arg: void \*

.. _`fc_fcp_rec_resp.description`:

Description
-----------

If the response is a reject then the scsi layer will handle
the timeout. If the response is a LS_ACC then if the I/O was not completed
set the timeout and return. If the I/O was completed then complete the
exchange and tell the SCSI layer.

.. _`fc_fcp_rec_error`:

fc_fcp_rec_error
================

.. c:function:: void fc_fcp_rec_error(struct fc_fcp_pkt *fsp, struct fc_frame *fp)

    Handler for REC errors

    :param fsp:
        The FCP packet the error is on
    :type fsp: struct fc_fcp_pkt \*

    :param fp:
        The REC frame
    :type fp: struct fc_frame \*

.. _`fc_fcp_recovery`:

fc_fcp_recovery
===============

.. c:function:: void fc_fcp_recovery(struct fc_fcp_pkt *fsp, u8 code)

    Handler for fcp_pkt recovery

    :param fsp:
        The FCP pkt that needs to be aborted
    :type fsp: struct fc_fcp_pkt \*

    :param code:
        *undescribed*
    :type code: u8

.. _`fc_fcp_srr`:

fc_fcp_srr
==========

.. c:function:: void fc_fcp_srr(struct fc_fcp_pkt *fsp, enum fc_rctl r_ctl, u32 offset)

    Send a SRR request (Sequence Retransmission Request)

    :param fsp:
        The FCP packet the SRR is to be sent on
    :type fsp: struct fc_fcp_pkt \*

    :param r_ctl:
        The R_CTL field for the SRR request
        This is called after receiving status but insufficient data, or
        when expecting status but the request has timed out.
    :type r_ctl: enum fc_rctl

    :param offset:
        *undescribed*
    :type offset: u32

.. _`fc_fcp_srr_resp`:

fc_fcp_srr_resp
===============

.. c:function:: void fc_fcp_srr_resp(struct fc_seq *seq, struct fc_frame *fp, void *arg)

    Handler for SRR response

    :param seq:
        The sequence the SRR is on
    :type seq: struct fc_seq \*

    :param fp:
        The SRR frame
    :type fp: struct fc_frame \*

    :param arg:
        The FCP packet the SRR is on
    :type arg: void \*

.. _`fc_fcp_srr_error`:

fc_fcp_srr_error
================

.. c:function:: void fc_fcp_srr_error(struct fc_fcp_pkt *fsp, struct fc_frame *fp)

    Handler for SRR errors

    :param fsp:
        The FCP packet that the SRR error is on
    :type fsp: struct fc_fcp_pkt \*

    :param fp:
        The SRR frame
    :type fp: struct fc_frame \*

.. _`fc_fcp_lport_queue_ready`:

fc_fcp_lport_queue_ready
========================

.. c:function:: int fc_fcp_lport_queue_ready(struct fc_lport *lport)

    Determine if the lport and it's queue is ready

    :param lport:
        The local port to be checked
    :type lport: struct fc_lport \*

.. _`fc_queuecommand`:

fc_queuecommand
===============

.. c:function:: int fc_queuecommand(struct Scsi_Host *shost, struct scsi_cmnd *sc_cmd)

    The queuecommand function of the SCSI template

    :param shost:
        The Scsi_Host that the command was issued to
    :type shost: struct Scsi_Host \*

    :param sc_cmd:
        *undescribed*
    :type sc_cmd: struct scsi_cmnd \*

.. _`fc_queuecommand.description`:

Description
-----------

This is the i/o strategy routine, called by the SCSI layer.

.. _`fc_io_compl`:

fc_io_compl
===========

.. c:function:: void fc_io_compl(struct fc_fcp_pkt *fsp)

    Handle responses for completed commands

    :param fsp:
        The FCP packet that is complete
    :type fsp: struct fc_fcp_pkt \*

.. _`fc_io_compl.description`:

Description
-----------

Translates fcp_pkt errors to a Linux SCSI errors.
The fcp packet lock must be held when calling.

.. _`fc_eh_abort`:

fc_eh_abort
===========

.. c:function:: int fc_eh_abort(struct scsi_cmnd *sc_cmd)

    Abort a command

    :param sc_cmd:
        The SCSI command to abort
    :type sc_cmd: struct scsi_cmnd \*

.. _`fc_eh_abort.description`:

Description
-----------

From SCSI host template.
Send an ABTS to the target device and wait for the response.

.. _`fc_eh_device_reset`:

fc_eh_device_reset
==================

.. c:function:: int fc_eh_device_reset(struct scsi_cmnd *sc_cmd)

    Reset a single LUN

    :param sc_cmd:
        The SCSI command which identifies the device whose
        LUN is to be reset
    :type sc_cmd: struct scsi_cmnd \*

.. _`fc_eh_device_reset.description`:

Description
-----------

Set from SCSI host template.

.. _`fc_eh_host_reset`:

fc_eh_host_reset
================

.. c:function:: int fc_eh_host_reset(struct scsi_cmnd *sc_cmd)

    Reset a Scsi_Host.

    :param sc_cmd:
        The SCSI command that identifies the SCSI host to be reset
    :type sc_cmd: struct scsi_cmnd \*

.. _`fc_slave_alloc`:

fc_slave_alloc
==============

.. c:function:: int fc_slave_alloc(struct scsi_device *sdev)

    Configure the queue depth of a Scsi_Host

    :param sdev:
        The SCSI device that identifies the SCSI host
    :type sdev: struct scsi_device \*

.. _`fc_slave_alloc.description`:

Description
-----------

Configures queue depth based on host's cmd_per_len. If not set
then we use the libfc default.

.. _`fc_fcp_destroy`:

fc_fcp_destroy
==============

.. c:function:: void fc_fcp_destroy(struct fc_lport *lport)

    Tear down the FCP layer for a given local port

    :param lport:
        The local port that no longer needs the FCP layer
    :type lport: struct fc_lport \*

.. _`fc_fcp_init`:

fc_fcp_init
===========

.. c:function:: int fc_fcp_init(struct fc_lport *lport)

    Initialize the FCP layer for a local port

    :param lport:
        The local port to initialize the exchange layer for
    :type lport: struct fc_lport \*

.. This file was automatic generated / don't edit.

