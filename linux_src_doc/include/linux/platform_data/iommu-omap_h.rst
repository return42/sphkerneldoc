.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/iommu-omap.h

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
        const char *name;
        struct omap_iommu *iommu_dev;
    }

.. _`omap_iommu_arch_data.members`:

Members
-------

name
    name of the iommu device

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

