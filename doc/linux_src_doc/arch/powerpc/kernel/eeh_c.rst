.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/eeh.c

.. _`eeh_slot_error_detail`:

eeh_slot_error_detail
=====================

.. c:function:: void eeh_slot_error_detail(struct eeh_pe *pe, int severity)

    Generate combined log including driver log and error log

    :param struct eeh_pe \*pe:
        EEH PE

    :param int severity:
        temporary or permanent error log

.. _`eeh_slot_error_detail.description`:

Description
-----------

This routine should be called to generate the combined log, which
is comprised of driver log and error log. The driver log is figured
out from the config space of the corresponding PCI device, while
the error log is fetched through platform dependent function call.

.. _`eeh_token_to_phys`:

eeh_token_to_phys
=================

.. c:function:: unsigned long eeh_token_to_phys(unsigned long token)

    Convert EEH address token to phys address

    :param unsigned long token:
        I/O token, should be address in the form 0xA....

.. _`eeh_token_to_phys.description`:

Description
-----------

This routine should be called to convert virtual I/O address
to physical one.

.. _`eeh_dev_check_failure`:

eeh_dev_check_failure
=====================

.. c:function:: int eeh_dev_check_failure(struct eeh_dev *edev)

    Check if all 1's data is due to EEH slot freeze

    :param struct eeh_dev \*edev:
        eeh device

.. _`eeh_dev_check_failure.description`:

Description
-----------

Check for an EEH failure for the given device node.  Call this
routine if the result of a read was all 0xff's and you want to
find out if this is due to an EEH slot freeze.  This routine
will query firmware for the EEH status.

Returns 0 if there has not been an EEH error; otherwise returns
a non-zero value and queues up a slot isolation event notification.

It is safe to call this routine in an interrupt context.

.. _`eeh_check_failure`:

eeh_check_failure
=================

.. c:function:: int eeh_check_failure(const volatile void __iomem *token)

    Check if all 1's data is due to EEH slot freeze

    :param const volatile void __iomem \*token:
        I/O address

.. _`eeh_check_failure.description`:

Description
-----------

Check for an EEH failure at the given I/O address. Call this
routine if the result of a read was all 0xff's and you want to
find out if this is due to an EEH slot freeze event. This routine
will query firmware for the EEH status.

Note this routine is safe to call in an interrupt context.

.. _`eeh_pci_enable`:

eeh_pci_enable
==============

.. c:function:: int eeh_pci_enable(struct eeh_pe *pe, int function)

    Enable MMIO or DMA transfers for this slot

    :param struct eeh_pe \*pe:
        EEH PE

    :param int function:
        *undescribed*

.. _`eeh_pci_enable.description`:

Description
-----------

This routine should be called to reenable frozen MMIO or DMA
so that it would work correctly again. It's useful while doing
recovery or log collection on the indicated device.

.. _`pcibios_set_pcie_reset_state`:

pcibios_set_pcie_reset_state
============================

.. c:function:: int pcibios_set_pcie_reset_state(struct pci_dev *dev, enum pcie_reset_state state)

    Set PCI-E reset state

    :param struct pci_dev \*dev:
        pci device struct

    :param enum pcie_reset_state state:
        reset state to enter

.. _`pcibios_set_pcie_reset_state.return-value`:

Return value
------------

0 if success

.. _`eeh_set_dev_freset`:

eeh_set_dev_freset
==================

.. c:function:: void *eeh_set_dev_freset(void *data, void *flag)

    Check the required reset for the indicated device

    :param void \*data:
        EEH device

    :param void \*flag:
        return value

.. _`eeh_set_dev_freset.each-device-might-have-its-preferred-reset-type`:

Each device might have its preferred reset type
-----------------------------------------------

fundamental or
hot reset. The routine is used to collected the information for
the indicated device and its children so that the bunch of the
devices could be reset properly.

.. _`eeh_reset_pe_once`:

eeh_reset_pe_once
=================

.. c:function:: void eeh_reset_pe_once(struct eeh_pe *pe)

    Assert the pci #RST line for 1/4 second

    :param struct eeh_pe \*pe:
        EEH PE

.. _`eeh_reset_pe_once.description`:

Description
-----------

Assert the PCI #RST line for 1/4 second.

.. _`eeh_reset_pe`:

eeh_reset_pe
============

.. c:function:: int eeh_reset_pe(struct eeh_pe *pe)

    Reset the indicated PE

    :param struct eeh_pe \*pe:
        EEH PE

.. _`eeh_reset_pe.description`:

Description
-----------

