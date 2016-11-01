.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_transport_fc.c

.. _`fc_get_event_number`:

fc_get_event_number
===================

.. c:function:: u32 fc_get_event_number( void)

    Obtain the next sequential FC event number

    :param  void:
        no arguments

.. _`fc_get_event_number.notes`:

Notes
-----

We could have inlined this, but it would have required fc_event_seq to
be exposed. For now, live with the subroutine call.
Atomic used to avoid lock/unlock...

.. _`fc_host_post_event`:

fc_host_post_event
==================

.. c:function:: void fc_host_post_event(struct Scsi_Host *shost, u32 event_number, enum fc_host_event_code event_code, u32 event_data)

    called to post an even on an fc_host.

    :param struct Scsi_Host \*shost:
        host the event occurred on

    :param u32 event_number:
        fc event number obtained from \ :c:func:`get_fc_event_number`\ 

    :param enum fc_host_event_code event_code:
        fc_host event being posted

    :param u32 event_data:
        32bits of data for the event being posted

.. _`fc_host_post_event.notes`:

Notes
-----

This routine assumes no locks are held on entry.

.. _`fc_host_post_vendor_event`:

fc_host_post_vendor_event
=========================

.. c:function:: void fc_host_post_vendor_event(struct Scsi_Host *shost, u32 event_number, u32 data_len, char *data_buf, u64 vendor_id)

    called to post a vendor unique event on an fc_host

    :param struct Scsi_Host \*shost:
        host the event occurred on

    :param u32 event_number:
        fc event number obtained from \ :c:func:`get_fc_event_number`\ 

    :param u32 data_len:
        amount, in bytes, of vendor unique data

    :param char \*data_buf:
        pointer to vendor unique data

    :param u64 vendor_id:
        Vendor id

.. _`fc_host_post_vendor_event.notes`:

Notes
-----

This routine assumes no locks are held on entry.

.. _`fc_timed_out`:

fc_timed_out
============

.. c:function:: enum blk_eh_timer_return fc_timed_out(struct scsi_cmnd *scmd)

    FC Transport I/O timeout intercept handler

    :param struct scsi_cmnd \*scmd:
        The SCSI command which timed out

.. _`fc_timed_out.description`:

Description
-----------

This routine protects against error handlers getting invoked while a
rport is in a blocked state, typically due to a temporarily loss of
connectivity. If the error handlers are allowed to proceed, requests
to abort i/o, reset the target, etc will likely fail as there is no way
to communicate with the device to perform the requested function. These
failures may result in the midlayer taking the device offline, requiring
manual intervention to restore operation.

This routine, called whenever an i/o times out, validates the state of
the underlying rport. If the rport is blocked, it returns
EH_RESET_TIMER, which will continue to reschedule the timeout.
Eventually, either the device will return, or devloss_tmo will fire,
and when the timeout then fires, it will be handled normally.
If the rport is not blocked, normal error handling continues.

.. _`fc_timed_out.notes`:

Notes
-----

This routine assumes no locks are held on entry.

.. _`fc_queue_work`:

fc_queue_work
=============

.. c:function:: int fc_queue_work(struct Scsi_Host *shost, struct work_struct *work)

    Queue work to the fc_host workqueue.

    :param struct Scsi_Host \*shost:
        Pointer to Scsi_Host bound to fc_host.

    :param struct work_struct \*work:
        Work to queue for execution.

.. _`fc_queue_work.return-value`:

Return value
------------

1 - work queued for execution
0 - work is already queued
-EINVAL - work queue doesn't exist

.. _`fc_flush_work`:

fc_flush_work
=============

.. c:function:: void fc_flush_work(struct Scsi_Host *shost)

    Flush a fc_host's workqueue.

    :param struct Scsi_Host \*shost:
        Pointer to Scsi_Host bound to fc_host.

.. _`fc_queue_devloss_work`:

fc_queue_devloss_work
=====================

.. c:function:: int fc_queue_devloss_work(struct Scsi_Host *shost, struct delayed_work *work, unsigned long delay)

    Schedule work for the fc_host devloss workqueue.

    :param struct Scsi_Host \*shost:
        Pointer to Scsi_Host bound to fc_host.

    :param struct delayed_work \*work:
        Work to queue for execution.

    :param unsigned long delay:
        jiffies to delay the work queuing

.. _`fc_queue_devloss_work.return-value`:

