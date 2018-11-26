.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pcie/aer.c

.. _`enable_ecrc_checking`:

enable_ecrc_checking
====================

.. c:function:: int enable_ecrc_checking(struct pci_dev *dev)

    enable PCIe ECRC checking for a device

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`enable_ecrc_checking.description`:

Description
-----------

Returns 0 on success, or negative on failure.

.. _`disable_ecrc_checking`:

disable_ecrc_checking
=====================

.. c:function:: int disable_ecrc_checking(struct pci_dev *dev)

    disables PCIe ECRC checking for a device

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`disable_ecrc_checking.description`:

Description
-----------

Returns 0 on success, or negative on failure.

.. _`pcie_set_ecrc_checking`:

pcie_set_ecrc_checking
======================

.. c:function:: void pcie_set_ecrc_checking(struct pci_dev *dev)

    set/unset PCIe ECRC checking for a device based on global policy

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pcie_ecrc_get_policy`:

pcie_ecrc_get_policy
====================

.. c:function:: void pcie_ecrc_get_policy(char *str)

    parse kernel command-line ecrc option

    :param str:
        *undescribed*
    :type str: char \*

.. _`aer_acpi_firmware_first`:

aer_acpi_firmware_first
=======================

.. c:function:: bool aer_acpi_firmware_first( void)

    Check if APEI should control AER.

    :param void:
        no arguments
    :type void: 

.. _`add_error_device`:

add_error_device
================

.. c:function:: int add_error_device(struct aer_err_info *e_info, struct pci_dev *dev)

    list device to be handled

    :param e_info:
        pointer to error info
    :type e_info: struct aer_err_info \*

    :param dev:
        pointer to pci_dev to be added
    :type dev: struct pci_dev \*

.. _`is_error_source`:

is_error_source
===============

.. c:function:: bool is_error_source(struct pci_dev *dev, struct aer_err_info *e_info)

    check whether the device is source of reported error

    :param dev:
        pointer to pci_dev to be checked
    :type dev: struct pci_dev \*

    :param e_info:
        pointer to reported error info
    :type e_info: struct aer_err_info \*

.. _`find_source_device`:

find_source_device
==================

.. c:function:: bool find_source_device(struct pci_dev *parent, struct aer_err_info *e_info)

    search through device hierarchy for source device

    :param parent:
        pointer to Root Port pci_dev data structure
    :type parent: struct pci_dev \*

    :param e_info:
        including detailed error information such like id
    :type e_info: struct aer_err_info \*

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

    :param dev:
        pointer to pci_dev data structure of error source device
    :type dev: struct pci_dev \*

    :param info:
        comprehensive error information
    :type info: struct aer_err_info \*

.. _`handle_error_source.description`:

Description
-----------

Invoked when an error being detected by Root Port.

.. _`aer_get_device_error_info`:

aer_get_device_error_info
=========================

.. c:function:: int aer_get_device_error_info(struct pci_dev *dev, struct aer_err_info *info)

    read error status from dev and store it to info

    :param dev:
        pointer to the device expected to have a error record
    :type dev: struct pci_dev \*

    :param info:
        pointer to structure to store the error record
    :type info: struct aer_err_info \*

.. _`aer_get_device_error_info.description`:

Description
-----------

Return 1 on success, 0 on error.

Note that \ ``info``\  is reused among all error devices. Clear fields properly.

.. _`aer_isr_one_error`:

aer_isr_one_error
=================

.. c:function:: void aer_isr_one_error(struct aer_rpc *rpc, struct aer_err_source *e_src)

    consume an error detected by root port

    :param rpc:
        pointer to the root port which holds an error
    :type rpc: struct aer_rpc \*

    :param e_src:
        pointer to an error source
    :type e_src: struct aer_err_source \*

.. _`aer_isr`:

aer_isr
=======

.. c:function:: irqreturn_t aer_isr(int irq, void *context)

    consume errors detected by root port

    :param irq:
        *undescribed*
    :type irq: int

    :param context:
        *undescribed*
    :type context: void \*

.. _`aer_isr.description`:

Description
-----------

Invoked, as DPC, when root port records new detected error

.. _`aer_irq`:

aer_irq
=======

.. c:function:: irqreturn_t aer_irq(int irq, void *context)

    Root Port's ISR

    :param irq:
        IRQ assigned to Root Port
    :type irq: int

    :param context:
        pointer to Root Port data structure
    :type context: void \*

.. _`aer_irq.description`:

Description
-----------

Invoked when Root Port detects AER messages.

.. _`set_downstream_devices_error_reporting`:

set_downstream_devices_error_reporting
======================================

.. c:function:: void set_downstream_devices_error_reporting(struct pci_dev *dev, bool enable)

    enable/disable the error reporting  bits on the root port and its downstream ports.

    :param dev:
        pointer to root port's pci_dev data structure
    :type dev: struct pci_dev \*

    :param enable:
        true = enable error reporting, false = disable error reporting.
    :type enable: bool

.. _`aer_enable_rootport`:

aer_enable_rootport
===================

.. c:function:: void aer_enable_rootport(struct aer_rpc *rpc)

    enable Root Port's interrupts when receiving messages

    :param rpc:
        pointer to a Root Port data structure
    :type rpc: struct aer_rpc \*

.. _`aer_enable_rootport.description`:

Description
-----------

Invoked when PCIe bus loads AER service driver.

.. _`aer_disable_rootport`:

aer_disable_rootport
====================

.. c:function:: void aer_disable_rootport(struct aer_rpc *rpc)

    disable Root Port's interrupts when receiving messages

    :param rpc:
        pointer to a Root Port data structure
    :type rpc: struct aer_rpc \*

.. _`aer_disable_rootport.description`:

Description
-----------

Invoked when PCIe bus unloads AER service driver.

.. _`aer_remove`:

aer_remove
==========

.. c:function:: void aer_remove(struct pcie_device *dev)

    clean up resources

    :param dev:
        pointer to the pcie_dev data structure
    :type dev: struct pcie_device \*

.. _`aer_remove.description`:

Description
-----------

Invoked when PCI Express bus unloads or AER probe fails.

.. _`aer_probe`:

aer_probe
=========

.. c:function:: int aer_probe(struct pcie_device *dev)

    initialize resources

    :param dev:
        pointer to the pcie_dev data structure
    :type dev: struct pcie_device \*

.. _`aer_probe.description`:

Description
-----------

Invoked when PCI Express bus loads AER service driver.

.. _`aer_root_reset`:

aer_root_reset
==============

.. c:function:: pci_ers_result_t aer_root_reset(struct pci_dev *dev)

    reset link on Root Port

    :param dev:
        pointer to Root Port's pci_dev data structure
    :type dev: struct pci_dev \*

.. _`aer_root_reset.description`:

Description
-----------

Invoked by Port Bus driver when performing link reset at Root Port.

.. _`pcie_aer_init`:

pcie_aer_init
=============

.. c:function:: int pcie_aer_init( void)

    register AER root service driver

    :param void:
        no arguments
    :type void: 

.. _`pcie_aer_init.description`:

Description
-----------

Invoked when AER root service driver is loaded.

.. This file was automatic generated / don't edit.

