.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_sl82c105.c

.. _`sl82c105_pre_reset`:

sl82c105_pre_reset
==================

.. c:function:: int sl82c105_pre_reset(struct ata_link *link, unsigned long deadline)

    probe begin

    :param link:
        ATA link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`sl82c105_pre_reset.description`:

Description
-----------

Set up cable type and use generic probe init

.. _`sl82c105_configure_piomode`:

sl82c105_configure_piomode
==========================

.. c:function:: void sl82c105_configure_piomode(struct ata_port *ap, struct ata_device *adev, int pio)

    set chip PIO timing

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

    :param pio:
        PIO mode
    :type pio: int

.. _`sl82c105_configure_piomode.description`:

Description
-----------

Called to do the PIO mode setup. Our timing registers are shared
so a configure_dmamode call will undo any work we do here and vice
versa

.. _`sl82c105_set_piomode`:

sl82c105_set_piomode
====================

.. c:function:: void sl82c105_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`sl82c105_set_piomode.description`:

Description
-----------

Called to do the PIO mode setup. Our timing registers are shared
but we want to set the PIO timing by default.

.. _`sl82c105_configure_dmamode`:

sl82c105_configure_dmamode
==========================

.. c:function:: void sl82c105_configure_dmamode(struct ata_port *ap, struct ata_device *adev)

    set DMA mode in chip

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`sl82c105_configure_dmamode.description`:

Description
-----------

Load DMA cycle times into the chip ready for a DMA transfer
to occur.

.. _`sl82c105_reset_engine`:

sl82c105_reset_engine
=====================

.. c:function:: void sl82c105_reset_engine(struct ata_port *ap)

    Reset the DMA engine

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

.. _`sl82c105_reset_engine.description`:

Description
-----------

The sl82c105 has some serious problems with the DMA engine
when transfers don't run as expected or ATAPI is used. The
recommended fix is to reset the engine each use using a chip
test register.

.. _`sl82c105_bmdma_start`:

sl82c105_bmdma_start
====================

.. c:function:: void sl82c105_bmdma_start(struct ata_queued_cmd *qc)

    DMA engine begin

    :param qc:
        ATA command
    :type qc: struct ata_queued_cmd \*

.. _`sl82c105_bmdma_start.description`:

Description
-----------

Reset the DMA engine each use as recommended by the errata
document.

.. _`sl82c105_bmdma_start.fixme`:

FIXME
-----

if we switch clock at BMDMA start/end we might get better
PIO performance on DMA capable devices.

.. _`sl82c105_bmdma_stop`:

sl82c105_bmdma_stop
===================

.. c:function:: void sl82c105_bmdma_stop(struct ata_queued_cmd *qc)

    DMA engine stop

    :param qc:
        ATA command
    :type qc: struct ata_queued_cmd \*

.. _`sl82c105_bmdma_stop.description`:

Description
-----------

Reset the DMA engine each use as recommended by the errata
document.

This function is also called to turn off DMA when a timeout occurs
during DMA operation. In both cases we need to reset the engine,
so no actual eng_timeout handler is required.

We assume bmdma_stop is always called if bmdma_start as called. If
not then we may need to wrap qc_issue.

.. _`sl82c105_qc_defer`:

sl82c105_qc_defer
=================

.. c:function:: int sl82c105_qc_defer(struct ata_queued_cmd *qc)

    implement serialization

    :param qc:
        command
    :type qc: struct ata_queued_cmd \*

.. _`sl82c105_qc_defer.description`:

Description
-----------

We must issue one command per host not per channel because
of the reset bug.

Q: is the scsi host lock sufficient ?

.. _`sl82c105_bridge_revision`:

sl82c105_bridge_revision
========================

.. c:function:: int sl82c105_bridge_revision(struct pci_dev *pdev)

    find bridge version

    :param pdev:
        PCI device for the ATA function
    :type pdev: struct pci_dev \*

.. _`sl82c105_bridge_revision.description`:

Description
-----------

Locates the PCI bridge associated with the ATA function and
providing it is a Winbond 553 reports the revision. If it cannot
find a revision or the right device it returns -1

.. This file was automatic generated / don't edit.

