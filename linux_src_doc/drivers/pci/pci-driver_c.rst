.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pci-driver.c

.. _`pci_add_dynid`:

pci_add_dynid
=============

.. c:function:: int pci_add_dynid(struct pci_driver *drv, unsigned int vendor, unsigned int device, unsigned int subvendor, unsigned int subdevice, unsigned int class, unsigned int class_mask, unsigned long driver_data)

    add a new PCI device ID to this driver and re-probe devices

    :param drv:
        target pci driver
    :type drv: struct pci_driver \*

    :param vendor:
        PCI vendor ID
    :type vendor: unsigned int

    :param device:
        PCI device ID
    :type device: unsigned int

    :param subvendor:
        PCI subvendor ID
    :type subvendor: unsigned int

    :param subdevice:
        PCI subdevice ID
    :type subdevice: unsigned int

    :param class:
        PCI class
    :type class: unsigned int

    :param class_mask:
        PCI class mask
    :type class_mask: unsigned int

    :param driver_data:
        private driver data
    :type driver_data: unsigned long

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

    :param driver:
        target device driver
    :type driver: struct device_driver \*

    :param buf:
        buffer for scanning device ID data
    :type buf: const char \*

    :param count:
        input size
    :type count: size_t

.. _`new_id_store.description`:

Description
-----------

Allow PCI IDs to be added to an existing driver via sysfs.

.. _`remove_id_store`:

remove_id_store
===============

.. c:function:: ssize_t remove_id_store(struct device_driver *driver, const char *buf, size_t count)

    remove a PCI device ID from this driver

    :param driver:
        target device driver
    :type driver: struct device_driver \*

    :param buf:
        buffer for scanning device ID data
    :type buf: const char \*

    :param count:
        input size
    :type count: size_t

.. _`remove_id_store.description`:

Description
-----------

Removes a dynamic pci device ID to this driver.

.. _`pci_match_id`:

pci_match_id
============

.. c:function:: const struct pci_device_id *pci_match_id(const struct pci_device_id *ids, struct pci_dev *dev)

    See if a pci device matches a given pci_id table

    :param ids:
        array of PCI device id structures to search in
    :type ids: const struct pci_device_id \*

    :param dev:
        the PCI device structure to match against.
    :type dev: struct pci_dev \*

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

    :param drv:
        the PCI driver to match against
    :type drv: struct pci_driver \*

    :param dev:
        the PCI device structure to match against
    :type dev: struct pci_dev \*

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

    :param drv:
        driver to call to check if it wants the PCI device
    :type drv: struct pci_driver \*

    :param pci_dev:
        PCI device being probed
    :type pci_dev: struct pci_dev \*

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

    :param pci_dev:
        PCI device to handle
    :type pci_dev: struct pci_dev \*

.. _`__pci_register_driver`:

__pci_register_driver
=====================

.. c:function:: int __pci_register_driver(struct pci_driver *drv, struct module *owner, const char *mod_name)

    register a new pci driver

    :param drv:
        the driver structure to register
    :type drv: struct pci_driver \*

    :param owner:
        owner module of drv
    :type owner: struct module \*

    :param mod_name:
        module name string
    :type mod_name: const char \*

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

    :param drv:
        the driver structure to unregister
    :type drv: struct pci_driver \*

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

    :param dev:
        the device to query
    :type dev: const struct pci_dev \*

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

    :param dev:
        the PCI device structure to match against
    :type dev: struct device \*

    :param drv:
        the device driver to search for matching PCI device id structures
    :type drv: struct device_driver \*

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

    :param dev:
        the device being referenced
    :type dev: struct pci_dev \*

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

    :param dev:
        device that's been disconnected
    :type dev: struct pci_dev \*

.. _`pci_dev_put.description`:

Description
-----------

Must be called when a user of a device is finished with it.  When the last
user of the device calls this function, the memory of the device is freed.

.. _`pci_uevent_ers`:

pci_uevent_ers
==============

.. c:function:: void pci_uevent_ers(struct pci_dev *pdev, enum pci_ers_result err_type)

    emit a uevent during recovery path of PCI device

    :param pdev:
        PCI device undergoing error recovery
    :type pdev: struct pci_dev \*

    :param err_type:
        type of error event
    :type err_type: enum pci_ers_result

.. _`pci_dma_configure`:

pci_dma_configure
=================

.. c:function:: int pci_dma_configure(struct device *dev)

    Setup DMA configuration

    :param dev:
        ptr to dev structure
    :type dev: struct device \*

.. _`pci_dma_configure.description`:

Description
-----------

Function to update PCI devices's DMA configuration using the same
info from the OF node or ACPI node of host bridge's parent (if any).

.. This file was automatic generated / don't edit.

