.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/iommu.c

.. _`iommu_group_alloc`:

iommu_group_alloc
=================

.. c:function:: struct iommu_group *iommu_group_alloc( void)

    Allocate a new group

    :param  void:
        no arguments

.. _`iommu_group_alloc.description`:

Description
-----------

This function is called by an iommu driver to allocate a new iommu
group.  The iommu group represents the minimum granularity of the iommu.
Upon successful return, the caller holds a reference to the supplied
group in order to hold the group until devices are added.  Use
\ :c:func:`iommu_group_put`\  to release this extra reference count, allowing the
group to be automatically reclaimed once it has no devices or external
references.

.. _`iommu_group_get_iommudata`:

iommu_group_get_iommudata
=========================

.. c:function:: void *iommu_group_get_iommudata(struct iommu_group *group)

    retrieve iommu_data registered for a group

    :param struct iommu_group \*group:
        the group

.. _`iommu_group_get_iommudata.description`:

Description
-----------

iommu drivers can store data in the group for use when doing iommu
operations.  This function provides a way to retrieve it.  Caller
should hold a group reference.

.. _`iommu_group_set_iommudata`:

iommu_group_set_iommudata
=========================

.. c:function:: void iommu_group_set_iommudata(struct iommu_group *group, void *iommu_data, void (*release)(void *iommu_data))

    set iommu_data for a group

    :param struct iommu_group \*group:
        the group

    :param void \*iommu_data:
        new data

    :param void (\*release)(void \*iommu_data):
        release function for iommu_data

.. _`iommu_group_set_iommudata.description`:

Description
-----------

iommu drivers can store data in the group for use when doing iommu
operations.  This function provides a way to set the data after
the group has been allocated.  Caller should hold a group reference.

.. _`iommu_group_set_name`:

iommu_group_set_name
====================

.. c:function:: int iommu_group_set_name(struct iommu_group *group, const char *name)

    set name for a group

    :param struct iommu_group \*group:
        the group

    :param const char \*name:
        name

.. _`iommu_group_set_name.description`:

Description
-----------

Allow iommu driver to set a name for a group.  When set it will
appear in a name attribute file under the group in sysfs.

.. _`iommu_group_add_device`:

iommu_group_add_device
======================

.. c:function:: int iommu_group_add_device(struct iommu_group *group, struct device *dev)

    add a device to an iommu group

    :param struct iommu_group \*group:
        the group into which to add the device (reference should be held)

    :param struct device \*dev:
        the device

.. _`iommu_group_add_device.description`:

Description
-----------

This function is called by an iommu driver to add a device into a
group.  Adding a device increments the group reference count.

.. _`iommu_group_remove_device`:

iommu_group_remove_device
=========================

.. c:function:: void iommu_group_remove_device(struct device *dev)

    remove a device from it's current group

    :param struct device \*dev:
        device to be removed

.. _`iommu_group_remove_device.description`:

Description
-----------

This function is called by an iommu driver to remove the device from
it's current group.  This decrements the iommu group reference count.

.. _`__iommu_group_for_each_dev`:

__iommu_group_for_each_dev
==========================

.. c:function:: int __iommu_group_for_each_dev(struct iommu_group *group, void *data, int (*fn)(struct device *, void *))

    iterate over each device in the group

    :param struct iommu_group \*group:
        the group

    :param void \*data:
        caller opaque data to be passed to callback function

    :param int (\*fn)(struct device \*, void \*):
        caller supplied callback function

.. _`__iommu_group_for_each_dev.description`:

Description
-----------

This function is called by group users to iterate over group devices.
Callers should hold a reference count to the group during callback.
The group->mutex is held across callbacks, which will block calls to
iommu_group_add/remove_device.

.. _`iommu_group_get`:

iommu_group_get
===============

.. c:function:: struct iommu_group *iommu_group_get(struct device *dev)

    Return the group for a device and increment reference

    :param struct device \*dev:
        get the group that this device belongs to

.. _`iommu_group_get.description`:

Description
-----------

This function is called by iommu drivers and users to get the group
for the specified device.  If found, the group is returned and the group
reference in incremented, else NULL.

.. _`iommu_group_ref_get`:

iommu_group_ref_get
===================

.. c:function:: struct iommu_group *iommu_group_ref_get(struct iommu_group *group)

    Increment reference on a group

    :param struct iommu_group \*group:
        the group to use, must not be NULL

.. _`iommu_group_ref_get.description`:

Description
-----------

This function is called by iommu drivers to take additional references on an
existing group.  Returns the given group for convenience.

.. _`iommu_group_put`:

iommu_group_put
===============

.. c:function:: void iommu_group_put(struct iommu_group *group)

    Decrement group reference

    :param struct iommu_group \*group:
        the group to use

.. _`iommu_group_put.description`:

Description
-----------

This function is called by iommu drivers and users to release the
iommu group.  Once the reference count is zero, the group is released.

.. _`iommu_group_register_notifier`:

iommu_group_register_notifier
=============================

.. c:function:: int iommu_group_register_notifier(struct iommu_group *group, struct notifier_block *nb)

    Register a notifier for group changes

    :param struct iommu_group \*group:
        the group to watch

    :param struct notifier_block \*nb:
        notifier block to signal

.. _`iommu_group_register_notifier.description`:

Description
-----------

This function allows iommu group users to track changes in a group.
See include/linux/iommu.h for actions sent via this notifier.  Caller
should hold a reference to the group throughout notifier registration.

.. _`iommu_group_unregister_notifier`:

iommu_group_unregister_notifier
===============================

.. c:function:: int iommu_group_unregister_notifier(struct iommu_group *group, struct notifier_block *nb)

    Unregister a notifier

    :param struct iommu_group \*group:
        the group to watch

    :param struct notifier_block \*nb:
        notifier block to signal

.. _`iommu_group_unregister_notifier.description`:

Description
-----------

Unregister a previously registered group notifier block.

.. _`iommu_group_id`:

iommu_group_id
==============

.. c:function:: int iommu_group_id(struct iommu_group *group)

    Return ID for a group

    :param struct iommu_group \*group:
        the group to ID

.. _`iommu_group_id.description`:

Description
-----------

Return the unique ID for the group matching the sysfs group number.

.. _`iommu_group_get_for_dev`:

iommu_group_get_for_dev
=======================

.. c:function:: struct iommu_group *iommu_group_get_for_dev(struct device *dev)

    Find or create the IOMMU group for a device

    :param struct device \*dev:
        target device

.. _`iommu_group_get_for_dev.description`:

Description
-----------

This function is intended to be called by IOMMU drivers and extended to
support common, bus-defined algorithms when determining or creating the
IOMMU group for a device.  On success, the caller will hold a reference
to the returned IOMMU group, which will already include the provided
device.  The reference should be released with \ :c:func:`iommu_group_put`\ .

.. _`bus_set_iommu`:

bus_set_iommu
=============

.. c:function:: int bus_set_iommu(struct bus_type *bus, const struct iommu_ops *ops)

    set iommu-callbacks for the bus

    :param struct bus_type \*bus:
        bus.

    :param const struct iommu_ops \*ops:
        the callbacks provided by the iommu-driver

.. _`bus_set_iommu.description`:

Description
-----------

This function is called by an iommu driver to set the iommu methods
used for a particular bus. Drivers for devices on that bus can use
the iommu-api after these ops are registered.
This special function is needed because IOMMUs are usually devices on
the bus itself, so the iommu drivers are not initialized when the bus
is set up. With this function the iommu-driver can set the iommu-ops
afterwards.

.. _`iommu_set_fault_handler`:

iommu_set_fault_handler
=======================

.. c:function:: void iommu_set_fault_handler(struct iommu_domain *domain, iommu_fault_handler_t handler, void *token)

    set a fault handler for an iommu domain

    :param struct iommu_domain \*domain:
        iommu domain

    :param iommu_fault_handler_t handler:
        fault handler

    :param void \*token:
        user data, will be passed back to the fault handler

.. _`iommu_set_fault_handler.description`:

Description
-----------

This function should be used by IOMMU users which want to be notified
whenever an IOMMU fault happens.

The fault handler itself should return 0 on success, and an appropriate
error code otherwise.

.. This file was automatic generated / don't edit.

