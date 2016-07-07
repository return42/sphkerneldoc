.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/host/pcie-xilinx.c

.. _`xilinx_pcie_port`:

struct xilinx_pcie_port
=======================

.. c:type:: struct xilinx_pcie_port

    PCIe port information

.. _`xilinx_pcie_port.definition`:

Definition
----------

.. code-block:: c

    struct xilinx_pcie_port {
        void __iomem *reg_base;
        u32 irq;
        unsigned long msi_pages;
        u8 root_busno;
        struct device *dev;
        struct irq_domain *irq_domain;
        struct list_head resources;
    }

.. _`xilinx_pcie_port.members`:

Members
-------

reg_base
    IO Mapped Register Base

irq
    Interrupt number

msi_pages
    MSI pages

root_busno
    Root Bus number

dev
    Device pointer

irq_domain
    IRQ domain pointer

resources
    Bus Resources

.. _`xilinx_pcie_clear_err_interrupts`:

xilinx_pcie_clear_err_interrupts
================================

.. c:function:: void xilinx_pcie_clear_err_interrupts(struct xilinx_pcie_port *port)

    Clear Error Interrupts

    :param struct xilinx_pcie_port \*port:
        PCIe port information

.. _`xilinx_pcie_valid_device`:

xilinx_pcie_valid_device
========================

.. c:function:: bool xilinx_pcie_valid_device(struct pci_bus *bus, unsigned int devfn)

    Check if a valid device is present on bus

    :param struct pci_bus \*bus:
        PCI Bus structure

    :param unsigned int devfn:
        device/function

.. _`xilinx_pcie_valid_device.return`:

Return
------

'true' on success and 'false' if invalid device is found

.. _`xilinx_pcie_map_bus`:

xilinx_pcie_map_bus
===================

.. c:function:: void __iomem *xilinx_pcie_map_bus(struct pci_bus *bus, unsigned int devfn, int where)

    Get configuration base

    :param struct pci_bus \*bus:
        PCI Bus structure

    :param unsigned int devfn:
        Device/function

    :param int where:
        Offset from base

.. _`xilinx_pcie_map_bus.return`:

Return
------

Base address of the configuration space needed to be
accessed.

.. _`xilinx_pcie_destroy_msi`:

xilinx_pcie_destroy_msi
=======================

.. c:function:: void xilinx_pcie_destroy_msi(unsigned int irq)

    Free MSI number

    :param unsigned int irq:
        IRQ to be freed

.. _`xilinx_pcie_assign_msi`:

xilinx_pcie_assign_msi
======================

.. c:function:: int xilinx_pcie_assign_msi(struct xilinx_pcie_port *port)

    Allocate MSI number

    :param struct xilinx_pcie_port \*port:
        PCIe port structure

.. _`xilinx_pcie_assign_msi.return`:

Return
------

A valid IRQ on success and error value on failure.

.. _`xilinx_msi_teardown_irq`:

xilinx_msi_teardown_irq
=======================

.. c:function:: void xilinx_msi_teardown_irq(struct msi_controller *chip, unsigned int irq)

    Destroy the MSI

    :param struct msi_controller \*chip:
        MSI Chip descriptor

    :param unsigned int irq:
        MSI IRQ to destroy

.. _`xilinx_pcie_msi_setup_irq`:

xilinx_pcie_msi_setup_irq
=========================

.. c:function:: int xilinx_pcie_msi_setup_irq(struct msi_controller *chip, struct pci_dev *pdev, struct msi_desc *desc)

    Setup MSI request

    :param struct msi_controller \*chip:
        MSI chip pointer

    :param struct pci_dev \*pdev:
        PCIe device pointer

    :param struct msi_desc \*desc:
        MSI descriptor pointer

.. _`xilinx_pcie_msi_setup_irq.return`:

Return
------

'0' on success and error value on failure

.. _`xilinx_pcie_msi_map`:

