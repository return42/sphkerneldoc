.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_piccolo.c

.. _`ata_tosh_init_one`:

ata_tosh_init_one
=================

.. c:function:: int ata_tosh_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    attach generic IDE

    :param dev:
        PCI device found
    :type dev: struct pci_dev \*

    :param id:
        match entry
    :type id: const struct pci_device_id \*

.. _`ata_tosh_init_one.description`:

Description
-----------

Called each time a matching IDE interface is found. We check if the
interface is one we wish to claim and if so we perform any chip
specific hacks then let the ATA layer do the heavy lifting.

.. This file was automatic generated / don't edit.

