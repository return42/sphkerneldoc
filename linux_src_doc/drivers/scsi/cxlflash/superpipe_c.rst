.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/cxlflash/superpipe.c

.. _`marshal_rele_to_resize`:

marshal_rele_to_resize
======================

.. c:function:: void marshal_rele_to_resize(struct dk_cxlflash_release *release, struct dk_cxlflash_resize *resize)

    translate release to resize structure

    :param struct dk_cxlflash_release \*release:
        *undescribed*

    :param struct dk_cxlflash_resize \*resize:
        Destination structure for the translate/copy.

.. _`marshal_det_to_rele`:

marshal_det_to_rele
===================

.. c:function:: void marshal_det_to_rele(struct dk_cxlflash_detach *detach, struct dk_cxlflash_release *release)

    translate detach to release structure

    :param struct dk_cxlflash_detach \*detach:
        Destination structure for the translate/copy.

    :param struct dk_cxlflash_release \*release:
        *undescribed*

.. _`marshal_udir_to_rele`:

marshal_udir_to_rele
====================

.. c:function:: void marshal_udir_to_rele(struct dk_cxlflash_udirect *udirect, struct dk_cxlflash_release *release)

    translate udirect to release structure

    :param struct dk_cxlflash_udirect \*udirect:
        Source structure from which to translate/copy.

    :param struct dk_cxlflash_release \*release:
        Destination structure for the translate/copy.

.. _`cxlflash_free_errpage`:

cxlflash_free_errpage
=====================

.. c:function:: void cxlflash_free_errpage( void)

    frees resources associated with global error page

    :param  void:
        no arguments

.. _`cxlflash_stop_term_user_contexts`:

cxlflash_stop_term_user_contexts
================================

.. c:function:: void cxlflash_stop_term_user_contexts(struct cxlflash_cfg *cfg)

    stops/terminates known user contexts

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`cxlflash_stop_term_user_contexts.description`:

Description
-----------

When the host needs to go down, all users must be quiesced and their
memory freed. This is accomplished by putting the contexts in error
state which will notify the user and let them 'drive' the tear down.
Meanwhile, this routine camps until all user contexts have been removed.

Note that the main loop in this routine will always execute at least once
to flush the reset_waitq.

.. _`find_error_context`:

find_error_context
==================

.. c:function:: struct ctx_info *find_error_context(struct cxlflash_cfg *cfg, u64 rctxid, struct file *file)

    locates a context by cookie on the error recovery list

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param u64 rctxid:
        Desired context by id.

    :param struct file \*file:
        Desired context by file.

.. _`find_error_context.return`:

Return
------

Found context on success, NULL on failure

.. _`get_context`:

get_context
===========

.. c:function:: struct ctx_info *get_context(struct cxlflash_cfg *cfg, u64 rctxid, void *arg, enum ctx_ctrl ctx_ctrl)

    obtains a validated and locked context reference

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param u64 rctxid:
        Desired context (raw, un-decoded format).

    :param void \*arg:
        LUN information or file associated with request.

    :param enum ctx_ctrl ctx_ctrl:
        Control information to 'steer' desired lookup.

.. _`get_context.note`:

NOTE
----

despite the name pid, in linux, current->pid actually refers
to the lightweight process id (tid) and can change if the process is
multi threaded. The tgid remains constant for the process and only changes
when the process of fork. For all intents and purposes, think of tgid
as a pid in the traditional sense.

.. _`get_context.return`:

Return
------

Validated context on success, NULL on failure

.. _`put_context`:

put_context
===========

.. c:function:: void put_context(struct ctx_info *ctxi)

    release a context that was retrieved from \ :c:func:`get_context`\ 

    :param struct ctx_info \*ctxi:
        Context to release.

.. _`put_context.description`:

Description
-----------

For now, releasing the context equates to unlocking it's mutex.

.. _`afu_attach`:

afu_attach
==========

.. c:function:: int afu_attach(struct cxlflash_cfg *cfg, struct ctx_info *ctxi)

    attach a context to the AFU

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param struct ctx_info \*ctxi:
        Context to attach.

.. _`afu_attach.description`:

Description
-----------

Upon setting the context capabilities, they must be confirmed with
a read back operation as the context might have been closed since
the mailbox was unlocked. When this occurs, registration is failed.

.. _`afu_attach.return`:

Return
------

0 on success, -errno on failure

.. _`read_cap16`:

