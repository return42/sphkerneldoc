.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/omap-iommu.c

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
    *undescribed*

.. _`to_omap_domain`:

to_omap_domain
==============

.. c:function:: struct omap_iommu_domain *to_omap_domain(struct iommu_domain *dom)

    Get struct omap_iommu_domain from generic iommu_domain

    :param struct iommu_domain \*dom:
        generic iommu domain handle

.. _`omap_iommu_save_ctx`:

omap_iommu_save_ctx
===================

.. c:function:: void omap_iommu_save_ctx(struct device *dev)

    Save registers for pm off-mode support

    :param struct device \*dev:
        client device

.. _`omap_iommu_restore_ctx`:

omap_iommu_restore_ctx
======================

.. c:function:: void omap_iommu_restore_ctx(struct device *dev)

    Restore registers for pm off-mode support

    :param struct device \*dev:
        client device

.. _`load_iotlb_entry`:

load_iotlb_entry
================

.. c:function:: int load_iotlb_entry(struct omap_iommu *obj, struct iotlb_entry *e)

    Set an iommu tlb entry

    :param struct omap_iommu \*obj:
        target iommu

    :param struct iotlb_entry \*e:
        an iommu tlb entry info

.. _`flush_iotlb_page`:

flush_iotlb_page
================

.. c:function:: void flush_iotlb_page(struct omap_iommu *obj, u32 da)

    Clear an iommu tlb entry

    :param struct omap_iommu \*obj:
        target iommu

    :param u32 da:
        iommu device virtual address

.. _`flush_iotlb_page.description`:

Description
-----------

Clear an iommu tlb entry which includes 'da' address.

.. _`flush_iotlb_all`:

flush_iotlb_all
===============

.. c:function:: void flush_iotlb_all(struct omap_iommu *obj)

    Clear all iommu tlb entries

    :param struct omap_iommu \*obj:
        target iommu

.. _`omap_iopgtable_store_entry`:

omap_iopgtable_store_entry
==========================

.. c:function:: int omap_iopgtable_store_entry(struct omap_iommu *obj, struct iotlb_entry *e)

    Make an iommu pte entry

    :param struct omap_iommu \*obj:
        target iommu

    :param struct iotlb_entry \*e:
        an iommu tlb entry info

.. _`iopgtable_lookup_entry`:

iopgtable_lookup_entry
======================

.. c:function:: void iopgtable_lookup_entry(struct omap_iommu *obj, u32 da, u32 **ppgd, u32 **ppte)

    Lookup an iommu pte entry

    :param struct omap_iommu \*obj:
        target iommu

    :param u32 da:
        iommu device virtual address

    :param u32 \*\*ppgd:
        iommu pgd entry pointer to be returned

    :param u32 \*\*ppte:
        iommu pte entry pointer to be returned

.. _`iopgtable_clear_entry`:

iopgtable_clear_entry
=====================

.. c:function:: size_t iopgtable_clear_entry(struct omap_iommu *obj, u32 da)

    Remove an iommu pte entry

    :param struct omap_iommu \*obj:
        target iommu

    :param u32 da:
        iommu device virtual address

.. _`omap_iommu_attach`:

omap_iommu_attach
=================

.. c:function:: struct omap_iommu *omap_iommu_attach(const char *name, u32 *iopgd)

    attach iommu device to an iommu domain

    :param const char \*name:
        name of target omap iommu device

    :param u32 \*iopgd:
        page table

.. _`omap_iommu_detach`:

omap_iommu_detach
=================

.. c:function:: void omap_iommu_detach(struct omap_iommu *obj)

    release iommu device

    :param struct omap_iommu \*obj:
        target iommu

.. This file was automatic generated / don't edit.

