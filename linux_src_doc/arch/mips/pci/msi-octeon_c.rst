.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/pci/msi-octeon.c

.. _`arch_setup_msi_irq`:

arch_setup_msi_irq
==================

.. c:function:: int arch_setup_msi_irq(struct pci_dev *dev, struct msi_desc *desc)

    legacy INT A-D. This routine will allocate multiple interrupts for MSI devices that support them. A device can override this by programming the MSI control bits [6:4] before calling \ :c:func:`pci_enable_msi`\ .

    :param dev:
        Device requesting MSI interrupts
    :type dev: struct pci_dev \*

    :param desc:
        MSI descriptor
    :type desc: struct msi_desc \*

.. _`arch_setup_msi_irq.description`:

Description
-----------

Returns 0 on success.

.. _`arch_teardown_msi_irq`:

arch_teardown_msi_irq
=====================

.. c:function:: void arch_teardown_msi_irq(unsigned int irq)

    MSI interrupts for the device are freed.

    :param irq:
        The devices first irq number. There may be multple in sequence.
    :type irq: unsigned int

.. This file was automatic generated / don't edit.

