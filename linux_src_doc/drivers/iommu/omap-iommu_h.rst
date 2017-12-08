.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/omap-iommu.h

.. _`omap_iommu_device`:

struct omap_iommu_device
========================

.. c:type:: struct omap_iommu_device

    omap iommu device data

.. _`omap_iommu_device.definition`:

Definition
----------

.. code-block:: c

    struct omap_iommu_device {
        u32 *pgtable;
        struct omap_iommu *iommu_dev;
    }

.. _`omap_iommu_device.members`:

Members
-------

pgtable
    page table used by an omap iommu attached to a domain

iommu_dev
    pointer to store an omap iommu instance attached to a domain

.. _`omap_iommu_domain`:

struct omap_iommu_domain
========================

.. c:type:: struct omap_iommu_domain

    omap iommu domain

.. _`omap_iommu_domain.definition`:

Definition
----------

.. code-block:: c

    struct omap_iommu_domain {
        u32 num_iommus;
        struct omap_iommu_device *iommus;
        struct device *dev;
        spinlock_t lock;
        struct iommu_domain domain;
    }

.. _`omap_iommu_domain.members`:

Members
-------

num_iommus
    number of iommus in this domain

iommus
    omap iommu device data for all iommus in this domain

dev
    Device using this domain.

lock
    domain lock, should be taken when attaching/detaching

domain
    generic domain handle used by iommu core code

.. _`omap_iommu_arch_data`:

struct omap_iommu_arch_data
===========================

.. c:type:: struct omap_iommu_arch_data

    omap iommu private data

.. _`omap_iommu_arch_data.definition`:

Definition
----------

.. code-block:: c

    struct omap_iommu_arch_data {
        struct omap_iommu *iommu_dev;
    }

.. _`omap_iommu_arch_data.members`:

Members
-------

iommu_dev
    handle of the iommu device

.. _`omap_iommu_arch_data.description`:

Description
-----------

This is an omap iommu private data object, which binds an iommu user
to its iommu device. This object should be placed at the iommu user's
dev_archdata so generic IOMMU API can be used without having to
utilize omap-specific plumbing anymore.

.. This file was automatic generated / don't edit.

