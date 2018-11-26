.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_cs5520.c

.. _`cs5520_set_timings`:

cs5520_set_timings
==================

.. c:function:: void cs5520_set_timings(struct ata_port *ap, struct ata_device *adev, int pio)

    program PIO timings

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

    :param pio:
        *undescribed*
    :type pio: int

.. _`cs5520_set_timings.description`:

Description
-----------

Program the PIO mode timings for the controller according to the pio
clocking table.

.. _`cs5520_set_piomode`:

cs5520_set_piomode
==================

.. c:function:: void cs5520_set_piomode(struct ata_port *ap, struct ata_device *adev)

    program PIO timings

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`cs5520_set_piomode.description`:

Description
-----------

Program the PIO mode timings for the controller according to the pio
clocking table.

.. _`cs5520_reinit_one`:

cs5520_reinit_one
=================

.. c:function:: int cs5520_reinit_one(struct pci_dev *pdev)

    device resume

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

.. _`cs5520_reinit_one.description`:

Description
-----------

Do any reconfiguration work needed by a resume from RAM. We need
to restore DMA mode support on BIOSen which disabled it

.. _`cs5520_pci_device_suspend`:

cs5520_pci_device_suspend
=========================

.. c:function:: int cs5520_pci_device_suspend(struct pci_dev *pdev, pm_message_t mesg)

    device suspend

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param mesg:
        *undescribed*
    :type mesg: pm_message_t

.. _`cs5520_pci_device_suspend.description`:

Description
-----------

We have to cut and waste bits from the standard method because
the 5520 is a bit odd and not just a pure ATA device. As a result
we must not disable it. The needed code is short and this avoids
chip specific mess in the core code.

.. This file was automatic generated / don't edit.

