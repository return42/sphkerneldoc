.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/iov.c

.. _`pci_iov_init`:

pci_iov_init
============

.. c:function:: int pci_iov_init(struct pci_dev *dev)

    initialize the IOV capability

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_iov_init.description`:

Description
-----------

Returns 0 on success, or negative on failure.

.. _`pci_iov_release`:

pci_iov_release
===============

.. c:function:: void pci_iov_release(struct pci_dev *dev)

    release resources used by the IOV capability

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_iov_remove`:

pci_iov_remove
==============

.. c:function:: void pci_iov_remove(struct pci_dev *dev)

    clean up SR-IOV state after PF driver is detached

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_iov_update_resource`:

pci_iov_update_resource
=======================

.. c:function:: void pci_iov_update_resource(struct pci_dev *dev, int resno)

    update a VF BAR

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

    :param resno:
        the resource number
    :type resno: int

.. _`pci_iov_update_resource.description`:

Description
-----------

Update a VF BAR in the SR-IOV capability of a PF.

.. _`pci_sriov_resource_alignment`:

pci_sriov_resource_alignment
============================

.. c:function:: resource_size_t pci_sriov_resource_alignment(struct pci_dev *dev, int resno)

    get resource alignment for VF BAR

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

    :param resno:
        the resource number
    :type resno: int

.. _`pci_sriov_resource_alignment.description`:

Description
-----------

Returns the alignment of the VF BAR found in the SR-IOV capability.
This is not the same as the resource size which is defined as
the VF BAR size multiplied by the number of VFs.  The alignment
is just the VF BAR size.

.. _`pci_restore_iov_state`:

pci_restore_iov_state
=====================

.. c:function:: void pci_restore_iov_state(struct pci_dev *dev)

    restore the state of the IOV capability

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_vf_drivers_autoprobe`:

pci_vf_drivers_autoprobe
========================

.. c:function:: void pci_vf_drivers_autoprobe(struct pci_dev *dev, bool auto_probe)

    set PF property drivers_autoprobe for VFs

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

    :param auto_probe:
        set VF drivers auto probe flag
    :type auto_probe: bool

.. _`pci_iov_bus_range`:

pci_iov_bus_range
=================

.. c:function:: int pci_iov_bus_range(struct pci_bus *bus)

    find bus range used by Virtual Function

    :param bus:
        the PCI bus
    :type bus: struct pci_bus \*

.. _`pci_iov_bus_range.description`:

Description
-----------

Returns max number of buses (exclude current one) used by Virtual
Functions.

.. _`pci_enable_sriov`:

pci_enable_sriov
================

.. c:function:: int pci_enable_sriov(struct pci_dev *dev, int nr_virtfn)

    enable the SR-IOV capability

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

    :param nr_virtfn:
        number of virtual functions to enable
    :type nr_virtfn: int

.. _`pci_enable_sriov.description`:

Description
-----------

Returns 0 on success, or negative on failure.

.. _`pci_disable_sriov`:

pci_disable_sriov
=================

.. c:function:: void pci_disable_sriov(struct pci_dev *dev)

    disable the SR-IOV capability

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_num_vf`:

pci_num_vf
==========

.. c:function:: int pci_num_vf(struct pci_dev *dev)

    return number of VFs associated with a PF device_release_driver

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_num_vf.description`:

Description
-----------

Returns number of VFs, or 0 if SR-IOV is not enabled.

.. _`pci_vfs_assigned`:

pci_vfs_assigned
================

.. c:function:: int pci_vfs_assigned(struct pci_dev *dev)

    returns number of VFs are assigned to a guest

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_vfs_assigned.description`:

Description
-----------

Returns number of VFs belonging to this device that are assigned to a guest.
If device is not a physical function returns 0.

.. _`pci_sriov_set_totalvfs`:

pci_sriov_set_totalvfs
======================

.. c:function:: int pci_sriov_set_totalvfs(struct pci_dev *dev, u16 numvfs)

    - reduce the TotalVFs available

    :param dev:
        the PCI PF device
    :type dev: struct pci_dev \*

    :param numvfs:
        number that should be used for TotalVFs supported
    :type numvfs: u16

.. _`pci_sriov_set_totalvfs.description`:

Description
-----------

Should be called from PF driver's probe routine with
device's mutex held.

Returns 0 if PF is an SRIOV-capable device and
value of numvfs valid. If not a PF return -ENOSYS;
if numvfs is invalid return -EINVAL;
if VFs already enabled, return -EBUSY.

.. _`pci_sriov_get_totalvfs`:

pci_sriov_get_totalvfs
======================

.. c:function:: int pci_sriov_get_totalvfs(struct pci_dev *dev)

    - get total VFs supported on this device

    :param dev:
        the PCI PF device
    :type dev: struct pci_dev \*

.. _`pci_sriov_get_totalvfs.description`:

Description
-----------

For a PCIe device with SRIOV support, return the PCIe
SRIOV capability value of TotalVFs or the value of driver_max_VFs
if the driver reduced it.  Otherwise 0.

.. _`pci_sriov_configure_simple`:

pci_sriov_configure_simple
==========================

.. c:function:: int pci_sriov_configure_simple(struct pci_dev *dev, int nr_virtfn)

    helper to configure SR-IOV

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

    :param nr_virtfn:
        number of virtual functions to enable, 0 to disable
    :type nr_virtfn: int

.. _`pci_sriov_configure_simple.description`:

Description
-----------

Enable or disable SR-IOV for devices that don't require any PF setup
before enabling SR-IOV.  Return value is negative on error, or number of
VFs allocated on success.

.. This file was automatic generated / don't edit.

