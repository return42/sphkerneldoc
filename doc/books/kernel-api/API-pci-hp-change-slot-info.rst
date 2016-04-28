.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-hp-change-slot-info:

=======================
pci_hp_change_slot_info
=======================

*man pci_hp_change_slot_info(9)*

*4.6.0-rc5*

changes the slot's information structure in the core


Synopsis
========

.. c:function:: int pci_hp_change_slot_info( struct hotplug_slot * slot, struct hotplug_slot_info * info )

Arguments
=========

``slot``
    pointer to the slot whose info has changed

``info``
    pointer to the info copy into the slot's info structure


Description
===========

``slot`` must have been registered with the pci hotplug subsystem
previously with a call to ``pci_hp_register``.

Returns 0 if successful, anything else for an error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
