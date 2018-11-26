.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_it821x.c

.. _`it821x_program`:

it821x_program
==============

.. c:function:: void it821x_program(struct ata_port *ap, struct ata_device *adev, u16 timing)

    program the PIO/MWDMA registers

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param adev:
        Device to program
    :type adev: struct ata_device \*

    :param timing:
        Timing value (66Mhz in top 8bits, 50 in the low 8)
    :type timing: u16

.. _`it821x_program.description`:

Description
-----------

Program the PIO/MWDMA timing for this channel according to the
current clock. These share the same register so are managed by
the DMA start/stop sequence as with the old driver.

.. _`it821x_program_udma`:

it821x_program_udma
===================

.. c:function:: void it821x_program_udma(struct ata_port *ap, struct ata_device *adev, u16 timing)

    program the UDMA registers

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param adev:
        ATA device to update
    :type adev: struct ata_device \*

    :param timing:
        Timing bits. Top 8 are for 66Mhz bottom for 50Mhz
    :type timing: u16

.. _`it821x_program_udma.description`:

Description
-----------

Program the UDMA timing for this drive according to the
current clock. Handles the dual clocks and also knows about
the errata on the 0x10 revision. The UDMA errata is partly handled
here and partly in start_dma.

.. _`it821x_clock_strategy`:

it821x_clock_strategy
=====================

.. c:function:: void it821x_clock_strategy(struct ata_port *ap, struct ata_device *adev)

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device being updated
    :type adev: struct ata_device \*

.. _`it821x_clock_strategy.description`:

Description
-----------

Select between the 50 and 66Mhz base clocks to get the best
results for this interface.

.. _`it821x_passthru_set_piomode`:

it821x_passthru_set_piomode
===========================

.. c:function:: void it821x_passthru_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set PIO mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`it821x_passthru_set_piomode.description`:

Description
-----------

Configure for PIO mode. This is complicated as the register is
shared by PIO and MWDMA and for both channels.

.. _`it821x_passthru_set_dmamode`:

it821x_passthru_set_dmamode
===========================

.. c:function:: void it821x_passthru_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set initial DMA mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`it821x_passthru_set_dmamode.description`:

Description
-----------

Set up the DMA modes. The actions taken depend heavily on the mode
to use. If UDMA is used as is hopefully the usual case then the
timing register is private and we need only consider the clock. If
we are using MWDMA then we have to manage the setting ourself as
we switch devices and mode.

.. _`it821x_passthru_bmdma_start`:

it821x_passthru_bmdma_start
===========================

.. c:function:: void it821x_passthru_bmdma_start(struct ata_queued_cmd *qc)

    DMA start callback

    :param qc:
        Command in progress
    :type qc: struct ata_queued_cmd \*

.. _`it821x_passthru_bmdma_start.description`:

Description
-----------

Usually drivers set the DMA timing at the point the set_dmamode call
is made. IT821x however requires we load new timings on the
transitions in some cases.

.. _`it821x_passthru_bmdma_stop`:

it821x_passthru_bmdma_stop
==========================

.. c:function:: void it821x_passthru_bmdma_stop(struct ata_queued_cmd *qc)

    DMA stop callback

    :param qc:
        ATA command
    :type qc: struct ata_queued_cmd \*

.. _`it821x_passthru_bmdma_stop.description`:

Description
-----------

We loaded new timings in dma_start, as a result we need to restore
the PIO timings in dma_stop so that the next command issue gets the
right clock values.

.. _`it821x_passthru_dev_select`:

it821x_passthru_dev_select
==========================

.. c:function:: void it821x_passthru_dev_select(struct ata_port *ap, unsigned int device)

    Select master/slave

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param device:
        Device number (not pointer)
    :type device: unsigned int

.. _`it821x_passthru_dev_select.description`:

Description
-----------

Device selection hook. If necessary perform clock switching

.. _`it821x_smart_qc_issue`:

it821x_smart_qc_issue
=====================

.. c:function:: unsigned int it821x_smart_qc_issue(struct ata_queued_cmd *qc)

    wrap qc issue prot

    :param qc:
        command
    :type qc: struct ata_queued_cmd \*

.. _`it821x_smart_qc_issue.description`:

Description
-----------

Wrap the command issue sequence for the IT821x. We need to
perform out own device selection timing loads before the
usual happenings kick off

.. _`it821x_passthru_qc_issue`:

it821x_passthru_qc_issue
========================

.. c:function:: unsigned int it821x_passthru_qc_issue(struct ata_queued_cmd *qc)

    wrap qc issue prot

    :param qc:
        command
    :type qc: struct ata_queued_cmd \*

.. _`it821x_passthru_qc_issue.description`:

