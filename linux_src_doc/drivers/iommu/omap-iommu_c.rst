.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/omap-iommu.c

.. _`to_omap_domain`:

to_omap_domain
==============

.. c:function:: struct omap_iommu_domain *to_omap_domain(struct iommu_domain *dom)

    Get struct omap_iommu_domain from generic iommu_domain

    :param dom:
        generic iommu domain handle
    :type dom: struct iommu_domain \*

.. _`omap_iommu_save_ctx`:

omap_iommu_save_ctx
===================

.. c:function:: void omap_iommu_save_ctx(struct device *dev)

    Save registers for pm off-mode support

    :param dev:
        client device
    :type dev: struct device \*

.. _`omap_iommu_restore_ctx`:

omap_iommu_restore_ctx
======================

.. c:function:: void omap_iommu_restore_ctx(struct device *dev)

    Restore registers for pm off-mode support

    :param dev:
        client device
    :type dev: struct device \*

.. _`load_iotlb_entry`:

load_iotlb_entry
================

.. c:function:: int load_iotlb_entry(struct omap_iommu *obj, struct iotlb_entry *e)

    Set an iommu tlb entry

    :param obj:
        target iommu
    :type obj: struct omap_iommu \*

    :param e:
        an iommu tlb entry info
    :type e: struct iotlb_entry \*

.. _`flush_iotlb_page`:

flush_iotlb_page
================

.. c:function:: void flush_iotlb_page(struct omap_iommu *obj, u32 da)

    Clear an iommu tlb entry

    :param obj:
        target iommu
    :type obj: struct omap_iommu \*

    :param da:
        iommu device virtual address
    :type da: u32

.. _`flush_iotlb_page.description`:

Description
-----------

Clear an iommu tlb entry which includes 'da' address.

.. _`flush_iotlb_all`:

flush_iotlb_all
===============

.. c:function:: void flush_iotlb_all(struct omap_iommu *obj)

    Clear all iommu tlb entries

    :param obj:
        target iommu
    :type obj: struct omap_iommu \*

.. _`omap_iopgtable_store_entry`:

omap_iopgtable_store_entry
==========================

.. c:function:: int omap_iopgtable_store_entry(struct omap_iommu *obj, struct iotlb_entry *e)

    Make an iommu pte entry

    :param obj:
        target iommu
    :type obj: struct omap_iommu \*

    :param e:
        an iommu tlb entry info
    :type e: struct iotlb_entry \*

.. _`iopgtable_lookup_entry`:

iopgtable_lookup_entry
======================

.. c:function:: void iopgtable_lookup_entry(struct omap_iommu *obj, u32 da, u32 **ppgd, u32 **ppte)

    Lookup an iommu pte entry

    :param obj:
        target iommu
    :type obj: struct omap_iommu \*

    :param da:
        iommu device virtual address
    :type da: u32

    :param ppgd:
        iommu pgd entry pointer to be returned
    :type ppgd: u32 \*\*

    :param ppte:
        iommu pte entry pointer to be returned
    :type ppte: u32 \*\*

.. _`iopgtable_clear_entry`:

iopgtable_clear_entry
=====================

.. c:function:: size_t iopgtable_clear_entry(struct omap_iommu *obj, u32 da)

    Remove an iommu pte entry

    :param obj:
        target iommu
    :type obj: struct omap_iommu \*

    :param da:
        iommu device virtual address
    :type da: u32

.. _`omap_iommu_attach`:

omap_iommu_attach
=================

.. c:function:: int omap_iommu_attach(struct omap_iommu *obj, u32 *iopgd)

    attach iommu device to an iommu domain

    :param obj:
        target omap iommu device
    :type obj: struct omap_iommu \*

    :param iopgd:
        page table
    :type iopgd: u32 \*

.. _`omap_iommu_detach`:

omap_iommu_detach
=================

.. c:function:: void omap_iommu_detach(struct omap_iommu *obj)

    release iommu device

    :param obj:
        target iommu
    :type obj: struct omap_iommu \*

.. This file was automatic generated / don't edit.

