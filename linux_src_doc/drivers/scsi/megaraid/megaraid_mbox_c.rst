.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/megaraid/megaraid_mbox.c

.. _`megaraid_init`:

megaraid_init
=============

.. c:function:: int megaraid_init( void)

    module load hook

    :param  void:
        no arguments

.. _`megaraid_init.description`:

Description
-----------

We register ourselves as hotplug enabled module and let PCI subsystem
discover our adapters.

.. _`megaraid_exit`:

megaraid_exit
=============

.. c:function:: void __exit megaraid_exit( void)

    driver unload entry point

    :param  void:
        no arguments

.. _`megaraid_exit.description`:

Description
-----------

We simply unwrap the megaraid_init routine here.

.. _`megaraid_probe_one`:

megaraid_probe_one
==================

.. c:function:: int megaraid_probe_one(struct pci_dev *pdev, const struct pci_device_id *id)

    PCI hotplug entry point

    :param struct pci_dev \*pdev:
        handle to this controller's PCI configuration space

    :param const struct pci_device_id \*id:
        pci device id of the class of controllers

.. _`megaraid_probe_one.description`:

Description
-----------

This routine should be called whenever a new adapter is detected by the
PCI hotplug susbsystem.

.. _`megaraid_detach_one`:

megaraid_detach_one
===================

.. c:function:: void megaraid_detach_one(struct pci_dev *pdev)

    release framework resources and call LLD release routine

    :param struct pci_dev \*pdev:
        handle for our PCI configuration space

.. _`megaraid_detach_one.description`:

Description
-----------

This routine is called during driver unload. We free all the allocated
resources and call the corresponding LLD so that it can also release all
its resources.

This routine is also called from the PCI hotplug system.

.. _`megaraid_mbox_shutdown`:

megaraid_mbox_shutdown
======================

.. c:function:: void megaraid_mbox_shutdown(struct pci_dev *pdev)

    PCI shutdown for megaraid HBA

    :param struct pci_dev \*pdev:
        generic driver model device

.. _`megaraid_mbox_shutdown.description`:

Description
-----------

Shutdown notification, perform flush cache.

.. _`megaraid_io_attach`:

megaraid_io_attach
==================

.. c:function:: int megaraid_io_attach(adapter_t *adapter)

    attach a device with the IO subsystem

    :param adapter_t \*adapter:
        controller's soft state

.. _`megaraid_io_attach.description`:

Description
-----------

Attach this device with the IO subsystem.

.. _`megaraid_io_detach`:

megaraid_io_detach
==================

.. c:function:: void megaraid_io_detach(adapter_t *adapter)

    detach a device from the IO subsystem

    :param adapter_t \*adapter:
        controller's soft state

.. _`megaraid_io_detach.description`:

Description
-----------

Detach this device from the IO subsystem.

.. _`megaraid_init_mbox`:

megaraid_init_mbox
==================

.. c:function:: int megaraid_init_mbox(adapter_t *adapter)

    initialize controller

    :param adapter_t \*adapter:
        our soft state

.. _`megaraid_init_mbox.description`:

Description
-----------

- Allocate 16-byte aligned mailbox memory for firmware handshake
- Allocate controller's memory resources
- Find out all initialization data
- Allocate memory required for all the commands
- Use internal library of FW routines, build up complete soft state

.. _`megaraid_fini_mbox`:

megaraid_fini_mbox
==================

.. c:function:: void megaraid_fini_mbox(adapter_t *adapter)

    undo controller initialization

    :param adapter_t \*adapter:
        our soft state

.. _`megaraid_alloc_cmd_packets`:

megaraid_alloc_cmd_packets
==========================

.. c:function:: int megaraid_alloc_cmd_packets(adapter_t *adapter)

    allocate shared mailbox

    :param adapter_t \*adapter:
        soft state of the raid controller

.. _`megaraid_alloc_cmd_packets.description`:

