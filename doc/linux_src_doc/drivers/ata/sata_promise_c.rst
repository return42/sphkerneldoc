.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/sata_promise.c

.. _`pdc_fill_sg`:

pdc_fill_sg
===========

.. c:function:: void pdc_fill_sg(struct ata_queued_cmd *qc)

    Fill PCI IDE PRD table

    :param struct ata_queued_cmd \*qc:
        Metadata associated with taskfile to be transferred

.. _`pdc_fill_sg.description`:

Description
-----------

Fill PCI IDE PRD (scatter-gather) table with segments
associated with the current disk command.
Make sure hardware does not choke on it.

.. _`pdc_fill_sg.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. This file was automatic generated / don't edit.

