.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_rdc.c

.. _`rdc_pata_cable_detect`:

rdc_pata_cable_detect
=====================

.. c:function:: int rdc_pata_cable_detect(struct ata_port *ap)

    Probe host controller cable detect info

    :param struct ata_port \*ap:
        Port for which cable detect info is desired

.. _`rdc_pata_cable_detect.description`:

Description
-----------

Read 80c cable indicator from ATA PCI device's PCI config
register.  This register is normally set by firmware (BIOS).

.. _`rdc_pata_cable_detect.locking`:

LOCKING
-------

None (inherited from caller).

.. _`rdc_pata_prereset`:

rdc_pata_prereset
=================

.. c:function:: int rdc_pata_prereset(struct ata_link *link, unsigned long deadline)

    prereset for PATA host controller

    :param struct ata_link \*link:
        Target link

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`rdc_pata_prereset.locking`:

LOCKING
-------

None (inherited from caller).

.. _`rdc_set_piomode`:

rdc_set_piomode
===============

.. c:function:: void rdc_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        um

.. _`rdc_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space.

.. _`rdc_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`rdc_set_dmamode`:

rdc_set_dmamode
===============

.. c:function:: void rdc_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Drive in question

.. _`rdc_set_dmamode.description`:

Description
-----------

Set UDMA mode for device, in host controller PCI config space.

.. _`rdc_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`rdc_init_one`:

rdc_init_one
============

.. c:function:: int rdc_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    Register PIIX ATA PCI device with kernel services

    :param struct pci_dev \*pdev:
        PCI device to register

    :param const struct pci_device_id \*ent:
        Entry in rdc_pci_tbl matching with \ ``pdev``\ 

.. _`rdc_init_one.description`:

Description
-----------

Called from kernel PCI layer.  We probe for combined mode (sigh),
and then hand over control to libata, for it to do the rest.

.. _`rdc_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`rdc_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