Description
-----------

Allocate and align the shared mailbox. This maibox is used to issue
all the commands. For IO based controllers, the mailbox is also registered
with the FW. Allocate memory for all commands as well.
This is our big allocator.

.. _`megaraid_free_cmd_packets`:

megaraid_free_cmd_packets
=========================

.. c:function:: void megaraid_free_cmd_packets(adapter_t *adapter)

    free memory

    :param adapter_t \*adapter:
        soft state of the raid controller

.. _`megaraid_free_cmd_packets.description`:

Description
-----------

Release memory resources allocated for commands.

.. _`megaraid_mbox_setup_dma_pools`:

megaraid_mbox_setup_dma_pools
=============================

.. c:function:: int megaraid_mbox_setup_dma_pools(adapter_t *adapter)

    setup dma pool for command packets

    :param adapter_t \*adapter:
        HBA soft state

.. _`megaraid_mbox_setup_dma_pools.description`:

Description
-----------

Setup the dma pools for mailbox, passthru and extended passthru structures,
and scatter-gather lists.

.. _`megaraid_mbox_teardown_dma_pools`:

megaraid_mbox_teardown_dma_pools
================================

.. c:function:: void megaraid_mbox_teardown_dma_pools(adapter_t *adapter)

    teardown dma pools for command packets

    :param adapter_t \*adapter:
        HBA soft state

.. _`megaraid_mbox_teardown_dma_pools.description`:

Description
-----------

Teardown the dma pool for mailbox, passthru and extended passthru
structures, and scatter-gather lists.

.. _`megaraid_alloc_scb`:

megaraid_alloc_scb
==================

.. c:function:: scb_t *megaraid_alloc_scb(adapter_t *adapter, struct scsi_cmnd *scp)

    detach and return a scb from the free list

    :param adapter_t \*adapter:
        controller's soft state

    :param struct scsi_cmnd \*scp:
        pointer to the scsi command to be executed

.. _`megaraid_alloc_scb.description`:

Description
-----------

Return the scb from the head of the free list. \ ``NULL``\  if there are none
available.

.. _`megaraid_dealloc_scb`:

megaraid_dealloc_scb
====================

.. c:function:: void megaraid_dealloc_scb(adapter_t *adapter, scb_t *scb)

    return the scb to the free pool

    :param adapter_t \*adapter:
        controller's soft state

    :param scb_t \*scb:
        scb to be freed

.. _`megaraid_dealloc_scb.description`:

Description
-----------

Return the scb back to the free list of scbs. The caller must 'flush' the
SCB before calling us. E.g., performing pci_unamp and/or pci_sync etc.

.. _`megaraid_dealloc_scb.note-note`:

NOTE NOTE
---------

Make sure the scb is not on any list before calling this
routine.

.. _`megaraid_mbox_mksgl`:

megaraid_mbox_mksgl
===================

.. c:function:: int megaraid_mbox_mksgl(adapter_t *adapter, scb_t *scb)

    make the scatter-gather list

    :param adapter_t \*adapter:
        controller's soft state

    :param scb_t \*scb:
        scsi control block

.. _`megaraid_mbox_mksgl.description`:

Description
-----------

Prepare the scatter-gather list.

.. _`mbox_post_cmd`:

mbox_post_cmd
=============

.. c:function:: int mbox_post_cmd(adapter_t *adapter, scb_t *scb)

    issue a mailbox command

    :param adapter_t \*adapter:
        controller's soft state

    :param scb_t \*scb:
        command to be issued

.. _`mbox_post_cmd.description`:

Description
-----------

Post the command to the controller if mailbox is available.

.. _`megaraid_queue_command_lck`:

megaraid_queue_command_lck
==========================

.. c:function:: int megaraid_queue_command_lck(struct scsi_cmnd *scp, void (*done)(struct scsi_cmnd *))

    generic queue entry point for all LLDs

    :param struct scsi_cmnd \*scp:
        pointer to the scsi command to be executed

    :param void (\*done)(struct scsi_cmnd \*):
        callback routine to be called after the cmd has be completed

