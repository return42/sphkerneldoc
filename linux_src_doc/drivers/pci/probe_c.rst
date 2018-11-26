.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/probe.c

.. _`__pci_read_base`:

__pci_read_base
===============

.. c:function:: int __pci_read_base(struct pci_dev *dev, enum pci_bar_type type, struct resource *res, unsigned int pos)

    Read a PCI BAR

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

    :param type:
        type of the BAR
    :type type: enum pci_bar_type

    :param res:
        resource buffer to be filled in
    :type res: struct resource \*

    :param pos:
        BAR position in the config space
    :type pos: unsigned int

.. _`__pci_read_base.description`:

Description
-----------

Returns 1 if the BAR is 64-bit, or 0 if 32-bit.

.. _`pci_ext_cfg_is_aliased`:

pci_ext_cfg_is_aliased
======================

.. c:function:: bool pci_ext_cfg_is_aliased(struct pci_dev *dev)

    Is ext config space just an alias of std config?

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`pci_ext_cfg_is_aliased.description`:

Description
-----------

PCI Express to PCI/PCI-X Bridge Specification, rev 1.0, 4.1.4 says that
when forwarding a type1 configuration request the bridge must check that
the extended register address field is zero.  The bridge is not permitted
to forward the transactions and must handle it as an Unsupported Request.
Some bridges do not follow this rule and simply drop the extended register
bits, resulting in the standard config space being aliased, every 256
bytes across the entire configuration space.  Test for this condition by
comparing the first dword of each potential alias to the vendor/device ID.

.. _`pci_ext_cfg_is_aliased.known-offenders`:

Known offenders
---------------

  ASM1083/1085 PCIe-to-PCI Reversible Bridge (1b21:1080, rev 01 & 03)
  AMD/ATI SBx00 PCI to PCI Bridge (1002:4384, rev 40)

.. _`pci_cfg_space_size_ext`:

pci_cfg_space_size_ext
======================

.. c:function:: int pci_cfg_space_size_ext(struct pci_dev *dev)

    Get the configuration space size of the PCI device

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`pci_cfg_space_size_ext.description`:

Description
-----------

Regular PCI devices have 256 bytes, but PCI-X 2 and PCI Express devices
have 4096 bytes.  Even if the device is capable, that doesn't mean we can
access it.  Maybe we don't have a way to generate extended config space
accesses, or the device is behind a reverse Express bridge.  So we try
reading the dword at 0x100 which must either be 0 or a valid extended
capability header.

.. _`pci_intx_mask_broken`:

pci_intx_mask_broken
====================

.. c:function:: int pci_intx_mask_broken(struct pci_dev *dev)

    Test PCI_COMMAND_INTX_DISABLE writability

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`pci_intx_mask_broken.description`:

Description
-----------

Test whether PCI_COMMAND_INTX_DISABLE is writable for \ ``dev``\ .  Check this
at enumeration-time to avoid modifying PCI_COMMAND at run-time.

.. _`pci_setup_device`:

pci_setup_device
================

.. c:function:: int pci_setup_device(struct pci_dev *dev)

    Fill in class and map information of a device

    :param dev:
        the device structure to fill
    :type dev: struct pci_dev \*

.. _`pci_setup_device.description`:

Description
-----------

Initialize the device structure with information about the device's
vendor,class,memory and IO-space addresses, IRQ lines etc.
Called at initialisation of the PCI subsystem and by CardBus services.
Returns 0 on success and negative if unknown type of device (not normal,
bridge or CardBus).

.. _`pcie_relaxed_ordering_enabled`:

pcie_relaxed_ordering_enabled
=============================

.. c:function:: bool pcie_relaxed_ordering_enabled(struct pci_dev *dev)

    Probe for PCIe relaxed ordering enable

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

.. _`pcie_relaxed_ordering_enabled.description`:

Description
-----------

Returns true if the device has enabled relaxed ordering attribute.

