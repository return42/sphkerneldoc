.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_pcmcia.c

.. _`pcmcia_set_mode`:

pcmcia_set_mode
===============

.. c:function:: int pcmcia_set_mode(struct ata_link *link, struct ata_device **r_failed_dev)

    PCMCIA specific mode setup

    :param link:
        link
    :type link: struct ata_link \*

    :param r_failed_dev:
        Return pointer for failed device
    :type r_failed_dev: struct ata_device \*\*

.. _`pcmcia_set_mode.description`:

Description
-----------

Perform the tuning and setup of the devices and timings, which
for PCMCIA is the same as any other controller. We wrap it however
as we need to spot hardware with incorrect or missing master/slave
decode, which alas is embarrassingly common in the PC world

.. _`pcmcia_set_mode_8bit`:

pcmcia_set_mode_8bit
====================

.. c:function:: int pcmcia_set_mode_8bit(struct ata_link *link, struct ata_device **r_failed_dev)

    PCMCIA specific mode setup

    :param link:
        link
    :type link: struct ata_link \*

    :param r_failed_dev:
        Return pointer for failed device
    :type r_failed_dev: struct ata_device \*\*

.. _`pcmcia_set_mode_8bit.description`:

Description
-----------

For the simple emulated 8bit stuff the less we do the better.

.. _`ata_data_xfer_8bit`:

ata_data_xfer_8bit
==================

.. c:function:: unsigned int ata_data_xfer_8bit(struct ata_queued_cmd *qc, unsigned char *buf, unsigned int buflen, int rw)

    Transfer data by 8bit PIO

    :param qc:
        queued command
    :type qc: struct ata_queued_cmd \*

    :param buf:
        data buffer
    :type buf: unsigned char \*

    :param buflen:
        buffer length
    :type buflen: unsigned int

    :param rw:
        read/write
    :type rw: int

.. _`ata_data_xfer_8bit.description`:

Description
-----------

Transfer data from/to the device data register by 8 bit PIO.

.. _`ata_data_xfer_8bit.locking`:

LOCKING
-------

Inherited from caller.

.. _`pcmcia_8bit_drain_fifo`:

pcmcia_8bit_drain_fifo
======================

.. c:function:: void pcmcia_8bit_drain_fifo(struct ata_queued_cmd *qc)

    Stock FIFO drain logic for SFF controllers

    :param qc:
        command
    :type qc: struct ata_queued_cmd \*

.. _`pcmcia_8bit_drain_fifo.description`:

Description
-----------

Drain the FIFO and device of any stuck data following a command
failing to complete. In some cases this is necessary before a
reset will recover the device.

.. _`pcmcia_init_one`:

pcmcia_init_one
===============

.. c:function:: int pcmcia_init_one(struct pcmcia_device *pdev)

    attach a PCMCIA interface

    :param pdev:
        pcmcia device
    :type pdev: struct pcmcia_device \*

.. _`pcmcia_init_one.description`:

Description
-----------

Register a PCMCIA IDE interface. Such interfaces are PIO 0 and
shared IRQ.

.. _`pcmcia_remove_one`:

pcmcia_remove_one
=================

.. c:function:: void pcmcia_remove_one(struct pcmcia_device *pdev)

    unplug an pcmcia interface

    :param pdev:
        pcmcia device
    :type pdev: struct pcmcia_device \*

.. _`pcmcia_remove_one.description`:

Description
-----------

A PCMCIA ATA device has been unplugged. Perform the needed
cleanup. Also called on module unload for any active devices.

.. This file was automatic generated / don't edit.