.. _`megaraid_queue_command_lck.description`:

Description
-----------

Queue entry point for mailbox based controllers.

.. _`megaraid_mbox_build_cmd`:

megaraid_mbox_build_cmd
=======================

.. c:function:: scb_t *megaraid_mbox_build_cmd(adapter_t *adapter, struct scsi_cmnd *scp, int *busy)

    transform the mid-layer scsi commands

    :param adapter_t \*adapter:
        controller's soft state

    :param struct scsi_cmnd \*scp:
        mid-layer scsi command pointer

    :param int \*busy:
        set if request could not be completed because of lack of
        resources

.. _`megaraid_mbox_build_cmd.description`:

Description
-----------

Transform the mid-layer scsi command to megaraid firmware lingua.
Convert the command issued by mid-layer to format understood by megaraid
firmware. We also complete certain commands without sending them to firmware.

.. _`megaraid_mbox_runpendq`:

megaraid_mbox_runpendq
======================

.. c:function:: void megaraid_mbox_runpendq(adapter_t *adapter, scb_t *scb_q)

    execute commands queued in the pending queue

    :param adapter_t \*adapter:
        controller's soft state

    :param scb_t \*scb_q:
        SCB to be queued in the pending list

.. _`megaraid_mbox_runpendq.description`:

Description
-----------

Scan the pending list for commands which are not yet issued and try to
post to the controller. The SCB can be a null pointer, which would indicate
no SCB to be queue, just try to execute the ones in the pending list.

.. _`megaraid_mbox_runpendq.note`:

NOTE
----

We do not actually traverse the pending list. The SCBs are plucked
out from the head of the pending list. If it is successfully issued, the
next SCB is at the head now.

.. _`megaraid_mbox_prepare_pthru`:

megaraid_mbox_prepare_pthru
===========================

.. c:function:: void megaraid_mbox_prepare_pthru(adapter_t *adapter, scb_t *scb, struct scsi_cmnd *scp)

    prepare a command for physical devices

    :param adapter_t \*adapter:
        pointer to controller's soft state

    :param scb_t \*scb:
        scsi control block

    :param struct scsi_cmnd \*scp:
        scsi command from the mid-layer

.. _`megaraid_mbox_prepare_pthru.description`:

Description
-----------

Prepare a command for the scsi physical devices.

.. _`megaraid_mbox_prepare_epthru`:

megaraid_mbox_prepare_epthru
============================

.. c:function:: void megaraid_mbox_prepare_epthru(adapter_t *adapter, scb_t *scb, struct scsi_cmnd *scp)

    prepare a command for physical devices

    :param adapter_t \*adapter:
        pointer to controller's soft state

    :param scb_t \*scb:
        scsi control block

    :param struct scsi_cmnd \*scp:
        scsi command from the mid-layer

.. _`megaraid_mbox_prepare_epthru.description`:

Description
-----------

Prepare a command for the scsi physical devices. This routine prepares
commands for devices which can take extended CDBs (>10 bytes).

.. _`megaraid_ack_sequence`:

megaraid_ack_sequence
=====================

.. c:function:: int megaraid_ack_sequence(adapter_t *adapter)

    interrupt ack sequence for memory mapped HBAs

    :param adapter_t \*adapter:
        controller's soft state

.. _`megaraid_ack_sequence.description`:

Description
-----------

Interrupt acknowledgement sequence for memory mapped HBAs. Find out the
completed command and put them on the completed list for later processing.

.. _`megaraid_ack_sequence.return`:

Return
------

1 if the interrupt is valid, 0 otherwise

.. _`megaraid_isr`:

megaraid_isr
============

