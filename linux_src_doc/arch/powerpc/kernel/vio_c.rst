.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/vio.c

.. _`vio_cmo_num_of_devs`:

vio_cmo_num_OF_devs
===================

.. c:function:: int vio_cmo_num_OF_devs( void)

    Count the number of OF devices that have DMA windows

    :param  void:
        no arguments

.. _`vio_cmo_alloc`:

vio_cmo_alloc
=============

.. c:function:: int vio_cmo_alloc(struct vio_dev *viodev, size_t size)

    allocate IO memory for CMO-enable devices

    :param struct vio_dev \*viodev:
        VIO device requesting IO memory

    :param size_t size:
        size of allocation requested

.. _`vio_cmo_alloc.description`:

Description
-----------

Allocations come from memory reserved for the devices and any excess
IO memory available to all devices.  The spare pool used to service
hotplug must be equal to \ ``VIO_CMO_MIN_ENT``\  for the excess pool to be
made available.

.. _`vio_cmo_alloc.return-codes`:

Return codes
------------

0 for successful allocation and -ENOMEM for a failure

.. _`vio_cmo_dealloc`:

vio_cmo_dealloc
===============

.. c:function:: void vio_cmo_dealloc(struct vio_dev *viodev, size_t size)

    deallocate IO memory from CMO-enable devices

    :param struct vio_dev \*viodev:
        VIO device freeing IO memory

    :param size_t size:
        size of deallocation

.. _`vio_cmo_dealloc.description`:

Description
-----------

IO memory is freed by the device back to the correct memory pools.
The spare pool is replenished first from either memory pool, then
the reserve pool is used to reduce device entitlement, the excess
pool is used to increase the reserve pool toward the desired entitlement
target, and then the remaining memory is returned to the pools.

.. _`vio_cmo_entitlement_update`:

vio_cmo_entitlement_update
==========================

.. c:function:: int vio_cmo_entitlement_update(size_t new_entitlement)

    Manage system entitlement changes

    :param size_t new_entitlement:
        new system entitlement to attempt to accommodate

.. _`vio_cmo_entitlement_update.description`:

Description
-----------

Increases in entitlement will be used to fulfill the spare entitlement
and the rest is given to the excess pool.  Decreases, if they are
possible, come from the excess pool and from unused device entitlement

.. _`vio_cmo_entitlement_update.return`:

Return
------

0 on success, -ENOMEM when change can not be made

.. _`vio_cmo_balance`:

vio_cmo_balance
===============

.. c:function:: void vio_cmo_balance(struct work_struct *work)

    Balance entitlement among devices

    :param struct work_struct \*work:
        work queue structure for this operation

.. _`vio_cmo_balance.description`:

Description
-----------

Any system entitlement above the minimum needed for devices, or
already allocated to devices, can be distributed to the devices.
The list of devices is iterated through to recalculate the desired
entitlement level and to determine how much entitlement above the
minimum entitlement is allocated to devices.

Small chunks of the available entitlement are given to devices until
their requirements are fulfilled or there is no entitlement left to give.
Upon completion sizes of the reserve and excess pools are calculated.

The system minimum entitlement level is also recalculated here.
Entitlement will be reserved for devices even after vio_bus_remove to
accommodate reloading the driver.  The OF tree is walked to count the
number of devices present and this will remove entitlement for devices
that have actually left the system after having vio_bus_remove called.

.. _`vio_cmo_set_dev_desired`:

vio_cmo_set_dev_desired
=======================

.. c:function:: void vio_cmo_set_dev_desired(struct vio_dev *viodev, size_t desired)

    Set desired entitlement for a device

    :param struct vio_dev \*viodev:
        struct vio_dev for device to alter

    :param size_t desired:
        new desired entitlement level in bytes

.. _`vio_cmo_set_dev_desired.description`:

Description
-----------

For use by devices to request a change to their entitlement at runtime or
through sysfs.  The desired entitlement level is changed and a balancing
of system resources is scheduled to run in the future.

.. _`vio_cmo_bus_probe`:

vio_cmo_bus_probe
=================

.. c:function:: int vio_cmo_bus_probe(struct vio_dev *viodev)

    Handle CMO specific bus probe activities

    :param struct vio_dev \*viodev:
        *undescribed*

.. _`vio_cmo_bus_probe.description`:

Description
-----------

\ ``viodev``\  - Pointer to struct vio_dev for device

Determine the devices IO memory entitlement needs, attempting
to satisfy the system minimum entitlement at first and scheduling
a balance operation to take care of the rest at a later time.

.. _`vio_cmo_bus_probe.return`:

Return
------

0 on success, -EINVAL when device doesn't support CMO, and
-ENOMEM when entitlement is not available for device or
device entry.

.. _`vio_cmo_bus_remove`:

vio_cmo_bus_remove
==================

.. c:function:: void vio_cmo_bus_remove(struct vio_dev *viodev)

    Handle CMO specific bus removal activities

    :param struct vio_dev \*viodev:
        *undescribed*

