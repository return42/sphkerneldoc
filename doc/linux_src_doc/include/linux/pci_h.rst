.. -*- coding: utf-8; mode: rst -*-

=====
pci.h
=====


.. _`pci_is_bridge`:

pci_is_bridge
=============

.. c:function:: bool pci_is_bridge (struct pci_dev *dev)

    check if the PCI device is a bridge

    :param struct pci_dev \*dev:
        PCI device



.. _`pci_is_bridge.description`:

Description
-----------

Return true if the PCI device is bridge whether it has subordinate
or not.



.. _`define_pci_device_table`:

DEFINE_PCI_DEVICE_TABLE
=======================

.. c:function:: DEFINE_PCI_DEVICE_TABLE ( _table)

    macro used to describe a pci device table

    :param _table:
        device table name



.. _`define_pci_device_table.description`:

Description
-----------

This macro is deprecated and should not be used in new code.



.. _`pci_device`:

PCI_DEVICE
==========

.. c:function:: PCI_DEVICE ( vend,  dev)

    macro used to describe a specific pci device

    :param vend:
        the 16 bit PCI Vendor ID

    :param dev:
        the 16 bit PCI Device ID



.. _`pci_device.description`:

Description
-----------

This macro is used to create a struct pci_device_id that matches a
specific device.  The subvendor and subdevice fields will be set to
PCI_ANY_ID.



.. _`pci_device_sub`:

PCI_DEVICE_SUB
==============

.. c:function:: PCI_DEVICE_SUB ( vend,  dev,  subvend,  subdev)

    macro used to describe a specific pci device with subsystem

    :param vend:
        the 16 bit PCI Vendor ID

    :param dev:
        the 16 bit PCI Device ID

    :param subvend:
        the 16 bit PCI Subvendor ID

    :param subdev:
        the 16 bit PCI Subdevice ID



.. _`pci_device_sub.description`:

Description
-----------

This macro is used to create a struct pci_device_id that matches a
specific device with subsystem information.



.. _`pci_device_class`:

PCI_DEVICE_CLASS
================

.. c:function:: PCI_DEVICE_CLASS ( dev_class,  dev_class_mask)

    macro used to describe a specific pci device class

    :param dev_class:
        the class, subclass, prog-if triple for this device

    :param dev_class_mask:
        the class mask for this device



.. _`pci_device_class.description`:

Description
-----------

This macro is used to create a struct pci_device_id that matches a
specific PCI class.  The vendor, device, subvendor, and subdevice
fields will be set to PCI_ANY_ID.



.. _`pci_vdevice`:

PCI_VDEVICE
===========

.. c:function:: PCI_VDEVICE ( vend,  dev)

    macro used to describe a specific pci device in short form

    :param vend:
        the vendor name

    :param dev:
        the 16 bit PCI Device ID



.. _`pci_vdevice.description`:

Description
-----------

This macro is used to create a struct pci_device_id that matches a
specific PCI device.  The subvendor, and subdevice fields will be set
to PCI_ANY_ID. The macro allows the next field to follow as the device
private data.



.. _`module_pci_driver`:

module_pci_driver
=================

.. c:function:: module_pci_driver ( __pci_driver)

    Helper macro for registering a PCI driver

    :param __pci_driver:
        pci_driver struct



.. _`module_pci_driver.description`:

Description
-----------

Helper macro for PCI drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces :c:func:`module_init` and :c:func:`module_exit`



.. _`builtin_pci_driver`:

builtin_pci_driver
==================

.. c:function:: builtin_pci_driver ( __pci_driver)

    Helper macro for registering a PCI driver

    :param __pci_driver:
        pci_driver struct



.. _`builtin_pci_driver.description`:

Description
-----------

Helper macro for PCI drivers which do not do anything special in their
init code. This eliminates a lot of boilerplate. Each driver may only
use this macro once, and calling it replaces device_initcall(...)



.. _`pci_pcie_cap`:

pci_pcie_cap
============

.. c:function:: int pci_pcie_cap (struct pci_dev *dev)

    get the saved PCIe capability offset

    :param struct pci_dev \*dev:
        PCI device



.. _`pci_pcie_cap.description`:

Description
-----------

PCIe capability offset is calculated at PCI device initialization
time and saved in the data structure. This function returns saved
PCIe capability offset. Using this instead of :c:func:`pci_find_capability`
reduces unnecessary search in the PCI configuration space. If you
need to calculate PCIe capability offset from raw device for some
reasons, please use :c:func:`pci_find_capability` instead.



.. _`pci_is_pcie`:

