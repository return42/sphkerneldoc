.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_scsih.c

.. _`sense_info`:

struct sense_info
=================

.. c:type:: struct sense_info

    common structure for obtaining sense keys

.. _`sense_info.definition`:

Definition
----------

.. code-block:: c

    struct sense_info {
        u8 skey;
        u8 asc;
        u8 ascq;
    }

.. _`sense_info.members`:

Members
-------

skey
    sense key

asc
    additional sense code

ascq
    additional sense code qualifier

.. _`fw_event_work`:

struct fw_event_work
====================

.. c:type:: struct fw_event_work

    firmware event struct

.. _`fw_event_work.definition`:

Definition
----------

.. code-block:: c

    struct fw_event_work {
        struct list_head list;
        struct work_struct work;
        struct MPT3SAS_ADAPTER *ioc;
        u16 device_handle;
        u8 VF_ID;
        u8 VP_ID;
        u8 ignore;
        u16 event;
        struct kref refcount;
        char event_data[0];
    }

.. _`fw_event_work.members`:

Members
-------

list
    link list framework

work
    work object (ioc->fault_reset_work_q)

ioc
    per adapter object

device_handle
    device handle

VF_ID
    virtual function id

VP_ID
    virtual port id

ignore
    flag meaning this event has been marked to ignore

event
    firmware event MPI2_EVENT_XXX defined in mpi2_ioc.h

refcount
    kref for this event

event_data
    reply event data payload follows

.. _`fw_event_work.description`:

Description
-----------

This object stored on ioc->fw_event_list.

.. _`_scsi_io_transfer`:

struct \_scsi_io_transfer
=========================

.. c:type:: struct _scsi_io_transfer

    scsi io transfer

.. _`_scsi_io_transfer.definition`:

Definition
----------

.. code-block:: c

    struct _scsi_io_transfer {
        u16 handle;
        u8 is_raid;
        enum dma_data_direction dir;
        u32 data_length;
        dma_addr_t data_dma;
        u8 sense[SCSI_SENSE_BUFFERSIZE];
        u32 lun;
        u8 cdb_length;
        u8 cdb[32];
        u8 timeout;
        u8 VF_ID;
        u8 VP_ID;
        u8 valid_reply;
        u32 sense_length;
        u16 ioc_status;
        u8 scsi_state;
        u8 scsi_status;
        u32 log_info;
        u32 transfer_length;
    }

.. _`_scsi_io_transfer.members`:

Members
-------

handle
    sas device handle (assigned by firmware)

is_raid
    flag set for hidden raid components

dir
    DMA_TO_DEVICE, DMA_FROM_DEVICE,

data_length
    data transfer length

data_dma
    dma pointer to data

sense
    sense data

lun
    lun number

cdb_length
    cdb length

cdb
    cdb contents

timeout
    timeout for this command

VF_ID
    virtual function id

VP_ID
    virtual port id

valid_reply
    flag set for reply message

sense_length
    sense length

ioc_status
    ioc status

scsi_state
    scsi state

scsi_status
    scsi staus

log_info
    log information

transfer_length
    data length transfer when there is a reply message

.. _`_scsi_io_transfer.description`:

Description
-----------

Used for sending internal scsi commands to devices within this module.
Refer to \_scsi_send_scsi_io().

.. _`_scsih_set_debug_level`:

_scsih_set_debug_level
======================

.. c:function:: int _scsih_set_debug_level(const char *val, struct kernel_param *kp)

    global setting of ioc->logging_level.

    :param const char \*val:
        *undescribed*

    :param struct kernel_param \*kp:
        *undescribed*

.. _`_scsih_set_debug_level.note`:

Note
----

The logging levels are defined in mpt3sas_debug.h.

.. _`_scsih_srch_boot_sas_address`:

_scsih_srch_boot_sas_address
============================

.. c:function:: int _scsih_srch_boot_sas_address(u64 sas_address, Mpi2BootDeviceSasWwid_t *boot_device)

    search based on sas_address

    :param u64 sas_address:
        sas address

    :param Mpi2BootDeviceSasWwid_t \*boot_device:
        boot device object from bios page 2

.. _`_scsih_srch_boot_sas_address.description`:

Description
-----------

Returns 1 when there's a match, 0 means no match.

.. _`_scsih_srch_boot_device_name`:

_scsih_srch_boot_device_name
============================

.. c:function:: int _scsih_srch_boot_device_name(u64 device_name, Mpi2BootDeviceDeviceName_t *boot_device)

    search based on device name

    :param u64 device_name:
        device name specified in INDENTIFY fram

    :param Mpi2BootDeviceDeviceName_t \*boot_device:
        boot device object from bios page 2

.. _`_scsih_srch_boot_device_name.description`:

Description
-----------

Returns 1 when there's a match, 0 means no match.

.. _`_scsih_srch_boot_encl_slot`:

_scsih_srch_boot_encl_slot
==========================

.. c:function:: int _scsih_srch_boot_encl_slot(u64 enclosure_logical_id, u16 slot_number, Mpi2BootDeviceEnclosureSlot_t *boot_device)

    search based on enclosure_logical_id/slot

    :param u64 enclosure_logical_id:
        enclosure logical id

    :param u16 slot_number:
        slot number

    :param Mpi2BootDeviceEnclosureSlot_t \*boot_device:
        boot device object from bios page 2

.. _`_scsih_srch_boot_encl_slot.description`:

Description
-----------

Returns 1 when there's a match, 0 means no match.

.. _`_scsih_is_boot_device`:

_scsih_is_boot_device
=====================

.. c:function:: int _scsih_is_boot_device(u64 sas_address, u64 device_name, u64 enclosure_logical_id, u16 slot, u8 form, Mpi2BiosPage2BootDevice_t *boot_device)

    search for matching boot device.

    :param u64 sas_address:
        sas address

    :param u64 device_name:
        device name specified in INDENTIFY fram

    :param u64 enclosure_logical_id:
        enclosure logical id

    :param u16 slot:
        *undescribed*

    :param u8 form:
        specifies boot device form

    :param Mpi2BiosPage2BootDevice_t \*boot_device:
        boot device object from bios page 2

.. _`_scsih_is_boot_device.description`:

Description
-----------

Returns 1 when there's a match, 0 means no match.

.. _`_scsih_get_sas_address`:

_scsih_get_sas_address
======================

.. c:function:: int _scsih_get_sas_address(struct MPT3SAS_ADAPTER *ioc, u16 handle, u64 *sas_address)

    set the sas_address for given device handle

    :param struct MPT3SAS_ADAPTER \*ioc:
        *undescribed*

    :param u16 handle:
        device handle

    :param u64 \*sas_address:
        sas address

.. _`_scsih_get_sas_address.description`:

Description
-----------

Returns 0 success, non-zero when failure

.. _`_scsih_determine_boot_device`:

_scsih_determine_boot_device
============================

.. c:function:: void _scsih_determine_boot_device(struct MPT3SAS_ADAPTER *ioc, void *device, u8 is_raid)

    determine boot device.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param void \*device:
        either sas_device or raid_device object

    :param u8 is_raid:
        [flag] 1 = raid object, 0 = sas object

.. _`_scsih_determine_boot_device.description`:

Description
-----------

Determines whether this device should be first reported device to
to scsi-ml or sas transport, this purpose is for persistent boot device.
There are primary, alternate, and current entries in bios page 2. The order
priority is primary, alternate, then current.  This routine saves
the corresponding device object and is_raid flag in the ioc object.
The saved data to be used later in \_scsih_probe_boot_devices().

.. _`mpt3sas_get_sdev_by_addr`:

mpt3sas_get_sdev_by_addr
========================

.. c:function:: struct _sas_device *mpt3sas_get_sdev_by_addr(struct MPT3SAS_ADAPTER *ioc, u64 sas_address)

    sas device search

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 sas_address:
        sas address

.. _`mpt3sas_get_sdev_by_addr.context`:

Context
-------

Calling function should acquire ioc->sas_device_lock

.. _`mpt3sas_get_sdev_by_addr.description`:

Description
-----------

This searches for sas_device based on sas_address, then return sas_device
object.

.. _`mpt3sas_get_sdev_by_handle`:

mpt3sas_get_sdev_by_handle
==========================

