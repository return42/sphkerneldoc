.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/megaraid.c

.. _`mega_setup_mailbox`:

mega_setup_mailbox
==================

.. c:function:: int mega_setup_mailbox(adapter_t *adapter)

    @adapter - pointer to our soft state

    :param adapter_t \*adapter:
        *undescribed*

.. _`mega_setup_mailbox.description`:

Description
-----------

Allocates a 8 byte aligned memory for the handshake mailbox.

.. _`mega_runpendq`:

mega_runpendq
=============

.. c:function:: void mega_runpendq(adapter_t *adapter)

    @adapter - pointer to our soft state

    :param adapter_t \*adapter:
        *undescribed*

.. _`mega_runpendq.description`:

Description
-----------

Runs through the list of pending requests.

.. _`mega_allocate_scb`:

mega_allocate_scb
=================

.. c:function:: scb_t *mega_allocate_scb(adapter_t *adapter, Scsi_Cmnd *cmd)

    @adapter - pointer to our soft state \ ``cmd``\  - scsi command from the mid-layer

    :param adapter_t \*adapter:
        *undescribed*

    :param Scsi_Cmnd \*cmd:
        *undescribed*

.. _`mega_allocate_scb.description`:

Description
-----------

Allocate a SCB structure. This is the central structure for controller
commands.

.. _`mega_get_ldrv_num`:

mega_get_ldrv_num
=================

.. c:function:: int mega_get_ldrv_num(adapter_t *adapter, Scsi_Cmnd *cmd, int channel)

    @adapter - pointer to our soft state \ ``cmd``\  - scsi mid layer command \ ``channel``\  - channel on the controller

    :param adapter_t \*adapter:
        *undescribed*

    :param Scsi_Cmnd \*cmd:
        *undescribed*

    :param int channel:
        *undescribed*

.. _`mega_get_ldrv_num.description`:

Description
-----------

Calculate the logical drive number based on the information in scsi command
and the channel number.

.. _`mega_build_cmd`:

mega_build_cmd
==============

.. c:function:: scb_t *mega_build_cmd(adapter_t *adapter, Scsi_Cmnd *cmd, int *busy)

    @adapter - pointer to our soft state \ ``cmd``\  - Prepare using this scsi command \ ``busy``\  - busy flag if no resources

    :param adapter_t \*adapter:
        *undescribed*

    :param Scsi_Cmnd \*cmd:
        *undescribed*

    :param int \*busy:
        *undescribed*

.. _`mega_build_cmd.description`:

Description
-----------

Prepares a command and scatter gather list for the controller. This routine
also finds out if the commands is intended for a logical drive or a
physical device and prepares the controller command accordingly.

We also re-order the logical drives and physical devices based on their
boot settings.

.. _`mega_prepare_passthru`:

mega_prepare_passthru
=====================

.. c:function:: mega_passthru *mega_prepare_passthru(adapter_t *adapter, scb_t *scb, Scsi_Cmnd *cmd, int channel, int target)

    @adapter - pointer to our soft state \ ``scb``\  - our scsi control block \ ``cmd``\  - scsi command from the mid-layer \ ``channel``\  - actual channel on the controller \ ``target``\  - actual id on the controller.

    :param adapter_t \*adapter:
        *undescribed*

    :param scb_t \*scb:
        *undescribed*

    :param Scsi_Cmnd \*cmd:
        *undescribed*

    :param int channel:
        *undescribed*

    :param int target:
        *undescribed*

.. _`mega_prepare_passthru.description`:

Description
-----------

prepare a command for the scsi physical devices.

.. _`mega_prepare_extpassthru`:

mega_prepare_extpassthru
========================

.. c:function:: mega_ext_passthru *mega_prepare_extpassthru(adapter_t *adapter, scb_t *scb, Scsi_Cmnd *cmd, int channel, int target)

    @adapter - pointer to our soft state \ ``scb``\  - our scsi control block \ ``cmd``\  - scsi command from the mid-layer \ ``channel``\  - actual channel on the controller \ ``target``\  - actual id on the controller.

    :param adapter_t \*adapter:
        *undescribed*

    :param scb_t \*scb:
        *undescribed*

    :param Scsi_Cmnd \*cmd:
        *undescribed*

    :param int channel:
        *undescribed*

    :param int target:
        *undescribed*