Return value
------------

1 on success / 0 already queued / < 0 for error

.. _`fc_flush_devloss`:

fc_flush_devloss
================

.. c:function:: void fc_flush_devloss(struct Scsi_Host *shost)

    Flush a fc_host's devloss workqueue.

    :param struct Scsi_Host \*shost:
        Pointer to Scsi_Host bound to fc_host.

.. _`fc_remove_host`:

fc_remove_host
==============

.. c:function:: void fc_remove_host(struct Scsi_Host *shost)

    called to terminate any fc_transport-related elements for a scsi host.

    :param struct Scsi_Host \*shost:
        Which \ :c:type:`struct Scsi_Host <Scsi_Host>`\ 

.. _`fc_remove_host.description`:

Description
-----------

This routine is expected to be called immediately preceding the
a driver's call to \ :c:func:`scsi_remove_host`\ .

.. _`fc_remove_host.warning`:

WARNING
-------

A driver utilizing the fc_transport, which fails to call
this routine prior to \ :c:func:`scsi_remove_host`\ , will leave dangling
objects in /sys/class/fc_remote_ports. Access to any of these
objects can result in a system crash !!!

.. _`fc_remove_host.notes`:

Notes
-----

This routine assumes no locks are held on entry.

.. _`fc_starget_delete`:

fc_starget_delete
=================

.. c:function:: void fc_starget_delete(struct work_struct *work)

    called to delete the scsi descendants of an rport

    :param struct work_struct \*work:
        remote port to be operated on.

.. _`fc_starget_delete.description`:

Description
-----------

Deletes target and all sdevs.

.. _`fc_rport_final_delete`:

fc_rport_final_delete
=====================

.. c:function:: void fc_rport_final_delete(struct work_struct *work)

    finish rport termination and delete it.

    :param struct work_struct \*work:
        remote port to be deleted.

.. _`fc_rport_create`:

fc_rport_create
===============

.. c:function:: struct fc_rport *fc_rport_create(struct Scsi_Host *shost, int channel, struct fc_rport_identifiers *ids)

    allocates and creates a remote FC port.

    :param struct Scsi_Host \*shost:
        scsi host the remote port is connected to.

    :param int channel:
        Channel on shost port connected to.

    :param struct fc_rport_identifiers \*ids:
        The world wide names, fc address, and FC4 port
        roles for the remote port.

.. _`fc_rport_create.description`:

Description
-----------

Allocates and creates the remoter port structure, including the
class and sysfs creation.

.. _`fc_rport_create.notes`:

Notes
-----

This routine assumes no locks are held on entry.

.. _`fc_remote_port_add`:

fc_remote_port_add
==================

.. c:function:: struct fc_rport *fc_remote_port_add(struct Scsi_Host *shost, int channel, struct fc_rport_identifiers *ids)

    notify fc transport of the existence of a remote FC port.

    :param struct Scsi_Host \*shost:
        scsi host the remote port is connected to.

    :param int channel:
        Channel on shost port connected to.

    :param struct fc_rport_identifiers \*ids:
        The world wide names, fc address, and FC4 port
        roles for the remote port.

.. _`fc_remote_port_add.description`:

Description
-----------

The LLDD calls this routine to notify the transport of the existence
of a remote port. The LLDD provides the unique identifiers (wwpn,wwn)
of the port, it's FC address (port_id), and the FC4 roles that are
active for the port.

For ports that are FCP targets (aka scsi targets), the FC transport
maintains consistent target id bindings on behalf of the LLDD.
A consistent target id binding is an assignment of a target id to
a remote port identifier, which persists while the scsi host is
attached. The remote port can disappear, then later reappear, and
it's target id assignment remains the same. This allows for shifts
in FC addressing (if binding by wwpn or wwnn) with no apparent
changes to the scsi subsystem which is based on scsi host number and
target id values.  Bindings are only valid during the attachment of
the scsi host. If the host detaches, then later re-attaches, target
id bindings may change.

This routine is responsible for returning a remote port structure.
The routine will search the list of remote ports it maintains
internally on behalf of consistent target id mappings. If found, the
remote port structure will be reused. Otherwise, a new remote port
structure will be allocated.

Whenever a remote port is allocated, a new fc_remote_port class
device is created.

Should not be called from interrupt context.

.. _`fc_remote_port_add.notes`:

Notes
-----

