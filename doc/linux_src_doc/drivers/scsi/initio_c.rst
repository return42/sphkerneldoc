.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/initio.c

.. _`initio_se2_instr`:

initio_se2_instr
================

.. c:function:: void initio_se2_instr(unsigned long base, u8 instr)

    bitbang an instruction

    :param unsigned long base:
        Base of InitIO controller

    :param u8 instr:
        Instruction for serial E2PROM

.. _`initio_se2_instr.description`:

Description
-----------

Bitbang an instruction out to the serial E2Prom

.. _`initio_se2_ew_en`:

initio_se2_ew_en
================

.. c:function:: void initio_se2_ew_en(unsigned long base)

    Enable erase/write

    :param unsigned long base:
        Base address of InitIO controller

.. _`initio_se2_ew_en.description`:

Description
-----------

Enable erase/write state of serial EEPROM

.. _`initio_se2_ew_ds`:

initio_se2_ew_ds
================

.. c:function:: void initio_se2_ew_ds(unsigned long base)

    Disable erase/write

    :param unsigned long base:
        Base address of InitIO controller

.. _`initio_se2_ew_ds.description`:

Description
-----------

Disable erase/write state of serial EEPROM

.. _`initio_se2_rd`:

initio_se2_rd
=============

.. c:function:: u16 initio_se2_rd(unsigned long base, u8 addr)

    read E2PROM word

    :param unsigned long base:
        Base of InitIO controller

    :param u8 addr:
        Address of word in E2PROM

.. _`initio_se2_rd.description`:

Description
-----------

Read a word from the NV E2PROM device

.. _`initio_se2_wr`:

initio_se2_wr
=============

.. c:function:: void initio_se2_wr(unsigned long base, u8 addr, u16 val)

    read E2PROM word

    :param unsigned long base:
        Base of InitIO controller

    :param u8 addr:
        Address of word in E2PROM

    :param u16 val:
        Value to write

.. _`initio_se2_wr.description`:

Description
-----------

Write a word to the NV E2PROM device. Used when recovering from
a problem with the NV.

.. _`initio_se2_rd_all`:

initio_se2_rd_all
=================

.. c:function:: int initio_se2_rd_all(unsigned long base)

    read hostadapter NV configuration

    :param unsigned long base:
        Base address of InitIO controller

.. _`initio_se2_rd_all.description`:

Description
-----------

Reads the E2PROM data into main memory. Ensures that the checksum
and header marker are valid. Returns 1 on success -1 on error.

.. _`initio_se2_update_all`:

initio_se2_update_all
=====================

.. c:function:: void initio_se2_update_all(unsigned long base)

    Update E2PROM

    :param unsigned long base:
        Base of InitIO controller

.. _`initio_se2_update_all.description`:

Description
-----------

Update the E2PROM by wrting any changes into the E2PROM
chip, rewriting the checksum.

.. _`initio_read_eeprom`:

initio_read_eeprom
==================

.. c:function:: void initio_read_eeprom(unsigned long base)

    Retrieve configuration

    :param unsigned long base:
        Base of InitIO Host Adapter

.. _`initio_read_eeprom.description`:

Description
-----------

Retrieve the host adapter configuration data from E2Prom. If the
data is invalid then the defaults are used and are also restored
into the E2PROM. This forms the access point for the SCSI driver
into the E2PROM layer, the other functions for the E2PROM are all
internal use.

Must be called single threaded, uses a shared global area.

.. _`initio_stop_bm`:

initio_stop_bm
==============

.. c:function:: void initio_stop_bm(struct initio_host *host)

    stop bus master

    :param struct initio_host \*host:
        InitIO we are stopping

.. _`initio_stop_bm.description`:

Description
-----------

Stop any pending DMA operation, aborting the DMA if necessary

.. _`initio_reset_scsi`:

initio_reset_scsi
=================

