.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic-v3.c

.. _`vgic_v3_save_pending_tables`:

vgic_v3_save_pending_tables
===========================

.. c:function:: int vgic_v3_save_pending_tables(struct kvm *kvm)

    Save the pending tables into guest RAM kvm lock and all vcpu lock must be held

    :param kvm:
        *undescribed*
    :type kvm: struct kvm \*

.. _`vgic_v3_rdist_overlap`:

vgic_v3_rdist_overlap
=====================

.. c:function:: bool vgic_v3_rdist_overlap(struct kvm *kvm, gpa_t base, size_t size)

    check if a region overlaps with any existing redistributor region

    :param kvm:
        kvm handle
    :type kvm: struct kvm \*

    :param base:
        base of the region
    :type base: gpa_t

    :param size:
        size of region
    :type size: size_t

.. _`vgic_v3_rdist_overlap.return`:

Return
------

true if there is an overlap

.. _`vgic_v3_rdist_free_slot`:

vgic_v3_rdist_free_slot
=======================

.. c:function:: struct vgic_redist_region *vgic_v3_rdist_free_slot(struct list_head *rd_regions)

    Look up registered rdist regions and identify one which has free space to put a new rdist region.

    :param rd_regions:
        redistributor region list head
    :type rd_regions: struct list_head \*

.. _`vgic_v3_rdist_free_slot.description`:

Description
-----------

A redistributor regions maps n redistributors, n = region size / (2 x 64kB).
Stride between redistributors is 0 and regions are filled in the index order.

.. _`vgic_v3_rdist_free_slot.return`:

Return
------

the redist region handle, if any, that has space to map a new rdist
region.

.. _`vgic_v3_probe`:

vgic_v3_probe
=============

.. c:function:: int vgic_v3_probe(const struct gic_kvm_info *info)

    probe for a GICv3 compatible interrupt controller in DT

    :param info:
        *undescribed*
    :type info: const struct gic_kvm_info \*

.. _`vgic_v3_probe.description`:

Description
-----------

Returns 0 if a GICv3 has been found, returns an error code otherwise

.. This file was automatic generated / don't edit.

