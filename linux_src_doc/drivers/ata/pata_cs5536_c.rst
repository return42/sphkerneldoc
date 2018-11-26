.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_cs5536.c

.. _`cs5536_cable_detect`:

cs5536_cable_detect
===================

.. c:function:: int cs5536_cable_detect(struct ata_port *ap)

    detect cable type

    :param ap:
        Port to detect on
    :type ap: struct ata_port \*

.. _`cs5536_cable_detect.description`:

Description
-----------

Perform cable detection for ATA66 capable cable.

Returns a cable type.

.. _`cs5536_set_piomode`:

cs5536_set_piomode
==================

.. c:function:: void cs5536_set_piomode(struct ata_port *ap, struct ata_device *adev)

    PIO setup

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        device on the interface
    :type adev: struct ata_device \*

.. _`cs5536_set_dmamode`:

cs5536_set_dmamode
==================

.. c:function:: void cs5536_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    DMA timing setup

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        Device being configured
    :type adev: struct ata_device \*

.. _`cs5536_init_one`:

cs5536_init_one
===============

.. c:function:: int cs5536_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

    :param id:
        Entry in match table
    :type id: const struct pci_device_id \*

.. This file was automatic generated / don't edit.

