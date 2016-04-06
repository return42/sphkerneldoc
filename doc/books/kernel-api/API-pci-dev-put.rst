
.. _API-pci-dev-put:

===========
pci_dev_put
===========

*man pci_dev_put(9)*

*4.6.0-rc1*

release a use of the pci device structure


Synopsis
========

.. c:function:: void pci_dev_put( struct pci_dev * dev )

Arguments
=========

``dev``
    device that's been disconnected


Description
===========

Must be called when a user of a device is finished with it. When the last user of the device calls this function, the memory of the device is freed.
