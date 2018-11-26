.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pci.h

.. _`pci_interrupt_pin`:

enum pci_interrupt_pin
======================

.. c:type:: enum pci_interrupt_pin

    PCI INTx interrupt values

.. _`pci_interrupt_pin.definition`:

Definition
----------

.. code-block:: c

    enum pci_interrupt_pin {
        PCI_INTERRUPT_UNKNOWN,
        PCI_INTERRUPT_INTA,
        PCI_INTERRUPT_INTB,
        PCI_INTERRUPT_INTC,
        PCI_INTERRUPT_INTD
    };

.. _`pci_interrupt_pin.constants`:

Constants
---------

PCI_INTERRUPT_UNKNOWN
    Unknown or unassigned interrupt

PCI_INTERRUPT_INTA
    PCI INTA pin

PCI_INTERRUPT_INTB
    PCI INTB pin

PCI_INTERRUPT_INTC
    PCI INTC pin

PCI_INTERRUPT_INTD
    PCI INTD pin

.. _`pci_interrupt_pin.description`:

Description
-----------

Corresponds to values for legacy PCI INTx interrupts, as can be found in the
PCI_INTERRUPT_PIN register.

.. _`pci_channel_state_t`:

typedef pci_channel_state_t
===========================

.. c:type:: typedef pci_channel_state_t

    the PCI device.  If some PCI bus between here and the PCI device has crashed or locked up, this info is reflected here.

.. _`pci_is_bridge`:

pci_is_bridge
=============

.. c:function:: bool pci_is_bridge(struct pci_dev *dev)

    check if the PCI device is a bridge

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`pci_is_bridge.description`:

Description
-----------

Return true if the PCI device is bridge whether it has subordinate
or not.

.. _`pci_device`:

PCI_DEVICE
==========

.. c:function::  PCI_DEVICE( vend,  dev)

    macro used to describe a specific PCI device

    :param vend:
        the 16 bit PCI Vendor ID
    :type vend: 

    :param dev:
        the 16 bit PCI Device ID
    :type dev: 

.. _`pci_device.description`:

Description
-----------

This macro is used to create a struct pci_device_id that matches a
specific device.  The subvendor and subdevice fields will be set to
PCI_ANY_ID.

.. _`pci_device_sub`:

PCI_DEVICE_SUB
==============

.. c:function::  PCI_DEVICE_SUB( vend,  dev,  subvend,  subdev)

    macro used to describe a specific PCI device with subsystem

    :param vend:
        the 16 bit PCI Vendor ID
    :type vend: 

    :param dev:
        the 16 bit PCI Device ID
    :type dev: 

    :param subvend:
        the 16 bit PCI Subvendor ID
    :type subvend: 

    :param subdev:
        the 16 bit PCI Subdevice ID
    :type subdev: 

.. _`pci_device_sub.description`:

Description
-----------

This macro is used to create a struct pci_device_id that matches a
specific device with subsystem information.

.. _`pci_device_class`:

PCI_DEVICE_CLASS
================

.. c:function::  PCI_DEVICE_CLASS( dev_class,  dev_class_mask)

    macro used to describe a specific PCI device class

    :param dev_class:
        the class, subclass, prog-if triple for this device
    :type dev_class: 

    :param dev_class_mask:
        the class mask for this device
    :type dev_class_mask: 

.. _`pci_device_class.description`:

Description
-----------

This macro is used to create a struct pci_device_id that matches a
specific PCI class.  The vendor, device, subvendor, and subdevice
fields will be set to PCI_ANY_ID.

.. _`pci_vdevice`:

PCI_VDEVICE
===========

.. c:function::  PCI_VDEVICE( vend,  dev)

    macro used to describe a specific PCI device in short form

    :param vend:
        the vendor name
    :type vend: 

    :param dev:
        the 16 bit PCI Device ID
    :type dev: 

.. _`pci_vdevice.description`:

Description
-----------

This macro is used to create a struct pci_device_id that matches a
specific PCI device.  The subvendor, and subdevice fields will be set
to PCI_ANY_ID. The macro allows the next field to follow as the device
private data.

.. _`pci_device_data`:

PCI_DEVICE_DATA
===============

.. c:function::  PCI_DEVICE_DATA( vend,  dev,  data)

    macro used to describe a specific PCI device in very short form

    :param vend:
        the vendor name (without PCI_VENDOR_ID\_ prefix)
    :type vend: 

    :param dev:
        the device name (without PCI_DEVICE_ID_<vend>_ prefix)
    :type dev: 

    :param data:
        the driver data to be filled
    :type data: 

