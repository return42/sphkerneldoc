.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-find-next-bus:

=================
pci_find_next_bus
=================

*man pci_find_next_bus(9)*

*4.6.0-rc5*

begin or continue searching for a PCI bus


Synopsis
========

.. c:function:: struct pci_bus * pci_find_next_bus( const struct pci_bus * from )

Arguments
=========

``from``
    Previous PCI bus found, or ``NULL`` for new search.


Description
===========

Iterates through the list of known PCI buses. A new search is initiated
by passing ``NULL`` as the ``from`` argument. Otherwise if ``from`` is
not ``NULL``, searches continue from next device on the global list.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