.. _`mega_prepare_extpassthru.description`:

Description
-----------

prepare a command for the scsi physical devices. This rountine prepares
commands for devices which can take extended CDBs (>10 bytes)

.. _`issue_scb`:

issue_scb
=========

.. c:function:: int issue_scb(adapter_t *adapter, scb_t *scb)

    @adapter - pointer to our soft state \ ``scb``\  - scsi control block

    :param adapter_t \*adapter:
        *undescribed*

    :param scb_t \*scb:
        *undescribed*

.. _`issue_scb.description`:

Description
-----------

Post a command to the card if the mailbox is available, otherwise return
busy. We also take the scb from the pending list if the mailbox is
available.

.. _`issue_scb_block`:

issue_scb_block
===============

.. c:function:: int issue_scb_block(adapter_t *adapter, u_char *raw_mbox)

    @adapter - pointer to our soft state \ ``raw_mbox``\  - the mailbox

    :param adapter_t \*adapter:
        *undescribed*

    :param u_char \*raw_mbox:
        *undescribed*

.. _`issue_scb_block.description`:

Description
-----------

Issue a scb in synchronous and non-interrupt mode

.. _`megaraid_isr_iomapped`:

megaraid_isr_iomapped
=====================

.. c:function:: irqreturn_t megaraid_isr_iomapped(int irq, void *devp)

    @irq - irq \ ``devp``\  - pointer to our soft state

    :param int irq:
        *undescribed*

    :param void \*devp:
        *undescribed*

.. _`megaraid_isr_iomapped.description`:

Description
-----------

Interrupt service routine for io-mapped controllers.
Find out if our device is interrupting. If yes, acknowledge the interrupt
and service the completed commands.

.. _`megaraid_isr_memmapped`:

megaraid_isr_memmapped
======================

.. c:function:: irqreturn_t megaraid_isr_memmapped(int irq, void *devp)

    @irq - irq \ ``devp``\  - pointer to our soft state

    :param int irq:
        *undescribed*

    :param void \*devp:
        *undescribed*

.. _`megaraid_isr_memmapped.description`:

Description
-----------

Interrupt service routine for memory-mapped controllers.
Find out if our device is interrupting. If yes, acknowledge the interrupt
and service the completed commands.

.. _`mega_cmd_done`:

mega_cmd_done
=============

.. c:function:: void mega_cmd_done(adapter_t *adapter, u8 completed, int nstatus, int status)

    @adapter - pointer to our soft state \ ``completed``\  - array of ids of completed commands \ ``nstatus``\  - number of completed commands \ ``status``\  - status of the last command completed

    :param adapter_t \*adapter:
        *undescribed*

    :param u8 completed:
        *undescribed*

    :param int nstatus:
        *undescribed*

    :param int status:
        *undescribed*

.. _`mega_cmd_done.description`:

Description
-----------

Complete the commands and call the scsi mid-layer callback hooks.

.. _`megaraid_abort_and_reset`:

megaraid_abort_and_reset
========================

.. c:function:: int megaraid_abort_and_reset(adapter_t *adapter, Scsi_Cmnd *cmd, int aor)

    @adapter - megaraid soft state \ ``cmd``\  - scsi command to be aborted or reset \ ``aor``\  - abort or reset flag

    :param adapter_t \*adapter:
        *undescribed*

    :param Scsi_Cmnd \*cmd:
        *undescribed*

    :param int aor:
        *undescribed*

.. _`megaraid_abort_and_reset.description`:

Description
-----------

Try to locate the scsi command in the pending queue. If found and is not
issued to the controller, abort/reset it. Otherwise return failure

.. _`mega_allocate_inquiry`:

mega_allocate_inquiry
=====================

.. c:function:: void *mega_allocate_inquiry(dma_addr_t *dma_handle, struct pci_dev *pdev)

    @dma_handle - handle returned for dma address \ ``pdev``\  - handle to pci device

    :param dma_addr_t \*dma_handle:
        *undescribed*

    :param struct pci_dev \*pdev:
        *undescribed*

