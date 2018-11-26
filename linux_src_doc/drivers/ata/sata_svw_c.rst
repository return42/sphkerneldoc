.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/sata_svw.c

.. _`k2_bmdma_setup_mmio`:

k2_bmdma_setup_mmio
===================

.. c:function:: void k2_bmdma_setup_mmio(struct ata_queued_cmd *qc)

    Set up PCI IDE BMDMA transaction (MMIO)

    :param qc:
        Info associated with this ATA transaction.
    :type qc: struct ata_queued_cmd \*

.. _`k2_bmdma_setup_mmio.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`k2_bmdma_start_mmio`:

k2_bmdma_start_mmio
===================

.. c:function:: void k2_bmdma_start_mmio(struct ata_queued_cmd *qc)

    Start a PCI IDE BMDMA transaction (MMIO)

    :param qc:
        Info associated with this ATA transaction.
    :type qc: struct ata_queued_cmd \*

.. _`k2_bmdma_start_mmio.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. This file was automatic generated / don't edit.

