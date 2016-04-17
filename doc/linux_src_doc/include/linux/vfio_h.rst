.. -*- coding: utf-8; mode: rst -*-

======
vfio.h
======


.. _`vfio_device_ops`:

struct vfio_device_ops
======================

.. c:type:: vfio_device_ops

    VFIO bus driver device callbacks


.. _`vfio_device_ops.definition`:

Definition
----------

.. code-block:: c

  struct vfio_device_ops {
    int (* open) (void *device_data);
    void (* release) (void *device_data);
    ssize_t (* read) (void *device_data, char __user *buf,size_t count, loff_t *ppos);
    ssize_t (* write) (void *device_data, const char __user *buf,size_t count, loff_t *size);
    long (* ioctl) (void *device_data, unsigned int cmd,unsigned long arg);
    int (* mmap) (void *device_data, struct vm_area_struct *vma);
    void (* request) (void *device_data, unsigned int count);
  };


.. _`vfio_device_ops.members`:

Members
-------

:``open``:
    Called when userspace creates new file descriptor for device

:``release``:
    Called when userspace releases file descriptor for device

:``read``:
    Perform read(2) on device file descriptor

:``write``:
    Perform write(2) on device file descriptor

:``ioctl``:
    Perform ioctl(2) on device file descriptor, supporting VFIO_DEVICE\_\*
    operations documented below

:``mmap``:
    Perform mmap(2) on a region of the device file descriptor

:``request``:
    Request for the bus driver to release the device




.. _`vfio_iommu_driver_ops`:

struct vfio_iommu_driver_ops
============================

.. c:type:: vfio_iommu_driver_ops

    VFIO IOMMU driver callbacks


.. _`vfio_iommu_driver_ops.definition`:

Definition
----------

.. code-block:: c

  struct vfio_iommu_driver_ops {
  };


.. _`vfio_iommu_driver_ops.members`:

Members
-------