read_cap16
==========

.. c:function:: int read_cap16(struct scsi_device *sdev, struct llun_info *lli)

    issues a SCSI READ_CAP16 command

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param struct llun_info \*lli:
        LUN destined for capacity request.

.. _`read_cap16.description`:

Description
-----------

The READ_CAP16 can take quite a while to complete. Should an EEH occur while
in \ :c:func:`scsi_execute`\ , the EEH handler will attempt to recover. As part of the
recovery, the handler drains all currently running ioctls, waiting until they
have completed before proceeding with a reset. As this routine is used on the
ioctl path, this can create a condition where the EEH handler becomes stuck,
infinitely waiting for this ioctl thread. To avoid this behavior, temporarily
unmark this thread as an ioctl thread by releasing the ioctl read semaphore.
This will allow the EEH handler to proceed with a recovery while this thread
is still running. Once the \ :c:func:`scsi_execute`\  returns, reacquire the ioctl read
semaphore and check the adapter state in case it changed while inside of
\ :c:func:`scsi_execute`\ . The state check will wait if the adapter is still being
recovered or return a failure if the recovery failed. In the event that the
adapter reset failed, simply return the failure as the ioctl would be unable
to continue.

Note that the above puts a requirement on this routine to only be called on
an ioctl thread.

.. _`read_cap16.return`:

Return
------

0 on success, -errno on failure

.. _`get_rhte`:

get_rhte
========

.. c:function:: struct sisl_rht_entry *get_rhte(struct ctx_info *ctxi, res_hndl_t rhndl, struct llun_info *lli)

    obtains validated resource handle table entry reference

    :param struct ctx_info \*ctxi:
        Context owning the resource handle.

    :param res_hndl_t rhndl:
        Resource handle associated with entry.

    :param struct llun_info \*lli:
        LUN associated with request.

.. _`get_rhte.return`:

Return
------

Validated RHTE on success, NULL on failure

.. _`rhte_checkout`:

rhte_checkout
=============

.. c:function:: struct sisl_rht_entry *rhte_checkout(struct ctx_info *ctxi, struct llun_info *lli)

    obtains free/empty resource handle table entry

    :param struct ctx_info \*ctxi:
        Context owning the resource handle.

    :param struct llun_info \*lli:
        LUN associated with request.

.. _`rhte_checkout.return`:

Return
------

Free RHTE on success, NULL on failure

.. _`rhte_checkin`:

rhte_checkin
============

.. c:function:: void rhte_checkin(struct ctx_info *ctxi, struct sisl_rht_entry *rhte)

    releases a resource handle table entry

    :param struct ctx_info \*ctxi:
        Context owning the resource handle.

    :param struct sisl_rht_entry \*rhte:
        RHTE to release.

.. _`rht_format1`:

rht_format1
===========

.. c:function:: void rht_format1(struct sisl_rht_entry *rhte, u64 lun_id, u32 perm, u32 port_sel)

    populates a RHTE for format 1

    :param struct sisl_rht_entry \*rhte:
        RHTE to populate.

    :param u64 lun_id:
        LUN ID of LUN associated with RHTE.

    :param u32 perm:
        Desired permissions for RHTE.

    :param u32 port_sel:
        Port selection mask

.. _`cxlflash_lun_attach`:

cxlflash_lun_attach
===================

.. c:function:: int cxlflash_lun_attach(struct glun_info *gli, enum lun_mode mode, bool locked)

    attaches a user to a LUN and manages the LUN's mode

    :param struct glun_info \*gli:
        LUN to attach.

    :param enum lun_mode mode:
        Desired mode of the LUN.

    :param bool locked:
        Mutex status on current thread.

.. _`cxlflash_lun_attach.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_lun_detach`:

cxlflash_lun_detach
===================

.. c:function:: void cxlflash_lun_detach(struct glun_info *gli)

    detaches a user from a LUN and resets the LUN's mode

    :param struct glun_info \*gli:
        LUN to detach.

.. _`cxlflash_lun_detach.description`:

Description
-----------

When resetting the mode, terminate block allocation resources as they
are no longer required (service is safe to call even when block allocation
resources were not present - such as when transitioning from physical mode).
These resources will be reallocated when needed (subsequent transition to
virtual mode).

.. _`_cxlflash_disk_release`:

_cxlflash_disk_release
======================

