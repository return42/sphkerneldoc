.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_cmd64x.c

.. _`cmd64x_set_timing`:

cmd64x_set_timing
=================

.. c:function:: void cmd64x_set_timing(struct ata_port *ap, struct ata_device *adev, u8 mode)

    set PIO and MWDMA timing

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

    :param mode:
        mode
    :type mode: u8

.. _`cmd64x_set_timing.description`:

Description
-----------

Called to do the PIO and MWDMA mode setup.

.. _`cmd64x_set_piomode`:

cmd64x_set_piomode
==================

.. c:function:: void cmd64x_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`cmd64x_set_piomode.description`:

Description
-----------

Used when configuring the devices ot set the PIO timings. All the
actual work is done by the PIO/MWDMA setting helper

.. _`cmd64x_set_dmamode`:

cmd64x_set_dmamode
==================

.. c:function:: void cmd64x_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set initial DMA mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`cmd64x_set_dmamode.description`:

Description
-----------

Called to do the DMA mode setup.

.. _`cmd64x_sff_irq_check`:

cmd64x_sff_irq_check
====================

.. c:function:: bool cmd64x_sff_irq_check(struct ata_port *ap)

    check IDE interrupt

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

.. _`cmd64x_sff_irq_check.description`:

Description
-----------

Check IDE interrupt in CFR/ARTTIM23 registers.

.. _`cmd64x_sff_irq_clear`:

cmd64x_sff_irq_clear
====================

.. c:function:: void cmd64x_sff_irq_clear(struct ata_port *ap)

    clear IDE interrupt

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

.. _`cmd64x_sff_irq_clear.description`:

Description
-----------

Clear IDE interrupt in CFR/ARTTIM23 and DMA status registers.

.. _`cmd648_sff_irq_check`:

cmd648_sff_irq_check
====================

.. c:function:: bool cmd648_sff_irq_check(struct ata_port *ap)

    check IDE interrupt

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

.. _`cmd648_sff_irq_check.description`:

Description
-----------

Check IDE interrupt in MRDMODE register.

.. _`cmd648_sff_irq_clear`:

cmd648_sff_irq_clear
====================

.. c:function:: void cmd648_sff_irq_clear(struct ata_port *ap)

    clear IDE interrupt

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

.. _`cmd648_sff_irq_clear.description`:

Description
-----------

Clear IDE interrupt in MRDMODE and DMA status registers.

.. _`cmd646r1_bmdma_stop`:

cmd646r1_bmdma_stop
===================

.. c:function:: void cmd646r1_bmdma_stop(struct ata_queued_cmd *qc)

    DMA stop callback

    :param qc:
        Command in progress
    :type qc: struct ata_queued_cmd \*

.. _`cmd646r1_bmdma_stop.description`:

Description
-----------

Stub for now while investigating the r1 quirk in the old driver.

.. This file was automatic generated / don't edit.

