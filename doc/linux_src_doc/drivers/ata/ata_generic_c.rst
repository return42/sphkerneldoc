.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/ata_generic.c

.. _`generic_set_mode`:

generic_set_mode
================

.. c:function:: int generic_set_mode(struct ata_link *link, struct ata_device **unused)

    mode setting

    :param struct ata_link \*link:
        link to set up

    :param struct ata_device \*\*unused:
        returned device on error

.. _`generic_set_mode.description`:

Description
-----------

Use a non standard set_mode function. We don't want to be tuned.
The BIOS configured everything. Our job is not to fiddle. We
read the dma enabled bits from the PCI configuration of the device
and respect them.

.. _`is_intel_ider`:

is_intel_ider
=============

.. c:function:: int is_intel_ider(struct pci_dev *dev)

    identify intel IDE-R devices

    :param struct pci_dev \*dev:
        PCI device

.. _`is_intel_ider.description`:

Description
-----------

Distinguish Intel IDE-R controller devices from other Intel IDE
devices. IDE-R devices have no timing registers and are in
most respects virtual. They should be driven by the ata_generic
driver.

IDE-R devices have PCI offset 0xF8.L as zero, later Intel ATA has
it non zero. All Intel ATA has 0x40 writable (timing), but it is
not writable on IDE-R devices (this is guaranteed).

.. _`ata_generic_init_one`:

ata_generic_init_one
====================

.. c:function:: int ata_generic_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    attach generic IDE

    :param struct pci_dev \*dev:
        PCI device found

    :param const struct pci_device_id \*id:
        match entry

.. _`ata_generic_init_one.description`:

Description
-----------

Called each time a matching IDE interface is found. We check if the
interface is one we wish to claim and if so we perform any chip
specific hacks then let the ATA layer do the heavy lifting.

.. This file was automatic generated / don't edit.

