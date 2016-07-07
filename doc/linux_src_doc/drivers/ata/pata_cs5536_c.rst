.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_cs5536.c

.. _`cs5536_cable_detect`:

cs5536_cable_detect
===================

.. c:function:: int cs5536_cable_detect(struct ata_port *ap)

    detect cable type

    :param struct ata_port \*ap:
        Port to detect on

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

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        device on the interface

.. _`cs5536_set_dmamode`:

cs5536_set_dmamode
==================

.. c:function:: void cs5536_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    DMA timing setup

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        Device being configured

.. _`cs5536_init_one`:

cs5536_init_one
===============

.. c:function:: int cs5536_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    :param struct pci_dev \*dev:
        PCI device

    :param const struct pci_device_id \*id:
        Entry in match table

.. This file was automatic generated / don't edit.