.. c:function:: int initio_reset_scsi(struct initio_host *host, int seconds)

    Reset SCSI host controller

    :param struct initio_host \*host:
        InitIO host to reset

    :param int seconds:
        Recovery time

.. _`initio_reset_scsi.description`:

Description
-----------

Perform a full reset of the SCSI subsystem.

.. _`initio_init`:

initio_init
===========

.. c:function:: void initio_init(struct initio_host *host, u8 *bios_addr)

    set up an InitIO host adapter

    :param struct initio_host \*host:
        InitIO host adapter

    :param u8 \*bios_addr:
        BIOS address

.. _`initio_init.description`:

Description
-----------

Set up the host adapter and devices according to the configuration
retrieved from the E2PROM.

.. _`initio_init.locking`:

Locking
-------

Calls E2PROM layer code which is not re-enterable so must
run single threaded for now.

.. _`initio_alloc_scb`:

initio_alloc_scb
================

.. c:function:: struct scsi_ctrl_blk *initio_alloc_scb(struct initio_host *host)

    Allocate an SCB

    :param struct initio_host \*host:
        InitIO host we are allocating for

.. _`initio_alloc_scb.description`:

Description
-----------

Walk the SCB list for the controller and allocate a free SCB if
one exists.

.. _`initio_release_scb`:

initio_release_scb
==================

.. c:function:: void initio_release_scb(struct initio_host *host, struct scsi_ctrl_blk *cmnd)

    Release an SCB

    :param struct initio_host \*host:
        InitIO host that owns the SCB

    :param struct scsi_ctrl_blk \*cmnd:
        SCB command block being returned

.. _`initio_release_scb.description`:

Description
-----------

Return an allocated SCB to the host free list

.. _`initio_next_state`:

initio_next_state
=================

.. c:function:: int initio_next_state(struct initio_host *host)

    Next SCSI state

    :param struct initio_host \*host:
        InitIO host we are processing

.. _`initio_next_state.description`:

Description
-----------

Progress the active command block along the state machine
until we hit a state which we must wait for activity to occur.

Returns zero or a negative code.

.. _`initio_state_1`:

initio_state_1
==============

.. c:function:: int initio_state_1(struct initio_host *host)

    SCSI state machine

    :param struct initio_host \*host:
        InitIO host we are controlling

.. _`initio_state_1.description`:

Description
-----------

Perform SCSI state processing for Select/Attention/Stop

.. _`initio_state_2`:

initio_state_2
==============

.. c:function:: int initio_state_2(struct initio_host *host)

    SCSI state machine

    :param struct initio_host \*host:
        InitIO host we are controlling

.. _`initio_state_2.description`:

Description
-----------

state after selection with attention
state after selection with attention3

.. _`initio_state_3`:

initio_state_3
==============

.. c:function:: int initio_state_3(struct initio_host *host)

    SCSI state machine

    :param struct initio_host \*host:
        InitIO host we are controlling

.. _`initio_state_3.description`:

Description
-----------

state before CDB xfer is done

.. _`initio_state_4`:

initio_state_4
==============

.. c:function:: int initio_state_4(struct initio_host *host)

    SCSI state machine

    :param struct initio_host \*host:
        InitIO host we are controlling

.. _`initio_state_4.description`:

Description
-----------

SCSI state machine. State 4

.. _`initio_state_5`:

initio_state_5
==============

.. c:function:: int initio_state_5(struct initio_host *host)

    SCSI state machine

    :param struct initio_host \*host:
        InitIO host we are controlling

.. _`initio_state_5.description`:

Description
-----------

State after dma xfer done or phase change before xfer done

.. _`initio_state_6`:

initio_state_6
==============

.. c:function:: int initio_state_6(struct initio_host *host)

    SCSI state machine

    :param struct initio_host \*host:
        InitIO host we are controlling

.. _`initio_state_6.description`:

Description
-----------

State after Data phase

.. _`initio_state_7`:

initio_state_7
==============

