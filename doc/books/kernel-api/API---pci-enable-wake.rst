
.. _API---pci-enable-wake:

=================
__pci_enable_wake
=================

*man __pci_enable_wake(9)*

*4.6.0-rc1*

enable PCI device as wakeup event source


Synopsis
========

.. c:function:: int __pci_enable_wake( struct pci_dev * dev, pci_power_t state, bool runtime, bool enable )

Arguments
=========

``dev``
    PCI device affected

``state``
    PCI state from which device will issue wakeup events

``runtime``
    True if the events are to be generated at run time

``enable``
    True to enable event generation; false to disable


Description
===========

This enables the device as a wakeup event source, or disables it. When such events involves platform-specific hooks, those hooks are called automatically by this routine.

Devices with legacy power management (no standard PCI PM capabilities) always require such platform hooks.


RETURN VALUE
============

0 is returned on success -EINVAL is returned if device is not supposed to wake up the system Error code depending on the platform is returned if both the platform and the native
mechanism fail to enable the generation of wake-up events