This routine should be called to reset indicated device, including
PE. A PE might include multiple PCI devices and sometimes PCI bridges
might be involved as well.

.. _`eeh_save_bars`:

eeh_save_bars
=============

.. c:function:: void eeh_save_bars(struct eeh_dev *edev)

    Save device bars

    :param struct eeh_dev \*edev:
        PCI device associated EEH device

.. _`eeh_save_bars.description`:

Description
-----------

Save the values of the device bars. Unlike the restore
routine, this routine is \*not\* recursive. This is because
PCI devices are added individually; but, for the restore,
an entire slot is reset at a time.

.. _`eeh_ops_register`:

eeh_ops_register
================

.. c:function:: int eeh_ops_register(struct eeh_ops *ops)

    Register platform dependent EEH operations

    :param struct eeh_ops \*ops:
        platform dependent EEH operations

.. _`eeh_ops_register.description`:

Description
-----------

Register the platform dependent EEH operation callback
functions. The platform should call this function before
any other EEH operations.

.. _`eeh_ops_unregister`:

eeh_ops_unregister
==================

.. c:function:: int __exit eeh_ops_unregister(const char *name)

    Unreigster platform dependent EEH operations

    :param const char \*name:
        name of EEH platform operations

.. _`eeh_ops_unregister.description`:

Description
-----------

Unregister the platform dependent EEH operation callback
functions.

.. _`eeh_init`:

eeh_init
========

.. c:function:: int eeh_init( void)

    EEH initialization

    :param  void:
        no arguments

.. _`eeh_init.description`:

Description
-----------

Initialize EEH by trying to enable it for all of the adapters in the system.
As a side effect we can determine here if eeh is supported at all.
Note that we leave EEH on so failed config cycles won't cause a machine
check.  If a user turns off EEH for a particular adapter they are really
telling Linux to ignore errors.  Some hardware (e.g. POWER5) won't
grant access to a slot if EEH isn't enabled, and so we always enable
EEH for all slots/all devices.

The eeh-force-off option disables EEH checking globally, for all slots.
Even if force-off is set, the EEH hardware is still enabled, so that
newer systems can boot.

.. _`eeh_add_device_early`:

eeh_add_device_early
====================

.. c:function:: void eeh_add_device_early(struct pci_dn *pdn)

    Enable EEH for the indicated device node

    :param struct pci_dn \*pdn:
        PCI device node for which to set up EEH

.. _`eeh_add_device_early.description`:

Description
-----------

This routine must be used to perform EEH initialization for PCI
devices that were added after system boot (e.g. hotplug, dlpar).
This routine must be called before any i/o is performed to the
adapter (inluding any config-space i/o).
Whether this actually enables EEH or not for this device depends
on the CEC architecture, type of the device, on earlier boot
command-line arguments & etc.

.. _`eeh_add_device_tree_early`:

eeh_add_device_tree_early
=========================

.. c:function:: void eeh_add_device_tree_early(struct pci_dn *pdn)

    Enable EEH for the indicated device

    :param struct pci_dn \*pdn:
        PCI device node

.. _`eeh_add_device_tree_early.description`:

Description
-----------

This routine must be used to perform EEH initialization for the
indicated PCI device that was added after system boot (e.g.
hotplug, dlpar).

.. _`eeh_add_device_late`:

eeh_add_device_late
===================

.. c:function:: void eeh_add_device_late(struct pci_dev *dev)

    Perform EEH initialization for the indicated pci device

    :param struct pci_dev \*dev:
        pci device for which to set up EEH

.. _`eeh_add_device_late.description`:

Description
-----------

This routine must be used to complete EEH initialization for PCI
devices that were added after system boot (e.g. hotplug, dlpar).

.. _`eeh_add_device_tree_late`:

eeh_add_device_tree_late
========================

.. c:function:: void eeh_add_device_tree_late(struct pci_bus *bus)

    Perform EEH initialization for the indicated PCI bus

    :param struct pci_bus \*bus:
        PCI bus

.. _`eeh_add_device_tree_late.description`:

Description
-----------

This routine must be used to perform EEH initialization for PCI
devices which are attached to the indicated PCI bus. The PCI bus
is added after system boot through hotplug or dlpar.

.. _`eeh_add_sysfs_files`:

eeh_add_sysfs_files
===================

.. c:function:: void eeh_add_sysfs_files(struct pci_bus *bus)

    Add EEH sysfs files for the indicated PCI bus

    :param struct pci_bus \*bus:
        PCI bus

.. _`eeh_add_sysfs_files.description`:

Description
-----------

