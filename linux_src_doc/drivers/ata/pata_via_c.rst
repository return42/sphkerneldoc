.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_via.c

.. _`via_cable_detect`:

via_cable_detect
================

.. c:function:: int via_cable_detect(struct ata_port *ap)

    cable detection

    :param ap:
        ATA port
    :type ap: struct ata_port \*

.. _`via_cable_detect.description`:

Description
-----------

Perform cable detection. Actually for the VIA case the BIOS
already did this for us. We read the values provided by the
BIOS. If you are using an 8235 in a non-PC configuration you
may need to update this code.

Hotplug also impacts on this.

.. _`via_do_set_mode`:

via_do_set_mode
===============

.. c:function:: void via_do_set_mode(struct ata_port *ap, struct ata_device *adev, int mode, int set_ast, int udma_type)

    set transfer mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

    :param mode:
        ATA mode being programmed
    :type mode: int

    :param set_ast:
        Set to program address setup
    :type set_ast: int

    :param udma_type:
        UDMA mode/format of registers
    :type udma_type: int

.. _`via_do_set_mode.description`:

Description
-----------

Program the VIA registers for DMA and PIO modes. Uses the ata timing
support in order to compute modes.

.. _`via_do_set_mode.fixme`:

FIXME
-----

Hotplug will require we serialize multiple mode changes
on the two channels.

.. _`via_mode_filter`:

via_mode_filter
===============

.. c:function:: unsigned long via_mode_filter(struct ata_device *dev, unsigned long mask)

    filter buggy device/mode pairs

    :param dev:
        ATA device
    :type dev: struct ata_device \*

    :param mask:
        Mode bitmask
    :type mask: unsigned long

.. _`via_mode_filter.description`:

Description
-----------

We need to apply some minimal filtering for old controllers and at least
one breed of Transcend SSD. Return the updated mask.

.. _`via_tf_load`:

via_tf_load
===========

.. c:function:: void via_tf_load(struct ata_port *ap, const struct ata_taskfile *tf)

    send taskfile registers to host controller

    :param ap:
        Port to which output is sent
    :type ap: struct ata_port \*

    :param tf:
        ATA taskfile register set
    :type tf: const struct ata_taskfile \*

.. _`via_tf_load.description`:

Description
-----------

Outputs ATA taskfile to standard ATA host controller.

.. _`via_tf_load.note`:

Note
----

This is to fix the internal bug of via chipsets, which
will reset the device register after changing the IEN bit on
ctl register

.. _`via_config_fifo`:

via_config_fifo
===============

.. c:function:: void via_config_fifo(struct pci_dev *pdev, unsigned int flags)

    set up the FIFO

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param flags:
        configuration flags
    :type flags: unsigned int

.. _`via_config_fifo.description`:

Description
-----------

Set the FIFO properties for this device if necessary. Used both on
set up and on and the resume path

.. _`via_init_one`:

via_init_one
============

.. c:function:: int via_init_one(struct pci_dev *pdev, const struct pci_device_id *id)

    discovery callback

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param id:
        PCI table info
    :type id: const struct pci_device_id \*

.. _`via_init_one.description`:

Description
-----------

A VIA IDE interface has been discovered. Figure out what revision
and perform configuration work before handing it to the ATA layer

.. _`via_reinit_one`:

via_reinit_one
==============

.. c:function:: int via_reinit_one(struct pci_dev *pdev)

    reinit after resume \ ``pdev``\ ; PCI device

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

.. _`via_reinit_one.description`:

Description
-----------

Called when the VIA PATA device is resumed. We must then
reconfigure the fifo and other setup we may have altered. In
addition the kernel needs to have the resume methods on PCI
quirk supported.

.. This file was automatic generated / don't edit.

