.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pcie/portdrv_acpi.c

.. _`pcie_port_acpi_setup`:

pcie_port_acpi_setup
====================

.. c:function:: void pcie_port_acpi_setup(struct pci_dev *port, int *srv_mask)

    Request the BIOS to release control of PCIe services.

    :param struct pci_dev \*port:
        PCIe Port service for a root port or event collector.

    :param int \*srv_mask:
        Bit mask of services that can be enabled for \ ``port``\ .

.. _`pcie_port_acpi_setup.description`:

Description
-----------

Invoked when \ ``port``\  is identified as a PCIe port device.  To avoid conflicts
with the BIOS PCIe port native services support requires the BIOS to yield
control of these services to the kernel.  The mask of services that the BIOS
allows to be enabled for \ ``port``\  is written to \ ``srv_mask``\ .

.. _`pcie_port_acpi_setup.note`:

NOTE
----

It turns out that we cannot do that for individual port services
separately, because that would make some systems work incorrectly.

.. This file was automatic generated / don't edit.

