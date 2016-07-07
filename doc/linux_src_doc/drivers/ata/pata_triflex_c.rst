.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_triflex.c

.. _`triflex_prereset`:

triflex_prereset
================

.. c:function:: int triflex_prereset(struct ata_link *link, unsigned long deadline)

    probe begin

    :param struct ata_link \*link:
        ATA link

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`triflex_prereset.description`:

Description
-----------

Set up cable type and use generic probe init

.. _`triflex_load_timing`:

triflex_load_timing
===================

.. c:function:: void triflex_load_timing(struct ata_port *ap, struct ata_device *adev, int speed)

    timing configuration

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        Device on the bus

    :param int speed:
        speed to configure

.. _`triflex_load_timing.description`:

Description
-----------

The Triflex has one set of timings per device per channel. This
means we must do some switching. As the PIO and DMA timings don't
match we have to do some reloading unlike PIIX devices where tuning
tricks can avoid it.

.. _`triflex_set_piomode`:

triflex_set_piomode
===================

.. c:function:: void triflex_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`triflex_set_piomode.description`:

Description
-----------

Use the timing loader to set up the PIO mode. We have to do this
because DMA start/stop will only be called once DMA occurs. If there
has been no DMA then the PIO timings are still needed.

.. _`triflex_bmdma_start`:

triflex_bmdma_start
===================

.. c:function:: void triflex_bmdma_start(struct ata_queued_cmd *qc)

    DMA start callback

    :param struct ata_queued_cmd \*qc:
        Command in progress

.. _`triflex_bmdma_start.description`:

Description
-----------

Usually drivers set the DMA timing at the point the set_dmamode call
is made. Triflex however requires we load new timings on the
transition or keep matching PIO/DMA pairs (ie MWDMA2/PIO4 etc).
We load the DMA timings just before starting DMA and then restore
the PIO timing when the DMA is finished.

.. _`triflex_bmdma_stop`:

triflex_bmdma_stop
==================

.. c:function:: void triflex_bmdma_stop(struct ata_queued_cmd *qc)

    DMA stop callback

    :param struct ata_queued_cmd \*qc:
        *undescribed*

.. _`triflex_bmdma_stop.description`:

Description
-----------

We loaded new timings in dma_start, as a result we need to restore
the PIO timings in dma_stop so that the next command issue gets the
right clock values.

.. This file was automatic generated / don't edit.