.. _`pci_release_dev`:

pci_release_dev
===============

.. c:function:: void pci_release_dev(struct device *dev)

    Free a PCI device structure when all users of it are finished

    :param dev:
        device that's been disconnected
    :type dev: struct device \*

.. _`pci_release_dev.description`:

Description
-----------

Will be called only by the device core when all users of this PCI device are
done.

.. _`pci_scan_slot`:

pci_scan_slot
=============

.. c:function:: int pci_scan_slot(struct pci_bus *bus, int devfn)

    Scan a PCI slot on a bus for devices

    :param bus:
        PCI bus to scan
    :type bus: struct pci_bus \*

    :param devfn:
        slot number to scan (must have zero function)
    :type devfn: int

.. _`pci_scan_slot.description`:

Description
-----------

Scan a PCI slot on the specified PCI bus for devices, adding
discovered devices to the \ ``bus->devices``\  list.  New devices
will not have is_added set.

Returns the number of new devices found.

.. _`pci_scan_child_bus_extend`:

pci_scan_child_bus_extend
=========================

.. c:function:: unsigned int pci_scan_child_bus_extend(struct pci_bus *bus, unsigned int available_buses)

    Scan devices below a bus

    :param bus:
        Bus to scan for devices
    :type bus: struct pci_bus \*

    :param available_buses:
        Total number of buses available (%0 does not try to
        extend beyond the minimal)
    :type available_buses: unsigned int

.. _`pci_scan_child_bus_extend.description`:

Description
-----------

Scans devices below \ ``bus``\  including subordinate buses. Returns new
subordinate number including all the found devices. Passing
\ ``available_buses``\  causes the remaining bus space to be distributed
equally between hotplug-capable bridges to allow future extension of the
hierarchy.

.. _`pci_scan_child_bus`:

pci_scan_child_bus
==================

.. c:function:: unsigned int pci_scan_child_bus(struct pci_bus *bus)

    Scan devices below a bus

    :param bus:
        Bus to scan for devices
    :type bus: struct pci_bus \*

.. _`pci_scan_child_bus.description`:

Description
-----------

Scans devices below \ ``bus``\  including subordinate buses. Returns new
subordinate number including all the found devices.

.. _`pcibios_root_bridge_prepare`:

pcibios_root_bridge_prepare
===========================

.. c:function:: int pcibios_root_bridge_prepare(struct pci_host_bridge *bridge)

    Platform-specific host bridge setup

    :param bridge:
        Host bridge to set up
    :type bridge: struct pci_host_bridge \*

.. _`pcibios_root_bridge_prepare.description`:

Description
-----------

Default empty implementation.  Replace with an architecture-specific setup
routine, if necessary.

.. _`pci_rescan_bus_bridge_resize`:

pci_rescan_bus_bridge_resize
============================

.. c:function:: unsigned int pci_rescan_bus_bridge_resize(struct pci_dev *bridge)

    Scan a PCI bus for devices

    :param bridge:
        PCI bridge for the bus to scan
    :type bridge: struct pci_dev \*

.. _`pci_rescan_bus_bridge_resize.description`:

Description
-----------

Scan a PCI bus and child buses for new devices, add them,
and enable them, resizing bridge mmio/io resource if necessary
and possible.  The caller must ensure the child devices are already
removed for resizing to occur.

Returns the max number of subordinate bus discovered.

.. _`pci_rescan_bus`:

pci_rescan_bus
==============

.. c:function:: unsigned int pci_rescan_bus(struct pci_bus *bus)

    Scan a PCI bus for devices

    :param bus:
        PCI bus to scan
    :type bus: struct pci_bus \*

.. _`pci_rescan_bus.description`:

Description
-----------

Scan a PCI bus and child buses for new devices, add them,
and enable them.

Returns the max number of subordinate bus discovered.

.. This file was automatic generated / don't edit.