.. _`vio_cmo_bus_remove.description`:

Description
-----------

\ ``viodev``\  - Pointer to struct vio_dev for device

Remove the device from the cmo device list.  The minimum entitlement
will be reserved for the device as long as it is in the system.  The
rest of the entitlement the device had been allocated will be returned
to the system.

.. _`vio_cmo_bus_init`:

vio_cmo_bus_init
================

.. c:function:: void vio_cmo_bus_init( void)

    CMO entitlement initialization at bus init time

    :param  void:
        no arguments

.. _`vio_cmo_bus_init.description`:

Description
-----------

Set up the reserve and excess entitlement pools based on available
system entitlement and the number of devices in the OF tree that
require entitlement in the reserve pool.

.. _`vio_h_cop_sync`:

vio_h_cop_sync
==============

.. c:function:: int vio_h_cop_sync(struct vio_dev *vdev, struct vio_pfo_op *op)

    Perform a synchronous PFO co-processor operation

    :param struct vio_dev \*vdev:
        *undescribed*

    :param struct vio_pfo_op \*op:
        *undescribed*

.. _`vio_h_cop_sync.description`:

Description
-----------

\ ``vdev``\  - Pointer to a struct vio_dev for device
\ ``op``\  - Pointer to a struct vio_pfo_op for the operation parameters

Calls the hypervisor to synchronously perform the PFO operation
described in \ ``op``\ .  In the case of a busy response from the hypervisor,
the operation will be re-submitted indefinitely unless a non-zero timeout
is specified or an error occurs. The timeout places a limit on when to
stop re-submitting a operation, the total time can be exceeded if an
operation is in progress.

If op->hcall_ret is not NULL, this will be set to the return from the
last h_cop_op call or it will be 0 if an error not involving the h_call
was encountered.

.. _`vio_h_cop_sync.return`:

Return
------

0 on success,
-EINVAL if the h_call fails due to an invalid parameter,
-E2BIG if the h_call can not be performed synchronously,
-EBUSY if a timeout is specified and has elapsed,
-EACCES if the memory area for data/status has been rescinded, or
-EPERM if a hardware fault has been indicated

.. _`vio_match_device`:

vio_match_device
================

.. c:function:: const struct vio_device_id *vio_match_device(const struct vio_device_id *ids, const struct vio_dev *dev)

    - Tell if a VIO device has a matching VIO device id structure.

    :param const struct vio_device_id \*ids:
        array of VIO device id structures to search in

    :param const struct vio_dev \*dev:
        the VIO device structure to match against

.. _`vio_match_device.description`:

Description
-----------

Used by a driver to check whether a VIO device present in the
system is in its list of supported devices. Returns the matching
vio_device_id structure or NULL if there is no match.

.. _`__vio_register_driver`:

__vio_register_driver
=====================

.. c:function:: int __vio_register_driver(struct vio_driver *viodrv, struct module *owner, const char *mod_name)

    - Register a new vio driver

    :param struct vio_driver \*viodrv:
        The vio_driver structure to be registered.

    :param struct module \*owner:
        *undescribed*

    :param const char \*mod_name:
        *undescribed*

.. _`vio_unregister_driver`:

vio_unregister_driver
=====================

.. c:function:: void vio_unregister_driver(struct vio_driver *viodrv)

    Remove registration of vio driver.

    :param struct vio_driver \*viodrv:
        The vio_driver struct to be removed form registration

.. _`vio_register_device_node`:

vio_register_device_node
========================

.. c:function:: struct vio_dev *vio_register_device_node(struct device_node *of_node)

    - Register a new vio device.

    :param struct device_node \*of_node:
        The OF node for this device.

.. _`vio_register_device_node.description`:

Description
-----------

Creates and initializes a vio_dev structure from the data in
of_node and adds it to the list of virtual devices.
Returns a pointer to the created vio_dev or NULL if node has
NULL device_type or compatible fields.

.. _`vio_bus_init`:

vio_bus_init
============

.. c:function:: int vio_bus_init( void)

    - Initialize the virtual IO bus

    :param  void:
        no arguments

.. _`vio_get_attribute`:

vio_get_attribute
=================

.. c:function:: const void *vio_get_attribute(struct vio_dev *vdev, char *which, int *length)

    - get attribute for virtual device

    :param struct vio_dev \*vdev:
        The vio device to get property.

    :param char \*which:
        The property/attribute to be extracted.

    :param int \*length:
        Pointer to length of returned data size (unused if NULL).

.. _`vio_get_attribute.description`:

Description
-----------

Calls prom.c's \ :c:func:`of_get_property`\  to return the value of the
attribute specified by \ ``which``\ 

.. _`vio_find_node`:

vio_find_node
=============

.. c:function:: struct vio_dev *vio_find_node(struct device_node *vnode)

    find an already-registered vio_dev

    :param struct device_node \*vnode:
        device_node of the virtual device we're looking for

.. This file was automatic generated / don't edit.