.. c:function:: irqreturn_t megaraid_isr(int irq, void *devp)

    isr for memory based mailbox based controllers

    :param int irq:
        irq

    :param void \*devp:
        pointer to our soft state

.. _`megaraid_isr.description`:

Description
-----------

Interrupt service routine for memory-mapped mailbox controllers.

.. _`megaraid_mbox_sync_scb`:

megaraid_mbox_sync_scb
======================

.. c:function:: void megaraid_mbox_sync_scb(adapter_t *adapter, scb_t *scb)

    sync kernel buffers

    :param adapter_t \*adapter:
        controller's soft state

    :param scb_t \*scb:
        pointer to the resource packet

.. _`megaraid_mbox_sync_scb.description`:

Description
-----------

DMA sync if required.

.. _`megaraid_mbox_dpc`:

megaraid_mbox_dpc
=================

.. c:function:: void megaraid_mbox_dpc(unsigned long devp)

    the tasklet to complete the commands from completed list

    :param unsigned long devp:
        pointer to HBA soft state

.. _`megaraid_mbox_dpc.description`:

Description
-----------

Pick up the commands from the completed list and send back to the owners.
This is a reentrant function and does not assume any locks are held while
it is being called.

.. _`megaraid_abort_handler`:

megaraid_abort_handler
======================

.. c:function:: int megaraid_abort_handler(struct scsi_cmnd *scp)

    abort the scsi command

    :param struct scsi_cmnd \*scp:
        command to be aborted

.. _`megaraid_abort_handler.description`:

Description
-----------

Abort a previous SCSI request. Only commands on the pending list can be
aborted. All the commands issued to the F/W must complete.

.. _`megaraid_reset_handler`:

megaraid_reset_handler
======================

.. c:function:: int megaraid_reset_handler(struct scsi_cmnd *scp)

    device reset handler for mailbox based driver

    :param struct scsi_cmnd \*scp:
        reference command

.. _`megaraid_reset_handler.description`:

Description
-----------

Reset handler for the mailbox based controller. First try to find out if
the FW is still live, in which case the outstanding commands counter mut go
down to 0. If that happens, also issue the reservation reset command to
relinquish (possible) reservations on the logical drives connected to this
host.

.. _`mbox_post_sync_cmd`:

mbox_post_sync_cmd
==================

.. c:function:: int mbox_post_sync_cmd(adapter_t *adapter, uint8_t raw_mbox)

    blocking command to the mailbox based controllers

    :param adapter_t \*adapter:
        controller's soft state

    :param uint8_t raw_mbox:
        the mailbox

.. _`mbox_post_sync_cmd.description`:

Description
-----------

Issue a scb in synchronous and non-interrupt mode for mailbox based
controllers.

.. _`mbox_post_sync_cmd_fast`:

mbox_post_sync_cmd_fast
=======================

.. c:function:: int mbox_post_sync_cmd_fast(adapter_t *adapter, uint8_t raw_mbox)

    blocking command to the mailbox based controllers

    :param adapter_t \*adapter:
        controller's soft state

    :param uint8_t raw_mbox:
        the mailbox

.. _`mbox_post_sync_cmd_fast.description`:

Description
-----------

Issue a scb in synchronous and non-interrupt mode for mailbox based
controllers. This is a faster version of the synchronous command and
therefore can be called in interrupt-context as well.

.. _`megaraid_busywait_mbox`:

megaraid_busywait_mbox
======================

.. c:function:: int megaraid_busywait_mbox(mraid_device_t *raid_dev)

    Wait until the controller's mailbox is available

    :param mraid_device_t \*raid_dev:
        RAID device (HBA) soft state

.. _`megaraid_busywait_mbox.description`:

Description
-----------

Wait until the controller's mailbox is available to accept more commands.
Wait for at most 1 second.

.. _`megaraid_mbox_product_info`:

megaraid_mbox_product_info
==========================

.. c:function:: int megaraid_mbox_product_info(adapter_t *adapter)

    some static information about the controller

    :param adapter_t \*adapter:
        our soft state

