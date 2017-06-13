.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/cxlflash/vlun.c

.. _`marshal_virt_to_resize`:

marshal_virt_to_resize
======================

.. c:function:: void marshal_virt_to_resize(struct dk_cxlflash_uvirtual *virt, struct dk_cxlflash_resize *resize)

    translate uvirtual to resize structure

    :param struct dk_cxlflash_uvirtual \*virt:
        Source structure from which to translate/copy.

    :param struct dk_cxlflash_resize \*resize:
        Destination structure for the translate/copy.

.. _`marshal_clone_to_rele`:

marshal_clone_to_rele
=====================

.. c:function:: void marshal_clone_to_rele(struct dk_cxlflash_clone *clone, struct dk_cxlflash_release *release)

    translate clone to release structure

    :param struct dk_cxlflash_clone \*clone:
        Source structure from which to translate/copy.

    :param struct dk_cxlflash_release \*release:
        *undescribed*

.. _`ba_init`:

ba_init
=======

.. c:function:: int ba_init(struct ba_lun *ba_lun)

    initializes a block allocator

    :param struct ba_lun \*ba_lun:
        Block allocator to initialize.

.. _`ba_init.return`:

Return
------

0 on success, -errno on failure

.. _`find_free_range`:

find_free_range
===============

.. c:function:: int find_free_range(u32 low, u32 high, struct ba_lun_info *bali, int *bit_word)

    locates a free bit within the block allocator

    :param u32 low:
        First word in block allocator to start search.

    :param u32 high:
        Last word in block allocator to search.

    :param struct ba_lun_info \*bali:
        LUN information structure owning the block allocator to search.

    :param int \*bit_word:
        Passes back the word in the block allocator owning the free bit.

.. _`find_free_range.return`:

Return
------

The bit position within the passed back word, -1 on failure

.. _`ba_alloc`:

ba_alloc
========

.. c:function:: u64 ba_alloc(struct ba_lun *ba_lun)

    allocates a block from the block allocator

    :param struct ba_lun \*ba_lun:
        Block allocator from which to allocate a block.

.. _`ba_alloc.return`:

Return
------

The allocated block, -1 on failure

.. _`validate_alloc`:

validate_alloc
==============

.. c:function:: int validate_alloc(struct ba_lun_info *bali, u64 aun)

    validates the specified block has been allocated

    :param struct ba_lun_info \*bali:
        *undescribed*

    :param u64 aun:
        Block to validate.

.. _`validate_alloc.return`:

Return
------

0 on success, -1 on failure

.. _`ba_free`:

ba_free
=======

.. c:function:: int ba_free(struct ba_lun *ba_lun, u64 to_free)

    frees a block from the block allocator

    :param struct ba_lun \*ba_lun:
        Block allocator from which to allocate a block.

    :param u64 to_free:
        Block to free.

.. _`ba_free.return`:

Return
------

0 on success, -1 on failure

.. _`ba_clone`:

ba_clone
========

.. c:function:: int ba_clone(struct ba_lun *ba_lun, u64 to_clone)

    Clone a chunk of the block allocation table

    :param struct ba_lun \*ba_lun:
        Block allocator from which to allocate a block.

    :param u64 to_clone:
        *undescribed*

.. _`ba_clone.return`:

Return
------

0 on success, -1 on failure

.. _`ba_space`:

ba_space
========

.. c:function:: u64 ba_space(struct ba_lun *ba_lun)

    returns the amount of free space left in the block allocator

    :param struct ba_lun \*ba_lun:
        Block allocator.

.. _`ba_space.return`:

Return
------

Amount of free space in block allocator

.. _`cxlflash_ba_terminate`:

cxlflash_ba_terminate
=====================

.. c:function:: void cxlflash_ba_terminate(struct ba_lun *ba_lun)

    frees resources associated with the block allocator

    :param struct ba_lun \*ba_lun:
        Block allocator.

.. _`cxlflash_ba_terminate.description`:

