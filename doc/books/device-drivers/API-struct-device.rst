.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-device:

=============
struct device
=============

*man struct device(9)*

*4.6.0-rc5*

The basic device structure


Synopsis
========

.. code-block:: c

    struct device {
      struct device * parent;
      struct device_private * p;
      struct kobject kobj;
      const char * init_name;
      const struct device_type * type;
      struct mutex mutex;
      struct bus_type * bus;
      struct device_driver * driver;
      void * platform_data;
      void * driver_data;
      struct dev_pm_info power;
      struct dev_pm_domain * pm_domain;
    #ifdef CONFIG_GENERIC_MSI_IRQ_DOMAIN
      struct irq_domain * msi_domain;
    #endif
    #ifdef CONFIG_PINCTRL
      struct dev_pin_info * pins;
    #endif
    #ifdef CONFIG_GENERIC_MSI_IRQ
      struct list_head msi_list;
    #endif
    #ifdef CONFIG_NUMA
      int numa_node;
    #endif
      u64 * dma_mask;
      u64 coherent_dma_mask;
      unsigned long dma_pfn_offset;
      struct device_dma_parameters * dma_parms;
      struct list_head dma_pools;
      struct dma_coherent_mem * dma_mem;
    #ifdef CONFIG_DMA_CMA
      struct cma * cma_area;
    #endif
      struct dev_archdata archdata;
      struct device_node * of_node;
      struct fwnode_handle * fwnode;
      dev_t devt;
      u32 id;
      spinlock_t devres_lock;
      struct list_head devres_head;
      struct klist_node knode_class;
      struct class * class;
      const struct attribute_group ** groups;
      void (* release) (struct device *dev);
      struct iommu_group * iommu_group;
      bool offline_disabled:1;
      bool offline:1;
    };


Members
=======

parent
    The device's “parent” device, the device to which it is attached. In
    most cases, a parent device is some sort of bus or host controller.
    If parent is NULL, the device, is a top-level device, which is not
    usually what you want.

p
    Holds the private data of the driver core portions of the device.
    See the comment of the struct device_private for detail.

kobj
    A top-level, abstract class from which other classes are derived.

init_name
    Initial name of the device.

type
    The type of device. This identifies the device type and carries
    type-specific information.

mutex
    Mutex to synchronize calls to its driver.

bus
    Type of bus device is on.

driver
    Which driver has allocated this

platform_data
    Platform data specific to the device.

driver_data
    Private pointer for driver specific info.

power
    For device power management. See Documentation/power/devices.txt for
    details.

pm_domain
    Provide callbacks that are executed during system suspend,
    hibernation, system resume and during runtime PM transitions along
    with subsystem-level and driver-level callbacks.

msi_domain
    The generic MSI domain this device is using.

pins
    For device pin management. See Documentation/pinctrl.txt for
    details.

msi_list
    Hosts MSI descriptors

numa_node
    NUMA node this device is close to.

dma_mask
    Dma mask (if dma'ble device).

coherent_dma_mask
    Like dma_mask, but for alloc_coherent mapping as not all hardware
    supports 64-bit addresses for consistent allocations such
    descriptors.

dma_pfn_offset
    offset of DMA memory range relatively of RAM

dma_parms
    A low level driver may set these to teach IOMMU code about segment
    limitations.

dma_pools
    Dma pools (if dma'ble device).

dma_mem
    Internal for coherent mem override.

cma_area
    Contiguous memory area for dma allocations

archdata
    For arch-specific additions.

of_node
    Associated device tree node.

fwnode
    Associated device node supplied by platform firmware.

devt
    For creating the sysfs “dev”.

id
    device instance

devres_lock
    Spinlock to protect the resource of the device.

devres_head
    The resources list of the device.

knode_class
    The node used to add the device to the class list.

class
    The class of the device.

groups
    Optional attribute groups.

release
    Callback to free the device after all references have gone away.
    This should be set by the allocator of the device (i.e. the bus
    driver that discovered the device).

iommu_group
    IOMMU group the device belongs to.

offline_disabled
    If set, the device is permanently online.

offline
    Set after successful invocation of bus type's .\ ``offline``.


Example
=======


.. code-block:: c

       For devices on custom boards, as typical of embedded
            and SOC based hardware, Linux often uses platform_data to point
            to board-specific structures describing devices and how they
            are wired.  That can include what ports are available, chip
            variants, which GPIO pins act in what additional roles, and so
            on.  This shrinks the Board Support Packages (BSPs) and
            minimizes board-specific #ifdefs in drivers.


Description
===========

At the lowest level, every device in a Linux system is represented by an
instance of struct device. The device structure contains the information
that the device model core needs to model the system. Most subsystems,
however, track additional information about the devices they host. As a
result, it is rare for devices to be represented by bare device
structures; instead, that structure, like kobject structures, is usually
embedded within a higher-level representation of the device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