.. c:function:: int _cxlflash_disk_release(struct scsi_device *sdev, struct ctx_info *ctxi, struct dk_cxlflash_release *release)

    releases the specified resource entry

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param struct ctx_info \*ctxi:
        Context owning resources.

    :param struct dk_cxlflash_release \*release:
        Release ioctl data structure.

.. _`_cxlflash_disk_release.description`:

Description
-----------

For LUNs in virtual mode, the virtual LUN associated with the specified
resource handle is resized to 0 prior to releasing the RHTE. Note that the
AFU sync should \_not\_ be performed when the context is sitting on the error
recovery list. A context on the error recovery list is not known to the AFU
due to reset. When the context is recovered, it will be reattached and made
known again to the AFU.

.. _`_cxlflash_disk_release.return`:

Return
------

0 on success, -errno on failure

.. _`destroy_context`:

destroy_context
===============

.. c:function:: void destroy_context(struct cxlflash_cfg *cfg, struct ctx_info *ctxi)

    releases a context

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param struct ctx_info \*ctxi:
        Context to release.

.. _`destroy_context.description`:

Description
-----------

This routine is safe to be called with a a non-initialized context.
Also note that the routine conditionally checks for the existence
of the context control map before clearing the RHT registers and
context capabilities because it is possible to destroy a context
while the context is in the error state (previous mapping was
removed [so there is no need to worry about clearing] and context
is waiting for a new mapping).

.. _`create_context`:

create_context
==============

.. c:function:: struct ctx_info *create_context(struct cxlflash_cfg *cfg)

    allocates and initializes a context

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`create_context.return`:

Return
------

Allocated context on success, NULL on failure

.. _`init_context`:

init_context
============

.. c:function:: void init_context(struct ctx_info *ctxi, struct cxlflash_cfg *cfg, void *ctx, int ctxid, struct file *file, u32 perms, u64 irqs)

    initializes a previously allocated context

    :param struct ctx_info \*ctxi:
        Previously allocated context

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param void \*ctx:
        Previously obtained context cookie.

    :param int ctxid:
        Previously obtained process element associated with CXL context.

    :param struct file \*file:
        Previously obtained file associated with CXL context.

    :param u32 perms:
        User-specified permissions.

    :param u64 irqs:
        User-specified number of interrupts.

.. _`remove_context`:

remove_context
==============

.. c:function:: void remove_context(struct kref *kref)

    context kref release handler

    :param struct kref \*kref:
        Kernel reference associated with context to be removed.

.. _`remove_context.description`:

Description
-----------

When a context no longer has any references it can safely be removed
from global access and destroyed. Note that it is assumed the thread
relinquishing access to the context holds its mutex.

.. _`_cxlflash_disk_detach`:

_cxlflash_disk_detach
=====================

.. c:function:: int _cxlflash_disk_detach(struct scsi_device *sdev, struct ctx_info *ctxi, struct dk_cxlflash_detach *detach)

    detaches a LUN from a context

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param struct ctx_info \*ctxi:
        Context owning resources.

    :param struct dk_cxlflash_detach \*detach:
        Detach ioctl data structure.

.. _`_cxlflash_disk_detach.description`:

Description
-----------

As part of the detach, all per-context resources associated with the LUN
are cleaned up. When detaching the last LUN for a context, the context
itself is cleaned up and released.

.. _`_cxlflash_disk_detach.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_cxl_release`:

cxlflash_cxl_release
====================

.. c:function:: int cxlflash_cxl_release(struct inode *inode, struct file *file)

    release handler for adapter file descriptor

    :param struct inode \*inode:
        File-system inode associated with fd.

    :param struct file \*file:
        File installed with adapter file descriptor.

.. _`cxlflash_cxl_release.description`:

Description
-----------

This routine is the release handler for the fops registered with
the CXL services on an initial attach for a context. It is called
when a close (explicity by the user or as part of a process tear
down) is performed on the adapter file descriptor returned to the
user. The user should be aware that explicitly performing a close
considered catastrophic and subsequent usage of the superpipe API
with previously saved off tokens will fail.

This routine derives the context reference and calls detach for
each LUN associated with the context.The final detach operation
causes the context itself to be freed. With exception to when the
CXL process element (context id) lookup fails (a case that should
theoretically never occur), every call into this routine results
in a complete freeing of a context.

.. _`cxlflash_cxl_release.return`:

Return
------

0 on success

.. _`unmap_context`:

unmap_context
=============

.. c:function:: void unmap_context(struct ctx_info *ctxi)

    clears a previously established mapping

    :param struct ctx_info \*ctxi:
        Context owning the mapping.

.. _`unmap_context.description`:

Description
-----------

This routine is used to switch between the error notification page
(dummy page of all 1's) and the real mapping (established by the CXL
fault handler).

.. _`get_err_page`:

get_err_page
============

.. c:function:: struct page *get_err_page(struct cxlflash_cfg *cfg)

    obtains and allocates the error notification page

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`get_err_page.return`:

Return
------

error notification page on success, NULL on failure

.. _`cxlflash_mmap_fault`:

cxlflash_mmap_fault
===================

.. c:function:: int cxlflash_mmap_fault(struct vm_fault *vmf)

    mmap fault handler for adapter file descriptor

    :param struct vm_fault \*vmf:
        VM fault associated with current fault.

.. _`cxlflash_mmap_fault.description`:

Description
-----------

To support error notification via MMIO, faults are 'caught' by this routine
that was inserted before passing back the adapter file descriptor on attach.
When a fault occurs, this routine evaluates if error recovery is active and
if so, installs the error page to 'notify' the user about the error state.
During normal operation, the fault is simply handled by the original fault
handler that was installed by CXL services as part of initializing the
adapter file descriptor. The VMA's page protection bits are toggled to
indicate cached/not-cached depending on the memory backing the fault.

.. _`cxlflash_mmap_fault.return`:

Return
------

0 on success, VM_FAULT_SIGBUS on failure

.. _`cxlflash_cxl_mmap`:

cxlflash_cxl_mmap
=================

.. c:function:: int cxlflash_cxl_mmap(struct file *file, struct vm_area_struct *vma)

    mmap handler for adapter file descriptor

    :param struct file \*file:
        File installed with adapter file descriptor.

    :param struct vm_area_struct \*vma:
        VM area associated with mapping.

.. _`cxlflash_cxl_mmap.description`:

Description
-----------

Installs local mmap vmops to 'catch' faults for error notification support.

.. _`cxlflash_cxl_mmap.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_mark_contexts_error`:

cxlflash_mark_contexts_error
============================

.. c:function:: int cxlflash_mark_contexts_error(struct cxlflash_cfg *cfg)

    move contexts to error state and list

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`cxlflash_mark_contexts_error.description`:

Description
-----------

A context is only moved over to the error list when there are no outstanding
references to it. This ensures that a running operation has completed.

.. _`cxlflash_mark_contexts_error.return`:

Return
------

0 on success, -errno on failure

.. _`check_state`:

check_state
===========

.. c:function:: int check_state(struct cxlflash_cfg *cfg)

    checks and responds to the current adapter state

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`check_state.description`:

Description
-----------

This routine can block and should only be used on process context.
It assumes that the caller is an ioctl thread and holding the ioctl
read semaphore. This is temporarily let up across the wait to allow
for draining actively running ioctls. Also note that when waking up
from waiting in reset, the state is unknown and must be checked again
before proceeding.

.. _`check_state.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_disk_attach`:

cxlflash_disk_attach
====================

.. c:function:: int cxlflash_disk_attach(struct scsi_device *sdev, struct dk_cxlflash_attach *attach)

    attach a LUN to a context

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param struct dk_cxlflash_attach \*attach:
        Attach ioctl data structure.

.. _`cxlflash_disk_attach.description`:

Description
-----------

Creates a context and attaches LUN to it. A LUN can only be attached
one time to a context (subsequent attaches for the same context/LUN pair
are not supported). Additional LUNs can be attached to a context by
specifying the 'reuse' flag defined in the cxlflash_ioctl.h header.

.. _`cxlflash_disk_attach.return`:

Return
------

0 on success, -errno on failure

.. _`recover_context`:

recover_context
===============

.. c:function:: int recover_context(struct cxlflash_cfg *cfg, struct ctx_info *ctxi, int *adap_fd)

    recovers a context in error

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param struct ctx_info \*ctxi:
        Context to release.

    :param int \*adap_fd:
        Adapter file descriptor associated with new/recovered context.

.. _`recover_context.description`:

Description
-----------

Restablishes the state for a context-in-error.

.. _`recover_context.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_afu_recover`:

cxlflash_afu_recover
====================