xilinx_pcie_msi_map
===================

.. c:function:: int xilinx_pcie_msi_map(struct irq_domain *domain, unsigned int irq, irq_hw_number_t hwirq)

    Set the handler for the MSI and mark IRQ as valid

    :param struct irq_domain \*domain:
        IRQ domain

    :param unsigned int irq:
        Virtual IRQ number

    :param irq_hw_number_t hwirq:
        HW interrupt number

.. _`xilinx_pcie_msi_map.return`:

Return
------

Always returns 0.

.. _`xilinx_pcie_enable_msi`:

xilinx_pcie_enable_msi
======================

.. c:function:: void xilinx_pcie_enable_msi(struct xilinx_pcie_port *port)

    Enable MSI support

    :param struct xilinx_pcie_port \*port:
        PCIe port information

.. _`xilinx_pcie_intx_map`:

xilinx_pcie_intx_map
====================

.. c:function:: int xilinx_pcie_intx_map(struct irq_domain *domain, unsigned int irq, irq_hw_number_t hwirq)

    Set the handler for the INTx and mark IRQ as valid

    :param struct irq_domain \*domain:
        IRQ domain

    :param unsigned int irq:
        Virtual IRQ number

    :param irq_hw_number_t hwirq:
        HW interrupt number

.. _`xilinx_pcie_intx_map.return`:

Return
------

Always returns 0.

.. _`xilinx_pcie_intr_handler`:

xilinx_pcie_intr_handler
========================

.. c:function:: irqreturn_t xilinx_pcie_intr_handler(int irq, void *data)

    Interrupt Service Handler

    :param int irq:
        IRQ number

    :param void \*data:
        PCIe port information

.. _`xilinx_pcie_intr_handler.return`:

Return
------

IRQ_HANDLED on success and IRQ_NONE on failure

.. _`xilinx_pcie_free_irq_domain`:

xilinx_pcie_free_irq_domain
===========================

.. c:function:: void xilinx_pcie_free_irq_domain(struct xilinx_pcie_port *port)

    Free IRQ domain

    :param struct xilinx_pcie_port \*port:
        PCIe port information

.. _`xilinx_pcie_init_irq_domain`:

xilinx_pcie_init_irq_domain
===========================

.. c:function:: int xilinx_pcie_init_irq_domain(struct xilinx_pcie_port *port)

    Initialize IRQ domain

    :param struct xilinx_pcie_port \*port:
        PCIe port information

.. _`xilinx_pcie_init_irq_domain.return`:

Return
------

'0' on success and error value on failure

.. _`xilinx_pcie_init_port`:

xilinx_pcie_init_port
=====================

.. c:function:: void xilinx_pcie_init_port(struct xilinx_pcie_port *port)

    Initialize hardware

    :param struct xilinx_pcie_port \*port:
        PCIe port information

.. _`xilinx_pcie_parse_dt`:

xilinx_pcie_parse_dt
====================

.. c:function:: int xilinx_pcie_parse_dt(struct xilinx_pcie_port *port)

    Parse Device tree

    :param struct xilinx_pcie_port \*port:
        PCIe port information

.. _`xilinx_pcie_parse_dt.return`:

Return
------

'0' on success and error value on failure

.. _`xilinx_pcie_probe`:

xilinx_pcie_probe
=================

.. c:function:: int xilinx_pcie_probe(struct platform_device *pdev)

    Probe function

    :param struct platform_device \*pdev:
        Platform device pointer

.. _`xilinx_pcie_probe.return`:

Return
------

'0' on success and error value on failure

.. _`xilinx_pcie_remove`:

xilinx_pcie_remove
==================

.. c:function:: int xilinx_pcie_remove(struct platform_device *pdev)

    Remove function

    :param struct platform_device \*pdev:
        Platform device pointer

.. _`xilinx_pcie_remove.return`:

Return
------

'0' always

.. This file was automatic generated / don't edit.

