.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pcie/aer/aerdrv.c

.. _`set_downstream_devices_error_reporting`:

set_downstream_devices_error_reporting
======================================

.. c:function:: void set_downstream_devices_error_reporting(struct pci_dev *dev, bool enable)

    enable/disable the error reporting  bits on the root port and its downstream ports.

    :param struct pci_dev \*dev:
        pointer to root port's pci_dev data structure

    :param bool enable:
        true = enable error reporting, false = disable error reporting.

.. _`aer_enable_rootport`:

aer_enable_rootport
===================

.. c:function:: void aer_enable_rootport(struct aer_rpc *rpc)

    enable Root Port's interrupts when receiving messages

    :param struct aer_rpc \*rpc:
        pointer to a Root Port data structure

.. _`aer_enable_rootport.description`:

Description
-----------

Invoked when PCIe bus loads AER service driver.

.. _`aer_disable_rootport`:

aer_disable_rootport
====================

.. c:function:: void aer_disable_rootport(struct aer_rpc *rpc)

    disable Root Port's interrupts when receiving messages

    :param struct aer_rpc \*rpc:
        pointer to a Root Port data structure

.. _`aer_disable_rootport.description`:

Description
-----------

Invoked when PCIe bus unloads AER service driver.

.. _`aer_irq`:

aer_irq
=======

.. c:function:: irqreturn_t aer_irq(int irq, void *context)

    Root Port's ISR

    :param int irq:
        IRQ assigned to Root Port

    :param void \*context:
        pointer to Root Port data structure

.. _`aer_irq.description`:

Description
-----------

Invoked when Root Port detects AER messages.

.. _`aer_alloc_rpc`:

aer_alloc_rpc
=============

.. c:function:: struct aer_rpc *aer_alloc_rpc(struct pcie_device *dev)

    allocate Root Port data structure

    :param struct pcie_device \*dev:
        pointer to the pcie_dev data structure

.. _`aer_alloc_rpc.description`:

Description
-----------

Invoked when Root Port's AER service is loaded.

.. _`aer_remove`:

aer_remove
==========

.. c:function:: void aer_remove(struct pcie_device *dev)

    clean up resources

    :param struct pcie_device \*dev:
        pointer to the pcie_dev data structure

.. _`aer_remove.description`:

Description
-----------

Invoked when PCI Express bus unloads or AER probe fails.

.. _`aer_probe`:

aer_probe
=========

.. c:function:: int aer_probe(struct pcie_device *dev)

    initialize resources

    :param struct pcie_device \*dev:
        pointer to the pcie_dev data structure

.. _`aer_probe.description`:

Description
-----------

Invoked when PCI Express bus loads AER service driver.

.. _`aer_root_reset`:

aer_root_reset
==============

.. c:function:: pci_ers_result_t aer_root_reset(struct pci_dev *dev)

    reset link on Root Port

    :param struct pci_dev \*dev:
        pointer to Root Port's pci_dev data structure

.. _`aer_root_reset.description`:

Description
-----------

Invoked by Port Bus driver when performing link reset at Root Port.

.. _`aer_error_resume`:

aer_error_resume
================

.. c:function:: void aer_error_resume(struct pci_dev *dev)

    clean up corresponding error status bits

    :param struct pci_dev \*dev:
        pointer to Root Port's pci_dev data structure

.. _`aer_error_resume.description`:

Description
-----------

Invoked by Port Bus driver during nonfatal recovery.

.. _`aer_service_init`:

aer_service_init
================

.. c:function:: int aer_service_init( void)

    register AER root service driver

    :param  void:
        no arguments

.. _`aer_service_init.description`:

Description
-----------

Invoked when AER root service driver is loaded.

.. This file was automatic generated / don't edit.