.. _`mega_allocate_inquiry.description`:

Description
-----------

allocates memory for inquiry structure

.. _`proc_show_config`:

proc_show_config
================

.. c:function:: int proc_show_config(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_config.description`:

Description
-----------

Display configuration information about the controller.

.. _`proc_show_stat`:

proc_show_stat
==============

.. c:function:: int proc_show_stat(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_stat.description`:

Description
-----------

Display statistical information about the I/O activity.

.. _`proc_show_mbox`:

proc_show_mbox
==============

.. c:function:: int proc_show_mbox(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_mbox.description`:

Description
-----------

Display mailbox information for the last command issued. This information
is good for debugging.

.. _`proc_show_rebuild_rate`:

proc_show_rebuild_rate
======================

.. c:function:: int proc_show_rebuild_rate(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_rebuild_rate.description`:

Description
-----------

Display current rebuild rate

.. _`proc_show_battery`:

proc_show_battery
=================

.. c:function:: int proc_show_battery(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_battery.description`:

Description
-----------

Display information about the battery module on the controller.

.. _`proc_show_pdrv`:

proc_show_pdrv
==============

.. c:function:: int proc_show_pdrv(struct seq_file *m, adapter_t *adapter, int channel)

    @m - Synthetic file construction data \ ``page``\  - buffer to write the data in \ ``adapter``\  - pointer to our soft state

    :param struct seq_file \*m:
        *undescribed*

    :param adapter_t \*adapter:
        *undescribed*

    :param int channel:
        *undescribed*

.. _`proc_show_pdrv.description`:

Description
-----------

Display information about the physical drives.

.. _`proc_show_pdrv_ch0`:

proc_show_pdrv_ch0
==================

.. c:function:: int proc_show_pdrv_ch0(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_pdrv_ch0.description`:

Description
-----------

Display information about the physical drives on physical channel 0.

.. _`proc_show_pdrv_ch1`:

proc_show_pdrv_ch1
==================

.. c:function:: int proc_show_pdrv_ch1(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_pdrv_ch1.description`:

Description
-----------

Display information about the physical drives on physical channel 1.

.. _`proc_show_pdrv_ch2`:

proc_show_pdrv_ch2
==================

.. c:function:: int proc_show_pdrv_ch2(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_pdrv_ch2.description`:

Description
-----------

Display information about the physical drives on physical channel 2.

.. _`proc_show_pdrv_ch3`:

proc_show_pdrv_ch3
==================

.. c:function:: int proc_show_pdrv_ch3(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_pdrv_ch3.description`:

Description
-----------

Display information about the physical drives on physical channel 3.

.. _`proc_show_rdrv`:

proc_show_rdrv
==============

.. c:function:: int proc_show_rdrv(struct seq_file *m, adapter_t *adapter, int start, int end)

    @m - Synthetic file construction data \ ``adapter``\  - pointer to our soft state \ ``start``\  - starting logical drive to display \ ``end``\  - ending logical drive to display

    :param struct seq_file \*m:
        *undescribed*

    :param adapter_t \*adapter:
        *undescribed*

    :param int start:
        *undescribed*

    :param int end:
        *undescribed*

.. _`proc_show_rdrv.description`:

Description
-----------

We do not print the inquiry information since its already available through
/proc/scsi/scsi interface

.. _`proc_show_rdrv_10`:

proc_show_rdrv_10
=================

.. c:function:: int proc_show_rdrv_10(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_rdrv_10.description`:

Description
-----------

Display real time information about the logical drives 0 through 9.

.. _`proc_show_rdrv_20`:

proc_show_rdrv_20
=================

.. c:function:: int proc_show_rdrv_20(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_rdrv_20.description`:

Description
-----------

Display real time information about the logical drives 0 through 9.

.. _`proc_show_rdrv_30`:

proc_show_rdrv_30
=================

.. c:function:: int proc_show_rdrv_30(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_rdrv_30.description`:

Description
-----------

Display real time information about the logical drives 0 through 9.

.. _`proc_show_rdrv_40`:

proc_show_rdrv_40
=================

.. c:function:: int proc_show_rdrv_40(struct seq_file *m, void *v)

    @m - Synthetic file construction data \ ``v``\  - File iterator

    :param struct seq_file \*m:
        *undescribed*

    :param void \*v:
        *undescribed*

.. _`proc_show_rdrv_40.description`:

Description
-----------

Display real time information about the logical drives 0 through 9.

.. _`mega_create_proc_entry`:

mega_create_proc_entry
======================

.. c:function:: void mega_create_proc_entry(int index, struct proc_dir_entry *parent)

    @index - index in soft state array \ ``parent``\  - parent node for this /proc entry

    :param int index:
        *undescribed*

    :param struct proc_dir_entry \*parent:
        *undescribed*

.. _`mega_create_proc_entry.description`:

Description
-----------

Creates /proc entries for our controllers.

.. _`megaraid_biosparam`:

megaraid_biosparam
==================

.. c:function:: int megaraid_biosparam(struct scsi_device *sdev, struct block_device *bdev, sector_t capacity, int geom)

    :param struct scsi_device \*sdev:
        *undescribed*

    :param struct block_device \*bdev:
        *undescribed*

    :param sector_t capacity:
        *undescribed*

    :param int geom:
        *undescribed*

.. _`megaraid_biosparam.description`:

Description
-----------

Return the disk geometry for a particular disk

.. _`mega_init_scb`:

mega_init_scb
=============

.. c:function:: int mega_init_scb(adapter_t *adapter)

    @adapter - pointer to our soft state

    :param adapter_t \*adapter:
        *undescribed*

.. _`mega_init_scb.allocate-memory-for-the-various-pointers-in-the-scb-structures`:

Allocate memory for the various pointers in the scb structures
--------------------------------------------------------------

scatter-gather list pointer, passthru and extended passthru structure
pointers.

.. _`megadev_open`:

megadev_open
============

.. c:function:: int megadev_open(struct inode *inode, struct file *filep)

    @inode - unused \ ``filep``\  - unused

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*filep:
        *undescribed*

.. _`megadev_open.description`:

Description
-----------

Routines for the character/ioctl interface to the driver. Find out if this
is a valid open.

.. _`megadev_ioctl`:

megadev_ioctl
=============

.. c:function:: int megadev_ioctl(struct file *filep, unsigned int cmd, unsigned long arg)

    @inode - Our device inode \ ``filep``\  - unused \ ``cmd``\  - ioctl command \ ``arg``\  - user buffer

    :param struct file \*filep:
        *undescribed*

    :param unsigned int cmd:
        *undescribed*

    :param unsigned long arg:
        *undescribed*

.. _`megadev_ioctl.description`:

Description
-----------

ioctl entry point for our private ioctl interface. We move the data in from
the user space, prepare the command (if necessary, convert the old MIMD
ioctl to new ioctl command), and issue a synchronous command to the
controller.

.. _`mega_m_to_n`:

mega_m_to_n
===========

.. c:function:: int mega_m_to_n(void __user *arg, nitioctl_t *uioc)

    @arg - user address \ ``uioc``\  - new ioctl structure

    :param void __user \*arg:
        *undescribed*

    :param nitioctl_t \*uioc:
        *undescribed*

.. _`mega_m_to_n.description`:

Description
-----------

A thin layer to convert older mimd interface ioctl structure to NIT ioctl
structure

Converts the older mimd ioctl structure to newer NIT structure

.. _`mega_is_bios_enabled`:

mega_is_bios_enabled
====================

.. c:function:: int mega_is_bios_enabled(adapter_t *adapter)

    @adapter - pointer to our soft state

    :param adapter_t \*adapter:
        *undescribed*

.. _`mega_is_bios_enabled.description`:

Description
-----------

issue command to find out if the BIOS is enabled for this controller

.. _`mega_enum_raid_scsi`:

mega_enum_raid_scsi
===================

.. c:function:: void mega_enum_raid_scsi(adapter_t *adapter)

    @adapter - pointer to our soft state

    :param adapter_t \*adapter:
        *undescribed*

.. _`mega_enum_raid_scsi.description`:

Description
-----------

Find out what channels are RAID/SCSI. This information is used to
differentiate the virtual channels and physical channels and to support
ROMB feature and non-disk devices.

.. _`mega_get_boot_drv`:

mega_get_boot_drv
=================

.. c:function:: void mega_get_boot_drv(adapter_t *adapter)

    @adapter - pointer to our soft state

    :param adapter_t \*adapter:
        *undescribed*

.. _`mega_get_boot_drv.description`:

Description
-----------

Find out which device is the boot device. Note, any logical drive or any
phyical device (e.g., a CDROM) can be designated as a boot device.

.. _`mega_support_random_del`:

mega_support_random_del
=======================

.. c:function:: int mega_support_random_del(adapter_t *adapter)

    @adapter - pointer to our soft state

    :param adapter_t \*adapter:
        *undescribed*

.. _`mega_support_random_del.description`:

Description
-----------

Find out if this controller supports random deletion and addition of
logical drives

.. _`mega_support_ext_cdb`:

mega_support_ext_cdb
====================

.. c:function:: int mega_support_ext_cdb(adapter_t *adapter)

    @adapter - pointer to our soft state

    :param adapter_t \*adapter:
        *undescribed*

.. _`mega_support_ext_cdb.description`:

Description
-----------

Find out if this firmware support cdblen > 10

.. _`mega_del_logdrv`:

mega_del_logdrv
===============

.. c:function:: int mega_del_logdrv(adapter_t *adapter, int logdrv)

    @adapter - pointer to our soft state \ ``logdrv``\  - logical drive to be deleted

    :param adapter_t \*adapter:
        *undescribed*

    :param int logdrv:
        *undescribed*

.. _`mega_del_logdrv.description`:

Description
-----------

Delete the specified logical drive. It is the responsibility of the user
app to let the OS know about this operation.

.. _`mega_get_max_sgl`:

mega_get_max_sgl
================

.. c:function:: void mega_get_max_sgl(adapter_t *adapter)

    @adapter - pointer to our soft state

    :param adapter_t \*adapter:
        *undescribed*

.. _`mega_get_max_sgl.description`:

Description
-----------

Find out the maximum number of scatter-gather elements supported by this
version of the firmware

.. _`mega_support_cluster`:

mega_support_cluster
====================

.. c:function:: int mega_support_cluster(adapter_t *adapter)

    @adapter - pointer to our soft state

    :param adapter_t \*adapter:
        *undescribed*

.. _`mega_support_cluster.description`:

Description
-----------

Find out if this firmware support cluster calls.

.. _`mega_adapinq`:

mega_adapinq
============

.. c:function:: int mega_adapinq(adapter_t *adapter, dma_addr_t dma_handle)

    @adapter - pointer to our soft state \ ``dma_handle``\  - DMA address of the buffer

    :param adapter_t \*adapter:
        *undescribed*

    :param dma_addr_t dma_handle:
        *undescribed*

.. _`mega_adapinq.description`:

Description
-----------

Issue internal commands while interrupts are available.
We only issue direct mailbox commands from within the driver. \ :c:func:`ioctl`\ 
interface using these routines can issue passthru commands.

.. _`mega_internal_command`:

mega_internal_command
=====================

.. c:function:: int mega_internal_command(adapter_t *adapter, megacmd_t *mc, mega_passthru *pthru)

    @adapter - pointer to our soft state \ ``mc``\  - the mailbox command \ ``pthru``\  - Passthru structure for DCDB commands

    :param adapter_t \*adapter:
        *undescribed*

    :param megacmd_t \*mc:
        *undescribed*

    :param mega_passthru \*pthru:
        *undescribed*

.. _`mega_internal_command.description`:

Description
-----------

Issue the internal commands in interrupt mode.
The last argument is the address of the passthru structure if the command
to be fired is a passthru command

.. _`mega_internal_command.note`:

Note
----

parameter 'pthru' is null for non-passthru commands.

.. This file was automatic generated / don't edit.