pci_is_pcie
===========

.. c:function:: bool pci_is_pcie (struct pci_dev *dev)

    check if the PCI device is PCI Express capable

    :param struct pci_dev \*dev:
        PCI device



.. _`pci_is_pcie.returns`:

Returns
-------

true if the PCI device is PCI Express capable, false otherwise.



.. _`pcie_caps_reg`:

pcie_caps_reg
=============

.. c:function:: u16 pcie_caps_reg (const struct pci_dev *dev)

    get the PCIe Capabilities Register

    :param const struct pci_dev \*dev:
        PCI device



.. _`pci_pcie_type`:

pci_pcie_type
=============

.. c:function:: int pci_pcie_type (const struct pci_dev *dev)

    get the PCIe device/port type

    :param const struct pci_dev \*dev:
        PCI device



.. _`pci_vpd_lrdt_size`:

pci_vpd_lrdt_size
=================

.. c:function:: u16 pci_vpd_lrdt_size (const u8 *lrdt)

    Extracts the Large Resource Data Type length

    :param const u8 \*lrdt:
        Pointer to the beginning of the Large Resource Data Type tag



.. _`pci_vpd_lrdt_size.description`:

Description
-----------

Returns the extracted Large Resource Data Type length.



.. _`pci_vpd_lrdt_tag`:

pci_vpd_lrdt_tag
================

.. c:function:: u16 pci_vpd_lrdt_tag (const u8 *lrdt)

    Extracts the Large Resource Data Type Tag Item

    :param const u8 \*lrdt:
        Pointer to the beginning of the Large Resource Data Type tag



.. _`pci_vpd_lrdt_tag.description`:

Description
-----------

Returns the extracted Large Resource Data Type Tag item.



.. _`pci_vpd_srdt_size`:

pci_vpd_srdt_size
=================

.. c:function:: u8 pci_vpd_srdt_size (const u8 *srdt)

    Extracts the Small Resource Data Type length

    :param const u8 \*srdt:

        *undescribed*



.. _`pci_vpd_srdt_size.description`:

Description
-----------

Returns the extracted Small Resource Data Type length.



.. _`pci_vpd_srdt_tag`:

pci_vpd_srdt_tag
================

.. c:function:: u8 pci_vpd_srdt_tag (const u8 *srdt)

    Extracts the Small Resource Data Type Tag Item

    :param const u8 \*srdt:

        *undescribed*



.. _`pci_vpd_srdt_tag.description`:

Description
-----------

Returns the extracted Small Resource Data Type Tag Item.



.. _`pci_vpd_info_field_size`:

pci_vpd_info_field_size
=======================

.. c:function:: u8 pci_vpd_info_field_size (const u8 *info_field)

    Extracts the information field length

    :param const u8 \*info_field:

        *undescribed*



.. _`pci_vpd_info_field_size.description`:

Description
-----------

Returns the extracted information field length.



.. _`pci_vpd_find_tag`:

pci_vpd_find_tag
================

.. c:function:: int pci_vpd_find_tag (const u8 *buf, unsigned int off, unsigned int len, u8 rdt)

    Locates the Resource Data Type tag provided

    :param const u8 \*buf:
        Pointer to buffered vpd data

    :param unsigned int off:
        The offset into the buffer at which to begin the search

    :param unsigned int len:
        The length of the vpd buffer

    :param u8 rdt:
        The Resource Data Type to search for



.. _`pci_vpd_find_tag.description`:

Description
-----------

Returns the index where the Resource Data Type was found or
-ENOENT otherwise.



.. _`pci_vpd_find_info_keyword`:

pci_vpd_find_info_keyword
=========================

.. c:function:: int pci_vpd_find_info_keyword (const u8 *buf, unsigned int off, unsigned int len, const char *kw)

    Locates an information field keyword in the VPD

    :param const u8 \*buf:
        Pointer to buffered vpd data

    :param unsigned int off:
        The offset into the buffer at which to begin the search

    :param unsigned int len:
        The length of the buffer area, relative to off, in which to search

    :param const char \*kw:
        The keyword to search for



.. _`pci_vpd_find_info_keyword.description`:

Description
-----------

Returns the index where the information field keyword was found or
-ENOENT otherwise.



.. _`pci_ari_enabled`:

pci_ari_enabled
===============

.. c:function:: bool pci_ari_enabled (struct pci_bus *bus)

    query ARI forwarding status

    :param struct pci_bus \*bus:
        the PCI bus



.. _`pci_ari_enabled.description`:

Description
-----------

Returns true if ARI forwarding is enabled.

