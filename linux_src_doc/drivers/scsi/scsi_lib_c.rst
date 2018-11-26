.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_lib.c

.. _`__scsi_queue_insert`:

__scsi_queue_insert
===================

.. c:function:: void __scsi_queue_insert(struct scsi_cmnd *cmd, int reason, bool unbusy)

    private queue insertion

    :param cmd:
        The SCSI command being requeued
    :type cmd: struct scsi_cmnd \*

    :param reason:
        The reason for the requeue
    :type reason: int

    :param unbusy:
        Whether the queue should be unbusied
    :type unbusy: bool

.. _`__scsi_queue_insert.description`:

Description
-----------

This is a private queue insertion.  The public interface
\ :c:func:`scsi_queue_insert`\  always assumes the queue should be unbusied
because it's always called before the completion.  This function is
for a requeue after completion, which should only occur in this
file.

.. _`__scsi_execute`:

__scsi_execute
==============

.. c:function:: int __scsi_execute(struct scsi_device *sdev, const unsigned char *cmd, int data_direction, void *buffer, unsigned bufflen, unsigned char *sense, struct scsi_sense_hdr *sshdr, int timeout, int retries, u64 flags, req_flags_t rq_flags, int *resid)

    insert request and wait for the result

    :param sdev:
        scsi device
    :type sdev: struct scsi_device \*

    :param cmd:
        scsi command
    :type cmd: const unsigned char \*

    :param data_direction:
        data direction
    :type data_direction: int

    :param buffer:
        data buffer
    :type buffer: void \*

    :param bufflen:
        len of buffer
    :type bufflen: unsigned

    :param sense:
        optional sense buffer
    :type sense: unsigned char \*

    :param sshdr:
        optional decoded sense header
    :type sshdr: struct scsi_sense_hdr \*

    :param timeout:
        request timeout in seconds
    :type timeout: int

    :param retries:
        number of times to retry request
    :type retries: int

    :param flags:
        flags for ->cmd_flags
    :type flags: u64

    :param rq_flags:
        flags for ->rq_flags
    :type rq_flags: req_flags_t

    :param resid:
        optional residual length
    :type resid: int \*

.. _`__scsi_execute.description`:

Description
-----------

Returns the scsi_cmnd result field if a command was executed, or a negative
Linux error code if we didn't get that far.

.. _`scsi_result_to_blk_status`:

scsi_result_to_blk_status
=========================

.. c:function:: blk_status_t scsi_result_to_blk_status(struct scsi_cmnd *cmd, int result)

    translate a SCSI result code into blk_status_t

    :param cmd:
        SCSI command
    :type cmd: struct scsi_cmnd \*

    :param result:
        scsi error code
    :type result: int

.. _`scsi_result_to_blk_status.description`:

Description
-----------

Translate a SCSI result code into a blk_status_t value. May reset the host
byte of \ ``cmd->result``\ .

.. _`scsi_initialize_rq`:

scsi_initialize_rq
==================

.. c:function:: void scsi_initialize_rq(struct request *rq)

    initialize struct scsi_cmnd partially

    :param rq:
        Request associated with the SCSI command to be initialized.
    :type rq: struct request \*

.. _`scsi_initialize_rq.description`:

Description
-----------

This function initializes the members of struct scsi_cmnd that must be
initialized before request processing starts and that won't be
reinitialized if a SCSI command is requeued.

Called from inside \ :c:func:`blk_get_request`\  for pass-through requests and from
inside \ :c:func:`scsi_init_command`\  for filesystem requests.

.. _`scsi_dispatch_cmd`:

scsi_dispatch_cmd
=================

.. c:function:: int scsi_dispatch_cmd(struct scsi_cmnd *cmd)

    Dispatch a command to the low-level driver.

    :param cmd:
        command block we are dispatching.
    :type cmd: struct scsi_cmnd \*

.. _`scsi_dispatch_cmd.return`:

