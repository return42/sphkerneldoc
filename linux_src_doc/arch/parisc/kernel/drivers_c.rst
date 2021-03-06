.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/parisc/kernel/drivers.c

.. _`for_each_padev`:

for_each_padev
==============

.. c:function:: int for_each_padev(int (*fn)(struct device *, void *), void *data)

    Iterate over all devices in the tree

    :param int (\*fn)(struct device \*, void \*):
        Function to call for each device.

    :param data:
        Data to pass to the called function.
    :type data: void \*

.. _`for_each_padev.description`:

Description
-----------

This performs a depth-first traversal of the tree, calling the
function passed for each node.  It calls the function for parents
before children.

.. _`match_device`:

match_device
============

.. c:function:: int match_device(struct parisc_driver *driver, struct parisc_device *dev)

    Report whether this driver can handle this device

    :param driver:
        the PA-RISC driver to try
    :type driver: struct parisc_driver \*

    :param dev:
        the PA-RISC device to try
    :type dev: struct parisc_device \*

.. _`register_parisc_driver`:

register_parisc_driver
======================

.. c:function:: int register_parisc_driver(struct parisc_driver *driver)

    Register this driver if it can handle a device

    :param driver:
        the PA-RISC driver to try
    :type driver: struct parisc_driver \*

.. _`count_parisc_driver`:

count_parisc_driver
===================

.. c:function:: int count_parisc_driver(struct parisc_driver *driver)

    count # of devices this driver would match

    :param driver:
        the PA-RISC driver to try
    :type driver: struct parisc_driver \*

.. _`count_parisc_driver.description`:

Description
-----------

Use by IOMMU support to "guess" the right size IOPdir.
Formula is something like memsize/(num_iommu \* entry_size).

.. _`unregister_parisc_driver`:

unregister_parisc_driver
========================

.. c:function:: int unregister_parisc_driver(struct parisc_driver *driver)

    Unregister this driver from the list of drivers

    :param driver:
        the PA-RISC driver to unregister
    :type driver: struct parisc_driver \*

.. _`find_pa_parent_type`:

find_pa_parent_type
===================

.. c:function:: const struct parisc_device *find_pa_parent_type(const struct parisc_device *padev, int type)

    Find a parent of a specific type

    :param padev:
        *undescribed*
    :type padev: const struct parisc_device \*

    :param type:
        The device type to search for.
    :type type: int

.. _`find_pa_parent_type.description`:

Description
-----------

Walks up the device tree looking for a device of the specified type.
If it finds it, it returns it.  If not, it returns NULL.

.. _`print_pa_hwpath`:

print_pa_hwpath
===============

.. c:function:: char *print_pa_hwpath(struct parisc_device *dev, char *output)

    Returns hardware path for PA devices

    :param dev:
        *undescribed*
    :type dev: struct parisc_device \*

    :param output:
        *undescribed*
    :type output: char \*

.. _`print_pa_hwpath.dev`:

dev
---

The device to return the path for

.. _`print_pa_hwpath.output`:

output
------

Pointer to a previously-allocated array to place the path in.

This function fills in the output array with a human-readable path
to a PA device.  This string is compatible with that used by PDC, and
may be printed on the outside of the box.

.. _`get_pci_node_path`:

get_pci_node_path
=================

.. c:function:: void get_pci_node_path(struct pci_dev *pdev, struct hardware_path *path)

    Determines the hardware path for a PCI device

    :param pdev:
        The device to return the path for
    :type pdev: struct pci_dev \*

    :param path:
        Pointer to a previously-allocated array to place the path in.
    :type path: struct hardware_path \*

.. _`get_pci_node_path.description`:

Description
-----------

This function fills in the hardware_path structure with the route to
the specified PCI device.  This structure is suitable for passing to
PDC calls.

.. _`print_pci_hwpath`:

print_pci_hwpath
================

.. c:function:: char *print_pci_hwpath(struct pci_dev *dev, char *output)

    Returns hardware path for PCI devices

    :param dev:
        *undescribed*
    :type dev: struct pci_dev \*

    :param output:
        *undescribed*
    :type output: char \*

.. _`print_pci_hwpath.dev`:

dev
---

The device to return the path for

.. _`print_pci_hwpath.output`:

output
------

Pointer to a previously-allocated array to place the path in.

This function fills in the output array with a human-readable path
to a PCI device.  This string is compatible with that used by PDC, and
may be printed on the outside of the box.

.. _`alloc_tree_node`:

