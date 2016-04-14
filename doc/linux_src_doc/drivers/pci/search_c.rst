.. -*- coding: utf-8; mode: rst -*-

========
search.c
========

.. _`pci_find_bus`:

pci_find_bus
============

.. c:function:: struct pci_bus *pci_find_bus (int domain, int busnr)

    locate PCI bus from a given domain and bus number

    :param int domain:
        number of PCI domain to search

    :param int busnr:
        number of desired PCI bus


.. _`pci_find_bus.description`:

Description
-----------

Given a PCI bus number and domain number, the desired PCI bus is located
in the global list of PCI buses.  If the bus is found, a pointer to its
data structure is returned.  If no bus is found, ``NULL`` is returned.


.. _`pci_find_next_bus`:

pci_find_next_bus
=================

.. c:function:: struct pci_bus *pci_find_next_bus (const struct pci_bus *from)

    begin or continue searching for a PCI bus

    :param const struct pci_bus \*from:
        Previous PCI bus found, or ``NULL`` for new search.


.. _`pci_find_next_bus.description`:

Description
-----------

Iterates through the list of known PCI buses.  A new search is
initiated by passing ``NULL`` as the ``from`` argument.  Otherwise if
``from`` is not ``NULL``\ , searches continue from next device on the
global list.


.. _`pci_get_slot`:

pci_get_slot
============

.. c:function:: struct pci_dev *pci_get_slot (struct pci_bus *bus, unsigned int devfn)

    locate PCI device for a given PCI slot

    :param struct pci_bus \*bus:
        PCI bus on which desired PCI device resides

    :param unsigned int devfn:
        encodes number of PCI slot in which the desired PCI
        device resides and the logical device number within that slot
        in case of multi-function devices.


.. _`pci_get_slot.description`:

Description
-----------

Given a PCI bus and slot/function number, the desired PCI device
is located in the list of PCI devices.
If the device is found, its reference count is increased and this
function returns a pointer to its data structure.  The caller must
decrement the reference count by calling :c:func:`pci_dev_put`.
If no device is found, ``NULL`` is returned.


.. _`pci_get_domain_bus_and_slot`:

pci_get_domain_bus_and_slot
===========================

.. c:function:: struct pci_dev *pci_get_domain_bus_and_slot (int domain, unsigned int bus, unsigned int devfn)

    locate PCI device for a given PCI domain (segment), bus, and slot

    :param int domain:
        PCI domain/segment on which the PCI device resides.

    :param unsigned int bus:
        PCI bus on which desired PCI device resides

    :param unsigned int devfn:
        encodes number of PCI slot in which the desired PCI device
        resides and the logical device number within that slot in case of
        multi-function devices.


.. _`pci_get_domain_bus_and_slot.description`:

Description
-----------

Given a PCI domain, bus, and slot/function number, the desired PCI
device is located in the list of PCI devices. If the device is
found, its reference count is increased and this function returns a
pointer to its data structure.  The caller must decrement the
reference count by calling :c:func:`pci_dev_put`.  If no device is found,
``NULL`` is returned.


.. _`pci_get_subsys`:

pci_get_subsys
==============

.. c:function:: struct pci_dev *pci_get_subsys (unsigned int vendor, unsigned int device, unsigned int ss_vendor, unsigned int ss_device, struct pci_dev *from)

    begin or continue searching for a PCI device by vendor/subvendor/device/subdevice id

    :param unsigned int vendor:
        PCI vendor id to match, or ``PCI_ANY_ID`` to match all vendor ids

    :param unsigned int device:
        PCI device id to match, or ``PCI_ANY_ID`` to match all device ids

    :param unsigned int ss_vendor:
        PCI subsystem vendor id to match, or ``PCI_ANY_ID`` to match all vendor ids

    :param unsigned int ss_device:
        PCI subsystem device id to match, or ``PCI_ANY_ID`` to match all device ids

    :param struct pci_dev \*from:
        Previous PCI device found in search, or ``NULL`` for new search.


.. _`pci_get_subsys.description`:

Description
-----------

Iterates through the list of known PCI devices.  If a PCI device is found
with a matching ``vendor``\ , ``device``\ , ``ss_vendor`` and ``ss_device``\ , a pointer to its
device structure is returned, and the reference count to the device is
incremented.  Otherwise, ``NULL`` is returned.  A new search is initiated by
passing ``NULL`` as the ``from`` argument.  Otherwise if ``from`` is not ``NULL``\ ,
searches continue from next device on the global list.
The reference count for ``from`` is always decremented if it is not ``NULL``\ .


.. _`pci_get_device`:

pci_get_device
==============

.. c:function:: struct pci_dev *pci_get_device (unsigned int vendor, unsigned int device, struct pci_dev *from)

    begin or continue searching for a PCI device by vendor/device id

    :param unsigned int vendor:
        PCI vendor id to match, or ``PCI_ANY_ID`` to match all vendor ids

    :param unsigned int device:
        PCI device id to match, or ``PCI_ANY_ID`` to match all device ids

    :param struct pci_dev \*from:
        Previous PCI device found in search, or ``NULL`` for new search.


.. _`pci_get_device.description`:

Description
-----------

Iterates through the list of known PCI devices.  If a PCI device is
found with a matching ``vendor`` and ``device``\ , the reference count to the
device is incremented and a pointer to its device structure is returned.
Otherwise, ``NULL`` is returned.  A new search is initiated by passing ``NULL``
as the ``from`` argument.  Otherwise if ``from`` is not ``NULL``\ , searches continue
from next device on the global list.  The reference count for ``from`` is
always decremented if it is not ``NULL``\ .


.. _`pci_get_class`:

pci_get_class
=============

.. c:function:: struct pci_dev *pci_get_class (unsigned int class, struct pci_dev *from)

    begin or continue searching for a PCI device by class

    :param unsigned int class:
        search for a PCI device with this class designation

    :param struct pci_dev \*from:
        Previous PCI device found in search, or ``NULL`` for new search.


.. _`pci_get_class.description`:

Description
-----------

Iterates through the list of known PCI devices.  If a PCI device is
found with a matching ``class``\ , the reference count to the device is
incremented and a pointer to its device structure is returned.
Otherwise, ``NULL`` is returned.
A new search is initiated by passing ``NULL`` as the ``from`` argument.
Otherwise if ``from`` is not ``NULL``\ , searches continue from next device
on the global list.  The reference count for ``from`` is always decremented
if it is not ``NULL``\ .


.. _`pci_dev_present`:

pci_dev_present
===============

.. c:function:: int pci_dev_present (const struct pci_device_id *ids)

    Returns 1 if device matching the device list is present, 0 if not.

    :param const struct pci_device_id \*ids:
        A pointer to a null terminated list of struct pci_device_id structures
        that describe the type of PCI device the caller is trying to find.


.. _`pci_dev_present.description`:

Description
-----------

Obvious fact: You do not have a reference to any device that might be found
by this function, so if that device is removed from the system right after
this function is finished, the value will be stale.  Use this function to
find devices that are usually built into a system, or for a general hint as
to if another device happens to be present at this specific moment in time.