Description
-----------

Safe to call in a partially allocated state.

.. _`init_vlun`:

init_vlun
=========

.. c:function:: int init_vlun(struct llun_info *lli)

    initializes a LUN for virtual use

    :param struct llun_info \*lli:
        *undescribed*

.. _`init_vlun.return`:

Return
------

0 on success, -errno on failure

.. _`write_same16`:

write_same16
============

.. c:function:: int write_same16(struct scsi_device *sdev, u64 lba, u32 nblks)

    sends a SCSI WRITE_SAME16 (0) command to specified LUN

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param u64 lba:
        Logical block address to start write same.

    :param u32 nblks:
        Number of logical blocks to write same.

.. _`write_same16.description`:

Description
-----------

The SCSI WRITE_SAME16 can take quite a while to complete. Should an EEH occur
while in \ :c:func:`scsi_execute`\ , the EEH handler will attempt to recover. As part of
the recovery, the handler drains all currently running ioctls, waiting until
they have completed before proceeding with a reset. As this routine is used
on the ioctl path, this can create a condition where the EEH handler becomes
stuck, infinitely waiting for this ioctl thread. To avoid this behavior,
temporarily unmark this thread as an ioctl thread by releasing the ioctl read
semaphore. This will allow the EEH handler to proceed with a recovery while
this thread is still running. Once the \ :c:func:`scsi_execute`\  returns, reacquire the
ioctl read semaphore and check the adapter state in case it changed while
inside of \ :c:func:`scsi_execute`\ . The state check will wait if the adapter is still
being recovered or return a failure if the recovery failed. In the event that
the adapter reset failed, simply return the failure as the ioctl would be
unable to continue.

Note that the above puts a requirement on this routine to only be called on
an ioctl thread.

.. _`write_same16.return`:

Return
------

0 on success, -errno on failure

.. _`grow_lxt`:

grow_lxt
========

.. c:function:: int grow_lxt(struct afu *afu, struct scsi_device *sdev, ctx_hndl_t ctxid, res_hndl_t rhndl, struct sisl_rht_entry *rhte, u64 *new_size)

    expands the translation table associated with the specified RHTE

    :param struct afu \*afu:
        AFU associated with the host.

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param ctx_hndl_t ctxid:
        Context ID of context owning the RHTE.

    :param res_hndl_t rhndl:
        Resource handle associated with the RHTE.

    :param struct sisl_rht_entry \*rhte:
        Resource handle entry (RHTE).

    :param u64 \*new_size:
        Number of translation entries associated with RHTE.

.. _`grow_lxt.description`:

Description
-----------

By design, this routine employs a 'best attempt' allocation and will
truncate the requested size down if there is not sufficient space in
the block allocator to satisfy the request but there does exist some
amount of space. The user is made aware of this by returning the size
allocated.

.. _`grow_lxt.return`:

Return
------

0 on success, -errno on failure

.. _`shrink_lxt`:

shrink_lxt
==========

.. c:function:: int shrink_lxt(struct afu *afu, struct scsi_device *sdev, res_hndl_t rhndl, struct sisl_rht_entry *rhte, struct ctx_info *ctxi, u64 *new_size)

    reduces translation table associated with the specified RHTE

    :param struct afu \*afu:
        AFU associated with the host.

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN.

    :param res_hndl_t rhndl:
        Resource handle associated with the RHTE.

    :param struct sisl_rht_entry \*rhte:
        Resource handle entry (RHTE).

    :param struct ctx_info \*ctxi:
        Context owning resources.

    :param u64 \*new_size:
        Number of translation entries associated with RHTE.

.. _`shrink_lxt.return`:

Return
------

0 on success, -errno on failure

.. _`_cxlflash_vlun_resize`:

_cxlflash_vlun_resize
=====================

