.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_cs5520.c

.. _`cs5520_set_timings`:

cs5520_set_timings
==================

.. c:function:: void cs5520_set_timings(struct ata_port *ap, struct ata_device *adev, int pio)

    program PIO timings

    :param struct ata_port \*ap:
        ATA port

    :param struct ata_device \*adev:
        ATA device

    :param int pio:
        *undescribed*

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

    :param struct ata_port \*ap:
        ATA port

    :param struct ata_device \*adev:
        ATA device

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

    :param struct pci_dev \*pdev:
        PCI device

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

    :param struct pci_dev \*pdev:
        PCI device

    :param pm_message_t mesg:
        *undescribed*

.. _`cs5520_pci_device_suspend.description`:

Description
-----------

We have to cut and waste bits from the standard method because
the 5520 is a bit odd and not just a pure ATA device. As a result
we must not disable it. The needed code is short and this avoids
chip specific mess in the core code.

.. This file was automatic generated / don't edit.

