.. -*- coding: utf-8; mode: rst -*-

=======
iommu.h
=======


.. _`iommu_dm_region`:

struct iommu_dm_region
======================

.. c:type:: iommu_dm_region

    descriptor for a direct mapped memory region


.. _`iommu_dm_region.definition`:

Definition
----------

.. code-block:: c

  struct iommu_dm_region {
    struct list_head list;
    phys_addr_t start;
    size_t length;
    int prot;
  };


.. _`iommu_dm_region.members`:

Members
-------

:``list``:
    Linked list pointers

:``start``:
    System physical start address of the region

:``length``:
    Length of the region in bytes

:``prot``:
    IOMMU Protection flags (READ/WRITE/...)




.. _`iommu_ops`:

struct iommu_ops
================

.. c:type:: iommu_ops

    iommu ops and capabilities


.. _`iommu_ops.definition`:

Definition
----------

.. code-block:: c

  struct iommu_ops {
    bool (* capable) (enum iommu_cap);
    struct iommu_domain *(* domain_alloc) (unsigned iommu_domain_type);
    void (* domain_free) (struct iommu_domain *);
    int (* attach_dev) (struct iommu_domain *domain, struct device *dev);
    void (* detach_dev) (struct iommu_domain *domain, struct device *dev);
    int (* map) (struct iommu_domain *domain, unsigned long iova,phys_addr_t paddr, size_t size, int prot);
    size_t (* unmap) (struct iommu_domain *domain, unsigned long iova,size_t size);
    size_t (* map_sg) (struct iommu_domain *domain, unsigned long iova,struct scatterlist *sg, unsigned int nents, int prot);
    phys_addr_t (* iova_to_phys) (struct iommu_domain *domain, dma_addr_t iova);
    int (* add_device) (struct device *dev);
    void (* remove_device) (struct device *dev);
    struct iommu_group *(* device_group) (struct device *dev);
    int (* domain_get_attr) (struct iommu_domain *domain,enum iommu_attr attr, void *data);
    int (* domain_set_attr) (struct iommu_domain *domain,enum iommu_attr attr, void *data);
    void (* get_dm_regions) (struct device *dev, struct list_head *list);
    void (* put_dm_regions) (struct device *dev, struct list_head *list);
    int (* domain_window_enable) (struct iommu_domain *domain, u32 wnd_nr,phys_addr_t paddr, u64 size, int prot);
    void (* domain_window_disable) (struct iommu_domain *domain, u32 wnd_nr);
    int (* domain_set_windows) (struct iommu_domain *domain, u32 w_count);
    u32 (* domain_get_windows) (struct iommu_domain *domain);
    int (* of_xlate) (struct device *dev, struct of_phandle_args *args);
    unsigned long pgsize_bitmap;
    void * priv;
  };


.. _`iommu_ops.members`:

Members
-------

:``capable``:
    check capability

:``domain_alloc``:
    allocate iommu domain

:``domain_free``:
    free iommu domain

:``attach_dev``:
    attach device to an iommu domain

:``detach_dev``:
    detach device from an iommu domain

:``map``:
    map a physically contiguous memory region to an iommu domain

:``unmap``:
    unmap a physically contiguous memory region from an iommu domain

:``map_sg``:
    map a scatter-gather list of physically contiguous memory chunks
    to an iommu domain

:``iova_to_phys``:
    translate iova to physical address

:``add_device``:
    add device to iommu grouping

:``remove_device``:
    remove device from iommu grouping

:``device_group``:
    find iommu group for a particular device

:``domain_get_attr``:
    Query domain attributes

:``domain_set_attr``:
    Change domain attributes

:``get_dm_regions``:
    Request list of direct mapping requirements for a device

:``put_dm_regions``:
    Free list of direct mapping requirements for a device

:``domain_window_enable``:
    Configure and enable a particular window for a domain

:``domain_window_disable``:
    Disable a particular window for a domain

:``domain_set_windows``:
    Set the number of windows for a domain

:``domain_get_windows``:
    Return the number of windows for a domain

:``of_xlate``:
    add OF master IDs to iommu grouping

:``pgsize_bitmap``:
    bitmap of supported page sizes

:``priv``:
    per-instance data private to the iommu driver




.. _`report_iommu_fault`:

report_iommu_fault
==================

.. c:function:: int report_iommu_fault (struct iommu_domain *domain, struct device *dev, unsigned long iova, int flags)

    report about an IOMMU fault to the IOMMU framework

    :param struct iommu_domain \*domain:
        the iommu domain where the fault has happened

    :param struct device \*dev:
        the device where the fault has happened

    :param unsigned long iova:
        the faulting address

    :param int flags:
        mmu fault flags (e.g. IOMMU_FAULT_READ/IOMMU_FAULT_WRITE/...)



.. _`report_iommu_fault.description`:

Description
-----------

This function should be called by the low-level IOMMU implementations
whenever IOMMU faults happen, to allow high-level users, that are
interested in such events, to know about them.



.. _`report_iommu_fault.this-event-may-be-useful-for-several-possible-use-cases`:

This event may be useful for several possible use cases
-------------------------------------------------------

- mere logging of the event
- dynamic TLB/PTE loading
- if restarting of the faulting device is required

Returns 0 on success and an appropriate error code otherwise (if dynamic
PTE/TLB loading will one day be supported, implementations will be able
to tell whether it succeeded or not according to this return value).

Specifically, -ENOSYS is returned if a fault handler isn't installed
(though fault handlers can also return -ENOSYS, in case they want to
elicit the default behavior of the IOMMU drivers).

