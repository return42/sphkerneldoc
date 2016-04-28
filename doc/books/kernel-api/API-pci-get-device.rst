.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-get-device:

==============
pci_get_device
==============

*man pci_get_device(9)*

*4.6.0-rc5*

begin or continue searching for a PCI device by vendor/device id


Synopsis
========

.. c:function:: struct pci_dev * pci_get_device( unsigned int vendor, unsigned int device, struct pci_dev * from )

Arguments
=========

``vendor``
    PCI vendor id to match, or ``PCI_ANY_ID`` to match all vendor ids

``device``
    PCI device id to match, or ``PCI_ANY_ID`` to match all device ids

``from``
    Previous PCI device found in search, or ``NULL`` for new search.


Description
===========

Iterates through the list of known PCI devices. If a PCI device is found
with a matching ``vendor`` and ``device``, the reference count to the
device is incremented and a pointer to its device structure is returned.
Otherwise, ``NULL`` is returned. A new search is initiated by passing
``NULL`` as the ``from`` argument. Otherwise if ``from`` is not
``NULL``, searches continue from next device on the global list. The
reference count for ``from`` is always decremented if it is not
``NULL``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
