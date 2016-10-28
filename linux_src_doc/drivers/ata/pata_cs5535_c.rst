.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_cs5535.c

.. _`cs5535_cable_detect`:

cs5535_cable_detect
===================

.. c:function:: int cs5535_cable_detect(struct ata_port *ap)

    detect cable type

    :param struct ata_port \*ap:
        Port to detect on

.. _`cs5535_cable_detect.description`:

Description
-----------

Perform cable detection for ATA66 capable cable. Return a libata
cable type.

.. _`cs5535_set_piomode`:

cs5535_set_piomode
==================

.. c:function:: void cs5535_set_piomode(struct ata_port *ap, struct ata_device *adev)

    PIO setup

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        device on the interface

.. _`cs5535_set_piomode.description`:

Description
-----------

Set our PIO requirements. The CS5535 is pretty clean about all this

.. _`cs5535_set_dmamode`:

cs5535_set_dmamode
==================

.. c:function:: void cs5535_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    DMA timing setup

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        Device being configured

.. _`cs5535_init_one`:

cs5535_init_one
===============

.. c:function:: int cs5535_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    Initialise a CS5530

    :param struct pci_dev \*dev:
        PCI device

    :param const struct pci_device_id \*id:
        Entry in match table

.. _`cs5535_init_one.description`:

Description
-----------

Install a driver for the newly found CS5530 companion chip. Most of
this is just housekeeping. We have to set the chip up correctly and
turn off various bits of emulation magic.

.. This file was automatic generated / don't edit.

