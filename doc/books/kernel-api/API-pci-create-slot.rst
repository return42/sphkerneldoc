
.. _API-pci-create-slot:

===============
pci_create_slot
===============

*man pci_create_slot(9)*

*4.6.0-rc1*

create or increment refcount for physical PCI slot


Synopsis
========

.. c:function:: struct pci_slot ⋆ pci_create_slot( struct pci_bus * parent, int slot_nr, const char * name, struct hotplug_slot * hotplug )

Arguments
=========

``parent``
    struct pci_bus of parent bridge

``slot_nr``
    PCI_SLOT(pci_dev->devfn) or -1 for placeholder

``name``
    user visible string presented in /sys/bus/pci/slots/<name>

``hotplug``
    set if caller is hotplug driver, NULL otherwise


Description
===========

PCI slots have first class attributes such as address, speed, width, and a ``struct pci_slot`` is used to manage them. This interface will either return a new ``struct pci_slot``
to the caller, or if the pci_slot already exists, its refcount will be incremented.

Slots are uniquely identified by a ``pci_bus``, ``slot_nr`` tuple.

There are known platforms with broken firmware that assign the same name to multiple slots. Workaround these broken platforms by renaming the slots on behalf of the caller. If
firmware assigns name N to


multiple slots
==============

The first slot is assigned N The second slot is assigned N-1 The third slot is assigned N-2 etc.


Placeholder slots
=================

In most cases, ``pci_bus``, ``slot_nr`` will be sufficient to uniquely identify a slot. There is one notable exception - pSeries (rpaphp), where the ``slot_nr`` cannot be
determined until a device is actually inserted into the slot. In this scenario, the caller may pass -1 for ``slot_nr``.

The following semantics are imposed when the caller passes ``slot_nr`` == -1. First, we no longer check for an existing ``struct`` pci_slot, as there may be many slots with
``slot_nr`` of -1. The other change in semantics is user-visible, which is the 'address' parameter presented in sysfs will


consist solely of a dddd
========================

bb tuple, where dddd is the PCI domain of the ``struct`` pci_bus and bb is the bus number. In other words, the devfn of the 'placeholder' slot will not be displayed.