This routine assumes no locks are held on entry.

.. _`fc_remote_port_delete`:

fc_remote_port_delete
=====================

.. c:function:: void fc_remote_port_delete(struct fc_rport *rport)

    notifies the fc transport that a remote port is no longer in existence.

    :param struct fc_rport \*rport:
        The remote port that no longer exists

.. _`fc_remote_port_delete.description`:

Description
-----------

The LLDD calls this routine to notify the transport that a remote
port is no longer part of the topology. Note: Although a port
may no longer be part of the topology, it may persist in the remote
ports displayed by the fc_host. We do this under 2 conditions:
1) If the port was a scsi target, we delay its deletion by "blocking" it.
This allows the port to temporarily disappear, then reappear without
disrupting the SCSI device tree attached to it. During the "blocked"
period the port will still exist.
2) If the port was a scsi target and disappears for longer than we
expect, we'll delete the port and the tear down the SCSI device tree
attached to it. However, we want to semi-persist the target id assigned
to that port if it eventually does exist. The port structure will
remain (although with minimal information) so that the target id
bindings remails.

If the remote port is not an FCP Target, it will be fully torn down
and deallocated, including the fc_remote_port class device.

If the remote port is an FCP Target, the port will be placed in a
temporary blocked state. From the LLDD's perspective, the rport no
longer exists. From the SCSI midlayer's perspective, the SCSI target
exists, but all sdevs on it are blocked from further I/O. The following
is then expected.

If the remote port does not return (signaled by a LLDD call to
\ :c:func:`fc_remote_port_add`\ ) within the dev_loss_tmo timeout, then the
scsi target is removed - killing all outstanding i/o and removing the
scsi devices attached ot it. The port structure will be marked Not
Present and be partially cleared, leaving only enough information to
recognize the remote port relative to the scsi target id binding if
it later appears.  The port will remain as long as there is a valid
binding (e.g. until the user changes the binding type or unloads the
scsi host with the binding).

If the remote port returns within the dev_loss_tmo value (and matches
according to the target id binding type), the port structure will be
reused. If it is no longer a SCSI target, the target will be torn
down. If it continues to be a SCSI target, then the target will be
unblocked (allowing i/o to be resumed), and a scan will be activated
to ensure that all luns are detected.

Called from normal process context only - cannot be called from interrupt.

.. _`fc_remote_port_delete.notes`:

Notes
-----

This routine assumes no locks are held on entry.

.. _`fc_remote_port_rolechg`:

fc_remote_port_rolechg
======================

.. c:function:: void fc_remote_port_rolechg(struct fc_rport *rport, u32 roles)

    notifies the fc transport that the roles on a remote may have changed.

    :param struct fc_rport \*rport:
        The remote port that changed.

    :param u32 roles:
        New roles for this port.

.. _`fc_remote_port_rolechg.description`:

Description
-----------

The LLDD calls this routine to notify the transport that the
roles on a remote port may have changed. The largest effect of this is
if a port now becomes a FCP Target, it must be allocated a
scsi target id.  If the port is no longer a FCP target, any
scsi target id value assigned to it will persist in case the
role changes back to include FCP Target. No changes in the scsi
midlayer will be invoked if the role changes (in the expectation
that the role will be resumed. If it doesn't normal error processing
will take place).

Should not be called from interrupt context.

.. _`fc_remote_port_rolechg.notes`:

Notes
-----

This routine assumes no locks are held on entry.

.. _`fc_timeout_deleted_rport`:

fc_timeout_deleted_rport
========================

.. c:function:: void fc_timeout_deleted_rport(struct work_struct *work)

    Timeout handler for a deleted remote port.

    :param struct work_struct \*work:
        rport target that failed to reappear in the allotted time.

.. _`fc_timeout_deleted_rport.description`:

Description
-----------

An attempt to delete a remote port blocks, and if it fails
to return in the allotted time this gets called.

.. _`fc_timeout_fail_rport_io`:

fc_timeout_fail_rport_io
========================

.. c:function:: void fc_timeout_fail_rport_io(struct work_struct *work)

    Timeout handler for a fast io failing on a disconnected SCSI target.

    :param struct work_struct \*work:
        rport to terminate io on.

.. _`fc_timeout_fail_rport_io.notes`:

Notes
-----

Only requests the failure of the io, not that all are flushed
prior to returning.

.. _`fc_scsi_scan_rport`:

