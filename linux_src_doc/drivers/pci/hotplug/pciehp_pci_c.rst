.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/pciehp_pci.c

.. _`pciehp_configure_device`:

pciehp_configure_device
=======================

.. c:function:: int pciehp_configure_device(struct controller *ctrl)

    enumerate PCI devices below a hotplug bridge

    :param ctrl:
        PCIe hotplug controller
    :type ctrl: struct controller \*

.. _`pciehp_configure_device.description`:

Description
-----------

Enumerate PCI devices below a hotplug bridge and add them to the system.
Return 0 on success, \ ``-EEXIST``\  if the devices are already enumerated or
\ ``-ENODEV``\  if enumeration failed.

.. _`pciehp_unconfigure_device`:

pciehp_unconfigure_device
=========================

.. c:function:: void pciehp_unconfigure_device(struct controller *ctrl, bool presence)

    remove PCI devices below a hotplug bridge

    :param ctrl:
        PCIe hotplug controller
    :type ctrl: struct controller \*

    :param presence:
        whether the card is still present in the slot;
        true for safe removal via sysfs or an Attention Button press,
        false for surprise removal
    :type presence: bool

.. _`pciehp_unconfigure_device.description`:

Description
-----------

Unbind PCI devices below a hotplug bridge from their drivers and remove
them from the system.  Safely removed devices are quiesced.  Surprise
removed devices are marked as such to prevent further accesses.

.. This file was automatic generated / don't edit.

