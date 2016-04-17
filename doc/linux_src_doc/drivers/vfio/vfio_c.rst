.. -*- coding: utf-8; mode: rst -*-

======
vfio.c
======


.. _`vfio_register_iommu_driver`:

vfio_register_iommu_driver
==========================

.. c:function:: int vfio_register_iommu_driver (const struct vfio_iommu_driver_ops *ops)

    :param const struct vfio_iommu_driver_ops \*ops:

        *undescribed*



.. _`vfio_alloc_group_minor`:

vfio_alloc_group_minor
======================

.. c:function:: int vfio_alloc_group_minor (struct vfio_group *group)

    both called with vfio.group_lock held

    :param struct vfio_group \*group:

        *undescribed*



.. _`vfio_container_get`:

vfio_container_get
==================

.. c:function:: void vfio_container_get (struct vfio_container *container)

    containers are created when /dev/vfio/vfio is opened, but their lifecycle extends until the last user is done, so it's freed via kref. Must support container/group/device being closed in any order.

    :param struct vfio_container \*container:

        *undescribed*



.. _`vfio_create_group`:

vfio_create_group
=================

.. c:function:: struct vfio_group *vfio_create_group (struct iommu_group *iommu_group)

    create, release, get, put, search

    :param struct iommu_group \*iommu_group:

        *undescribed*



.. _`vfio_group_create_device`:

vfio_group_create_device
========================

.. c:function:: struct vfio_device *vfio_group_create_device (struct vfio_group *group, struct device *dev, const struct vfio_device_ops *ops, void *device_data)

    create, release, get, put, search

    :param struct vfio_group \*group:

        *undescribed*

    :param struct device \*dev:

        *undescribed*

    :param const struct vfio_device_ops \*ops:

        *undescribed*

    :param void \*device_data:

        *undescribed*



.. _`vfio_group_nb_add_dev`:

vfio_group_nb_add_dev
=====================

.. c:function:: int vfio_group_nb_add_dev (struct vfio_group *group, struct device *dev)

    :param struct vfio_group \*group:

        *undescribed*

    :param struct device \*dev:

        *undescribed*



.. _`vfio_add_group_dev`:

vfio_add_group_dev
==================

.. c:function:: int vfio_add_group_dev (struct device *dev, const struct vfio_device_ops *ops, void *device_data)

    :param struct device \*dev:

        *undescribed*

    :param const struct vfio_device_ops \*ops:

        *undescribed*

    :param void \*device_data:

        *undescribed*



.. _`vfio_device_get_from_dev`:

vfio_device_get_from_dev
========================

.. c:function:: struct vfio_device *vfio_device_get_from_dev (struct device *dev)

     caller thinks they own the device, they could be racing with a release call path, so we can't trust drvdata for the shortcut. Go the long way around, from the iommu_group to the vfio_group to the vfio_device.

    :param struct device \*dev:

        *undescribed*



.. _`vfio_ioctl_check_extension`:

vfio_ioctl_check_extension
==========================

.. c:function:: long vfio_ioctl_check_extension (struct vfio_container *container, unsigned long arg)

    :param struct vfio_container \*container:

        *undescribed*

    :param unsigned long arg:

        *undescribed*



.. _`__vfio_group_unset_container`:

__vfio_group_unset_container
============================

.. c:function:: void __vfio_group_unset_container (struct vfio_group *group)

    :param struct vfio_group \*group:

        *undescribed*



.. _`vfio_device_fops_release`:

vfio_device_fops_release
========================

.. c:function:: int vfio_device_fops_release (struct inode *inode, struct file *filep)

    :param struct inode \*inode:

        *undescribed*

    :param struct file \*filep:

        *undescribed*



.. _`vfio_group_get_external_user`:

vfio_group_get_external_user
============================

.. c:function:: struct vfio_group *vfio_group_get_external_user (struct file *filep)

    :param struct file \*filep:

        *undescribed*



.. _`vfio_group_get_external_user.the-protocol-includes`:

The protocol includes
---------------------

1. do normal VFIO init operation:

       - opening a new container;
       - attaching group(s) to it;
       - setting an IOMMU driver for a container.

When IOMMU is set for a container, all groups in it are
considered ready to use by an external user.

2. User space passes a group fd to an external user.
The external user calls :c:func:`vfio_group_get_external_user`



.. _`vfio_group_get_external_user.to-verify-that`:

to verify that
--------------

- the group is initialized;
- IOMMU is set for it.
If both checks passed, :c:func:`vfio_group_get_external_user`
increments the container user counter to prevent
the VFIO group from disposal before KVM exits.

3. The external user calls :c:func:`vfio_external_user_iommu_id`
to know an IOMMU ID.

4. When the external KVM finishes, it calls
:c:func:`vfio_group_put_external_user` to release the VFIO group.
This call decrements the container user counter.



.. _`vfio_info_cap_add`:

vfio_info_cap_add
=================

.. c:function:: struct vfio_info_cap_header *vfio_info_cap_add (struct vfio_info_cap *caps, size_t size, u16 id, u16 version)

    module support

    :param struct vfio_info_cap \*caps:

        *undescribed*

    :param size_t size:

        *undescribed*

    :param u16 id:

        *undescribed*

    :param u16 version:

        *undescribed*



.. _`vfio_devnode`:

vfio_devnode
============

.. c:function:: char *vfio_devnode (struct device *dev, umode_t *mode)

    :param struct device \*dev:

        *undescribed*

    :param umode_t \*mode:

        *undescribed*

