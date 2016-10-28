.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_cs5530.c

.. _`cs5530_set_piomode`:

cs5530_set_piomode
==================

.. c:function:: void cs5530_set_piomode(struct ata_port *ap, struct ata_device *adev)

    PIO setup

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        device on the interface

.. _`cs5530_set_piomode.description`:

Description
-----------

Set our PIO requirements. This is fairly simple on the CS5530
chips.

.. _`cs5530_set_dmamode`:

cs5530_set_dmamode
==================

.. c:function:: void cs5530_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    DMA timing setup

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        Device being configured

.. _`cs5530_set_dmamode.description`:

Description
-----------

We cannot mix MWDMA and UDMA without reloading timings each switch
master to slave. We track the last DMA setup in order to minimise
reloads.

.. _`cs5530_qc_issue`:

cs5530_qc_issue
===============

.. c:function:: unsigned int cs5530_qc_issue(struct ata_queued_cmd *qc)

    command issue

    :param struct ata_queued_cmd \*qc:
        command pending

.. _`cs5530_qc_issue.description`:

Description
-----------

Called when the libata layer is about to issue a command. We wrap
this interface so that we can load the correct ATA timings if
necessary.  Specifically we have a problem that there is only
one MWDMA/UDMA bit.

.. _`cs5530_init_chip`:

cs5530_init_chip
================

.. c:function:: int cs5530_init_chip( void)

    Chipset init

    :param  void:
        no arguments

.. _`cs5530_init_chip.description`:

Description
-----------

Perform the chip initialisation work that is shared between both
setup and resume paths

.. _`cs5530_init_one`:

cs5530_init_one
===============

.. c:function:: int cs5530_init_one(struct pci_dev *pdev, const struct pci_device_id *id)

    Initialise a CS5530

    :param struct pci_dev \*pdev:
        *undescribed*

    :param const struct pci_device_id \*id:
        Entry in match table

.. _`cs5530_init_one.description`:

Description
-----------

Install a driver for the newly found CS5530 companion chip. Most of
this is just housekeeping. We have to set the chip up correctly and
turn off various bits of emulation magic.

.. This file was automatic generated / don't edit.