.. _`megaraid_mbox_product_info.description`:

Description
-----------

Issue commands to the controller to grab some parameters required by our
caller.

.. _`megaraid_mbox_extended_cdb`:

megaraid_mbox_extended_cdb
==========================

.. c:function:: int megaraid_mbox_extended_cdb(adapter_t *adapter)

    check for support for extended CDBs

    :param adapter_t \*adapter:
        soft state for the controller

.. _`megaraid_mbox_extended_cdb.description`:

Description
-----------

This routine check whether the controller in question supports extended
( > 10 bytes ) CDBs.

.. _`megaraid_mbox_support_ha`:

megaraid_mbox_support_ha
========================

.. c:function:: int megaraid_mbox_support_ha(adapter_t *adapter, uint16_t *init_id)

    Do we support clustering

    :param adapter_t \*adapter:
        soft state for the controller

    :param uint16_t \*init_id:
        ID of the initiator

.. _`megaraid_mbox_support_ha.description`:

Description
-----------

Determine if the firmware supports clustering and the ID of the initiator.

.. _`megaraid_mbox_support_random_del`:

megaraid_mbox_support_random_del
================================

.. c:function:: int megaraid_mbox_support_random_del(adapter_t *adapter)

    Do we support random deletion

    :param adapter_t \*adapter:
        soft state for the controller

.. _`megaraid_mbox_support_random_del.description`:

Description
-----------

Determine if the firmware supports random deletion.

.. _`megaraid_mbox_support_random_del.return`:

Return
------

1 is operation supported, 0 otherwise

.. _`megaraid_mbox_get_max_sg`:

megaraid_mbox_get_max_sg
========================

.. c:function:: int megaraid_mbox_get_max_sg(adapter_t *adapter)

    maximum sg elements supported by the firmware

    :param adapter_t \*adapter:
        soft state for the controller

.. _`megaraid_mbox_get_max_sg.description`:

Description
-----------

Find out the maximum number of scatter-gather elements supported by the
firmware.

.. _`megaraid_mbox_enum_raid_scsi`:

megaraid_mbox_enum_raid_scsi
============================

.. c:function:: void megaraid_mbox_enum_raid_scsi(adapter_t *adapter)

    enumerate the RAID and SCSI channels

    :param adapter_t \*adapter:
        soft state for the controller

.. _`megaraid_mbox_enum_raid_scsi.description`:

Description
-----------

Enumerate the RAID and SCSI channels for ROMB platforms so that channels
can be exported as regular SCSI channels.

.. _`megaraid_mbox_flush_cache`:

megaraid_mbox_flush_cache
=========================

.. c:function:: void megaraid_mbox_flush_cache(adapter_t *adapter)

    flush adapter and disks cache

    :param adapter_t \*adapter:
        soft state for the controller

.. _`megaraid_mbox_flush_cache.description`:

Description
-----------

Flush adapter cache followed by disks cache.

.. _`megaraid_mbox_fire_sync_cmd`:

megaraid_mbox_fire_sync_cmd
===========================

.. c:function:: int megaraid_mbox_fire_sync_cmd(adapter_t *adapter)

    fire the sync cmd

    :param adapter_t \*adapter:
        soft state for the controller

.. _`megaraid_mbox_fire_sync_cmd.description`:

Description
-----------

Clears the pending cmds in FW and reinits its RAID structs.

.. _`megaraid_mbox_display_scb`:

megaraid_mbox_display_scb
=========================

.. c:function:: void megaraid_mbox_display_scb(adapter_t *adapter, scb_t *scb)

    display SCB information, mostly debug purposes

    :param adapter_t \*adapter:
        controller's soft state

    :param scb_t \*scb:
        SCB to be displayed

.. _`megaraid_mbox_display_scb.description`:

Description
-----------

Diplay information about the given SCB iff the current debug level is
verbose.

