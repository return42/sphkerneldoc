
.. _API-pci-msi-enabled:

===============
pci_msi_enabled
===============

*man pci_msi_enabled(9)*

*4.6.0-rc1*

is MSI enabled?


Synopsis
========

.. c:function:: int pci_msi_enabled( void )

Arguments
=========

``void``
    no arguments


Description
===========

Returns true if MSI has not been disabled by the command-line option pci=nomsi.