.. _`pci_device_data.description`:

Description
-----------

This macro is used to create a struct pci_device_id that matches a
specific PCI device.  The subvendor, and subdevice fields will be set
to PCI_ANY_ID.

.. _`module_pci_driver`:

module_pci_driver
=================

.. c:function::  module_pci_driver( __pci_driver)

    Helper macro for registering a PCI driver

    :param __pci_driver:
        pci_driver struct
    :type __pci_driver: 

.. _`module_pci_driver.description`:

Description
-----------

Helper macro for PCI drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. _`builtin_pci_driver`:

builtin_pci_driver
==================

.. c:function::  builtin_pci_driver( __pci_driver)

    Helper macro for registering a PCI driver

    :param __pci_driver:
        pci_driver struct
    :type __pci_driver: 

.. _`builtin_pci_driver.description`:

Description
-----------

Helper macro for PCI drivers which do not do anything special in their
init code. This eliminates a lot of boilerplate. Each driver may only
use this macro once, and calling it replaces device_initcall(...)

.. _`pci_irqd_intx_xlate`:

pci_irqd_intx_xlate
===================

.. c:function:: int pci_irqd_intx_xlate(struct irq_domain *d, struct device_node *node, const u32 *intspec, unsigned int intsize, unsigned long *out_hwirq, unsigned int *out_type)

    Translate PCI INTx value to an IRQ domain hwirq

    :param d:
        the INTx IRQ domain
    :type d: struct irq_domain \*

    :param node:
        the DT node for the device whose interrupt we're translating
    :type node: struct device_node \*

    :param intspec:
        the interrupt specifier data from the DT
    :type intspec: const u32 \*

    :param intsize:
        the number of entries in \ ``intspec``\ 
    :type intsize: unsigned int

    :param out_hwirq:
        pointer at which to write the hwirq number
    :type out_hwirq: unsigned long \*

    :param out_type:
        pointer at which to write the interrupt type
    :type out_type: unsigned int \*

.. _`pci_irqd_intx_xlate.description`:

Description
-----------

Translate a PCI INTx interrupt number from device tree in the range 1-4, as
stored in the standard PCI_INTERRUPT_PIN register, to a value in the range
0-3 suitable for use in a 4 entry IRQ domain. That is, subtract one from the
INTx value to obtain the hwirq number.

Returns 0 on success, or -EINVAL if the interrupt specifier is out of range.

.. _`pci_pcie_cap`:

pci_pcie_cap
============

.. c:function:: int pci_pcie_cap(struct pci_dev *dev)

    get the saved PCIe capability offset

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`pci_pcie_cap.description`:

Description
-----------

PCIe capability offset is calculated at PCI device initialization
time and saved in the data structure. This function returns saved
PCIe capability offset. Using this instead of \ :c:func:`pci_find_capability`\ 
reduces unnecessary search in the PCI configuration space. If you
need to calculate PCIe capability offset from raw device for some
reasons, please use \ :c:func:`pci_find_capability`\  instead.

.. _`pci_is_pcie`:

pci_is_pcie
===========

.. c:function:: bool pci_is_pcie(struct pci_dev *dev)

    check if the PCI device is PCI Express capable

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`pci_is_pcie.return`:

Return
------

true if the PCI device is PCI Express capable, false otherwise.

.. _`pcie_caps_reg`:

pcie_caps_reg
=============

.. c:function:: u16 pcie_caps_reg(const struct pci_dev *dev)

    get the PCIe Capabilities Register

    :param dev:
        PCI device
    :type dev: const struct pci_dev \*

.. _`pci_pcie_type`:

pci_pcie_type
=============

.. c:function:: int pci_pcie_type(const struct pci_dev *dev)

    get the PCIe device/port type

    :param dev:
        PCI device
    :type dev: const struct pci_dev \*

.. _`pci_vpd_lrdt_size`:

pci_vpd_lrdt_size
=================

.. c:function:: u16 pci_vpd_lrdt_size(const u8 *lrdt)

    Extracts the Large Resource Data Type length

    :param lrdt:
        Pointer to the beginning of the Large Resource Data Type tag
    :type lrdt: const u8 \*

.. _`pci_vpd_lrdt_size.description`:

Description
-----------

Returns the extracted Large Resource Data Type length.

.. _`pci_vpd_lrdt_tag`:

pci_vpd_lrdt_tag
================

.. c:function:: u16 pci_vpd_lrdt_tag(const u8 *lrdt)

    Extracts the Large Resource Data Type Tag Item

    :param lrdt:
        Pointer to the beginning of the Large Resource Data Type tag
    :type lrdt: const u8 \*

.. _`pci_vpd_lrdt_tag.description`:

Description
-----------

Returns the extracted Large Resource Data Type Tag item.

.. _`pci_vpd_srdt_size`:

pci_vpd_srdt_size
=================

.. c:function:: u8 pci_vpd_srdt_size(const u8 *srdt)

    Extracts the Small Resource Data Type length

    :param srdt:
        Pointer to the beginning of the Small Resource Data Type tag
    :type srdt: const u8 \*

.. _`pci_vpd_srdt_size.description`:

Description
-----------

Returns the extracted Small Resource Data Type length.

.. _`pci_vpd_srdt_tag`:

pci_vpd_srdt_tag
================

.. c:function:: u8 pci_vpd_srdt_tag(const u8 *srdt)

    Extracts the Small Resource Data Type Tag Item

    :param srdt:
        Pointer to the beginning of the Small Resource Data Type tag
    :type srdt: const u8 \*

.. _`pci_vpd_srdt_tag.description`:

Description
-----------

Returns the extracted Small Resource Data Type Tag Item.

.. _`pci_vpd_info_field_size`:

pci_vpd_info_field_size
=======================

.. c:function:: u8 pci_vpd_info_field_size(const u8 *info_field)

    Extracts the information field length

    :param info_field:
        *undescribed*
    :type info_field: const u8 \*

.. _`pci_vpd_info_field_size.description`:

Description
-----------

Returns the extracted information field length.

.. _`pci_vpd_find_tag`:

pci_vpd_find_tag
================

.. c:function:: int pci_vpd_find_tag(const u8 *buf, unsigned int off, unsigned int len, u8 rdt)

    Locates the Resource Data Type tag provided

    :param buf:
        Pointer to buffered vpd data
    :type buf: const u8 \*

    :param off:
        The offset into the buffer at which to begin the search
    :type off: unsigned int

    :param len:
        The length of the vpd buffer
    :type len: unsigned int

    :param rdt:
        The Resource Data Type to search for
    :type rdt: u8

.. _`pci_vpd_find_tag.description`:

Description
-----------

Returns the index where the Resource Data Type was found or
-ENOENT otherwise.

.. _`pci_vpd_find_info_keyword`:

pci_vpd_find_info_keyword
=========================

.. c:function:: int pci_vpd_find_info_keyword(const u8 *buf, unsigned int off, unsigned int len, const char *kw)

    Locates an information field keyword in the VPD

    :param buf:
        Pointer to buffered vpd data
    :type buf: const u8 \*

    :param off:
        The offset into the buffer at which to begin the search
    :type off: unsigned int

    :param len:
        The length of the buffer area, relative to off, in which to search
    :type len: unsigned int

    :param kw:
        The keyword to search for
    :type kw: const char \*

.. _`pci_vpd_find_info_keyword.description`:

Description
-----------

Returns the index where the information field keyword was found or
-ENOENT otherwise.

.. _`pci_ari_enabled`:

pci_ari_enabled
===============

.. c:function:: bool pci_ari_enabled(struct pci_bus *bus)

    query ARI forwarding status

    :param bus:
        the PCI bus
    :type bus: struct pci_bus \*

.. _`pci_ari_enabled.description`:

Description
-----------

Returns true if ARI forwarding is enabled.

.. _`pci_is_thunderbolt_attached`:

pci_is_thunderbolt_attached
===========================

.. c:function:: bool pci_is_thunderbolt_attached(struct pci_dev *pdev)

    whether device is on a Thunderbolt daisy chain

    :param pdev:
        PCI device to check
    :type pdev: struct pci_dev \*

.. _`pci_is_thunderbolt_attached.description`:

Description
-----------

Walk upwards from \ ``pdev``\  and check for each encountered bridge if it's part
of a Thunderbolt controller.  Reaching the host bridge means \ ``pdev``\  is not
Thunderbolt-attached.  (But rather soldered to the mainboard usually.)

.. This file was automatic generated / don't edit.

