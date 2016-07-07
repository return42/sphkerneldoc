.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/vfio.h

.. _`vfio_device_ops`:

struct vfio_device_ops
======================

.. c:type:: struct vfio_device_ops

    VFIO bus driver device callbacks

.. _`vfio_device_ops.definition`:

Definition
----------

.. code-block:: c

    struct vfio_device_ops {
        char *name;
        int (* open) (void *device_data);
        void (* release) (void *device_data);
        ssize_t (* read) (void *device_data, char __user *buf,size_t count, loff_t *ppos);
        ssize_t (* write) (void *device_data, const char __user *buf,size_t count, loff_t *size);
        long (* ioctl) (void *device_data, unsigned int cmd,unsigned long arg);
        int (* mmap) (void *device_data, struct vm_area_struct *vma);
        void (* request) (void *device_data, unsigned int count);
    }

.. _`vfio_device_ops.members`:

Members
-------

name
    *undescribed*

open
    Called when userspace creates new file descriptor for device

release
    Called when userspace releases file descriptor for device

read
    Perform read(2) on device file descriptor

write
    Perform write(2) on device file descriptor

ioctl
    Perform ioctl(2) on device file descriptor, supporting VFIO_DEVICE\_\*
    operations documented below

mmap
    Perform mmap(2) on a region of the device file descriptor

request
    Request for the bus driver to release the device

.. _`vfio_iommu_driver_ops`:

struct vfio_iommu_driver_ops
============================

.. c:type:: struct vfio_iommu_driver_ops

    VFIO IOMMU driver callbacks

.. _`vfio_iommu_driver_ops.definition`:

Definition
----------

.. code-block:: c

    struct vfio_iommu_driver_ops {
        char *name;
        struct module *owner;
        void *(* open) (unsigned long arg);
        void (* release) (void *iommu_data);
        ssize_t (* read) (void *iommu_data, char __user *buf,size_t count, loff_t *ppos);
        ssize_t (* write) (void *iommu_data, const char __user *buf,size_t count, loff_t *size);
        long (* ioctl) (void *iommu_data, unsigned int cmd,unsigned long arg);
        int (* mmap) (void *iommu_data, struct vm_area_struct *vma);
        int (* attach_group) (void *iommu_data,struct iommu_group *group);
        void (* detach_group) (void *iommu_data,struct iommu_group *group);
    }

.. _`vfio_iommu_driver_ops.members`:

Members
-------

name
    *undescribed*

owner
    *undescribed*

open
    *undescribed*

release
    *undescribed*

read
    *undescribed*

write
    *undescribed*

ioctl
    *undescribed*

mmap
    *undescribed*

attach_group
    *undescribed*

detach_group
    *undescribed*

.. This file was automatic generated / don't edit.

