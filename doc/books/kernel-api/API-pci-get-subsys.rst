
.. _API-pci-get-subsys:

==============
pci_get_subsys
==============

*man pci_get_subsys(9)*

*4.6.0-rc1*

begin or continue searching for a PCI device by vendor/subvendor/device/subdevice id


Synopsis
========

.. c:function:: struct pci_dev ⋆ pci_get_subsys( unsigned int vendor, unsigned int device, unsigned int ss_vendor, unsigned int ss_device, struct pci_dev * from )

Arguments
=========

``vendor``
    PCI vendor id to match, or ``PCI_ANY_ID`` to match all vendor ids

``device``
    PCI device id to match, or ``PCI_ANY_ID`` to match all device ids

``ss_vendor``
    PCI subsystem vendor id to match, or ``PCI_ANY_ID`` to match all vendor ids

``ss_device``
    PCI subsystem device id to match, or ``PCI_ANY_ID`` to match all device ids

``from``
    Previous PCI device found in search, or ``NULL`` for new search.


Description
===========

Iterates through the list of known PCI devices. If a PCI device is found with a matching ``vendor``, ``device``, ``ss_vendor`` and ``ss_device``, a pointer to its device structure
is returned, and the reference count to the device is incremented. Otherwise, ``NULL`` is returned. A new search is initiated by passing ``NULL`` as the ``from`` argument.
Otherwise if ``from`` is not ``NULL``, searches continue from next device on the global list. The reference count for ``from`` is always decremented if it is not ``NULL``.
