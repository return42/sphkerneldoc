.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_it8213.c

.. _`it8213_pre_reset`:

it8213_pre_reset
================

.. c:function:: int it8213_pre_reset(struct ata_link *link, unsigned long deadline)

    probe begin

    :param struct ata_link \*link:
        link

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`it8213_pre_reset.description`:

Description
-----------

Filter out ports by the enable bits before doing the normal reset
and probe.

.. _`it8213_cable_detect`:

it8213_cable_detect
===================

.. c:function:: int it8213_cable_detect(struct ata_port *ap)

    check for 40/80 pin

    :param struct ata_port \*ap:
        Port

.. _`it8213_cable_detect.description`:

Description
-----------

Perform cable detection for the 8213 ATA interface. This is
different to the PIIX arrangement

.. _`it8213_set_piomode`:

it8213_set_piomode
==================

.. c:function:: void it8213_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device whose timings we are configuring

.. _`it8213_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space.

.. _`it8213_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`it8213_set_dmamode`:

it8213_set_dmamode
==================

.. c:function:: void it8213_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device to program

.. _`it8213_set_dmamode.description`:

Description
-----------

Set UDMA/MWDMA mode for device, in host controller PCI config space.
This device is basically an ICH alike.

.. _`it8213_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`it8213_init_one`:

it8213_init_one
===============

.. c:function:: int it8213_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    Register 8213 ATA PCI device with kernel services

    :param struct pci_dev \*pdev:
        PCI device to register

    :param const struct pci_device_id \*ent:
        Entry in it8213_pci_tbl matching with \ ``pdev``\ 

.. _`it8213_init_one.description`:

Description
-----------

Called from kernel PCI layer.

.. _`it8213_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`it8213_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

