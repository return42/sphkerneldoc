.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/piix.c

.. _`piix_set_pio_mode`:

piix_set_pio_mode
=================

.. c:function:: void piix_set_pio_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for PIO mode

    :param hwif:
        *undescribed*
    :type hwif: ide_hwif_t \*

    :param drive:
        drive
    :type drive: ide_drive_t \*

.. _`piix_set_pio_mode.description`:

Description
-----------

Set the interface PIO mode based upon the settings done by AMI BIOS.

.. _`piix_set_dma_mode`:

piix_set_dma_mode
=================

.. c:function:: void piix_set_dma_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for DMA mode

    :param hwif:
        port
    :type hwif: ide_hwif_t \*

    :param drive:
        drive
    :type drive: ide_drive_t \*

.. _`piix_set_dma_mode.description`:

Description
-----------

Set a PIIX host controller to the desired DMA mode.  This involves
programming the right timing data into the PCI configuration space.

.. _`init_chipset_ich`:

init_chipset_ich
================

.. c:function:: int init_chipset_ich(struct pci_dev *dev)

    set up the ICH chipset

    :param dev:
        PCI device to set up
    :type dev: struct pci_dev \*

.. _`init_chipset_ich.description`:

Description
-----------

Initialize the PCI device as required.  For the ICH this turns
out to be nice and simple.

.. _`ich_clear_irq`:

ich_clear_irq
=============

.. c:function:: void ich_clear_irq(ide_drive_t *drive)

    clear BMDMA status

    :param drive:
        IDE drive
    :type drive: ide_drive_t \*

.. _`ich_clear_irq.description`:

Description
-----------

ICHx contollers set DMA INTR no matter DMA or PIO.
BMDMA status might need to be cleared even for
PIO interrupts to prevent spurious/lost IRQ.

.. _`init_hwif_piix`:

init_hwif_piix
==============

.. c:function:: void init_hwif_piix(ide_hwif_t *hwif)

    fill in the hwif for the PIIX

    :param hwif:
        IDE interface
    :type hwif: ide_hwif_t \*

.. _`init_hwif_piix.description`:

Description
-----------

Set up the ide_hwif_t for the PIIX interface according to the
capabilities of the hardware.

.. _`piix_init_one`:

piix_init_one
=============

.. c:function:: int piix_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    called when a PIIX is found

    :param dev:
        the piix device
    :type dev: struct pci_dev \*

    :param id:
        the matching pci id
    :type id: const struct pci_device_id \*

.. _`piix_init_one.description`:

Description
-----------

Called when the PCI registration layer (or the IDE initialization)
finds a device matching our IDE device tables.

.. _`piix_check_450nx`:

piix_check_450nx
================

.. c:function:: void piix_check_450nx( void)

    Check for problem 450NX setup

    :param void:
        no arguments
    :type void: 

.. _`piix_check_450nx.description`:

Description
-----------

Check for the present of 450NX errata #19 and errata #25. If
they are found, disable use of DMA IDE

.. This file was automatic generated / don't edit.

