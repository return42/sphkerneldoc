.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/setup-pci.c

.. _`ide_setup_pci_baseregs`:

ide_setup_pci_baseregs
======================

.. c:function:: int ide_setup_pci_baseregs(struct pci_dev *dev, const char *name)

    place a PCI IDE controller native

    :param struct pci_dev \*dev:
        PCI device of interface to switch native

    :param const char \*name:
        Name of interface

.. _`ide_setup_pci_baseregs.description`:

Description
-----------

We attempt to place the PCI interface into PCI native mode. If
we succeed the BARs are ok and the controller is in PCI mode.
Returns 0 on success or an errno code.

.. _`ide_setup_pci_baseregs.fixme`:

FIXME
-----

if we program the interface and then fail to set the BARS
we don't switch it back to legacy mode. Do we actually care ??

.. _`ide_pci_dma_base`:

ide_pci_dma_base
================

.. c:function:: unsigned long ide_pci_dma_base(ide_hwif_t *hwif, const struct ide_port_info *d)

    setup BMIBA

    :param ide_hwif_t \*hwif:
        IDE interface

    :param const struct ide_port_info \*d:
        IDE port info

.. _`ide_pci_dma_base.description`:

Description
-----------

Fetch the DMA Bus-Master-I/O-Base-Address (BMIBA) from PCI space.

.. _`ide_pci_enable`:

ide_pci_enable
==============

.. c:function:: int ide_pci_enable(struct pci_dev *dev, const struct ide_port_info *d)

    do PCI enables

    :param struct pci_dev \*dev:
        PCI device

    :param const struct ide_port_info \*d:
        IDE port info

.. _`ide_pci_enable.description`:

Description
-----------

Enable the IDE PCI device. We attempt to enable the device in full
but if that fails then we only need IO space. The PCI code should
have setup the proper resources for us already for controllers in
legacy mode.

Returns zero on success or an error code

.. _`ide_pci_configure`:

ide_pci_configure
=================

.. c:function:: int ide_pci_configure(struct pci_dev *dev, const struct ide_port_info *d)

    configure an unconfigured device

    :param struct pci_dev \*dev:
        PCI device

    :param const struct ide_port_info \*d:
        IDE port info

.. _`ide_pci_configure.description`:

Description
-----------

Enable and configure the PCI device we have been passed.
Returns zero on success or an error code.

.. _`ide_pci_check_iomem`:

ide_pci_check_iomem
===================

.. c:function:: int ide_pci_check_iomem(struct pci_dev *dev, const struct ide_port_info *d, int bar)

    check a register is I/O

    :param struct pci_dev \*dev:
        PCI device

    :param const struct ide_port_info \*d:
        IDE port info

    :param int bar:
        BAR number

.. _`ide_pci_check_iomem.description`:

Description
-----------

Checks if a BAR is configured and points to MMIO space. If so,
return an error code. Otherwise return 0

.. _`ide_hw_configure`:

ide_hw_configure
================

.. c:function:: int ide_hw_configure(struct pci_dev *dev, const struct ide_port_info *d, unsigned int port, struct ide_hw *hw)

    configure a struct ide_hw instance

    :param struct pci_dev \*dev:
        PCI device holding interface

    :param const struct ide_port_info \*d:
        IDE port info

    :param unsigned int port:
        port number

    :param struct ide_hw \*hw:
        struct ide_hw instance corresponding to this port

.. _`ide_hw_configure.description`:

Description
-----------

Perform the initial set up for the hardware interface structure. This
is done per interface port rather than per PCI device. There may be
more than one port per device.

Returns zero on success or an error code.

.. _`ide_hwif_setup_dma`:

ide_hwif_setup_dma
==================

.. c:function:: int ide_hwif_setup_dma(ide_hwif_t *hwif, const struct ide_port_info *d)

    configure DMA interface

    :param ide_hwif_t \*hwif:
        IDE interface

    :param const struct ide_port_info \*d:
        IDE port info

.. _`ide_hwif_setup_dma.description`:

Description
-----------

Set up the DMA base for the interface. Enable the master bits as
necessary and attempt to bring the device DMA into a ready to use
state

.. _`ide_setup_pci_controller`:

ide_setup_pci_controller
========================

.. c:function:: int ide_setup_pci_controller(struct pci_dev *dev, const struct ide_port_info *d, int noisy)

    set up IDE PCI

    :param struct pci_dev \*dev:
        PCI device

    :param const struct ide_port_info \*d:
        IDE port info

    :param int noisy:
        verbose flag

.. _`ide_setup_pci_controller.description`:

Description
-----------

Set up the PCI and controller side of the IDE interface. This brings
up the PCI side of the device, checks that the device is enabled
and enables it if need be

.. _`ide_pci_setup_ports`:

ide_pci_setup_ports
===================

.. c:function:: void ide_pci_setup_ports(struct pci_dev *dev, const struct ide_port_info *d, struct ide_hw *hw, struct ide_hw **hws)

    configure ports/devices on PCI IDE

    :param struct pci_dev \*dev:
        PCI device

    :param const struct ide_port_info \*d:
        IDE port info

    :param struct ide_hw \*hw:
        struct ide_hw instances corresponding to this PCI IDE device

    :param struct ide_hw \*\*hws:
        struct ide_hw pointers table to update

.. _`ide_pci_setup_ports.description`:

Description
-----------

Scan the interfaces attached to this device and do any
necessary per port setup. Attach the devices and ask the
generic DMA layer to do its work for us.

Normally called automaticall from do_ide_pci_setup_device,
but is also used directly as a helper function by some controllers
where the chipset setup is not the default PCI IDE one.

.. This file was automatic generated / don't edit.

