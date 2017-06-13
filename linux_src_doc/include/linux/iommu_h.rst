.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iommu.h

.. _`iommu_resv_region`:

struct iommu_resv_region
========================

.. c:type:: struct iommu_resv_region

    descriptor for a reserved memory region

.. _`iommu_resv_region.definition`:

Definition
----------

.. code-block:: c

    struct iommu_resv_region {
        struct list_head list;
        phys_addr_t start;
        size_t length;
        int prot;
        enum iommu_resv_type type;
    }

.. _`iommu_resv_region.members`:

Members
-------

list
    Linked list pointers

start
    System physical start address of the region

length
    Length of the region in bytes

prot
    IOMMU Protection flags (READ/WRITE/...)

type
    Type of the reserved region

.. _`iommu_ops`:

struct iommu_ops
================

.. c:type:: struct iommu_ops

    iommu ops and capabilities

.. _`iommu_ops.definition`:

Definition
----------

.. code-block:: c

    struct iommu_ops {
        bool (*capable)(enum iommu_cap);
        struct iommu_domain *(*domain_alloc)(unsigned iommu_domain_type);
        void (*domain_free)(struct iommu_domain *);
        int (*attach_dev)(struct iommu_domain *domain, struct device *dev);
        void (*detach_dev)(struct iommu_domain *domain, struct device *dev);
        int (*map)(struct iommu_domain *domain, unsigned long iova,phys_addr_t paddr, size_t size, int prot);
        size_t (*unmap)(struct iommu_domain *domain, unsigned long iova,size_t size);
        size_t (*map_sg)(struct iommu_domain *domain, unsigned long iova,struct scatterlist *sg, unsigned int nents, int prot);
        phys_addr_t (*iova_to_phys)(struct iommu_domain *domain, dma_addr_t iova);
        int (*add_device)(struct device *dev);
        void (*remove_device)(struct device *dev);
        struct iommu_group *(*device_group)(struct device *dev);
        int (*domain_get_attr)(struct iommu_domain *domain,enum iommu_attr attr, void *data);
        int (*domain_set_attr)(struct iommu_domain *domain,enum iommu_attr attr, void *data);
        void (*get_resv_regions)(struct device *dev, struct list_head *list);
        void (*put_resv_regions)(struct device *dev, struct list_head *list);
        void (*apply_resv_region)(struct device *dev,struct iommu_domain *domain,struct iommu_resv_region *region);
        int (*domain_window_enable)(struct iommu_domain *domain, u32 wnd_nr,phys_addr_t paddr, u64 size, int prot);
        void (*domain_window_disable)(struct iommu_domain *domain, u32 wnd_nr);
        int (*domain_set_windows)(struct iommu_domain *domain, u32 w_count);
        u32 (*domain_get_windows)(struct iommu_domain *domain);
        int (*of_xlate)(struct device *dev, struct of_phandle_args *args);
        unsigned long pgsize_bitmap;
    }

.. _`iommu_ops.members`:

Members
-------

capable
    check capability

domain_alloc
    allocate iommu domain

domain_free
    free iommu domain

attach_dev
    attach device to an iommu domain

detach_dev
    detach device from an iommu domain

map
    map a physically contiguous memory region to an iommu domain

unmap
    unmap a physically contiguous memory region from an iommu domain

map_sg
    map a scatter-gather list of physically contiguous memory chunks
    to an iommu domain

iova_to_phys
    translate iova to physical address

add_device
    add device to iommu grouping

remove_device
    remove device from iommu grouping

device_group
    find iommu group for a particular device

domain_get_attr
    Query domain attributes

domain_set_attr
    Change domain attributes

get_resv_regions
    Request list of reserved regions for a device

put_resv_regions
    Free list of reserved regions for a device

apply_resv_region
    Temporary helper call-back for iova reserved ranges

domain_window_enable
    Configure and enable a particular window for a domain

domain_window_disable
    Disable a particular window for a domain

domain_set_windows
    Set the number of windows for a domain

domain_get_windows
    Return the number of windows for a domain

of_xlate
    add OF master IDs to iommu grouping

pgsize_bitmap
    bitmap of all possible supported page sizes

.. _`iommu_device`:

struct iommu_device
===================

.. c:type:: struct iommu_device

    IOMMU core representation of one IOMMU hardware instance

.. _`iommu_device.definition`:

Definition
----------

.. code-block:: c

    struct iommu_device {
        struct list_head list;
        const struct iommu_ops *ops;
        struct fwnode_handle *fwnode;
        struct device dev;
    }

.. _`iommu_device.members`:

Members
-------

list
    Used by the iommu-core to keep a list of registered iommus

ops
    iommu-ops for talking to this iommu

fwnode
    *undescribed*

dev
    struct device for sysfs handling

.. _`iommu_fwspec`:

struct iommu_fwspec
===================

.. c:type:: struct iommu_fwspec

    per-device IOMMU instance data

.. _`iommu_fwspec.definition`:

Definition
----------

.. code-block:: c

    struct iommu_fwspec {
        const struct iommu_ops *ops;
        struct fwnode_handle *iommu_fwnode;
        void *iommu_priv;
        unsigned int num_ids;
        u32 ids;
    }

.. _`iommu_fwspec.members`:

Members
-------

ops
    ops for this device's IOMMU

iommu_fwnode
    firmware handle for this device's IOMMU

iommu_priv
    IOMMU driver private data for this device

num_ids
    number of associated device IDs

ids
    IDs which this device may present to the IOMMU

.. This file was automatic generated / don't edit.

