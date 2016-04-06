.. -*- coding: utf-8; mode: rst -*-

==========
ata_piix.c
==========



.. _xref_ich_pata_cable_detect:

ich_pata_cable_detect
=====================

.. c:function:: int ich_pata_cable_detect (struct ata_port * ap)

    Probe host controller cable detect info

    :param struct ata_port * ap:
        Port for which cable detect info is desired



Description
-----------

	Read 80c cable indicator from ATA PCI device's PCI config
	register.  This register is normally set by firmware (BIOS).



LOCKING
-------

	None (inherited from caller).




.. _xref_piix_pata_prereset:

piix_pata_prereset
==================

.. c:function:: int piix_pata_prereset (struct ata_link * link, unsigned long deadline)

    prereset for PATA host controller

    :param struct ata_link * link:
        Target link

    :param unsigned long deadline:
        deadline jiffies for the operation



LOCKING
-------

	None (inherited from caller).




.. _xref_piix_set_piomode:

piix_set_piomode
================

.. c:function:: void piix_set_piomode (struct ata_port * ap, struct ata_device * adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port * ap:
        Port whose timings we are configuring

    :param struct ata_device * adev:
        Drive in question



Description
-----------

	Set PIO mode for device, in host controller PCI config space.



LOCKING
-------

	None (inherited from caller).




.. _xref_do_pata_set_dmamode:

do_pata_set_dmamode
===================

.. c:function:: void do_pata_set_dmamode (struct ata_port * ap, struct ata_device * adev, int isich)

    Initialize host controller PATA PIO timings

    :param struct ata_port * ap:
        Port whose timings we are configuring

    :param struct ata_device * adev:
        Drive in question

    :param int isich:
        set if the chip is an ICH device



Description
-----------

	Set UDMA mode for device, in host controller PCI config space.



LOCKING
-------

	None (inherited from caller).




.. _xref_piix_set_dmamode:

piix_set_dmamode
================

.. c:function:: void piix_set_dmamode (struct ata_port * ap, struct ata_device * adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port * ap:
        Port whose timings we are configuring

    :param struct ata_device * adev:
        um



Description
-----------

	Set MW/UDMA mode for device, in host controller PCI config space.



LOCKING
-------

	None (inherited from caller).




.. _xref_ich_set_dmamode:

ich_set_dmamode
===============

.. c:function:: void ich_set_dmamode (struct ata_port * ap, struct ata_device * adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port * ap:
        Port whose timings we are configuring

    :param struct ata_device * adev:
        um



Description
-----------

	Set MW/UDMA mode for device, in host controller PCI config space.



LOCKING
-------

	None (inherited from caller).




.. _xref_piix_check_450nx_errata:

piix_check_450nx_errata
=======================

.. c:function:: int piix_check_450nx_errata (struct pci_dev * ata_dev)

    Check for problem 450NX setup

    :param struct pci_dev * ata_dev:
        the PCI device to check



Description
-----------

	Check for the present of 450NX errata #19 and errata #25. If
	they are found return an error code so we can turn off DMA




.. _xref_piix_init_one:

piix_init_one
=============

.. c:function:: int piix_init_one (struct pci_dev * pdev, const struct pci_device_id * ent)

    Register PIIX ATA PCI device with kernel services

    :param struct pci_dev * pdev:
        PCI device to register

    :param const struct pci_device_id * ent:
        Entry in piix_pci_tbl matching with **pdev**



Description
-----------

	Called from kernel PCI layer.  We probe for combined mode (sigh),
	and then hand over control to libata, for it to do the rest.



LOCKING
-------

	Inherited from PCI layer (may sleep).



RETURNS
-------

	Zero on success, or -ERRNO value.


