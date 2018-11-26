.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_atiixp.c

.. _`atiixp_prereset`:

atiixp_prereset
===============

.. c:function:: int atiixp_prereset(struct ata_link *link, unsigned long deadline)

    perform reset handling

    :param link:
        ATA link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`atiixp_prereset.description`:

Description
-----------

Reset sequence checking enable bits to see which ports are
active.

.. _`atiixp_set_pio_timing`:

atiixp_set_pio_timing
=====================

.. c:function:: void atiixp_set_pio_timing(struct ata_port *ap, struct ata_device *adev, int pio)

    set initial PIO mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

    :param pio:
        *undescribed*
    :type pio: int

.. _`atiixp_set_pio_timing.description`:

Description
-----------

Called by both the pio and dma setup functions to set the controller
timings for PIO transfers. We must load both the mode number and
timing values into the controller.

.. _`atiixp_set_piomode`:

atiixp_set_piomode
==================

.. c:function:: void atiixp_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`atiixp_set_piomode.description`:

Description
-----------

Called to do the PIO mode setup. We use a shared helper for this
as the DMA setup must also adjust the PIO timing information.

.. _`atiixp_set_dmamode`:

atiixp_set_dmamode
==================

.. c:function:: void atiixp_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set initial DMA mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`atiixp_set_dmamode.description`:

Description
-----------

Called to do the DMA mode setup. We use timing tables for most
modes but must tune an appropriate PIO mode to match.

.. _`atiixp_bmdma_start`:

atiixp_bmdma_start
==================

.. c:function:: void atiixp_bmdma_start(struct ata_queued_cmd *qc)

    DMA start callback

    :param qc:
        Command in progress
    :type qc: struct ata_queued_cmd \*

.. _`atiixp_bmdma_start.description`:

Description
-----------

When DMA begins we need to ensure that the UDMA control
register for the channel is correctly set.

.. _`atiixp_bmdma_start.note`:

Note
----

The host lock held by the libata layer protects
us from two channels both trying to set DMA bits at once

.. _`atiixp_bmdma_stop`:

atiixp_bmdma_stop
=================

.. c:function:: void atiixp_bmdma_stop(struct ata_queued_cmd *qc)

    DMA stop callback

    :param qc:
        Command in progress
    :type qc: struct ata_queued_cmd \*

.. _`atiixp_bmdma_stop.description`:

Description
-----------

DMA has completed. Clear the UDMA flag as the next operations will
be PIO ones not UDMA data transfer.

.. _`atiixp_bmdma_stop.note`:

Note
----

The host lock held by the libata layer protects
us from two channels both trying to set DMA bits at once

.. This file was automatic generated / don't edit.