This routine must be used to add EEH sysfs files for PCI
devices which are attached to the indicated PCI bus. The PCI bus
is added after system boot through hotplug or dlpar.

.. _`eeh_remove_device`:

eeh_remove_device
=================

.. c:function:: void eeh_remove_device(struct pci_dev *dev)

    Undo EEH setup for the indicated pci device

    :param struct pci_dev \*dev:
        pci device to be removed

.. _`eeh_remove_device.description`:

Description
-----------

This routine should be called when a device is removed from
a running system (e.g. by hotplug or dlpar).  It unregisters
the PCI device from the EEH subsystem.  I/O errors affecting
this device will no longer be detected after this call; thus,
i/o errors affecting this slot may leave this device unusable.

.. _`eeh_dev_open`:

eeh_dev_open
============

.. c:function:: int eeh_dev_open(struct pci_dev *pdev)

    Increase count of pass through devices for PE

    :param struct pci_dev \*pdev:
        PCI device

.. _`eeh_dev_open.description`:

Description
-----------

Increase count of passed through devices for the indicated
PE. In the result, the EEH errors detected on the PE won't be
reported. The PE owner will be responsible for detection
and recovery.

.. _`eeh_dev_release`:

eeh_dev_release
===============

.. c:function:: void eeh_dev_release(struct pci_dev *pdev)

    Decrease count of pass through devices for PE

    :param struct pci_dev \*pdev:
        PCI device

.. _`eeh_dev_release.description`:

Description
-----------

Decrease count of pass through devices for the indicated PE. If
there is no passed through device in PE, the EEH errors detected
on the PE will be reported and handled as usual.

.. _`eeh_iommu_group_to_pe`:

eeh_iommu_group_to_pe
=====================

.. c:function:: struct eeh_pe *eeh_iommu_group_to_pe(struct iommu_group *group)

    Convert IOMMU group to EEH PE

    :param struct iommu_group \*group:
        IOMMU group

.. _`eeh_iommu_group_to_pe.description`:

Description
-----------

The routine is called to convert IOMMU group to EEH PE.

.. _`eeh_pe_set_option`:

eeh_pe_set_option
=================

.. c:function:: int eeh_pe_set_option(struct eeh_pe *pe, int option)

    Set options for the indicated PE

    :param struct eeh_pe \*pe:
        EEH PE

    :param int option:
        requested option

.. _`eeh_pe_set_option.description`:

Description
-----------

The routine is called to enable or disable EEH functionality
on the indicated PE, to enable IO or DMA for the frozen PE.

.. _`eeh_pe_get_state`:

eeh_pe_get_state
================

.. c:function:: int eeh_pe_get_state(struct eeh_pe *pe)

    Retrieve PE's state

    :param struct eeh_pe \*pe:
        EEH PE

.. _`eeh_pe_get_state.description`:

Description
-----------

Retrieve the PE's state, which includes 3 aspects: enabled
DMA, enabled IO and asserted reset.

.. _`eeh_pe_reset`:

eeh_pe_reset
============

.. c:function:: int eeh_pe_reset(struct eeh_pe *pe, int option)

    Issue PE reset according to specified type

    :param struct eeh_pe \*pe:
        EEH PE

    :param int option:
        reset type

.. _`eeh_pe_reset.description`:

Description
-----------

The routine is called to reset the specified PE with the
indicated type, either fundamental reset or hot reset.
PE reset is the most important part for error recovery.

.. _`eeh_pe_configure`:

eeh_pe_configure
================

.. c:function:: int eeh_pe_configure(struct eeh_pe *pe)

    Configure PCI bridges after PE reset

    :param struct eeh_pe \*pe:
        EEH PE

.. _`eeh_pe_configure.description`:

Description
-----------

The routine is called to restore the PCI config space for
those PCI devices, especially PCI bridges affected by PE
reset issued previously.

.. _`eeh_pe_inject_err`:

eeh_pe_inject_err
=================

.. c:function:: int eeh_pe_inject_err(struct eeh_pe *pe, int type, int func, unsigned long addr, unsigned long mask)

    Injecting the specified PCI error to the indicated PE

    :param struct eeh_pe \*pe:
        the indicated PE

    :param int type:
        error type

    :param int func:
        *undescribed*

    :param unsigned long addr:
        address

    :param unsigned long mask:
        address mask

.. _`eeh_pe_inject_err.description`:

Description
-----------

The routine is called to inject the specified PCI error, which
is determined by \ ``type``\  and \ ``function``\ , to the indicated PE for
testing purpose.

.. This file was automatic generated / don't edit.

