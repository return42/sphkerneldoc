.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pci-driver.c

.. _`pci_add_dynid`:

pci_add_dynid
=============

.. c:function:: int pci_add_dynid(struct pci_driver *drv, unsigned int vendor, unsigned int device, unsigned int subvendor, unsigned int subdevice, unsigned int class, unsigned int class_mask, unsigned long driver_data)

    add a new PCI device ID to this driver and re-probe devices

    :param struct pci_driver \*drv:
        target pci driver

    :param unsigned int vendor:
        PCI vendor ID

    :param unsigned int device:
        PCI device ID

    :param unsigned int subvendor:
        PCI subvendor ID

    :param unsigned int subdevice:
        PCI subdevice ID

    :param unsigned int class:
        PCI class

    :param unsigned int class_mask:
        PCI class mask

    :param unsigned long driver_data:
        private driver data

.. _`pci_add_dynid.description`:

Description
-----------

Adds a new dynamic pci device ID to this driver and causes the
driver to probe for all devices again.  \ ``drv``\  must have been
registered prior to calling this function.

.. _`pci_add_dynid.context`:

Context
-------

Does GFP_KERNEL allocation.

.. _`pci_add_dynid.return`:

Return
------

0 on success, -errno on failure.

.. _`new_id_store`:

new_id_store
============

.. c:function:: ssize_t new_id_store(struct device_driver *driver, const char *buf, size_t count)

    sysfs frontend to \ :c:func:`pci_add_dynid`\ 

    :param struct device_driver \*driver:
        target device driver

    :param const char \*buf:
        buffer for scanning device ID data

    :param size_t count:
        input size

.. _`new_id_store.description`:

Description
-----------

Allow PCI IDs to be added to an existing driver via sysfs.

.. _`remove_id_store`:

remove_id_store
===============

.. c:function:: ssize_t remove_id_store(struct device_driver *driver, const char *buf, size_t count)

    remove a PCI device ID from this driver

    :param struct device_driver \*driver:
        target device driver

    :param const char \*buf:
        buffer for scanning device ID data

    :param size_t count:
        input size

.. _`remove_id_store.description`:

Description
-----------

Removes a dynamic pci device ID to this driver.

.. _`pci_match_id`:

pci_match_id
============

.. c:function:: const struct pci_device_id *pci_match_id(const struct pci_device_id *ids, struct pci_dev *dev)

    See if a pci device matches a given pci_id table

    :param const struct pci_device_id \*ids:
        array of PCI device id structures to search in

    :param struct pci_dev \*dev:
        the PCI device structure to match against.

.. _`pci_match_id.description`:

Description
-----------

Used by a driver to check whether a PCI device present in the
system is in its list of supported devices.  Returns the matching
pci_device_id structure or \ ``NULL``\  if there is no match.

Deprecated, don't use this as it will not catch any dynamic ids
that a driver might want to check for.

.. _`pci_match_device`:

pci_match_device
================

.. c:function:: const struct pci_device_id *pci_match_device(struct pci_driver *drv, struct pci_dev *dev)

    Tell if a PCI device structure has a matching PCI device id structure

    :param struct pci_driver \*drv:
        the PCI driver to match against

    :param struct pci_dev \*dev:
        the PCI device structure to match against

.. _`pci_match_device.description`:

Description
-----------

Used by a driver to check whether a PCI device present in the
system is in its list of supported devices.  Returns the matching
pci_device_id structure or \ ``NULL``\  if there is no match.

.. _`__pci_device_probe`:

__pci_device_probe
==================

.. c:function:: int __pci_device_probe(struct pci_driver *drv, struct pci_dev *pci_dev)

    check if a driver wants to claim a specific PCI device

    :param struct pci_driver \*drv:
        driver to call to check if it wants the PCI device

    :param struct pci_dev \*pci_dev:
        PCI device being probed

.. _`__pci_device_probe.description`:

Description
-----------

returns 0 on success, else error.
side-effect: pci_dev->driver is set to drv when drv claims pci_dev.

.. _`pci_restore_standard_config`:

pci_restore_standard_config
===========================

.. c:function:: int pci_restore_standard_config(struct pci_dev *pci_dev)

    restore standard config registers of PCI device

    :param struct pci_dev \*pci_dev:
        PCI device to handle

.. _`__pci_register_driver`:

__pci_register_driver
=====================

.. c:function:: int __pci_register_driver(struct pci_driver *drv, struct module *owner, const char *mod_name)

    register a new pci driver

    :param struct pci_driver \*drv:
        the driver structure to register

    :param struct module \*owner:
        owner module of drv

    :param const char \*mod_name:
        module name string

.. _`__pci_register_driver.description`:

Description
-----------

Adds the driver structure to the list of registered drivers.
Returns a negative value on error, otherwise 0.
If no error occurred, the driver remains registered even if
no device was claimed during registration.

.. _`pci_unregister_driver`:

pci_unregister_driver
=====================

.. c:function:: void pci_unregister_driver(struct pci_driver *drv)

    unregister a pci driver

    :param struct pci_driver \*drv:
        the driver structure to unregister

.. _`pci_unregister_driver.description`:

Description
-----------

Deletes the driver structure from the list of registered PCI drivers,
gives it a chance to clean up by calling its \ :c:func:`remove`\  function for
each device it was responsible for, and marks those devices as
driverless.

.. _`pci_dev_driver`:

pci_dev_driver
==============

.. c:function:: struct pci_driver *pci_dev_driver(const struct pci_dev *dev)

    get the pci_driver of a device

    :param const struct pci_dev \*dev:
        the device to query

.. _`pci_dev_driver.description`:

Description
-----------

Returns the appropriate pci_driver structure or \ ``NULL``\  if there is no
registered driver for the device.

.. _`pci_bus_match`:

pci_bus_match
=============

.. c:function:: int pci_bus_match(struct device *dev, struct device_driver *drv)

    Tell if a PCI device structure has a matching PCI device id structure

    :param struct device \*dev:
        the PCI device structure to match against

    :param struct device_driver \*drv:
        the device driver to search for matching PCI device id structures

.. _`pci_bus_match.description`:

Description
-----------

Used by a driver to check whether a PCI device present in the
system is in its list of supported devices. Returns the matching
pci_device_id structure or \ ``NULL``\  if there is no match.

.. _`pci_dev_get`:

pci_dev_get
===========

.. c:function:: struct pci_dev *pci_dev_get(struct pci_dev *dev)

    increments the reference count of the pci device structure

    :param struct pci_dev \*dev:
        the device being referenced

.. _`pci_dev_get.description`:

Description
-----------

Each live reference to a device should be refcounted.

Drivers for PCI devices should normally record such references in
their \ :c:func:`probe`\  methods, when they bind to a device, and release
them by calling \ :c:func:`pci_dev_put`\ , in their \ :c:func:`disconnect`\  methods.

A pointer to the device with the incremented reference counter is returned.

.. _`pci_dev_put`:

pci_dev_put
===========

.. c:function:: void pci_dev_put(struct pci_dev *dev)

    release a use of the pci device structure

    :param struct pci_dev \*dev:
        device that's been disconnected

.. _`pci_dev_put.description`:

Description
-----------

Must be called when a user of a device is finished with it.  When the last
user of the device calls this function, the memory of the device is freed.

.. This file was automatic generated / don't edit.