alloc_tree_node
===============

.. c:function:: struct parisc_device *alloc_tree_node(struct device *parent, char id)

    returns a device entry in the iotree

    :param parent:
        the parent node in the tree
    :type parent: struct device \*

    :param id:
        the element of the module path for this entry
    :type id: char

.. _`alloc_tree_node.description`:

Description
-----------

Checks all the children of \ ``parent``\  for a matching \ ``id``\ .  If none
found, it allocates a new device and returns it.

.. _`register_parisc_device`:

register_parisc_device
======================

.. c:function:: int register_parisc_device(struct parisc_device *dev)

    Locate a driver to manage this device.

    :param dev:
        The parisc device.
    :type dev: struct parisc_device \*

.. _`register_parisc_device.description`:

Description
-----------

Search the driver list for a driver that is willing to manage
this device.

.. _`match_pci_device`:

match_pci_device
================

.. c:function:: int match_pci_device(struct device *dev, int index, struct hardware_path *modpath)

    Matches a pci device against a given hardware path entry.

    :param dev:
        the generic device (known to be contained by a pci_dev).
    :type dev: struct device \*

    :param index:
        the current BC index
    :type index: int

    :param modpath:
        the hardware path.
    :type modpath: struct hardware_path \*

.. _`match_parisc_device`:

match_parisc_device
===================

.. c:function:: int match_parisc_device(struct device *dev, int index, struct hardware_path *modpath)

    Matches a parisc device against a given hardware path entry.

    :param dev:
        the generic device (known to be contained by a parisc_device).
    :type dev: struct device \*

    :param index:
        the current BC index
    :type index: int

    :param modpath:
        the hardware path.
    :type modpath: struct hardware_path \*

.. _`parse_tree_node`:

parse_tree_node
===============

.. c:function:: struct device *parse_tree_node(struct device *parent, int index, struct hardware_path *modpath)

    returns a device entry in the iotree

    :param parent:
        the parent node in the tree
    :type parent: struct device \*

    :param index:
        the current BC index
    :type index: int

    :param modpath:
        the hardware_path struct to match a device against
    :type modpath: struct hardware_path \*

.. _`parse_tree_node.description`:

Description
-----------

Checks all the children of \ ``parent``\  for a matching \ ``id``\ .  If none
found, it returns NULL.

.. _`hwpath_to_device`:

hwpath_to_device
================

.. c:function:: struct device *hwpath_to_device(struct hardware_path *modpath)

    Finds the generic device corresponding to a given hardware path.

    :param modpath:
        the hardware path.
    :type modpath: struct hardware_path \*

.. _`device_to_hwpath`:

device_to_hwpath
================

.. c:function:: void device_to_hwpath(struct device *dev, struct hardware_path *path)

    Populates the hwpath corresponding to the given device. \ ``param``\  dev the target device \ ``param``\  path pointer to a previously allocated hwpath struct to be filled in

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param path:
        *undescribed*
    :type path: struct hardware_path \*

.. _`walk_native_bus`:

walk_native_bus
===============

.. c:function:: void walk_native_bus(unsigned long io_io_low, unsigned long io_io_high, struct device *parent)

    - Probe a bus for devices

    :param io_io_low:
        Base address of this bus.
    :type io_io_low: unsigned long

    :param io_io_high:
        Last address of this bus.
    :type io_io_high: unsigned long

    :param parent:
        The parent bus device.
    :type parent: struct device \*

.. _`walk_native_bus.description`:

Description
-----------

A native bus (eg Runway or GSC) may have up to 64 devices on it,
spaced at intervals of 0x1000 bytes.  PDC may not inform us of these
devices, so we have to probe for them.  Unfortunately, we may find
devices which are not physically connected (such as extra serial &
keyboard ports).  This problem is not yet solved.

.. _`walk_central_bus`:

walk_central_bus
================

.. c:function:: void walk_central_bus( void)

    Find devices attached to the central bus

    :param void:
        no arguments
    :type void: 

.. _`walk_central_bus.description`:

Description
-----------

PDC doesn't tell us about all devices in the system.  This routine
finds devices connected to the central bus.

.. _`init_parisc_bus`:

init_parisc_bus
===============

.. c:function:: void init_parisc_bus( void)

    Some preparation to be done before inventory

    :param void:
        no arguments
    :type void: 

.. _`print_parisc_devices`:

print_parisc_devices
====================

.. c:function:: void print_parisc_devices( void)

    Print out a list of devices found in this system

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