.. c:function:: int cxlflash_afu_recover(struct scsi_device *sdev, struct dk_cxlflash_recover_afu *recover)

    initiates AFU recovery

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param struct dk_cxlflash_recover_afu \*recover:
        Recover ioctl data structure.

.. _`cxlflash_afu_recover.description`:

Description
-----------

Only a single recovery is allowed at a time to avoid exhausting CXL
resources (leading to recovery failure) in the event that we're up
against the maximum number of contexts limit. For similar reasons,
a context recovery is retried if there are multiple recoveries taking
place at the same time and the failure was due to CXL services being
unable to keep up.

As this routine is called on ioctl context, it holds the ioctl r/w
semaphore that is used to drain ioctls in recovery scenarios. The
implementation to achieve the pacing described above (a local mutex)
requires that the ioctl r/w semaphore be dropped and reacquired to
avoid a 3-way deadlock when multiple process recoveries operate in
parallel.

Because a user can detect an error condition before the kernel, it is
quite possible for this routine to act as the kernel's EEH detection
source (MMIO read of mbox_r). Because of this, there is a window of
time where an EEH might have been detected but not yet 'serviced'
(callback invoked, causing the device to enter reset state). To avoid
looping in this routine during that window, a 1 second sleep is in place
between the time the MMIO failure is detected and the time a wait on the
reset wait queue is attempted via \ :c:func:`check_state`\ .

.. _`cxlflash_afu_recover.return`:

Return
------

0 on success, -errno on failure

.. _`process_sense`:

process_sense
=============

.. c:function:: int process_sense(struct scsi_device *sdev, struct dk_cxlflash_verify *verify)

    evaluates and processes sense data

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param struct dk_cxlflash_verify \*verify:
        Verify ioctl data structure.

.. _`process_sense.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_disk_verify`:

cxlflash_disk_verify
====================

.. c:function:: int cxlflash_disk_verify(struct scsi_device *sdev, struct dk_cxlflash_verify *verify)

    verifies a LUN is the same and handle size changes

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param struct dk_cxlflash_verify \*verify:
        Verify ioctl data structure.

.. _`cxlflash_disk_verify.return`:

Return
------

0 on success, -errno on failure

.. _`decode_ioctl`:

decode_ioctl
============

.. c:function:: char *decode_ioctl(int cmd)

    translates an encoded ioctl to an easily identifiable string

    :param int cmd:
        The ioctl command to decode.

.. _`decode_ioctl.return`:

Return
------

A string identifying the decoded ioctl.

.. _`cxlflash_disk_direct_open`:

cxlflash_disk_direct_open
=========================

.. c:function:: int cxlflash_disk_direct_open(struct scsi_device *sdev, void *arg)

    opens a direct (physical) disk

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param void \*arg:
        UDirect ioctl data structure.

.. _`cxlflash_disk_direct_open.description`:

Description
-----------

On successful return, the user is informed of the resource handle
to be used to identify the direct lun and the size (in blocks) of
the direct lun in last LBA format.

.. _`cxlflash_disk_direct_open.return`:

Return
------

0 on success, -errno on failure

.. _`ioctl_common`:

ioctl_common
============

.. c:function:: int ioctl_common(struct scsi_device *sdev, int cmd)

    common IOCTL handler for driver

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param int cmd:
        IOCTL command.

.. _`ioctl_common.description`:

Description
-----------

Handles common fencing operations that are valid for multiple ioctls. Always
allow through ioctls that are cleanup oriented in nature, even when operating
in a failed/terminating state.

.. _`ioctl_common.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_ioctl`:

cxlflash_ioctl
==============

.. c:function:: int cxlflash_ioctl(struct scsi_device *sdev, int cmd, void __user *arg)

    IOCTL handler for driver

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param int cmd:
        IOCTL command.

    :param void __user \*arg:
        Userspace ioctl data structure.

.. _`cxlflash_ioctl.description`:

Description
-----------

A read/write semaphore is used to implement a 'drain' of currently
running ioctls. The read semaphore is taken at the beginning of each
ioctl thread and released upon concluding execution. Additionally the
semaphore should be released and then reacquired in any ioctl execution
path which will wait for an event to occur that is outside the scope of
the ioctl (i.e. an adapter reset). To drain the ioctls currently running,
a thread simply needs to acquire the write semaphore.

.. _`cxlflash_ioctl.return`:

Return
------

0 on success, -errno on failure

.. This file was automatic generated / don't edit.