Return
------

nonzero return request was rejected and device's queue needs to be
plugged.

.. _`scsi_done`:

scsi_done
=========

.. c:function:: void scsi_done(struct scsi_cmnd *cmd)

    Invoke completion on finished SCSI command.

    :param cmd:
        The SCSI Command for which a low-level device driver (LLDD) gives
        ownership back to SCSI Core -- i.e. the LLDD has finished with it.
    :type cmd: struct scsi_cmnd \*

.. _`scsi_done.description`:

Description
-----------

This function is the mid-level's (SCSI Core) interrupt routine,
which regains ownership of the SCSI command (de facto) from a LLDD, and
calls \ :c:func:`blk_complete_request`\  for further processing.

This function is interrupt context safe.

.. _`scsi_device_from_queue`:

scsi_device_from_queue
======================

.. c:function:: struct scsi_device *scsi_device_from_queue(struct request_queue *q)

    return sdev associated with a request_queue

    :param q:
        The request queue to return the sdev from
    :type q: struct request_queue \*

.. _`scsi_device_from_queue.description`:

Description
-----------

Return the sdev associated with a request queue or NULL if the
request_queue does not reference a SCSI device.

.. _`scsi_mode_select`:

scsi_mode_select
================

.. c:function:: int scsi_mode_select(struct scsi_device *sdev, int pf, int sp, int modepage, unsigned char *buffer, int len, int timeout, int retries, struct scsi_mode_data *data, struct scsi_sense_hdr *sshdr)

    issue a mode select

    :param sdev:
        SCSI device to be queried
    :type sdev: struct scsi_device \*

    :param pf:
        Page format bit (1 == standard, 0 == vendor specific)
    :type pf: int

    :param sp:
        Save page bit (0 == don't save, 1 == save)
    :type sp: int

    :param modepage:
        mode page being requested
    :type modepage: int

    :param buffer:
        request buffer (may not be smaller than eight bytes)
    :type buffer: unsigned char \*

    :param len:
        length of request buffer.
    :type len: int

    :param timeout:
        command timeout
    :type timeout: int

    :param retries:
        number of retries before failing
    :type retries: int

    :param data:
        returns a structure abstracting the mode header data
    :type data: struct scsi_mode_data \*

    :param sshdr:
        place to put sense data (or NULL if no sense to be collected).
        must be SCSI_SENSE_BUFFERSIZE big.
    :type sshdr: struct scsi_sense_hdr \*

.. _`scsi_mode_select.description`:

Description
-----------

     Returns zero if successful; negative error number or scsi
     status on error

.. _`scsi_mode_sense`:

scsi_mode_sense
===============

.. c:function:: int scsi_mode_sense(struct scsi_device *sdev, int dbd, int modepage, unsigned char *buffer, int len, int timeout, int retries, struct scsi_mode_data *data, struct scsi_sense_hdr *sshdr)

    issue a mode sense, falling back from 10 to six bytes if necessary.

    :param sdev:
        SCSI device to be queried
    :type sdev: struct scsi_device \*

    :param dbd:
        set if mode sense will allow block descriptors to be returned
    :type dbd: int

    :param modepage:
        mode page being requested
    :type modepage: int

    :param buffer:
        request buffer (may not be smaller than eight bytes)
    :type buffer: unsigned char \*

    :param len:
        length of request buffer.
    :type len: int

    :param timeout:
        command timeout
    :type timeout: int

    :param retries:
        number of retries before failing
    :type retries: int

    :param data:
        returns a structure abstracting the mode header data
    :type data: struct scsi_mode_data \*

    :param sshdr:
        place to put sense data (or NULL if no sense to be collected).
        must be SCSI_SENSE_BUFFERSIZE big.
    :type sshdr: struct scsi_sense_hdr \*

.. _`scsi_mode_sense.description`:

Description
-----------

     Returns zero if unsuccessful, or the header offset (either 4
     or 8 depending on whether a six or ten byte command was
     issued) if successful.

.. _`scsi_test_unit_ready`:

scsi_test_unit_ready
====================

.. c:function:: int scsi_test_unit_ready(struct scsi_device *sdev, int timeout, int retries, struct scsi_sense_hdr *sshdr)

    test if unit is ready

    :param sdev:
        scsi device to change the state of.
    :type sdev: struct scsi_device \*

    :param timeout:
        command timeout
    :type timeout: int

    :param retries:
        number of retries before failing
    :type retries: int

    :param sshdr:
        outpout pointer for decoded sense information.
    :type sshdr: struct scsi_sense_hdr \*

.. _`scsi_test_unit_ready.description`:

Description
-----------

     Returns zero if unsuccessful or an error if TUR failed.  For
     removable media, UNIT_ATTENTION sets ->changed flag.

.. _`scsi_device_set_state`:

scsi_device_set_state
=====================

.. c:function:: int scsi_device_set_state(struct scsi_device *sdev, enum scsi_device_state state)

    Take the given device through the device state model.

    :param sdev:
        scsi device to change the state of.
    :type sdev: struct scsi_device \*

    :param state:
        state to change to.
    :type state: enum scsi_device_state

.. _`scsi_device_set_state.description`:

Description
-----------

     Returns zero if successful or an error if the requested
     transition is illegal.

.. _`scsi_evt_emit`:

scsi_evt_emit
=============

.. c:function:: void scsi_evt_emit(struct scsi_device *sdev, struct scsi_event *evt)

    emit a single SCSI device uevent

    :param sdev:
        associated SCSI device
    :type sdev: struct scsi_device \*

    :param evt:
        event to emit
    :type evt: struct scsi_event \*

.. _`scsi_evt_emit.description`:

Description
-----------

     Send a single uevent (scsi_event) to the associated scsi_device.

.. _`scsi_evt_thread`:

scsi_evt_thread
===============

.. c:function:: void scsi_evt_thread(struct work_struct *work)

    send a uevent for each scsi event

    :param work:
        work struct for scsi_device
    :type work: struct work_struct \*

.. _`scsi_evt_thread.description`:

Description
-----------

     Dispatch queued events to their associated scsi_device kobjects
     as uevents.

.. _`sdev_evt_send`:

sdev_evt_send
=============

.. c:function:: void sdev_evt_send(struct scsi_device *sdev, struct scsi_event *evt)

    send asserted event to uevent thread

    :param sdev:
        scsi_device event occurred on
    :type sdev: struct scsi_device \*

    :param evt:
        event to send
    :type evt: struct scsi_event \*

.. _`sdev_evt_send.description`:

Description
-----------

     Assert scsi device event asynchronously.

.. _`sdev_evt_alloc`:

sdev_evt_alloc
==============

.. c:function:: struct scsi_event *sdev_evt_alloc(enum scsi_device_event evt_type, gfp_t gfpflags)

    allocate a new scsi event

    :param evt_type:
        type of event to allocate
    :type evt_type: enum scsi_device_event

    :param gfpflags:
        GFP flags for allocation
    :type gfpflags: gfp_t

.. _`sdev_evt_alloc.description`:

Description
-----------

     Allocates and returns a new scsi_event.

.. _`sdev_evt_send_simple`:

sdev_evt_send_simple
====================

.. c:function:: void sdev_evt_send_simple(struct scsi_device *sdev, enum scsi_device_event evt_type, gfp_t gfpflags)

    send asserted event to uevent thread

    :param sdev:
        scsi_device event occurred on
    :type sdev: struct scsi_device \*

    :param evt_type:
        type of event to send
    :type evt_type: enum scsi_device_event

    :param gfpflags:
        GFP flags for allocation
    :type gfpflags: gfp_t

.. _`sdev_evt_send_simple.description`:

Description
-----------

     Assert scsi device event asynchronously, given an event type.

.. _`scsi_request_fn_active`:

scsi_request_fn_active
======================

.. c:function:: int scsi_request_fn_active(struct scsi_device *sdev)

    number of kernel threads inside \ :c:func:`scsi_request_fn`\ 

    :param sdev:
        SCSI device to count the number of \ :c:func:`scsi_request_fn`\  callers for.
    :type sdev: struct scsi_device \*

.. _`scsi_wait_for_queuecommand`:

scsi_wait_for_queuecommand
==========================

.. c:function:: void scsi_wait_for_queuecommand(struct scsi_device *sdev)

    wait for ongoing \ :c:func:`queuecommand`\  calls

    :param sdev:
        SCSI device pointer.
    :type sdev: struct scsi_device \*

.. _`scsi_wait_for_queuecommand.description`:

Description
-----------

Wait until the ongoing shost->hostt->queuecommand() calls that are
invoked from \ :c:func:`scsi_request_fn`\  have finished.

.. _`scsi_device_quiesce`:

scsi_device_quiesce
===================

.. c:function:: int scsi_device_quiesce(struct scsi_device *sdev)

    Block user issued commands.

    :param sdev:
        scsi device to quiesce.
    :type sdev: struct scsi_device \*

.. _`scsi_device_quiesce.description`:

Description
-----------

     This works by trying to transition to the SDEV_QUIESCE state
     (which must be a legal transition).  When the device is in this
     state, only special requests will be accepted, all others will
     be deferred.  Since special requests may also be requeued requests,
     a successful return doesn't guarantee the device will be
     totally quiescent.

     Must be called with user context, may sleep.

     Returns zero if unsuccessful or an error if not.

.. _`scsi_device_resume`:

scsi_device_resume
==================

.. c:function:: void scsi_device_resume(struct scsi_device *sdev)

    Restart user issued commands to a quiesced device.

    :param sdev:
        scsi device to resume.
    :type sdev: struct scsi_device \*

.. _`scsi_device_resume.description`:

Description
-----------

     Moves the device from quiesced back to running and restarts the
     queues.

     Must be called with user context, may sleep.

.. _`scsi_internal_device_block_nowait`:

scsi_internal_device_block_nowait
=================================

.. c:function:: int scsi_internal_device_block_nowait(struct scsi_device *sdev)

    try to transition to the SDEV_BLOCK state

    :param sdev:
        device to block
    :type sdev: struct scsi_device \*

.. _`scsi_internal_device_block_nowait.description`:

Description
-----------

Pause SCSI command processing on the specified device. Does not sleep.

Returns zero if successful or a negative error code upon failure.

.. _`scsi_internal_device_block_nowait.notes`:

Notes
-----

This routine transitions the device to the SDEV_BLOCK state (which must be
a legal transition). When the device is in this state, command processing
is paused until the device leaves the SDEV_BLOCK state. See also
\ :c:func:`scsi_internal_device_unblock_nowait`\ .

.. _`scsi_internal_device_block`:

scsi_internal_device_block
==========================

.. c:function:: int scsi_internal_device_block(struct scsi_device *sdev)

    try to transition to the SDEV_BLOCK state

    :param sdev:
        device to block
    :type sdev: struct scsi_device \*

.. _`scsi_internal_device_block.description`:

Description
-----------

Pause SCSI command processing on the specified device and wait until all
ongoing \ :c:func:`scsi_request_fn`\  / \ :c:func:`scsi_queue_rq`\  calls have finished. May sleep.

Returns zero if successful or a negative error code upon failure.

.. _`scsi_internal_device_block.note`:

Note
----

This routine transitions the device to the SDEV_BLOCK state (which must be
a legal transition). When the device is in this state, command processing
is paused until the device leaves the SDEV_BLOCK state. See also
\ :c:func:`scsi_internal_device_unblock`\ .

To do: avoid that \ :c:func:`scsi_send_eh_cmnd`\  calls \ :c:func:`queuecommand`\  after
\ :c:func:`scsi_internal_device_block`\  has blocked a SCSI device and also
remove the rport mutex lock and unlock calls from \ :c:func:`srp_queuecommand`\ .

.. _`scsi_internal_device_unblock_nowait`:

scsi_internal_device_unblock_nowait
===================================

.. c:function:: int scsi_internal_device_unblock_nowait(struct scsi_device *sdev, enum scsi_device_state new_state)

    resume a device after a block request

    :param sdev:
        device to resume
    :type sdev: struct scsi_device \*

    :param new_state:
        state to set the device to after unblocking
    :type new_state: enum scsi_device_state

.. _`scsi_internal_device_unblock_nowait.description`:

Description
-----------

Restart the device queue for a previously suspended SCSI device. Does not
sleep.

Returns zero if successful or a negative error code upon failure.

.. _`scsi_internal_device_unblock_nowait.notes`:

Notes
-----

This routine transitions the device to the SDEV_RUNNING state or to one of
the offline states (which must be a legal transition) allowing the midlayer
to goose the queue for this device.

.. _`scsi_internal_device_unblock`:

scsi_internal_device_unblock
============================

.. c:function:: int scsi_internal_device_unblock(struct scsi_device *sdev, enum scsi_device_state new_state)

    resume a device after a block request

    :param sdev:
        device to resume
    :type sdev: struct scsi_device \*

    :param new_state:
        state to set the device to after unblocking
    :type new_state: enum scsi_device_state

.. _`scsi_internal_device_unblock.description`:

Description
-----------

Restart the device queue for a previously suspended SCSI device. May sleep.

Returns zero if successful or a negative error code upon failure.

.. _`scsi_internal_device_unblock.notes`:

Notes
-----

This routine transitions the device to the SDEV_RUNNING state or to one of
the offline states (which must be a legal transition) allowing the midlayer
to goose the queue for this device.

.. _`scsi_kmap_atomic_sg`:

scsi_kmap_atomic_sg
===================

.. c:function:: void *scsi_kmap_atomic_sg(struct scatterlist *sgl, int sg_count, size_t *offset, size_t *len)

    find and atomically map an sg-elemnt

    :param sgl:
        scatter-gather list
    :type sgl: struct scatterlist \*

    :param sg_count:
        number of segments in sg
    :type sg_count: int

    :param offset:
        offset in bytes into sg, on return offset into the mapped area
    :type offset: size_t \*

    :param len:
        bytes to map, on return number of bytes mapped
    :type len: size_t \*

.. _`scsi_kmap_atomic_sg.description`:

Description
-----------

Returns virtual address of the start of the mapped page

.. _`scsi_kunmap_atomic_sg`:

scsi_kunmap_atomic_sg
=====================

.. c:function:: void scsi_kunmap_atomic_sg(void *virt)

    atomically unmap a virtual address, previously mapped with scsi_kmap_atomic_sg

    :param virt:
        virtual address to be unmapped
    :type virt: void \*

.. _`scsi_vpd_lun_id`:

scsi_vpd_lun_id
===============

.. c:function:: int scsi_vpd_lun_id(struct scsi_device *sdev, char *id, size_t id_len)

    return a unique device identification

    :param sdev:
        SCSI device
    :type sdev: struct scsi_device \*

    :param id:
        buffer for the identification
    :type id: char \*

    :param id_len:
        length of the buffer
    :type id_len: size_t

.. _`scsi_vpd_lun_id.description`:

Description
-----------

Copies a unique device identification into \ ``id``\  based
on the information in the VPD page 0x83 of the device.
The string will be formatted as a SCSI name string.

Returns the length of the identification or error on failure.
If the identifier is longer than the supplied buffer the actual
identifier length is returned and the buffer is not zero-padded.

.. This file was automatic generated / don't edit.

