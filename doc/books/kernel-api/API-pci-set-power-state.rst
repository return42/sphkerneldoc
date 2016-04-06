
.. _API-pci-set-power-state:

===================
pci_set_power_state
===================

*man pci_set_power_state(9)*

*4.6.0-rc1*

Set the power state of a PCI device


Synopsis
========

.. c:function:: int pci_set_power_state( struct pci_dev * dev, pci_power_t state )

Arguments
=========

``dev``
    PCI device to handle.

``state``
    PCI power state (D0, D1, D2, D3hot) to put the device into.


Description
===========

Transition a device to a new power state, using the platform firmware and/or the device's PCI PM registers.


RETURN VALUE
============

-EINVAL if the requested state is invalid. -EIO if device does not support PCI PM or its PM capabilities register has a wrong version, or device doesn't support the requested
state. 0 if device already is in the requested state. 0 if device's power state has been successfully changed.