.. c:function:: int _cxlflash_vlun_resize(struct scsi_device *sdev, struct ctx_info *ctxi, struct dk_cxlflash_resize *resize)

    changes the size of a virtual LUN

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN owning virtual LUN.

    :param struct ctx_info \*ctxi:
        Context owning resources.

    :param struct dk_cxlflash_resize \*resize:
        Resize ioctl data structure.

.. _`_cxlflash_vlun_resize.description`:

Description
-----------

On successful return, the user is informed of the new size (in blocks)
of the virtual LUN in last LBA format. When the size of the virtual
LUN is zero, the last LBA is reflected as -1. See comment in the
prologue for \_cxlflash_disk_release() regarding AFU syncs and contexts
on the error recovery list.

.. _`_cxlflash_vlun_resize.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_restore_luntable`:

cxlflash_restore_luntable
=========================

.. c:function:: void cxlflash_restore_luntable(struct cxlflash_cfg *cfg)

    Restore LUN table to prior state

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`get_num_ports`:

get_num_ports
=============

.. c:function:: u8 get_num_ports(u32 psm)

    compute number of ports from port selection mask

    :param u32 psm:
        Port selection mask.

.. _`get_num_ports.return`:

Return
------

Population count of port selection mask

.. _`init_luntable`:

init_luntable
=============

.. c:function:: int init_luntable(struct cxlflash_cfg *cfg, struct llun_info *lli)

    write an entry in the LUN table

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param struct llun_info \*lli:
        Per adapter LUN information structure.

.. _`init_luntable.description`:

Description
-----------

On successful return, a LUN table entry is created:
- at the top for LUNs visible on multiple ports.
- at the bottom for LUNs visible only on one port.

.. _`init_luntable.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_disk_virtual_open`:

cxlflash_disk_virtual_open
==========================

.. c:function:: int cxlflash_disk_virtual_open(struct scsi_device *sdev, void *arg)

    open a virtual disk of specified size

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN owning virtual LUN.

    :param void \*arg:
        UVirtual ioctl data structure.

.. _`cxlflash_disk_virtual_open.description`:

Description
-----------

On successful return, the user is informed of the resource handle
to be used to identify the virtual LUN and the size (in blocks) of
the virtual LUN in last LBA format. When the size of the virtual LUN
is zero, the last LBA is reflected as -1.

.. _`cxlflash_disk_virtual_open.return`:

Return
------

0 on success, -errno on failure

.. _`clone_lxt`:

clone_lxt
=========

.. c:function:: int clone_lxt(struct afu *afu, struct blka *blka, ctx_hndl_t ctxid, res_hndl_t rhndl, struct sisl_rht_entry *rhte, struct sisl_rht_entry *rhte_src)

    copies translation tables from source to destination RHTE

    :param struct afu \*afu:
        AFU associated with the host.

    :param struct blka \*blka:
        Block allocator associated with LUN.

    :param ctx_hndl_t ctxid:
        Context ID of context owning the RHTE.

    :param res_hndl_t rhndl:
        Resource handle associated with the RHTE.

    :param struct sisl_rht_entry \*rhte:
        Destination resource handle entry (RHTE).

    :param struct sisl_rht_entry \*rhte_src:
        Source resource handle entry (RHTE).

.. _`clone_lxt.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_disk_clone`:

cxlflash_disk_clone
===================

.. c:function:: int cxlflash_disk_clone(struct scsi_device *sdev, struct dk_cxlflash_clone *clone)

    clone a context by making snapshot of another

    :param struct scsi_device \*sdev:
        SCSI device associated with LUN owning virtual LUN.

    :param struct dk_cxlflash_clone \*clone:
        Clone ioctl data structure.

.. _`cxlflash_disk_clone.description`:

Description
-----------

This routine effectively performs cxlflash_disk_open operation for each
in-use virtual resource in the source context. Note that the destination
context must be in pristine state and cannot have any resource handles
open at the time of the clone.

.. _`cxlflash_disk_clone.return`:

Return
------

0 on success, -errno on failure

.. This file was automatic generated / don't edit.

