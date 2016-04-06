
.. _API-pci-enable-msi-range:

====================
pci_enable_msi_range
====================

*man pci_enable_msi_range(9)*

*4.6.0-rc1*

configure device's MSI capability structure


Synopsis
========

.. c:function:: int pci_enable_msi_range( struct pci_dev * dev, int minvec, int maxvec )

Arguments
=========

``dev``
    device to configure

``minvec``
    minimal number of interrupts to configure

``maxvec``
    maximum number of interrupts to configure


Description
===========

This function tries to allocate a maximum possible number of interrupts in a range between ``minvec`` and ``maxvec``. It returns a negative errno if an error occurs. If it
succeeds, it returns the actual number of interrupts allocated and updates the ``dev``'s irq member to the lowest new interrupt number; the other interrupt numbers allocated to
this device are consecutive.
