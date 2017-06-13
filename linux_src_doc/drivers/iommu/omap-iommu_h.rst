.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/omap-iommu.h

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
        u32 *pgtable;
        struct omap_iommu *iommu_dev;
        struct device *dev;
        spinlock_t lock;
        struct iommu_domain domain;
    }

.. _`omap_iommu_domain.members`:

Members
-------

pgtable
    the page table

iommu_dev
    an omap iommu device attached to this domain. only a single
    iommu device can be attached for now.

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

.. _`dev_to_omap_iommu`:

dev_to_omap_iommu
=================

.. c:function:: struct omap_iommu *dev_to_omap_iommu(struct device *dev)

    retrieves an omap iommu object from a user device

    :param struct device \*dev:
        iommu client device

.. This file was automatic generated / don't edit.