.. c:function:: int initio_state_7(struct initio_host *host)

    SCSI state machine

    :param struct initio_host \*host:
        InitIO host we are controlling

.. _`initio_xfer_data_in`:

initio_xfer_data_in
===================

.. c:function:: int initio_xfer_data_in(struct initio_host *host)

    Commence data input

    :param struct initio_host \*host:
        InitIO host in use

.. _`initio_xfer_data_in.description`:

Description
-----------

Commence a block of data transfer. The transfer itself will
be managed by the controller and we will get a completion (or
failure) interrupt.

.. _`initio_xfer_data_out`:

initio_xfer_data_out
====================

.. c:function:: int initio_xfer_data_out(struct initio_host *host)

    Commence data output

    :param struct initio_host \*host:
        InitIO host in use

.. _`initio_xfer_data_out.description`:

Description
-----------

Commence a block of data transfer. The transfer itself will
be managed by the controller and we will get a completion (or
failure) interrupt.

.. _`int_initio_scsi_rst`:

int_initio_scsi_rst
===================

.. c:function:: int int_initio_scsi_rst(struct initio_host *host)

    SCSI reset occurred

    :param struct initio_host \*host:
        Host seeing the reset

.. _`int_initio_scsi_rst.description`:

Description
-----------

A SCSI bus reset has occurred. Clean up any pending transfer
the hardware is doing by DMA and then abort all active and
disconnected commands. The mid layer should sort the rest out
for us

.. _`int_initio_resel`:

int_initio_resel
================

.. c:function:: int int_initio_resel(struct initio_host *host)

    Reselection occurred

    :param struct initio_host \*host:
        InitIO host adapter

.. _`int_initio_resel.description`:

Description
-----------

A SCSI reselection event has been signalled and the interrupt
is now being processed. Work out which command block needs attention
and continue processing that command.

.. _`int_initio_bad_seq`:

int_initio_bad_seq
==================

.. c:function:: int int_initio_bad_seq(struct initio_host *host)

    out of phase

    :param struct initio_host \*host:
        InitIO host flagging event

.. _`int_initio_bad_seq.description`:

Description
-----------

We have ended up out of phase somehow. Reset the host controller
and throw all our toys out of the pram. Let the midlayer clean up

.. _`initio_msgout_abort_targ`:

initio_msgout_abort_targ
========================

.. c:function:: int initio_msgout_abort_targ(struct initio_host *host)

    abort a tag

    :param struct initio_host \*host:
        InitIO host

.. _`initio_msgout_abort_targ.description`:

Description
-----------

Abort when the target/lun does not match or when our SCB is not
busy. Used by untagged commands.

.. _`initio_msgout_abort_tag`:

initio_msgout_abort_tag
=======================

.. c:function:: int initio_msgout_abort_tag(struct initio_host *host)

    abort a tag

    :param struct initio_host \*host:
        InitIO host

.. _`initio_msgout_abort_tag.description`:

Description
-----------

Abort when the target/lun does not match or when our SCB is not
busy. Used for tagged commands.

.. _`initio_msgin`:

initio_msgin
============

.. c:function:: int initio_msgin(struct initio_host *host)

    Message in

    :param struct initio_host \*host:
        InitIO Host

.. _`initio_msgin.description`:

Description
-----------

Process incoming message

.. _`initio_bus_device_reset`:

initio_bus_device_reset
=======================

.. c:function:: int initio_bus_device_reset(struct initio_host *host)

    SCSI Bus Device Reset

    :param struct initio_host \*host:
        InitIO host to reset

.. _`initio_bus_device_reset.description`:

Description
-----------

Perform a device reset and abort all pending SCBs for the
victim device

.. _`i91u_intr`:

i91u_intr
=========

.. c:function:: irqreturn_t i91u_intr(int irqno, void *dev_id)

    IRQ handler

    :param int irqno:
        IRQ number

    :param void \*dev_id:
        IRQ identifier