.. c:function:: struct _sas_device *mpt3sas_get_sdev_by_handle(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    sas device search

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        sas device handle (assigned by firmware)

.. _`mpt3sas_get_sdev_by_handle.context`:

Context
-------

Calling function should acquire ioc->sas_device_lock

.. _`mpt3sas_get_sdev_by_handle.description`:

Description
-----------

This searches for sas_device based on sas_address, then return sas_device
object.

.. _`_scsih_sas_device_remove`:

_scsih_sas_device_remove
========================

.. c:function:: void _scsih_sas_device_remove(struct MPT3SAS_ADAPTER *ioc, struct _sas_device *sas_device)

    remove sas_device from list.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_device \*sas_device:
        the sas_device object

.. _`_scsih_sas_device_remove.context`:

Context
-------

This function will acquire ioc->sas_device_lock.

.. _`_scsih_sas_device_remove.description`:

Description
-----------

If sas_device is on the list, remove it and decrement its reference count.

.. _`_scsih_device_remove_by_handle`:

_scsih_device_remove_by_handle
==============================

.. c:function:: void _scsih_device_remove_by_handle(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    removing device object by handle

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

.. _`_scsih_device_remove_by_handle.description`:

Description
-----------

Return nothing.

.. _`mpt3sas_device_remove_by_sas_address`:

mpt3sas_device_remove_by_sas_address
====================================

.. c:function:: void mpt3sas_device_remove_by_sas_address(struct MPT3SAS_ADAPTER *ioc, u64 sas_address)

    removing device object by sas address

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 sas_address:
        device sas_address

.. _`mpt3sas_device_remove_by_sas_address.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_device_add`:

_scsih_sas_device_add
=====================

.. c:function:: void _scsih_sas_device_add(struct MPT3SAS_ADAPTER *ioc, struct _sas_device *sas_device)

    insert sas_device to the list.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_device \*sas_device:
        the sas_device object

.. _`_scsih_sas_device_add.context`:

Context
-------

This function will acquire ioc->sas_device_lock.

.. _`_scsih_sas_device_add.description`:

Description
-----------

Adding new object to the ioc->sas_device_list.

.. _`_scsih_sas_device_init_add`:

_scsih_sas_device_init_add
==========================

.. c:function:: void _scsih_sas_device_init_add(struct MPT3SAS_ADAPTER *ioc, struct _sas_device *sas_device)

    insert sas_device to the list.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_device \*sas_device:
        the sas_device object

.. _`_scsih_sas_device_init_add.context`:

Context
-------

This function will acquire ioc->sas_device_lock.

.. _`_scsih_sas_device_init_add.description`:

Description
-----------

Adding new object at driver load time to the ioc->sas_device_init_list.

.. _`_scsih_raid_device_find_by_id`:

_scsih_raid_device_find_by_id
=============================

.. c:function:: struct _raid_device *_scsih_raid_device_find_by_id(struct MPT3SAS_ADAPTER *ioc, int id, int channel)

    raid device search

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param int id:
        sas device target id

    :param int channel:
        sas device channel

.. _`_scsih_raid_device_find_by_id.context`:

Context
-------

Calling function should acquire ioc->raid_device_lock

.. _`_scsih_raid_device_find_by_id.description`:

Description
-----------

This searches for raid_device based on target id, then return raid_device
object.

.. _`mpt3sas_raid_device_find_by_handle`:

mpt3sas_raid_device_find_by_handle
==================================

.. c:function:: struct _raid_device *mpt3sas_raid_device_find_by_handle(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    raid device search

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        sas device handle (assigned by firmware)

.. _`mpt3sas_raid_device_find_by_handle.context`:

Context
-------

Calling function should acquire ioc->raid_device_lock

.. _`mpt3sas_raid_device_find_by_handle.description`:

Description
-----------

This searches for raid_device based on handle, then return raid_device
object.

.. _`_scsih_raid_device_find_by_wwid`:

_scsih_raid_device_find_by_wwid
===============================

.. c:function:: struct _raid_device *_scsih_raid_device_find_by_wwid(struct MPT3SAS_ADAPTER *ioc, u64 wwid)

    raid device search

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 wwid:
        *undescribed*

.. _`_scsih_raid_device_find_by_wwid.context`:

Context
-------

Calling function should acquire ioc->raid_device_lock

.. _`_scsih_raid_device_find_by_wwid.description`:

Description
-----------

This searches for raid_device based on wwid, then return raid_device
object.

.. _`_scsih_raid_device_add`:

_scsih_raid_device_add
======================

.. c:function:: void _scsih_raid_device_add(struct MPT3SAS_ADAPTER *ioc, struct _raid_device *raid_device)

    add raid_device object

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _raid_device \*raid_device:
        raid_device object

.. _`_scsih_raid_device_add.description`:

Description
-----------

This is added to the raid_device_list link list.

.. _`_scsih_raid_device_remove`:

_scsih_raid_device_remove
=========================

.. c:function:: void _scsih_raid_device_remove(struct MPT3SAS_ADAPTER *ioc, struct _raid_device *raid_device)

    delete raid_device object

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _raid_device \*raid_device:
        raid_device object

.. _`mpt3sas_scsih_expander_find_by_handle`:

mpt3sas_scsih_expander_find_by_handle
=====================================

.. c:function:: struct _sas_node *mpt3sas_scsih_expander_find_by_handle(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    expander device search

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        expander handle (assigned by firmware)

.. _`mpt3sas_scsih_expander_find_by_handle.context`:

Context
-------

Calling function should acquire ioc->sas_device_lock

.. _`mpt3sas_scsih_expander_find_by_handle.description`:

Description
-----------

This searches for expander device based on handle, then returns the
sas_node object.

.. _`mpt3sas_scsih_expander_find_by_sas_address`:

mpt3sas_scsih_expander_find_by_sas_address
==========================================

.. c:function:: struct _sas_node *mpt3sas_scsih_expander_find_by_sas_address(struct MPT3SAS_ADAPTER *ioc, u64 sas_address)

    expander device search

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 sas_address:
        sas address

.. _`mpt3sas_scsih_expander_find_by_sas_address.context`:

Context
-------

Calling function should acquire ioc->sas_node_lock.

.. _`mpt3sas_scsih_expander_find_by_sas_address.description`:

Description
-----------

This searches for expander device based on sas_address, then returns the
sas_node object.

.. _`_scsih_expander_node_add`:

_scsih_expander_node_add
========================

.. c:function:: void _scsih_expander_node_add(struct MPT3SAS_ADAPTER *ioc, struct _sas_node *sas_expander)

    insert expander device to the list.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_node \*sas_expander:
        the sas_device object

.. _`_scsih_expander_node_add.context`:

Context
-------

This function will acquire ioc->sas_node_lock.

.. _`_scsih_expander_node_add.description`:

Description
-----------

Adding new object to the ioc->sas_expander_list.

Return nothing.

.. _`_scsih_is_end_device`:

_scsih_is_end_device
====================

.. c:function:: int _scsih_is_end_device(u32 device_info)

    determines if device is an end device

    :param u32 device_info:
        bitfield providing information about the device.

.. _`_scsih_is_end_device.context`:

Context
-------

none

.. _`_scsih_is_end_device.description`:

Description
-----------

Returns 1 if end device.

.. _`_scsih_scsi_lookup_get`:

_scsih_scsi_lookup_get
======================

.. c:function:: struct scsi_cmnd *_scsih_scsi_lookup_get(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    returns scmd entry

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

.. _`_scsih_scsi_lookup_get.description`:

Description
-----------

Returns the smid stored scmd pointer.

.. _`_scsih_scsi_lookup_get_clear`:

_scsih_scsi_lookup_get_clear
============================

.. c:function:: struct scsi_cmnd *_scsih_scsi_lookup_get_clear(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    returns scmd entry

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

.. _`_scsih_scsi_lookup_get_clear.description`:

Description
-----------

Returns the smid stored scmd pointer.
Then will derefrence the stored scmd pointer.

.. _`_scsih_scsi_lookup_find_by_scmd`:

_scsih_scsi_lookup_find_by_scmd
===============================

.. c:function:: u16 _scsih_scsi_lookup_find_by_scmd(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd)

    scmd lookup

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

.. _`_scsih_scsi_lookup_find_by_scmd.context`:

Context
-------

This function will acquire ioc->scsi_lookup_lock.

.. _`_scsih_scsi_lookup_find_by_scmd.description`:

Description
-----------

This will search for a scmd pointer in the scsi_lookup array,
returning the revelent smid.  A returned value of zero means invalid.

.. _`_scsih_scsi_lookup_find_by_target`:

_scsih_scsi_lookup_find_by_target
=================================

.. c:function:: u8 _scsih_scsi_lookup_find_by_target(struct MPT3SAS_ADAPTER *ioc, int id, int channel)

    search for matching channel:id

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param int id:
        target id

    :param int channel:
        channel

.. _`_scsih_scsi_lookup_find_by_target.context`:

Context
-------

This function will acquire ioc->scsi_lookup_lock.

.. _`_scsih_scsi_lookup_find_by_target.description`:

Description
-----------

This will search for a matching channel:id in the scsi_lookup array,
returning 1 if found.

.. _`_scsih_scsi_lookup_find_by_lun`:

_scsih_scsi_lookup_find_by_lun
==============================

.. c:function:: u8 _scsih_scsi_lookup_find_by_lun(struct MPT3SAS_ADAPTER *ioc, int id, unsigned int lun, int channel)

    search for matching channel:id:lun

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param int id:
        target id

    :param unsigned int lun:
        lun number

    :param int channel:
        channel

.. _`_scsih_scsi_lookup_find_by_lun.context`:

Context
-------

This function will acquire ioc->scsi_lookup_lock.

.. _`_scsih_scsi_lookup_find_by_lun.description`:

Description
-----------

This will search for a matching channel:id:lun in the scsi_lookup array,
returning 1 if found.

.. _`scsih_change_queue_depth`:

scsih_change_queue_depth
========================

.. c:function:: int scsih_change_queue_depth(struct scsi_device *sdev, int qdepth)

    setting device queue depth

    :param struct scsi_device \*sdev:
        scsi device struct

    :param int qdepth:
        requested queue depth

.. _`scsih_change_queue_depth.description`:

Description
-----------

Returns queue depth.

.. _`scsih_target_alloc`:

scsih_target_alloc
==================

.. c:function:: int scsih_target_alloc(struct scsi_target *starget)

    target add routine

    :param struct scsi_target \*starget:
        scsi target struct

.. _`scsih_target_alloc.description`:

Description
-----------

Returns 0 if ok. Any other return is assumed to be an error and
the device is ignored.

.. _`scsih_target_destroy`:

scsih_target_destroy
====================

.. c:function:: void scsih_target_destroy(struct scsi_target *starget)

    target destroy routine

    :param struct scsi_target \*starget:
        scsi target struct

.. _`scsih_target_destroy.description`:

Description
-----------

Returns nothing.

.. _`scsih_slave_alloc`:

scsih_slave_alloc
=================

.. c:function:: int scsih_slave_alloc(struct scsi_device *sdev)

    device add routine

    :param struct scsi_device \*sdev:
        scsi device struct

.. _`scsih_slave_alloc.description`:

Description
-----------

Returns 0 if ok. Any other return is assumed to be an error and
the device is ignored.

.. _`scsih_slave_destroy`:

scsih_slave_destroy
===================

.. c:function:: void scsih_slave_destroy(struct scsi_device *sdev)

    device destroy routine

    :param struct scsi_device \*sdev:
        scsi device struct

.. _`scsih_slave_destroy.description`:

Description
-----------

Returns nothing.

.. _`_scsih_display_sata_capabilities`:

_scsih_display_sata_capabilities
================================

.. c:function:: void _scsih_display_sata_capabilities(struct MPT3SAS_ADAPTER *ioc, u16 handle, struct scsi_device *sdev)

    sata capabilities

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

    :param struct scsi_device \*sdev:
        scsi device struct

.. _`scsih_is_raid`:

scsih_is_raid
=============

.. c:function:: int scsih_is_raid(struct device *dev)

    return boolean indicating device is raid volume \ ``dev``\  the device struct object

    :param struct device \*dev:
        *undescribed*

.. _`scsih_get_resync`:

scsih_get_resync
================

.. c:function:: void scsih_get_resync(struct device *dev)

    get raid volume resync percent complete \ ``dev``\  the device struct object

    :param struct device \*dev:
        *undescribed*

.. _`scsih_get_state`:

scsih_get_state
===============

.. c:function:: void scsih_get_state(struct device *dev)

    get raid volume level \ ``dev``\  the device struct object

    :param struct device \*dev:
        *undescribed*

.. _`_scsih_set_level`:

_scsih_set_level
================

.. c:function:: void _scsih_set_level(struct MPT3SAS_ADAPTER *ioc, struct scsi_device *sdev, u8 volume_type)

    set raid level

    :param struct MPT3SAS_ADAPTER \*ioc:
        *undescribed*

    :param struct scsi_device \*sdev:
        scsi device struct

    :param u8 volume_type:
        volume type

.. _`_scsih_get_volume_capabilities`:

_scsih_get_volume_capabilities
==============================

.. c:function:: int _scsih_get_volume_capabilities(struct MPT3SAS_ADAPTER *ioc, struct _raid_device *raid_device)

    volume capabilities

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _raid_device \*raid_device:
        *undescribed*

.. _`_scsih_get_volume_capabilities.description`:

Description
-----------

Returns 0 for success, else 1

.. _`_scsih_enable_tlr`:

_scsih_enable_tlr
=================

.. c:function:: void _scsih_enable_tlr(struct MPT3SAS_ADAPTER *ioc, struct scsi_device *sdev)

    setting TLR flags

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct scsi_device \*sdev:
        scsi device struct

.. _`_scsih_enable_tlr.description`:

Description
-----------

Enabling Transaction Layer Retries for tape devices when
vpd page 0x90 is present

.. _`scsih_slave_configure`:

scsih_slave_configure
=====================

.. c:function:: int scsih_slave_configure(struct scsi_device *sdev)

    device configure routine.

    :param struct scsi_device \*sdev:
        scsi device struct

.. _`scsih_slave_configure.description`:

Description
-----------

Returns 0 if ok. Any other return is assumed to be an error and
the device is ignored.

.. _`scsih_bios_param`:

scsih_bios_param
================

.. c:function:: int scsih_bios_param(struct scsi_device *sdev, struct block_device *bdev, sector_t capacity, int params[])

    fetch head, sector, cylinder info for a disk

    :param struct scsi_device \*sdev:
        scsi device struct

    :param struct block_device \*bdev:
        pointer to block device context

    :param sector_t capacity:
        device size (in 512 byte sectors)

    :param int params:
        three element array to place output:
        params[0] number of heads (max 255)
        params[1] number of sectors (max 63)
        params[2] number of cylinders

.. _`scsih_bios_param.description`:

Description
-----------

Return nothing.

.. _`_scsih_response_code`:

_scsih_response_code
====================

.. c:function:: void _scsih_response_code(struct MPT3SAS_ADAPTER *ioc, u8 response_code)

    translation of device response code

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u8 response_code:
        response code returned by the device

.. _`_scsih_response_code.description`:

Description
-----------

Return nothing.

.. _`_scsih_tm_done`:

_scsih_tm_done
==============

.. c:function:: u8 _scsih_tm_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    tm completion routine

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`_scsih_tm_done.context`:

Context
-------

none.

.. _`_scsih_tm_done.description`:

Description
-----------

The callback handler when using scsih_issue_tm.

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`mpt3sas_scsih_set_tm_flag`:

mpt3sas_scsih_set_tm_flag
=========================

.. c:function:: void mpt3sas_scsih_set_tm_flag(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    set per target tm_busy

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

.. _`mpt3sas_scsih_set_tm_flag.description`:

Description
-----------

During taskmangement request, we need to freeze the device queue.

.. _`mpt3sas_scsih_clear_tm_flag`:

mpt3sas_scsih_clear_tm_flag
===========================

.. c:function:: void mpt3sas_scsih_clear_tm_flag(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    clear per target tm_busy

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

.. _`mpt3sas_scsih_clear_tm_flag.description`:

Description
-----------

During taskmangement request, we need to freeze the device queue.

.. _`mpt3sas_scsih_issue_tm`:

mpt3sas_scsih_issue_tm
======================

.. c:function:: int mpt3sas_scsih_issue_tm(struct MPT3SAS_ADAPTER *ioc, u16 handle, uint channel, uint id, uint lun, u8 type, u16 smid_task, ulong timeout)

    main routine for sending tm requests

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter struct

    :param u16 handle:
        *undescribed*

    :param uint channel:
        the channel assigned by the OS

    :param uint id:
        the id assigned by the OS

    :param uint lun:
        lun number

    :param u8 type:
        MPI2_SCSITASKMGMT_TASKTYPE__XXX (defined in mpi2_init.h)

    :param u16 smid_task:
        smid assigned to the task

    :param ulong timeout:
        timeout in seconds

.. _`mpt3sas_scsih_issue_tm.context`:

Context
-------

user

.. _`mpt3sas_scsih_issue_tm.description`:

Description
-----------

A generic API for sending task management requests to firmware.

The callback index is set inside \`ioc->tm_cb_idx\`.

Return SUCCESS or FAILED.

.. _`_scsih_tm_display_info`:

_scsih_tm_display_info
======================

.. c:function:: void _scsih_tm_display_info(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd)

    displays info about the device

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter struct

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

.. _`_scsih_tm_display_info.description`:

Description
-----------

Called by task management callback handlers.

.. _`scsih_abort`:

scsih_abort
===========

.. c:function:: int scsih_abort(struct scsi_cmnd *scmd)

    eh threads main abort routine

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

.. _`scsih_abort.description`:

Description
-----------

Returns SUCCESS if command aborted else FAILED

.. _`scsih_dev_reset`:

scsih_dev_reset
===============

.. c:function:: int scsih_dev_reset(struct scsi_cmnd *scmd)

    eh threads main device reset routine

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

.. _`scsih_dev_reset.description`:

Description
-----------

Returns SUCCESS if command aborted else FAILED

.. _`scsih_target_reset`:

scsih_target_reset
==================

.. c:function:: int scsih_target_reset(struct scsi_cmnd *scmd)

    eh threads main target reset routine

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

.. _`scsih_target_reset.description`:

Description
-----------

Returns SUCCESS if command aborted else FAILED

.. _`scsih_host_reset`:

scsih_host_reset
================

.. c:function:: int scsih_host_reset(struct scsi_cmnd *scmd)

    eh threads main host reset routine

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

.. _`scsih_host_reset.description`:

Description
-----------

Returns SUCCESS if command aborted else FAILED

.. _`_scsih_fw_event_add`:

_scsih_fw_event_add
===================

.. c:function:: void _scsih_fw_event_add(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    insert and queue up fw_event

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        object describing the event

.. _`_scsih_fw_event_add.context`:

Context
-------

This function will acquire ioc->fw_event_lock.

.. _`_scsih_fw_event_add.description`:

Description
-----------

This adds the firmware event object into link list, then queues it up to
be processed from user context.

Return nothing.

.. _`_scsih_fw_event_del_from_list`:

_scsih_fw_event_del_from_list
=============================

.. c:function:: void _scsih_fw_event_del_from_list(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    delete fw_event from the list

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        object describing the event

.. _`_scsih_fw_event_del_from_list.context`:

Context
-------

This function will acquire ioc->fw_event_lock.

.. _`_scsih_fw_event_del_from_list.description`:

Description
-----------

If the fw_event is on the fw_event_list, remove it and do a put.

Return nothing.

.. _`_scsih_error_recovery_delete_devices`:

_scsih_error_recovery_delete_devices
====================================

.. c:function:: void _scsih_error_recovery_delete_devices(struct MPT3SAS_ADAPTER *ioc)

    remove devices not responding

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_error_recovery_delete_devices.description`:

Description
-----------

Return nothing.

.. _`mpt3sas_port_enable_complete`:

mpt3sas_port_enable_complete
============================

.. c:function:: void mpt3sas_port_enable_complete(struct MPT3SAS_ADAPTER *ioc)

    port enable completed (fake event)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`mpt3sas_port_enable_complete.description`:

Description
-----------

Return nothing.

.. _`_scsih_fw_event_cleanup_queue`:

_scsih_fw_event_cleanup_queue
=============================

.. c:function:: void _scsih_fw_event_cleanup_queue(struct MPT3SAS_ADAPTER *ioc)

    cleanup event queue

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_fw_event_cleanup_queue.description`:

Description
-----------

Walk the firmware event queue, either killing timers, or waiting
for outstanding events to complete

Return nothing.

.. _`_scsih_internal_device_block`:

_scsih_internal_device_block
============================

.. c:function:: void _scsih_internal_device_block(struct scsi_device *sdev, struct MPT3SAS_DEVICE *sas_device_priv_data)

    block the sdev device

    :param struct scsi_device \*sdev:
        per device object

    :param struct MPT3SAS_DEVICE \*sas_device_priv_data:
        per device driver private data

.. _`_scsih_internal_device_block.description`:

Description
-----------

make sure device is blocked without error, if not
print an error

.. _`_scsih_internal_device_unblock`:

_scsih_internal_device_unblock
==============================

.. c:function:: void _scsih_internal_device_unblock(struct scsi_device *sdev, struct MPT3SAS_DEVICE *sas_device_priv_data)

    unblock the sdev device

    :param struct scsi_device \*sdev:
        per device object

    :param struct MPT3SAS_DEVICE \*sas_device_priv_data:
        per device driver private data
        make sure device is unblocked without error, if not retry
        by blocking and then unblocking

.. _`_scsih_ublock_io_all_device`:

_scsih_ublock_io_all_device
===========================

.. c:function:: void _scsih_ublock_io_all_device(struct MPT3SAS_ADAPTER *ioc)

    unblock every device

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_ublock_io_all_device.description`:

Description
-----------

change the device state from block to running

.. _`_scsih_ublock_io_device`:

_scsih_ublock_io_device
=======================

.. c:function:: void _scsih_ublock_io_device(struct MPT3SAS_ADAPTER *ioc, u64 sas_address)

    prepare device to be deleted

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 sas_address:
        *undescribed*

.. _`_scsih_ublock_io_device.description`:

Description
-----------

unblock then put device in offline state

.. _`_scsih_block_io_all_device`:

_scsih_block_io_all_device
==========================

.. c:function:: void _scsih_block_io_all_device(struct MPT3SAS_ADAPTER *ioc)

    set the device state to SDEV_BLOCK

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_block_io_all_device.description`:

Description
-----------

During device pull we need to appropiately set the sdev state.

.. _`_scsih_block_io_device`:

_scsih_block_io_device
======================

.. c:function:: void _scsih_block_io_device(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    set the device state to SDEV_BLOCK

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

.. _`_scsih_block_io_device.description`:

Description
-----------

During device pull we need to appropiately set the sdev state.

.. _`_scsih_block_io_to_children_attached_to_ex`:

_scsih_block_io_to_children_attached_to_ex
==========================================

.. c:function:: void _scsih_block_io_to_children_attached_to_ex(struct MPT3SAS_ADAPTER *ioc, struct _sas_node *sas_expander)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_node \*sas_expander:
        the sas_device object

.. _`_scsih_block_io_to_children_attached_to_ex.description`:

Description
-----------

This routine set sdev state to SDEV_BLOCK for all devices
attached to this expander. This function called when expander is
pulled.

.. _`_scsih_block_io_to_children_attached_directly`:

_scsih_block_io_to_children_attached_directly
=============================================

.. c:function:: void _scsih_block_io_to_children_attached_directly(struct MPT3SAS_ADAPTER *ioc, Mpi2EventDataSasTopologyChangeList_t *event_data)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventDataSasTopologyChangeList_t \*event_data:
        topology change event data

.. _`_scsih_block_io_to_children_attached_directly.description`:

Description
-----------

This routine set sdev state to SDEV_BLOCK for all devices
direct attached during device pull.

.. _`_scsih_tm_tr_send`:

_scsih_tm_tr_send
=================

.. c:function:: void _scsih_tm_tr_send(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    send task management request

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

.. _`_scsih_tm_tr_send.context`:

Context
-------

interrupt time.

.. _`_scsih_tm_tr_send.description`:

Description
-----------

This code is to initiate the device removal handshake protocol
with controller firmware.  This function will issue target reset
using high priority request queue.  It will send a sas iounit
control request (MPI2_SAS_OP_REMOVE_DEVICE) from this completion.

This is designed to send muliple task management request at the same
time to the fifo. If the fifo is full, we will append the request,
and process it in a future completion.

.. _`_scsih_tm_tr_complete`:

_scsih_tm_tr_complete
=====================

.. c:function:: u8 _scsih_tm_tr_complete(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`_scsih_tm_tr_complete.context`:

Context
-------

interrupt time.

.. _`_scsih_tm_tr_complete.description`:

Description
-----------

This is the target reset completion routine.
This code is part of the code to initiate the device removal
handshake protocol with controller firmware.
It will send a sas iounit control request (MPI2_SAS_OP_REMOVE_DEVICE)

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_scsih_sas_control_complete`:

_scsih_sas_control_complete
===========================

.. c:function:: u8 _scsih_sas_control_complete(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    completion routine

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`_scsih_sas_control_complete.context`:

Context
-------

interrupt time.

.. _`_scsih_sas_control_complete.description`:

Description
-----------

This is the sas iounit control completion routine.
This code is part of the code to initiate the device removal
handshake protocol with controller firmware.

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_scsih_tm_tr_volume_send`:

_scsih_tm_tr_volume_send
========================

.. c:function:: void _scsih_tm_tr_volume_send(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    send target reset request for volumes

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

.. _`_scsih_tm_tr_volume_send.context`:

Context
-------

interrupt time.

.. _`_scsih_tm_tr_volume_send.description`:

Description
-----------

This is designed to send muliple task management request at the same
time to the fifo. If the fifo is full, we will append the request,
and process it in a future completion.

.. _`_scsih_tm_volume_tr_complete`:

_scsih_tm_volume_tr_complete
============================

.. c:function:: u8 _scsih_tm_volume_tr_complete(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    target reset completion

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`_scsih_tm_volume_tr_complete.context`:

Context
-------

interrupt time.

.. _`_scsih_tm_volume_tr_complete.description`:

Description
-----------

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_scsih_issue_delayed_event_ack`:

_scsih_issue_delayed_event_ack
==============================

.. c:function:: void _scsih_issue_delayed_event_ack(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 event, u32 event_context)

    issue delayed Event ACK messages

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u16 event:
        Event ID

    :param u32 event_context:
        used to track events uniquely

.. _`_scsih_issue_delayed_event_ack.description`:

Description
-----------

Context - processed in interrupt context.

.. _`_scsih_issue_delayed_sas_io_unit_ctrl`:

_scsih_issue_delayed_sas_io_unit_ctrl
=====================================

.. c:function:: void _scsih_issue_delayed_sas_io_unit_ctrl(struct MPT3SAS_ADAPTER *ioc, u16 smid, u16 handle)

    issue delayed sas_io_unit_ctrl messages

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u16 handle:
        device handle

.. _`_scsih_issue_delayed_sas_io_unit_ctrl.description`:

Description
-----------

Context - processed in interrupt context.

.. _`mpt3sas_check_for_pending_internal_cmds`:

mpt3sas_check_for_pending_internal_cmds
=======================================

.. c:function:: u8 mpt3sas_check_for_pending_internal_cmds(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    check for pending internal messages

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

.. _`mpt3sas_check_for_pending_internal_cmds.context`:

Context
-------

Executed in interrupt context

.. _`mpt3sas_check_for_pending_internal_cmds.description`:

Description
-----------

This will check delayed internal messages list, and process the
next request.

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_scsih_check_for_pending_tm`:

_scsih_check_for_pending_tm
===========================

.. c:function:: u8 _scsih_check_for_pending_tm(struct MPT3SAS_ADAPTER *ioc, u16 smid)

    check for pending task management

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

.. _`_scsih_check_for_pending_tm.description`:

Description
-----------

This will check delayed target reset list, and feed the
next reqeust.

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_scsih_check_topo_delete_events`:

_scsih_check_topo_delete_events
===============================

.. c:function:: void _scsih_check_topo_delete_events(struct MPT3SAS_ADAPTER *ioc, Mpi2EventDataSasTopologyChangeList_t *event_data)

    sanity check on topo events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventDataSasTopologyChangeList_t \*event_data:
        the event data payload

.. _`_scsih_check_topo_delete_events.description`:

Description
-----------

This routine added to better handle cable breaker.

This handles the case where driver receives multiple expander
add and delete events in a single shot.  When there is a delete event
the routine will void any pending add events waiting in the event queue.

Return nothing.

.. _`_scsih_set_volume_delete_flag`:

_scsih_set_volume_delete_flag
=============================

.. c:function:: void _scsih_set_volume_delete_flag(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    setting volume delete flag

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

.. _`_scsih_set_volume_delete_flag.description`:

Description
-----------

This returns nothing.

.. _`_scsih_set_volume_handle_for_tr`:

_scsih_set_volume_handle_for_tr
===============================

.. c:function:: void _scsih_set_volume_handle_for_tr(u16 handle, u16 *a, u16 *b)

    set handle for target reset to volume

    :param u16 handle:
        input handle

    :param u16 \*a:
        handle for volume a

    :param u16 \*b:
        handle for volume b

.. _`_scsih_set_volume_handle_for_tr.description`:

Description
-----------

IR firmware only supports two raid volumes.  The purpose of this
routine is to set the volume handle in either a or b. When the given
input handle is non-zero, or when a and b have not been set before.

.. _`_scsih_check_ir_config_unhide_events`:

_scsih_check_ir_config_unhide_events
====================================

.. c:function:: void _scsih_check_ir_config_unhide_events(struct MPT3SAS_ADAPTER *ioc, Mpi2EventDataIrConfigChangeList_t *event_data)

    check for UNHIDE events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventDataIrConfigChangeList_t \*event_data:
        the event data payload

.. _`_scsih_check_ir_config_unhide_events.context`:

Context
-------

interrupt time.

.. _`_scsih_check_ir_config_unhide_events.description`:

Description
-----------

This routine will send target reset to volume, followed by target
resets to the PDs. This is called when a PD has been removed, or
volume has been deleted or removed. When the target reset is sent
to volume, the PD target resets need to be queued to start upon
completion of the volume target reset.

Return nothing.

.. _`_scsih_check_volume_delete_events`:

_scsih_check_volume_delete_events
=================================

.. c:function:: void _scsih_check_volume_delete_events(struct MPT3SAS_ADAPTER *ioc, Mpi2EventDataIrVolume_t *event_data)

    set delete flag for volumes

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventDataIrVolume_t \*event_data:
        the event data payload

.. _`_scsih_check_volume_delete_events.context`:

Context
-------

interrupt time.

.. _`_scsih_check_volume_delete_events.description`:

Description
-----------

This will handle the case when the cable connected to entire volume is
pulled. We will take care of setting the deleted flag so normal IO will
not be sent.

Return nothing.

.. _`_scsih_temp_threshold_events`:

_scsih_temp_threshold_events
============================

.. c:function:: void _scsih_temp_threshold_events(struct MPT3SAS_ADAPTER *ioc, Mpi2EventDataTemperature_t *event_data)

    display temperature threshold exceeded events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventDataTemperature_t \*event_data:
        the temp threshold event data

.. _`_scsih_temp_threshold_events.context`:

Context
-------

interrupt time.

.. _`_scsih_temp_threshold_events.description`:

Description
-----------

Return nothing.

.. _`_scsih_flush_running_cmds`:

_scsih_flush_running_cmds
=========================

.. c:function:: void _scsih_flush_running_cmds(struct MPT3SAS_ADAPTER *ioc)

    completing outstanding commands.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_flush_running_cmds.description`:

Description
-----------

The flushing out of all pending scmd commands following host reset,
where all IO is dropped to the floor.

Return nothing.

.. _`_scsih_setup_eedp`:

_scsih_setup_eedp
=================

.. c:function:: void _scsih_setup_eedp(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd, Mpi2SCSIIORequest_t *mpi_request)

    setup MPI request for EEDP transfer

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

    :param Mpi2SCSIIORequest_t \*mpi_request:
        pointer to the SCSI_IO reqest message frame

.. _`_scsih_setup_eedp.description`:

Description
-----------

Supporting protection 1 and 3.

Returns nothing

.. _`_scsih_eedp_error_handling`:

_scsih_eedp_error_handling
==========================

.. c:function:: void _scsih_eedp_error_handling(struct scsi_cmnd *scmd, u16 ioc_status)

    return sense code for EEDP errors

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

    :param u16 ioc_status:
        ioc status

.. _`_scsih_eedp_error_handling.description`:

Description
-----------

Returns nothing

.. _`scsih_qcmd`:

scsih_qcmd
==========

.. c:function:: int scsih_qcmd(struct Scsi_Host *shost, struct scsi_cmnd *scmd)

    main scsi request entry point

    :param struct Scsi_Host \*shost:
        *undescribed*

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

.. _`scsih_qcmd.description`:

Description
-----------

The callback index is set inside \`ioc->scsi_io_cb_idx\`.

Returns 0 on success.  If there's a failure, return either:
SCSI_MLQUEUE_DEVICE_BUSY if the device queue is full, or
SCSI_MLQUEUE_HOST_BUSY if the entire host queue is full

.. _`_scsih_normalize_sense`:

_scsih_normalize_sense
======================

.. c:function:: void _scsih_normalize_sense(char *sense_buffer, struct sense_info *data)

    normalize descriptor and fixed format sense data

    :param char \*sense_buffer:
        sense data returned by target

    :param struct sense_info \*data:
        normalized skey/asc/ascq

.. _`_scsih_normalize_sense.description`:

Description
-----------

Return nothing.

.. _`_scsih_scsi_ioc_info`:

_scsih_scsi_ioc_info
====================

.. c:function:: void _scsih_scsi_ioc_info(struct MPT3SAS_ADAPTER *ioc, struct scsi_cmnd *scmd, Mpi2SCSIIOReply_t *mpi_reply, u16 smid)

    translated non-succesfull SCSI_IO request

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct scsi_cmnd \*scmd:
        pointer to scsi command object

    :param Mpi2SCSIIOReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param u16 smid:
        *undescribed*

.. _`_scsih_scsi_ioc_info.description`:

Description
-----------

scsi_status - SCSI Status code returned from target device
scsi_state - state info associated with SCSI_IO determined by ioc
ioc_status - ioc supplied status info

Return nothing.

.. _`_scsih_turn_on_pfa_led`:

_scsih_turn_on_pfa_led
======================

.. c:function:: void _scsih_turn_on_pfa_led(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    illuminate PFA LED

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

.. _`_scsih_turn_on_pfa_led.context`:

Context
-------

process

.. _`_scsih_turn_on_pfa_led.description`:

Description
-----------

Return nothing.

.. _`_scsih_turn_off_pfa_led`:

_scsih_turn_off_pfa_led
=======================

.. c:function:: void _scsih_turn_off_pfa_led(struct MPT3SAS_ADAPTER *ioc, struct _sas_device *sas_device)

    turn off Fault LED

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_device \*sas_device:
        sas device whose PFA LED has to turned off

.. _`_scsih_turn_off_pfa_led.context`:

Context
-------

process

.. _`_scsih_turn_off_pfa_led.description`:

Description
-----------

Return nothing.

.. _`_scsih_send_event_to_turn_on_pfa_led`:

_scsih_send_event_to_turn_on_pfa_led
====================================

.. c:function:: void _scsih_send_event_to_turn_on_pfa_led(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    fire delayed event

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

.. _`_scsih_send_event_to_turn_on_pfa_led.context`:

Context
-------

interrupt.

.. _`_scsih_send_event_to_turn_on_pfa_led.description`:

Description
-----------

Return nothing.

.. _`_scsih_smart_predicted_fault`:

_scsih_smart_predicted_fault
============================

.. c:function:: void _scsih_smart_predicted_fault(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    process smart errors

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle

.. _`_scsih_smart_predicted_fault.context`:

Context
-------

interrupt.

.. _`_scsih_smart_predicted_fault.description`:

Description
-----------

Return nothing.

.. _`_scsih_io_done`:

_scsih_io_done
==============

.. c:function:: u8 _scsih_io_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    scsi request callback

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`_scsih_io_done.description`:

Description
-----------

Callback handler when using \_scsih_qcmd.

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_scsih_sas_host_refresh`:

_scsih_sas_host_refresh
=======================

.. c:function:: void _scsih_sas_host_refresh(struct MPT3SAS_ADAPTER *ioc)

    refreshing sas host object contents

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_sas_host_refresh.context`:

Context
-------

user

.. _`_scsih_sas_host_refresh.description`:

Description
-----------

During port enable, fw will send topology events for every device. Its
possible that the handles may change from the previous setting, so this
code keeping handles updating if changed.

Return nothing.

.. _`_scsih_sas_host_add`:

_scsih_sas_host_add
===================

.. c:function:: void _scsih_sas_host_add(struct MPT3SAS_ADAPTER *ioc)

    create sas host object

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_sas_host_add.description`:

Description
-----------

Creating host side data object, stored in ioc->sas_hba

Return nothing.

.. _`_scsih_expander_add`:

_scsih_expander_add
===================

.. c:function:: int _scsih_expander_add(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    creating expander object

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        expander handle

.. _`_scsih_expander_add.description`:

Description
-----------

Creating expander object, stored in ioc->sas_expander_list.

Return 0 for success, else error.

.. _`mpt3sas_expander_remove`:

mpt3sas_expander_remove
=======================

.. c:function:: void mpt3sas_expander_remove(struct MPT3SAS_ADAPTER *ioc, u64 sas_address)

    removing expander object

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 sas_address:
        expander sas_address

.. _`mpt3sas_expander_remove.description`:

Description
-----------

Return nothing.

.. _`_scsih_done`:

_scsih_done
===========

.. c:function:: u8 _scsih_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    internal SCSI_IO callback handler.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`_scsih_done.description`:

Description
-----------

Callback handler when sending internal generated SCSI_IO.
The callback index passed is \`ioc->scsih_cb_idx\`

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_scsih_check_access_status`:

_scsih_check_access_status
==========================

.. c:function:: u8 _scsih_check_access_status(struct MPT3SAS_ADAPTER *ioc, u64 sas_address, u16 handle, u8 access_status)

    check access flags

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 sas_address:
        sas address

    :param u16 handle:
        sas device handle

    :param u8 access_status:
        *undescribed*

.. _`_scsih_check_access_status.description`:

Description
-----------

Return 0 for success, else failure

.. _`_scsih_check_device`:

_scsih_check_device
===================

.. c:function:: void _scsih_check_device(struct MPT3SAS_ADAPTER *ioc, u64 parent_sas_address, u16 handle, u8 phy_number, u8 link_rate)

    checking device responsiveness

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 parent_sas_address:
        sas address of parent expander or sas host

    :param u16 handle:
        attached device handle

    :param u8 phy_number:
        *undescribed*

    :param u8 link_rate:
        new link rate

.. _`_scsih_check_device.description`:

Description
-----------

Returns nothing.

.. _`_scsih_add_device`:

_scsih_add_device
=================

.. c:function:: int _scsih_add_device(struct MPT3SAS_ADAPTER *ioc, u16 handle, u8 phy_num, u8 is_pd)

    creating sas device object

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        sas device handle

    :param u8 phy_num:
        phy number end device attached to

    :param u8 is_pd:
        is this hidden raid component

.. _`_scsih_add_device.description`:

Description
-----------

Creating end device object, stored in ioc->sas_device_list.

Returns 0 for success, non-zero for failure.

.. _`_scsih_remove_device`:

_scsih_remove_device
====================

.. c:function:: void _scsih_remove_device(struct MPT3SAS_ADAPTER *ioc, struct _sas_device *sas_device)

    removing sas device object

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_device \*sas_device:
        *undescribed*

.. _`_scsih_remove_device.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_topology_change_event_debug`:

_scsih_sas_topology_change_event_debug
======================================

.. c:function:: void _scsih_sas_topology_change_event_debug(struct MPT3SAS_ADAPTER *ioc, Mpi2EventDataSasTopologyChangeList_t *event_data)

    debug for topology event

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventDataSasTopologyChangeList_t \*event_data:
        event data payload

.. _`_scsih_sas_topology_change_event_debug.context`:

Context
-------

user.

.. _`_scsih_sas_topology_change_event`:

_scsih_sas_topology_change_event
================================

.. c:function:: int _scsih_sas_topology_change_event(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    handle topology changes

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        The fw_event_work object

.. _`_scsih_sas_topology_change_event.context`:

Context
-------

user.

.. _`_scsih_sas_device_status_change_event_debug`:

_scsih_sas_device_status_change_event_debug
===========================================

.. c:function:: void _scsih_sas_device_status_change_event_debug(struct MPT3SAS_ADAPTER *ioc, Mpi2EventDataSasDeviceStatusChange_t *event_data)

    debug for device event

    :param struct MPT3SAS_ADAPTER \*ioc:
        *undescribed*

    :param Mpi2EventDataSasDeviceStatusChange_t \*event_data:
        event data payload

.. _`_scsih_sas_device_status_change_event_debug.context`:

Context
-------

user.

.. _`_scsih_sas_device_status_change_event_debug.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_device_status_change_event`:

_scsih_sas_device_status_change_event
=====================================

.. c:function:: void _scsih_sas_device_status_change_event(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    handle device status change

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        The fw_event_work object

.. _`_scsih_sas_device_status_change_event.context`:

Context
-------

user.

.. _`_scsih_sas_device_status_change_event.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_enclosure_dev_status_change_event_debug`:

_scsih_sas_enclosure_dev_status_change_event_debug
==================================================

.. c:function:: void _scsih_sas_enclosure_dev_status_change_event_debug(struct MPT3SAS_ADAPTER *ioc, Mpi2EventDataSasEnclDevStatusChange_t *event_data)

    debug for enclosure event

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventDataSasEnclDevStatusChange_t \*event_data:
        event data payload

.. _`_scsih_sas_enclosure_dev_status_change_event_debug.context`:

Context
-------

user.

.. _`_scsih_sas_enclosure_dev_status_change_event_debug.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_enclosure_dev_status_change_event`:

_scsih_sas_enclosure_dev_status_change_event
============================================

.. c:function:: void _scsih_sas_enclosure_dev_status_change_event(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    handle enclosure events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        The fw_event_work object

.. _`_scsih_sas_enclosure_dev_status_change_event.context`:

Context
-------

user.

.. _`_scsih_sas_enclosure_dev_status_change_event.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_broadcast_primitive_event`:

_scsih_sas_broadcast_primitive_event
====================================

.. c:function:: void _scsih_sas_broadcast_primitive_event(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    handle broadcast events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        The fw_event_work object

.. _`_scsih_sas_broadcast_primitive_event.context`:

Context
-------

user.

.. _`_scsih_sas_broadcast_primitive_event.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_discovery_event`:

_scsih_sas_discovery_event
==========================

.. c:function:: void _scsih_sas_discovery_event(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    handle discovery events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        The fw_event_work object

.. _`_scsih_sas_discovery_event.context`:

Context
-------

user.

.. _`_scsih_sas_discovery_event.description`:

Description
-----------

Return nothing.

.. _`_scsih_ir_fastpath`:

_scsih_ir_fastpath
==================

.. c:function:: int _scsih_ir_fastpath(struct MPT3SAS_ADAPTER *ioc, u16 handle, u8 phys_disk_num)

    turn on fastpath for IR physdisk

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        device handle for physical disk

    :param u8 phys_disk_num:
        physical disk number

.. _`_scsih_ir_fastpath.description`:

Description
-----------

Return 0 for success, else failure.

.. _`_scsih_reprobe_lun`:

_scsih_reprobe_lun
==================

.. c:function:: void _scsih_reprobe_lun(struct scsi_device *sdev, void *no_uld_attach)

    reprobing lun

    :param struct scsi_device \*sdev:
        scsi device struct

    :param void \*no_uld_attach:
        sdev->no_uld_attach flag setting

.. _`_scsih_sas_volume_add`:

_scsih_sas_volume_add
=====================

.. c:function:: void _scsih_sas_volume_add(struct MPT3SAS_ADAPTER *ioc, Mpi2EventIrConfigElement_t *element)

    add new volume

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventIrConfigElement_t \*element:
        IR config element data

.. _`_scsih_sas_volume_add.context`:

Context
-------

user.

.. _`_scsih_sas_volume_add.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_volume_delete`:

_scsih_sas_volume_delete
========================

.. c:function:: void _scsih_sas_volume_delete(struct MPT3SAS_ADAPTER *ioc, u16 handle)

    delete volume

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        volume device handle

.. _`_scsih_sas_volume_delete.context`:

Context
-------

user.

.. _`_scsih_sas_volume_delete.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_pd_expose`:

_scsih_sas_pd_expose
====================

.. c:function:: void _scsih_sas_pd_expose(struct MPT3SAS_ADAPTER *ioc, Mpi2EventIrConfigElement_t *element)

    expose pd component to /dev/sdX

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventIrConfigElement_t \*element:
        IR config element data

.. _`_scsih_sas_pd_expose.context`:

Context
-------

user.

.. _`_scsih_sas_pd_expose.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_pd_hide`:

_scsih_sas_pd_hide
==================

.. c:function:: void _scsih_sas_pd_hide(struct MPT3SAS_ADAPTER *ioc, Mpi2EventIrConfigElement_t *element)

    hide pd component from /dev/sdX

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventIrConfigElement_t \*element:
        IR config element data

.. _`_scsih_sas_pd_hide.context`:

Context
-------

user.

.. _`_scsih_sas_pd_hide.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_pd_delete`:

_scsih_sas_pd_delete
====================

.. c:function:: void _scsih_sas_pd_delete(struct MPT3SAS_ADAPTER *ioc, Mpi2EventIrConfigElement_t *element)

    delete pd component

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventIrConfigElement_t \*element:
        IR config element data

.. _`_scsih_sas_pd_delete.context`:

Context
-------

user.

.. _`_scsih_sas_pd_delete.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_pd_add`:

_scsih_sas_pd_add
=================

.. c:function:: void _scsih_sas_pd_add(struct MPT3SAS_ADAPTER *ioc, Mpi2EventIrConfigElement_t *element)

    remove pd component

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventIrConfigElement_t \*element:
        IR config element data

.. _`_scsih_sas_pd_add.context`:

Context
-------

user.

.. _`_scsih_sas_pd_add.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_ir_config_change_event_debug`:

_scsih_sas_ir_config_change_event_debug
=======================================

.. c:function:: void _scsih_sas_ir_config_change_event_debug(struct MPT3SAS_ADAPTER *ioc, Mpi2EventDataIrConfigChangeList_t *event_data)

    debug for IR Config Change events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventDataIrConfigChangeList_t \*event_data:
        event data payload

.. _`_scsih_sas_ir_config_change_event_debug.context`:

Context
-------

user.

.. _`_scsih_sas_ir_config_change_event_debug.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_ir_config_change_event`:

_scsih_sas_ir_config_change_event
=================================

.. c:function:: void _scsih_sas_ir_config_change_event(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    handle ir configuration change events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        The fw_event_work object

.. _`_scsih_sas_ir_config_change_event.context`:

Context
-------

user.

.. _`_scsih_sas_ir_config_change_event.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_ir_volume_event`:

_scsih_sas_ir_volume_event
==========================

.. c:function:: void _scsih_sas_ir_volume_event(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    IR volume event

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        The fw_event_work object

.. _`_scsih_sas_ir_volume_event.context`:

Context
-------

user.

.. _`_scsih_sas_ir_volume_event.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_ir_physical_disk_event`:

_scsih_sas_ir_physical_disk_event
=================================

.. c:function:: void _scsih_sas_ir_physical_disk_event(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    PD event

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        The fw_event_work object

.. _`_scsih_sas_ir_physical_disk_event.context`:

Context
-------

user.

.. _`_scsih_sas_ir_physical_disk_event.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_ir_operation_status_event_debug`:

_scsih_sas_ir_operation_status_event_debug
==========================================

.. c:function:: void _scsih_sas_ir_operation_status_event_debug(struct MPT3SAS_ADAPTER *ioc, Mpi2EventDataIrOperationStatus_t *event_data)

    debug for IR op event

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2EventDataIrOperationStatus_t \*event_data:
        event data payload

.. _`_scsih_sas_ir_operation_status_event_debug.context`:

Context
-------

user.

.. _`_scsih_sas_ir_operation_status_event_debug.description`:

Description
-----------

Return nothing.

.. _`_scsih_sas_ir_operation_status_event`:

_scsih_sas_ir_operation_status_event
====================================

.. c:function:: void _scsih_sas_ir_operation_status_event(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    handle RAID operation events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        The fw_event_work object

.. _`_scsih_sas_ir_operation_status_event.context`:

Context
-------

user.

.. _`_scsih_sas_ir_operation_status_event.description`:

Description
-----------

Return nothing.

.. _`_scsih_prep_device_scan`:

_scsih_prep_device_scan
=======================

.. c:function:: void _scsih_prep_device_scan(struct MPT3SAS_ADAPTER *ioc)

    initialize parameters prior to device scan

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_prep_device_scan.description`:

Description
-----------

Set the deleted flag prior to device scan.  If the device is found during
the scan, then we clear the deleted flag.

.. _`_scsih_mark_responding_sas_device`:

_scsih_mark_responding_sas_device
=================================

.. c:function:: void _scsih_mark_responding_sas_device(struct MPT3SAS_ADAPTER *ioc, Mpi2SasDevicePage0_t *sas_device_pg0)

    mark a sas_devices as responding

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2SasDevicePage0_t \*sas_device_pg0:
        SAS Device page 0

.. _`_scsih_mark_responding_sas_device.description`:

Description
-----------

After host reset, find out whether devices are still responding.
Used in \_scsih_remove_unresponsive_sas_devices.

Return nothing.

.. _`_scsih_search_responding_sas_devices`:

_scsih_search_responding_sas_devices
====================================

.. c:function:: void _scsih_search_responding_sas_devices(struct MPT3SAS_ADAPTER *ioc)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_search_responding_sas_devices.description`:

Description
-----------

After host reset, find out whether devices are still responding.
If not remove.

Return nothing.

.. _`_scsih_mark_responding_raid_device`:

_scsih_mark_responding_raid_device
==================================

.. c:function:: void _scsih_mark_responding_raid_device(struct MPT3SAS_ADAPTER *ioc, u64 wwid, u16 handle)

    mark a raid_device as responding

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 wwid:
        world wide identifier for raid volume

    :param u16 handle:
        device handle

.. _`_scsih_mark_responding_raid_device.description`:

Description
-----------

After host reset, find out whether devices are still responding.
Used in \_scsih_remove_unresponsive_raid_devices.

Return nothing.

.. _`_scsih_search_responding_raid_devices`:

_scsih_search_responding_raid_devices
=====================================

.. c:function:: void _scsih_search_responding_raid_devices(struct MPT3SAS_ADAPTER *ioc)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_search_responding_raid_devices.description`:

Description
-----------

After host reset, find out whether devices are still responding.
If not remove.

Return nothing.

.. _`_scsih_mark_responding_expander`:

_scsih_mark_responding_expander
===============================

.. c:function:: void _scsih_mark_responding_expander(struct MPT3SAS_ADAPTER *ioc, u64 sas_address, u16 handle)

    mark a expander as responding

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u64 sas_address:
        sas address

    :param u16 handle:
        *undescribed*

.. _`_scsih_mark_responding_expander.description`:

Description
-----------

After host reset, find out whether devices are still responding.
Used in \_scsih_remove_unresponsive_expanders.

Return nothing.

.. _`_scsih_search_responding_expanders`:

_scsih_search_responding_expanders
==================================

.. c:function:: void _scsih_search_responding_expanders(struct MPT3SAS_ADAPTER *ioc)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_search_responding_expanders.description`:

Description
-----------

After host reset, find out whether devices are still responding.
If not remove.

Return nothing.

.. _`_scsih_remove_unresponding_sas_devices`:

_scsih_remove_unresponding_sas_devices
======================================

.. c:function:: void _scsih_remove_unresponding_sas_devices(struct MPT3SAS_ADAPTER *ioc)

    removing unresponding devices

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_remove_unresponding_sas_devices.description`:

Description
-----------

Return nothing.

.. _`_scsih_scan_for_devices_after_reset`:

_scsih_scan_for_devices_after_reset
===================================

.. c:function:: void _scsih_scan_for_devices_after_reset(struct MPT3SAS_ADAPTER *ioc)

    scan for devices after host reset

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_scan_for_devices_after_reset.description`:

Description
-----------

Return nothing.

.. _`mpt3sas_scsih_reset_handler`:

mpt3sas_scsih_reset_handler
===========================

.. c:function:: void mpt3sas_scsih_reset_handler(struct MPT3SAS_ADAPTER *ioc, int reset_phase)

    reset callback handler (for scsih)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param int reset_phase:
        phase

.. _`mpt3sas_scsih_reset_handler.description`:

Description
-----------

The handler for doing any required cleanup or initialization.

The reset phase can be MPT3_IOC_PRE_RESET, MPT3_IOC_AFTER_RESET,
MPT3_IOC_DONE_RESET

Return nothing.

.. _`_mpt3sas_fw_work`:

_mpt3sas_fw_work
================

.. c:function:: void _mpt3sas_fw_work(struct MPT3SAS_ADAPTER *ioc, struct fw_event_work *fw_event)

    delayed task for processing firmware events

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct fw_event_work \*fw_event:
        The fw_event_work object

.. _`_mpt3sas_fw_work.context`:

Context
-------

user.

.. _`_mpt3sas_fw_work.description`:

Description
-----------

Return nothing.

.. _`_firmware_event_work`:

_firmware_event_work
====================

.. c:function:: void _firmware_event_work(struct work_struct *work)

    :param struct work_struct \*work:
        The fw_event_work object

.. _`_firmware_event_work.context`:

Context
-------

user.

.. _`_firmware_event_work.description`:

Description
-----------

wrappers for the work thread handling firmware events

Return nothing.

.. _`mpt3sas_scsih_event_callback`:

mpt3sas_scsih_event_callback
============================

.. c:function:: u8 mpt3sas_scsih_event_callback(struct MPT3SAS_ADAPTER *ioc, u8 msix_index, u32 reply)

    firmware event handler (called at ISR time)

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`mpt3sas_scsih_event_callback.context`:

Context
-------

interrupt.

.. _`mpt3sas_scsih_event_callback.description`:

Description
-----------

This function merely adds a new work task into ioc->firmware_event_thread.
The tasks are worked from \_firmware_event_work in user context.

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_scsih_expander_node_remove`:

_scsih_expander_node_remove
===========================

.. c:function:: void _scsih_expander_node_remove(struct MPT3SAS_ADAPTER *ioc, struct _sas_node *sas_expander)

    removing expander device from list.

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct _sas_node \*sas_expander:
        the sas_device object

.. _`_scsih_expander_node_remove.context`:

Context
-------

Calling function should acquire ioc->sas_node_lock.

.. _`_scsih_expander_node_remove.description`:

Description
-----------

Removing object and freeing associated memory from the
ioc->sas_expander_list.

Return nothing.

.. _`_scsih_ir_shutdown`:

_scsih_ir_shutdown
==================

.. c:function:: void _scsih_ir_shutdown(struct MPT3SAS_ADAPTER *ioc)

    IR shutdown notification

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_ir_shutdown.description`:

Description
-----------

Sending RAID Action to alert the Integrated RAID subsystem of the IOC that
the host system is shutting down.

Return nothing.

.. _`scsih_remove`:

scsih_remove
============

.. c:function:: void scsih_remove(struct pci_dev *pdev)

    detach and remove add host

    :param struct pci_dev \*pdev:
        PCI device struct

.. _`scsih_remove.description`:

Description
-----------

Routine called when unloading the driver.
Return nothing.

.. _`scsih_shutdown`:

scsih_shutdown
==============

.. c:function:: void scsih_shutdown(struct pci_dev *pdev)

    routine call during system shutdown

    :param struct pci_dev \*pdev:
        PCI device struct

.. _`scsih_shutdown.description`:

Description
-----------

Return nothing.

.. _`_scsih_probe_boot_devices`:

_scsih_probe_boot_devices
=========================

.. c:function:: void _scsih_probe_boot_devices(struct MPT3SAS_ADAPTER *ioc)

    reports 1st device

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_probe_boot_devices.description`:

Description
-----------

If specified in bios page 2, this routine reports the 1st
device scsi-ml or sas transport for persistent boot device
purposes.  Please refer to function \_scsih_determine_boot_device()

.. _`_scsih_probe_raid`:

_scsih_probe_raid
=================

.. c:function:: void _scsih_probe_raid(struct MPT3SAS_ADAPTER *ioc)

    reporting raid volumes to scsi-ml

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_probe_raid.description`:

Description
-----------

Called during initial loading of the driver.

.. _`_scsih_probe_sas`:

_scsih_probe_sas
================

.. c:function:: void _scsih_probe_sas(struct MPT3SAS_ADAPTER *ioc)

    reporting sas devices to sas transport

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_probe_sas.description`:

Description
-----------

Called during initial loading of the driver.

.. _`_scsih_probe_devices`:

_scsih_probe_devices
====================

.. c:function:: void _scsih_probe_devices(struct MPT3SAS_ADAPTER *ioc)

    probing for devices

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

.. _`_scsih_probe_devices.description`:

Description
-----------

Called during initial loading of the driver.

.. _`scsih_scan_start`:

scsih_scan_start
================

.. c:function:: void scsih_scan_start(struct Scsi_Host *shost)

    scsi lld callback for .scan_start

    :param struct Scsi_Host \*shost:
        SCSI host pointer

.. _`scsih_scan_start.description`:

Description
-----------

The shost has the ability to discover targets on its own instead
of scanning the entire bus.  In our implemention, we will kick off
firmware discovery.

.. _`scsih_scan_finished`:

scsih_scan_finished
===================

.. c:function:: int scsih_scan_finished(struct Scsi_Host *shost, unsigned long time)

    scsi lld callback for .scan_finished

    :param struct Scsi_Host \*shost:
        SCSI host pointer

    :param unsigned long time:
        elapsed time of the scan in jiffies

.. _`scsih_scan_finished.description`:

Description
-----------

This function will be called periodicallyn until it returns 1 with the
scsi_host and the elapsed time of the scan in jiffies. In our implemention,
we wait for firmware discovery to complete, then return 1.

.. _`_scsih_determine_hba_mpi_version`:

_scsih_determine_hba_mpi_version
================================

.. c:function:: u16 _scsih_determine_hba_mpi_version(struct pci_dev *pdev)

    determine in which MPI version class this device belongs to.

    :param struct pci_dev \*pdev:
        PCI device struct

.. _`_scsih_determine_hba_mpi_version.description`:

Description
-----------

return MPI2_VERSION for SAS 2.0 HBA devices,
MPI25_VERSION for SAS 3.0 HBA devices, and
MPI26 VERSION for Cutlass & Invader SAS 3.0 HBA devices

.. _`_scsih_probe`:

_scsih_probe
============

.. c:function:: int _scsih_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    attach and add scsi host

    :param struct pci_dev \*pdev:
        PCI device struct

    :param const struct pci_device_id \*id:
        pci device id

.. _`_scsih_probe.description`:

Description
-----------

Returns 0 success, anything else error.

.. _`scsih_suspend`:

scsih_suspend
=============

.. c:function:: int scsih_suspend(struct pci_dev *pdev, pm_message_t state)

    power management suspend main entry point

    :param struct pci_dev \*pdev:
        PCI device struct

    :param pm_message_t state:
        PM state change to (usually PCI_D3)

.. _`scsih_suspend.description`:

Description
-----------

Returns 0 success, anything else error.

.. _`scsih_resume`:

scsih_resume
============

.. c:function:: int scsih_resume(struct pci_dev *pdev)

    power management resume main entry point

    :param struct pci_dev \*pdev:
        PCI device struct

.. _`scsih_resume.description`:

Description
-----------

Returns 0 success, anything else error.

.. _`scsih_pci_error_detected`:

scsih_pci_error_detected
========================

.. c:function:: pci_ers_result_t scsih_pci_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    Called when a PCI error is detected.

    :param struct pci_dev \*pdev:
        PCI device struct

    :param pci_channel_state_t state:
        PCI channel state

.. _`scsih_pci_error_detected.description`:

Description
-----------

Called when a PCI error is detected.

.. _`scsih_pci_error_detected.return-value`:

Return value
------------

PCI_ERS_RESULT_NEED_RESET or PCI_ERS_RESULT_DISCONNECT

.. _`scsih_pci_slot_reset`:

scsih_pci_slot_reset
====================

.. c:function:: pci_ers_result_t scsih_pci_slot_reset(struct pci_dev *pdev)

    Called when PCI slot has been reset.

    :param struct pci_dev \*pdev:
        PCI device struct

.. _`scsih_pci_slot_reset.description`:

Description
-----------

This routine is called by the pci error recovery
code after the PCI slot has been reset, just before we
should resume normal operations.

.. _`scsih_pci_resume`:

scsih_pci_resume
================

.. c:function:: void scsih_pci_resume(struct pci_dev *pdev)

    resume normal ops after PCI reset

    :param struct pci_dev \*pdev:
        pointer to PCI device

.. _`scsih_pci_resume.description`:

Description
-----------

Called when the error recovery driver tells us that its
OK to resume normal operation. Use completion to allow
halted scsi ops to resume.

.. _`scsih_pci_mmio_enabled`:

scsih_pci_mmio_enabled
======================

.. c:function:: pci_ers_result_t scsih_pci_mmio_enabled(struct pci_dev *pdev)

    Enable MMIO and dump debug registers

    :param struct pci_dev \*pdev:
        pointer to PCI device

.. _`scsih_init`:

scsih_init
==========

.. c:function:: int scsih_init( void)

    main entry point for this driver.

    :param  void:
        no arguments

.. _`scsih_init.description`:

Description
-----------

Returns 0 success, anything else error.

.. _`scsih_exit`:

scsih_exit
==========

.. c:function:: void scsih_exit( void)

    exit point for this driver (when it is a module).

    :param  void:
        no arguments

.. _`scsih_exit.description`:

Description
-----------

Returns 0 success, anything else error.

.. _`_mpt3sas_init`:

_mpt3sas_init
=============

.. c:function:: int _mpt3sas_init( void)

    main entry point for this driver.

    :param  void:
        no arguments

.. _`_mpt3sas_init.description`:

Description
-----------

Returns 0 success, anything else error.

.. _`_mpt3sas_exit`:

_mpt3sas_exit
=============

.. c:function:: void __exit _mpt3sas_exit( void)

    exit point for this driver (when it is a module).

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