.. _`megaraid_mbox_setup_device_map`:

megaraid_mbox_setup_device_map
==============================

.. c:function:: void megaraid_mbox_setup_device_map(adapter_t *adapter)

    manage device ids

    :param adapter_t \*adapter:
        Driver's soft state

.. _`megaraid_mbox_setup_device_map.description`:

Description
-----------

Manage the device ids to have an appropriate mapping between the kernel
scsi addresses and megaraid scsi and logical drive addresses. We export
scsi devices on their actual addresses, whereas the logical drives are
exported on a virtual scsi channel.

.. _`megaraid_cmm_register`:

megaraid_cmm_register
=====================

.. c:function:: int megaraid_cmm_register(adapter_t *adapter)

    register with the management module

    :param adapter_t \*adapter:
        HBA soft state

.. _`megaraid_cmm_register.description`:

Description
-----------

Register with the management module, which allows applications to issue
ioctl calls to the drivers. This interface is used by the management module
to setup sysfs support as well.

.. _`megaraid_cmm_unregister`:

megaraid_cmm_unregister
=======================

.. c:function:: int megaraid_cmm_unregister(adapter_t *adapter)

    un-register with the management module

    :param adapter_t \*adapter:
        HBA soft state

.. _`megaraid_cmm_unregister.description`:

Description
-----------

Un-register with the management module.

.. _`megaraid_cmm_unregister.fixme`:

FIXME
-----

mgmt module must return failure for unregister if it has pending
commands in LLD.

.. _`megaraid_mbox_mm_handler`:

megaraid_mbox_mm_handler
========================

.. c:function:: int megaraid_mbox_mm_handler(unsigned long drvr_data, uioc_t *kioc, uint32_t action)

    interface for CMM to issue commands to LLD

    :param unsigned long drvr_data:
        LLD specific data

    :param uioc_t \*kioc:
        CMM interface packet

    :param uint32_t action:
        command action

.. _`megaraid_mbox_mm_handler.description`:

Description
-----------

This routine is invoked whenever the Common Management Module (CMM) has a
command for us. The 'action' parameter specifies if this is a new command
or otherwise.

.. _`megaraid_mbox_mm_command`:

megaraid_mbox_mm_command
========================

.. c:function:: int megaraid_mbox_mm_command(adapter_t *adapter, uioc_t *kioc)

    issues commands routed through CMM

    :param adapter_t \*adapter:
        HBA soft state

    :param uioc_t \*kioc:
        management command packet

.. _`megaraid_mbox_mm_command.description`:

Description
-----------

Issues commands, which are routed through the management module.

.. _`megaraid_mbox_mm_done`:

megaraid_mbox_mm_done
=====================

.. c:function:: void megaraid_mbox_mm_done(adapter_t *adapter, scb_t *scb)

    callback for CMM commands

    :param adapter_t \*adapter:
        HBA soft state

    :param scb_t \*scb:
        completed command

.. _`megaraid_mbox_mm_done.description`:

Description
-----------

Callback routine for internal commands originated from the management
module.

.. _`gather_hbainfo`:

gather_hbainfo
==============

.. c:function:: int gather_hbainfo(adapter_t *adapter, mraid_hba_info_t *hinfo)

    HBA characteristics for the applications

    :param adapter_t \*adapter:
        HBA soft state

    :param mraid_hba_info_t \*hinfo:
        pointer to the caller's host info strucuture

.. _`megaraid_sysfs_alloc_resources`:

megaraid_sysfs_alloc_resources
==============================

.. c:function:: int megaraid_sysfs_alloc_resources(adapter_t *adapter)

    allocate sysfs related resources

    :param adapter_t \*adapter:
        controller's soft state

.. _`megaraid_sysfs_alloc_resources.description`:

Description
-----------