Description
-----------

Wrap the command issue sequence for the IT821x. We need to
perform out own device selection timing loads before the
usual happenings kick off

.. _`it821x_smart_set_mode`:

it821x_smart_set_mode
=====================

.. c:function:: int it821x_smart_set_mode(struct ata_link *link, struct ata_device **unused)

    mode setting

    :param link:
        interface to set up
    :type link: struct ata_link \*

    :param unused:
        device that failed (error only)
    :type unused: struct ata_device \*\*

.. _`it821x_smart_set_mode.description`:

Description
-----------

Use a non standard set_mode function. We don't want to be tuned.
The BIOS configured everything. Our job is not to fiddle. We
read the dma enabled bits from the PCI configuration of the device
and respect them.

.. _`it821x_dev_config`:

it821x_dev_config
=================

.. c:function:: void it821x_dev_config(struct ata_device *adev)

    Called each device identify

    :param adev:
        Device that has just been identified
    :type adev: struct ata_device \*

.. _`it821x_dev_config.description`:

Description
-----------

Perform the initial setup needed for each device that is chip
special. In our case we need to lock the sector count to avoid
blowing the brains out of the firmware with large LBA48 requests

.. _`it821x_read_id`:

it821x_read_id
==============

.. c:function:: unsigned int it821x_read_id(struct ata_device *adev, struct ata_taskfile *tf, u16 *id)

    Hack identify data up

    :param adev:
        device to read
    :type adev: struct ata_device \*

    :param tf:
        proposed taskfile
    :type tf: struct ata_taskfile \*

    :param id:
        buffer for returned ident data
    :type id: u16 \*

.. _`it821x_read_id.description`:

Description
-----------

Query the devices on this firmware driven port and slightly
mash the identify data to stop us and common tools trying to
use features not firmware supported. The firmware itself does
some masking (eg SMART) but not enough.

.. _`it821x_check_atapi_dma`:

it821x_check_atapi_dma
======================

.. c:function:: int it821x_check_atapi_dma(struct ata_queued_cmd *qc)

    ATAPI DMA handler

    :param qc:
        Command we are about to issue
    :type qc: struct ata_queued_cmd \*

.. _`it821x_check_atapi_dma.description`:

Description
-----------

Decide if this ATAPI command can be issued by DMA on this
controller. Return 0 if it can be.

.. _`it821x_display_disk`:

it821x_display_disk
===================

.. c:function:: void it821x_display_disk(int n, u8 *buf)

    display disk setup

    :param n:
        Device number
    :type n: int

    :param buf:
        Buffer block from firmware
    :type buf: u8 \*

.. _`it821x_display_disk.description`:

Description
-----------

Produce a nice informative display of the device setup as provided
by the firmware.

.. _`it821x_firmware_command`:

it821x_firmware_command
=======================

.. c:function:: u8 *it821x_firmware_command(struct ata_port *ap, u8 cmd, int len)

    issue firmware command

    :param ap:
        IT821x port to interrogate
    :type ap: struct ata_port \*

    :param cmd:
        command
    :type cmd: u8

    :param len:
        length
    :type len: int

.. _`it821x_firmware_command.description`:

Description
-----------

Issue firmware commands expecting data back from the controller. We
use this to issue commands that do not go via the normal paths. Other
commands such as 0xFC can be issued normally.

.. _`it821x_probe_firmware`:

it821x_probe_firmware
=====================

.. c:function:: void it821x_probe_firmware(struct ata_port *ap)

    firmware reporting/setup

    :param ap:
        IT821x port being probed
    :type ap: struct ata_port \*

.. _`it821x_probe_firmware.description`:

Description
-----------

Probe the firmware of the controller by issuing firmware command
0xFA and analysing the returned data.

.. _`it821x_port_start`:

it821x_port_start
=================

.. c:function:: int it821x_port_start(struct ata_port *ap)

    port setup

    :param ap:
        ATA port being set up
    :type ap: struct ata_port \*

.. _`it821x_port_start.description`:

Description
-----------

The it821x needs to maintain private data structures and also to
use the standard PCI interface which lacks support for this
functionality. We instead set up the private data on the port
start hook, and tear it down on port stop

.. _`it821x_rdc_cable`:

it821x_rdc_cable
================

.. c:function:: int it821x_rdc_cable(struct ata_port *ap)

    Cable detect for RDC1010

    :param ap:
        port we are checking
    :type ap: struct ata_port \*

.. _`it821x_rdc_cable.description`:

Description
-----------

Return the RDC1010 cable type. Unlike the IT821x we know how to do
this and can do host side cable detect

.. This file was automatic generated / don't edit.

