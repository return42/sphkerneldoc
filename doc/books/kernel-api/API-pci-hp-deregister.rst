.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-hp-deregister:

=================
pci_hp_deregister
=================

*man pci_hp_deregister(9)*

*4.6.0-rc5*

deregister a hotplug_slot with the PCI hotplug subsystem


Synopsis
========

.. c:function:: int pci_hp_deregister( struct hotplug_slot * slot )

Arguments
=========

``slot``
    pointer to the ``struct hotplug_slot`` to deregister


Description
===========

The ``slot`` must have been registered with the pci hotplug subsystem
previously with a call to ``pci_hp_register``.

Returns 0 if successful, anything else for an error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