fc_scsi_scan_rport
==================

.. c:function:: void fc_scsi_scan_rport(struct work_struct *work)

    called to perform a scsi scan on a remote port.

    :param struct work_struct \*work:
        remote port to be scanned.

.. _`fc_block_scsi_eh`:

fc_block_scsi_eh
================

.. c:function:: int fc_block_scsi_eh(struct scsi_cmnd *cmnd)

    Block SCSI eh thread for blocked fc_rport

    :param struct scsi_cmnd \*cmnd:
        SCSI command that scsi_eh is trying to recover

.. _`fc_block_scsi_eh.description`:

Description
-----------

This routine can be called from a FC LLD scsi_eh callback. It
blocks the scsi_eh thread until the fc_rport leaves the
FC_PORTSTATE_BLOCKED, or the fast_io_fail_tmo fires. This is
necessary to avoid the scsi_eh failing recovery actions for blocked
rports which would lead to offlined SCSI devices.

.. _`fc_block_scsi_eh.return`:

Return
------

0 if the fc_rport left the state FC_PORTSTATE_BLOCKED.
FAST_IO_FAIL if the fast_io_fail_tmo fired, this should be
passed back to scsi_eh.

.. _`fc_vport_setup`:

fc_vport_setup
==============

.. c:function:: int fc_vport_setup(struct Scsi_Host *shost, int channel, struct device *pdev, struct fc_vport_identifiers *ids, struct fc_vport **ret_vport)

    allocates and creates a FC virtual port.

    :param struct Scsi_Host \*shost:
        scsi host the virtual port is connected to.

    :param int channel:
        Channel on shost port connected to.

    :param struct device \*pdev:
        parent device for vport

    :param struct fc_vport_identifiers \*ids:
        The world wide names, FC4 port roles, etc for
        the virtual port.

    :param struct fc_vport \*\*ret_vport:
        The pointer to the created vport.

.. _`fc_vport_setup.description`:

Description
-----------

Allocates and creates the vport structure, calls the parent host
to instantiate the vport, the completes w/ class and sysfs creation.

.. _`fc_vport_setup.notes`:

Notes
-----

This routine assumes no locks are held on entry.

.. _`fc_vport_create`:

fc_vport_create
===============

.. c:function:: struct fc_vport *fc_vport_create(struct Scsi_Host *shost, int channel, struct fc_vport_identifiers *ids)

    Admin App or LLDD requests creation of a vport

    :param struct Scsi_Host \*shost:
        scsi host the virtual port is connected to.

    :param int channel:
        channel on shost port connected to.

    :param struct fc_vport_identifiers \*ids:
        The world wide names, FC4 port roles, etc for
        the virtual port.

.. _`fc_vport_create.notes`:

Notes
-----

This routine assumes no locks are held on entry.

.. _`fc_vport_terminate`:

fc_vport_terminate
==================

.. c:function:: int fc_vport_terminate(struct fc_vport *vport)

    Admin App or LLDD requests termination of a vport

    :param struct fc_vport \*vport:
        fc_vport to be terminated

.. _`fc_vport_terminate.description`:

Description
-----------

Calls the LLDD \ :c:func:`vport_delete`\  function, then deallocates and removes
the vport from the shost and object tree.

.. _`fc_vport_terminate.notes`:

Notes
-----

This routine assumes no locks are held on entry.

.. _`fc_vport_sched_delete`:

fc_vport_sched_delete
=====================

.. c:function:: void fc_vport_sched_delete(struct work_struct *work)

    workq-based delete request for a vport

    :param struct work_struct \*work:
        vport to be deleted.

.. _`fc_destroy_bsgjob`:

fc_destroy_bsgjob
=================

.. c:function:: void fc_destroy_bsgjob(struct fc_bsg_job *job)

    routine to teardown/delete a fc bsg job

    :param struct fc_bsg_job \*job:
        fc_bsg_job that is to be torn down

.. _`fc_bsg_jobdone`:

fc_bsg_jobdone
==============

.. c:function:: void fc_bsg_jobdone(struct fc_bsg_job *job)

    completion routine for bsg requests that the LLD has completed

    :param struct fc_bsg_job \*job:
        fc_bsg_job that is complete

.. _`fc_bsg_softirq_done`:

fc_bsg_softirq_done
===================

