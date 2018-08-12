.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pcie/aer.c

.. _`enable_ecrc_checking`:

enable_ecrc_checking
====================

.. c:function:: int enable_ecrc_checking(struct pci_dev *dev)

    enable PCIe ECRC checking for a device

    :param struct pci_dev \*dev:
        the PCI device

.. _`enable_ecrc_checking.description`:

Description
-----------

Returns 0 on success, or negative on failure.

.. _`disable_ecrc_checking`:

disable_ecrc_checking
=====================

.. c:function:: int disable_ecrc_checking(struct pci_dev *dev)

    disables PCIe ECRC checking for a device

    :param struct pci_dev \*dev:
        the PCI device

.. _`disable_ecrc_checking.description`:

Description
-----------

Returns 0 on success, or negative on failure.

.. _`pcie_set_ecrc_checking`:

pcie_set_ecrc_checking
======================

.. c:function:: void pcie_set_ecrc_checking(struct pci_dev *dev)

    set/unset PCIe ECRC checking for a device based on global policy

    :param struct pci_dev \*dev:
        the PCI device

.. _`pcie_ecrc_get_policy`:

pcie_ecrc_get_policy
====================

.. c:function:: void pcie_ecrc_get_policy(char *str)

    parse kernel command-line ecrc option

    :param char \*str:
        *undescribed*

.. _`aer_acpi_firmware_first`:

aer_acpi_firmware_first
=======================

.. c:function:: bool aer_acpi_firmware_first( void)

    Check if APEI should control AER.

    :param  void:
        no arguments

.. _`add_error_device`:

add_error_device
================

.. c:function:: int add_error_device(struct aer_err_info *e_info, struct pci_dev *dev)

    list device to be handled

    :param struct aer_err_info \*e_info:
        pointer to error info

    :param struct pci_dev \*dev:
        pointer to pci_dev to be added

.. _`is_error_source`:

is_error_source
===============

.. c:function:: bool is_error_source(struct pci_dev *dev, struct aer_err_info *e_info)

    check whether the device is source of reported error

    :param struct pci_dev \*dev:
        pointer to pci_dev to be checked

    :param struct aer_err_info \*e_info:
        pointer to reported error info

.. _`find_source_device`:

find_source_device
==================

.. c:function:: bool find_source_device(struct pci_dev *parent, struct aer_err_info *e_info)

    search through device hierarchy for source device

    :param struct pci_dev \*parent:
        pointer to Root Port pci_dev data structure

    :param struct aer_err_info \*e_info:
        including detailed error information such like id

.. _`find_source_device.description`:

Description
-----------

Return true if found.

Invoked by DPC when error is detected at the Root Port.
Caller of this function must set id, severity, and multi_error_valid of
struct aer_err_info pointed by \ ``e_info``\  properly.  This function must fill
e_info->error_dev_num and e_info->dev[], based on the given information.

.. _`handle_error_source`:

handle_error_source
===================

.. c:function:: void handle_error_source(struct pci_dev *dev, struct aer_err_info *info)

    handle logging error into an event log

    :param struct pci_dev \*dev:
        pointer to pci_dev data structure of error source device

    :param struct aer_err_info \*info:
        comprehensive error information

.. _`handle_error_source.description`:

Description
-----------

Invoked when an error being detected by Root Port.

.. _`get_device_error_info`:

get_device_error_info
=====================

.. c:function:: int get_device_error_info(struct pci_dev *dev, struct aer_err_info *info)

    read error status from dev and store it to info

    :param struct pci_dev \*dev:
        pointer to the device expected to have a error record

    :param struct aer_err_info \*info:
        pointer to structure to store the error record

.. _`get_device_error_info.description`:

Description
-----------

Return 1 on success, 0 on error.

Note that \ ``info``\  is reused among all error devices. Clear fields properly.

.. _`aer_isr_one_error`:

aer_isr_one_error
=================

.. c:function:: void aer_isr_one_error(struct aer_rpc *rpc, struct aer_err_source *e_src)

    consume an error detected by root port

    :param struct aer_rpc \*rpc:
        pointer to the root port which holds an error

    :param struct aer_err_source \*e_src:
        pointer to an error source

.. _`get_e_source`:

get_e_source
============

.. c:function:: int get_e_source(struct aer_rpc *rpc, struct aer_err_source *e_src)

    retrieve an error source

    :param struct aer_rpc \*rpc:
        pointer to the root port which holds an error

    :param struct aer_err_source \*e_src:
        pointer to store retrieved error source

.. _`get_e_source.description`:

Description
-----------

Return 1 if an error source is retrieved, otherwise 0.

Invoked by DPC handler to consume an error.

.. _`aer_isr`:

aer_isr
=======

.. c:function:: void aer_isr(struct work_struct *work)

    consume errors detected by root port

    :param struct work_struct \*work:
        definition of this work item

.. _`aer_isr.description`:

Description
-----------

Invoked, as DPC, when root port records new detected error

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