.. _`i91u_intr.description`:

Description
-----------

Take the relevant locks and then invoke the actual isr processing
code under the lock.

.. _`initio_build_scb`:

initio_build_scb
================

.. c:function:: void initio_build_scb(struct initio_host *host, struct scsi_ctrl_blk *cblk, struct scsi_cmnd *cmnd)

    Build the mappings and SCB

    :param struct initio_host \*host:
        InitIO host taking the command

    :param struct scsi_ctrl_blk \*cblk:
        Firmware command block

    :param struct scsi_cmnd \*cmnd:
        SCSI midlayer command block

.. _`initio_build_scb.description`:

Description
-----------

Translate the abstract SCSI command into a firmware command block
suitable for feeding to the InitIO host controller. This also requires
we build the scatter gather lists and ensure they are mapped properly.

.. _`i91u_queuecommand_lck`:

i91u_queuecommand_lck
=====================

.. c:function:: int i91u_queuecommand_lck(struct scsi_cmnd *cmd, void (*done)(struct scsi_cmnd *))

    Queue a new command if possible

    :param struct scsi_cmnd \*cmd:
        SCSI command block from the mid layer

    :param void (\*done)(struct scsi_cmnd \*):
        Completion handler

.. _`i91u_queuecommand_lck.description`:

Description
-----------

Attempts to queue a new command with the host adapter. Will return
zero if successful or indicate a host busy condition if not (which
will cause the mid layer to call us again later with the command)

.. _`i91u_bus_reset`:

i91u_bus_reset
==============

.. c:function:: int i91u_bus_reset(struct scsi_cmnd *cmnd)

    reset the SCSI bus

    :param struct scsi_cmnd \*cmnd:
        Command block we want to trigger the reset for

.. _`i91u_bus_reset.description`:

Description
-----------

Initiate a SCSI bus reset sequence

.. _`i91u_biosparam`:

i91u_biosparam
==============

.. c:function:: int i91u_biosparam(struct scsi_device *sdev, struct block_device *dev, sector_t capacity, int *info_array)

    return the "logical geometry

    :param struct scsi_device \*sdev:
        SCSI device
        \ ``dev``\ ; Matching block device

    :param struct block_device \*dev:
        *undescribed*

    :param sector_t capacity:
        Sector size of drive

    :param int \*info_array:
        Return space for BIOS geometry

.. _`i91u_biosparam.description`:

Description
-----------

Map the device geometry in a manner compatible with the host
controller BIOS behaviour.

.. _`i91u_biosparam.fixme`:

FIXME
-----

limited to 2^32 sector devices.

.. _`i91u_unmap_scb`:

i91u_unmap_scb
==============

.. c:function:: void i91u_unmap_scb(struct pci_dev *pci_dev, struct scsi_cmnd *cmnd)

    Unmap a command

    :param struct pci_dev \*pci_dev:
        PCI device the command is for

    :param struct scsi_cmnd \*cmnd:
        The command itself

.. _`i91u_unmap_scb.description`:

Description
-----------

Unmap any PCI mapping/IOMMU resources allocated when the command
was mapped originally as part of initio_build_scb

.. _`i91uscbpost`:

i91uSCBPost
===========

.. c:function:: void i91uSCBPost(u8 *host_mem, u8 *cblk_mem)

    SCSI callback

    :param u8 \*host_mem:
        *undescribed*

    :param u8 \*cblk_mem:
        *undescribed*

.. _`i91uscbpost.description`:

Description
-----------

This is callback routine be called when tulip finish one
SCSI command.

.. _`initio_remove_one`:

initio_remove_one
=================

.. c:function:: void initio_remove_one(struct pci_dev *pdev)

    control shutdown

    :param struct pci_dev \*pdev:
        PCI device being released

.. _`initio_remove_one.description`:

Description
-----------

Release the resources assigned to this adapter after it has
finished being used.

.. This file was automatic generated / don't edit.