.. c:function:: void fc_bsg_softirq_done(struct request *rq)

    softirq done routine for destroying the bsg requests

    :param struct request \*rq:
        BSG request that holds the job to be destroyed

.. _`fc_bsg_job_timeout`:

fc_bsg_job_timeout
==================

.. c:function:: enum blk_eh_timer_return fc_bsg_job_timeout(struct request *req)

    handler for when a bsg request timesout

    :param struct request \*req:
        request that timed out

.. _`fc_req_to_bsgjob`:

fc_req_to_bsgjob
================

.. c:function:: int fc_req_to_bsgjob(struct Scsi_Host *shost, struct fc_rport *rport, struct request *req)

    Allocate/create the fc_bsg_job structure for the bsg request

    :param struct Scsi_Host \*shost:
        SCSI Host corresponding to the bsg object

    :param struct fc_rport \*rport:
        (optional) FC Remote Port corresponding to the bsg object

    :param struct request \*req:
        BSG request that needs a job structure

.. _`fc_bsg_host_dispatch`:

fc_bsg_host_dispatch
====================

.. c:function:: enum fc_dispatch_result fc_bsg_host_dispatch(struct request_queue *q, struct Scsi_Host *shost, struct fc_bsg_job *job)

    process fc host bsg requests and dispatch to LLDD

    :param struct request_queue \*q:
        fc host request queue

    :param struct Scsi_Host \*shost:
        scsi host rport attached to

    :param struct fc_bsg_job \*job:
        bsg job to be processed

.. _`fc_bsg_rport_dispatch`:

fc_bsg_rport_dispatch
=====================

.. c:function:: enum fc_dispatch_result fc_bsg_rport_dispatch(struct request_queue *q, struct Scsi_Host *shost, struct fc_rport *rport, struct fc_bsg_job *job)

    process rport bsg requests and dispatch to LLDD

    :param struct request_queue \*q:
        rport request queue

    :param struct Scsi_Host \*shost:
        scsi host rport attached to

    :param struct fc_rport \*rport:
        rport request destined to

    :param struct fc_bsg_job \*job:
        bsg job to be processed

.. _`fc_bsg_request_handler`:

fc_bsg_request_handler
======================

.. c:function:: void fc_bsg_request_handler(struct request_queue *q, struct Scsi_Host *shost, struct fc_rport *rport, struct device *dev)

    generic handler for bsg requests

    :param struct request_queue \*q:
        request queue to manage

    :param struct Scsi_Host \*shost:
        Scsi_Host related to the bsg object

    :param struct fc_rport \*rport:
        FC remote port related to the bsg object (optional)

    :param struct device \*dev:
        device structure for bsg object

.. _`fc_bsg_host_handler`:

fc_bsg_host_handler
===================

.. c:function:: void fc_bsg_host_handler(struct request_queue *q)

    handler for bsg requests for a fc host

    :param struct request_queue \*q:
        fc host request queue

.. _`fc_bsg_rport_handler`:

fc_bsg_rport_handler
====================

.. c:function:: void fc_bsg_rport_handler(struct request_queue *q)

    handler for bsg requests for a fc rport

    :param struct request_queue \*q:
        rport request queue

.. _`fc_bsg_hostadd`:

fc_bsg_hostadd
==============

.. c:function:: int fc_bsg_hostadd(struct Scsi_Host *shost, struct fc_host_attrs *fc_host)

    Create and add the bsg hooks so we can receive requests

    :param struct Scsi_Host \*shost:
        shost for fc_host

    :param struct fc_host_attrs \*fc_host:
        fc_host adding the structures to

.. _`fc_bsg_rportadd`:

fc_bsg_rportadd
===============

.. c:function:: int fc_bsg_rportadd(struct Scsi_Host *shost, struct fc_rport *rport)

    Create and add the bsg hooks so we can receive requests

    :param struct Scsi_Host \*shost:
        shost that rport is attached to

    :param struct fc_rport \*rport:
        rport that the bsg hooks are being attached to

.. _`fc_bsg_remove`:

fc_bsg_remove
=============

.. c:function:: void fc_bsg_remove(struct request_queue *q)

    Deletes the bsg hooks on fchosts/rports

    :param struct request_queue \*q:
        the request_queue that is to be torn down.

.. _`fc_bsg_remove.notes`:

Notes
-----

Before unregistering the queue empty any requests that are blocked

.. This file was automatic generated / don't edit.

