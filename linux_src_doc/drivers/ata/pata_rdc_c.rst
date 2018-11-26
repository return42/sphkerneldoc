.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_rdc.c

.. _`rdc_pata_cable_detect`:

rdc_pata_cable_detect
=====================

.. c:function:: int rdc_pata_cable_detect(struct ata_port *ap)

    Probe host controller cable detect info

    :param ap:
        Port for which cable detect info is desired
    :type ap: struct ata_port \*

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

    :param link:
        Target link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`rdc_pata_prereset.locking`:

LOCKING
-------

None (inherited from caller).

.. _`rdc_set_piomode`:

rdc_set_piomode
===============

.. c:function:: void rdc_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        um
    :type adev: struct ata_device \*

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

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Drive in question
    :type adev: struct ata_device \*

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

    :param pdev:
        PCI device to register
    :type pdev: struct pci_dev \*

    :param ent:
        Entry in rdc_pci_tbl matching with \ ``pdev``\ 
    :type ent: const struct pci_device_id \*

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