Allocate packets required to issue FW calls whenever the sysfs attributes
are read. These attributes would require up-to-date information from the
FW. Also set up resources for mutual exclusion to share these resources and
the wait queue.

Return 0 on success.
Return -ERROR_CODE on failure.

.. _`megaraid_sysfs_free_resources`:

megaraid_sysfs_free_resources
=============================

.. c:function:: void megaraid_sysfs_free_resources(adapter_t *adapter)

    free sysfs related resources

    :param adapter_t \*adapter:
        controller's soft state

.. _`megaraid_sysfs_free_resources.description`:

Description
-----------

Free packets allocated for sysfs FW commands

.. _`megaraid_sysfs_get_ldmap_done`:

megaraid_sysfs_get_ldmap_done
=============================

.. c:function:: void megaraid_sysfs_get_ldmap_done(uioc_t *uioc)

    callback for get ldmap

    :param uioc_t \*uioc:
        completed packet

.. _`megaraid_sysfs_get_ldmap_done.description`:

Description
-----------

Callback routine called in the ISR/tasklet context for get ldmap call

.. _`megaraid_sysfs_get_ldmap_timeout`:

megaraid_sysfs_get_ldmap_timeout
================================

.. c:function:: void megaraid_sysfs_get_ldmap_timeout(struct timer_list *t)

    timeout handling for get ldmap

    :param struct timer_list \*t:
        timed out timer

.. _`megaraid_sysfs_get_ldmap_timeout.description`:

Description
-----------

Timeout routine to recover and return to application, in case the adapter
has stopped responding. A timeout of 60 seconds for this command seems like
a good value.

.. _`megaraid_sysfs_get_ldmap`:

megaraid_sysfs_get_ldmap
========================

.. c:function:: int megaraid_sysfs_get_ldmap(adapter_t *adapter)

    get update logical drive map

    :param adapter_t \*adapter:
        controller's soft state

.. _`megaraid_sysfs_get_ldmap.description`:

Description
-----------

This routine will be called whenever user reads the logical drive
attributes, go get the current logical drive mapping table from the
firmware. We use the management API's to issue commands to the controller.

.. _`megaraid_sysfs_get_ldmap.note`:

NOTE
----

The commands issuance functionality is not generalized and
implemented in context of "get ld map" command only. If required, the
command issuance logical can be trivially pulled out and implemented as a
standalone library. For now, this should suffice since there is no other
user of this interface.

Return 0 on success.
Return -1 on failure.

.. _`megaraid_sysfs_show_app_hndl`:

megaraid_sysfs_show_app_hndl
============================

.. c:function:: ssize_t megaraid_sysfs_show_app_hndl(struct device *dev, struct device_attribute *attr, char *buf)

    display application handle for this adapter

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        buffer to send data to

.. _`megaraid_sysfs_show_app_hndl.description`:

Description
-----------

Display the handle used by the applications while executing management
tasks on the adapter. We invoke a management module API to get the adapter
handle, since we do not interface with applications directly.

.. _`megaraid_sysfs_show_ldnum`:

megaraid_sysfs_show_ldnum
=========================

.. c:function:: ssize_t megaraid_sysfs_show_ldnum(struct device *dev, struct device_attribute *attr, char *buf)

    display the logical drive number for this device

    :param struct device \*dev:
        device object representation for the scsi device

    :param struct device_attribute \*attr:
        device attribute to show

    :param char \*buf:
        buffer to send data to

.. _`megaraid_sysfs_show_ldnum.description`:

Description
-----------

Display the logical drive number for the device in question, if it a valid
logical drive. For physical devices, "-1" is returned.

.. _`megaraid_sysfs_show_ldnum.the-logical-drive-number-is-displayed-in-following-format`:

The logical drive number is displayed in following format
---------------------------------------------------------


<SCSI ID> <LD NUM> <LD STICKY ID> <APP ADAPTER HANDLE>

<int>     <int>       <int>            <int>

.. This file was automatic generated / don't edit.

