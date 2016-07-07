.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_pdc202xx_old.c

.. _`pdc202xx_configure_piomode`:

pdc202xx_configure_piomode
==========================

.. c:function:: void pdc202xx_configure_piomode(struct ata_port *ap, struct ata_device *adev, int pio)

    set chip PIO timing

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

    :param int pio:
        PIO mode

.. _`pdc202xx_configure_piomode.description`:

Description
-----------

Called to do the PIO mode setup. Our timing registers are shared
so a configure_dmamode call will undo any work we do here and vice
versa

.. _`pdc202xx_set_piomode`:

pdc202xx_set_piomode
====================

.. c:function:: void pdc202xx_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`pdc202xx_set_piomode.description`:

Description
-----------

Called to do the PIO mode setup. Our timing registers are shared
but we want to set the PIO timing by default.

.. _`pdc202xx_set_dmamode`:

pdc202xx_set_dmamode
====================

.. c:function:: void pdc202xx_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set DMA mode in chip

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`pdc202xx_set_dmamode.description`:

Description
-----------

Load DMA cycle times into the chip ready for a DMA transfer
to occur.

.. _`pdc2026x_bmdma_start`:

pdc2026x_bmdma_start
====================

.. c:function:: void pdc2026x_bmdma_start(struct ata_queued_cmd *qc)

    DMA engine begin

    :param struct ata_queued_cmd \*qc:
        ATA command

.. _`pdc2026x_bmdma_start.description`:

Description
-----------

In UDMA3 or higher we have to clock switch for the duration of the
DMA transfer sequence.

.. _`pdc2026x_bmdma_start.note`:

Note
----

The host lock held by the libata layer protects
us from two channels both trying to set DMA bits at once

.. _`pdc2026x_bmdma_stop`:

pdc2026x_bmdma_stop
===================

.. c:function:: void pdc2026x_bmdma_stop(struct ata_queued_cmd *qc)

    DMA engine stop

    :param struct ata_queued_cmd \*qc:
        ATA command

.. _`pdc2026x_bmdma_stop.description`:

Description
-----------

After a DMA completes we need to put the clock back to 33MHz for
PIO timings.

.. _`pdc2026x_bmdma_stop.note`:

Note
----

The host lock held by the libata layer protects
us from two channels both trying to set DMA bits at once

.. _`pdc2026x_dev_config`:

pdc2026x_dev_config
===================

.. c:function:: void pdc2026x_dev_config(struct ata_device *adev)

    device setup hook

    :param struct ata_device \*adev:
        newly found device

.. _`pdc2026x_dev_config.description`:

Description
-----------

Perform chip specific early setup. We need to lock the transfer
sizes to 8bit to avoid making the state engine on the 2026x cards
barf.

.. _`pdc2026x_check_atapi_dma`:

pdc2026x_check_atapi_dma
========================

.. c:function:: int pdc2026x_check_atapi_dma(struct ata_queued_cmd *qc)

    Check whether ATAPI DMA can be supported for this command

    :param struct ata_queued_cmd \*qc:
        Metadata associated with taskfile to check

.. _`pdc2026x_check_atapi_dma.description`:

Description
-----------

Just say no - not supported on older Promise.

.. _`pdc2026x_check_atapi_dma.locking`:

LOCKING
-------

None (inherited from caller).

.. _`pdc2026x_check_atapi_dma.return`:

Return
------

0 when ATAPI DMA can be used
1 otherwise

.. This file was automatic generated / don't edit.

