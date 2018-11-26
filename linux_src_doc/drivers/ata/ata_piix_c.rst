.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/ata_piix.c

.. _`ich_pata_cable_detect`:

ich_pata_cable_detect
=====================

.. c:function:: int ich_pata_cable_detect(struct ata_port *ap)

    Probe host controller cable detect info

    :param ap:
        Port for which cable detect info is desired
    :type ap: struct ata_port \*

.. _`ich_pata_cable_detect.description`:

Description
-----------

     Read 80c cable indicator from ATA PCI device's PCI config
     register.  This register is normally set by firmware (BIOS).

.. _`ich_pata_cable_detect.locking`:

LOCKING
-------

     None (inherited from caller).

.. _`piix_pata_prereset`:

piix_pata_prereset
==================

.. c:function:: int piix_pata_prereset(struct ata_link *link, unsigned long deadline)

    prereset for PATA host controller

    :param link:
        Target link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`piix_pata_prereset.locking`:

LOCKING
-------

     None (inherited from caller).

.. _`piix_set_piomode`:

piix_set_piomode
================

.. c:function:: void piix_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Drive in question
    :type adev: struct ata_device \*

.. _`piix_set_piomode.description`:

Description
-----------

     Set PIO mode for device, in host controller PCI config space.

.. _`piix_set_piomode.locking`:

LOCKING
-------

     None (inherited from caller).

.. _`do_pata_set_dmamode`:

do_pata_set_dmamode
===================

.. c:function:: void do_pata_set_dmamode(struct ata_port *ap, struct ata_device *adev, int isich)

    Initialize host controller PATA PIO timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        Drive in question
    :type adev: struct ata_device \*

    :param isich:
        set if the chip is an ICH device
    :type isich: int

.. _`do_pata_set_dmamode.description`:

Description
-----------

     Set UDMA mode for device, in host controller PCI config space.

.. _`do_pata_set_dmamode.locking`:

LOCKING
-------

     None (inherited from caller).

.. _`piix_set_dmamode`:

piix_set_dmamode
================

.. c:function:: void piix_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        um
    :type adev: struct ata_device \*

.. _`piix_set_dmamode.description`:

Description
-----------

     Set MW/UDMA mode for device, in host controller PCI config space.

.. _`piix_set_dmamode.locking`:

LOCKING
-------

     None (inherited from caller).

.. _`ich_set_dmamode`:

ich_set_dmamode
===============

.. c:function:: void ich_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param ap:
        Port whose timings we are configuring
    :type ap: struct ata_port \*

    :param adev:
        um
    :type adev: struct ata_device \*

.. _`ich_set_dmamode.description`:

Description
-----------

     Set MW/UDMA mode for device, in host controller PCI config space.

.. _`ich_set_dmamode.locking`:

LOCKING
-------

     None (inherited from caller).

.. _`piix_check_450nx_errata`:

piix_check_450nx_errata
=======================

.. c:function:: int piix_check_450nx_errata(struct pci_dev *ata_dev)

    Check for problem 450NX setup

    :param ata_dev:
        the PCI device to check
    :type ata_dev: struct pci_dev \*

.. _`piix_check_450nx_errata.description`:

Description
-----------

     Check for the present of 450NX errata #19 and errata #25. If
     they are found return an error code so we can turn off DMA

.. _`piix_init_one`:

piix_init_one
=============

.. c:function:: int piix_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    Register PIIX ATA PCI device with kernel services

    :param pdev:
        PCI device to register
    :type pdev: struct pci_dev \*

    :param ent:
        Entry in piix_pci_tbl matching with \ ``pdev``\ 
    :type ent: const struct pci_device_id \*

.. _`piix_init_one.description`:

Description
-----------

     Called from kernel PCI layer.  We probe for combined mode (sigh),
     and then hand over control to libata, for it to do the rest.

.. _`piix_init_one.locking`:

LOCKING
-------

     Inherited from PCI layer (may sleep).

.. _`piix_init_one.return`:

Return
------

     Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

