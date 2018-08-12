.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/mpt.h

.. _`hypervisor-service-apis-for-gvt-g-core-logic`:

Hypervisor Service APIs for GVT-g Core Logic
============================================

This is the glue layer between specific hypervisor MPT modules and GVT-g core
logic. Each kind of hypervisor MPT module provides a collection of function
callbacks and will be attached to GVT host when the driver is loading.
GVT-g core logic will call these APIs to request specific services from
hypervisor.

.. _`intel_gvt_hypervisor_host_init`:

intel_gvt_hypervisor_host_init
==============================

.. c:function:: int intel_gvt_hypervisor_host_init(struct device *dev, void *gvt, const void *ops)

    init GVT-g host side

    :param struct device \*dev:
        *undescribed*

    :param void \*gvt:
        *undescribed*

    :param const void \*ops:
        *undescribed*

.. _`intel_gvt_hypervisor_host_init.return`:

Return
------

Zero on success, negative error code if failed

.. _`intel_gvt_hypervisor_host_exit`:

intel_gvt_hypervisor_host_exit
==============================

.. c:function:: void intel_gvt_hypervisor_host_exit(struct device *dev, void *gvt)

    exit GVT-g host side

    :param struct device \*dev:
        *undescribed*

    :param void \*gvt:
        *undescribed*

.. _`intel_gvt_hypervisor_attach_vgpu`:

intel_gvt_hypervisor_attach_vgpu
================================

.. c:function:: int intel_gvt_hypervisor_attach_vgpu(struct intel_vgpu *vgpu)

    call hypervisor to initialize vGPU related stuffs inside hypervisor.

    :param struct intel_vgpu \*vgpu:
        *undescribed*

.. _`intel_gvt_hypervisor_attach_vgpu.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_detach_vgpu`:

intel_gvt_hypervisor_detach_vgpu
================================

.. c:function:: void intel_gvt_hypervisor_detach_vgpu(struct intel_vgpu *vgpu)

    call hypervisor to release vGPU related stuffs inside hypervisor.

    :param struct intel_vgpu \*vgpu:
        *undescribed*

.. _`intel_gvt_hypervisor_detach_vgpu.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_inject_msi`:

intel_gvt_hypervisor_inject_msi
===============================

.. c:function:: int intel_gvt_hypervisor_inject_msi(struct intel_vgpu *vgpu)

    inject a MSI interrupt into vGPU

    :param struct intel_vgpu \*vgpu:
        *undescribed*

.. _`intel_gvt_hypervisor_inject_msi.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_virt_to_mfn`:

intel_gvt_hypervisor_virt_to_mfn
================================

.. c:function:: unsigned long intel_gvt_hypervisor_virt_to_mfn(void *p)

    translate a host VA into MFN

    :param void \*p:
        host kernel virtual address

.. _`intel_gvt_hypervisor_virt_to_mfn.return`:

Return
------

MFN on success, INTEL_GVT_INVALID_ADDR if failed.

.. _`intel_gvt_hypervisor_enable_page_track`:

intel_gvt_hypervisor_enable_page_track
======================================

.. c:function:: int intel_gvt_hypervisor_enable_page_track(struct intel_vgpu *vgpu, unsigned long gfn)

    track a guest page

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned long gfn:
        the gfn of guest

.. _`intel_gvt_hypervisor_enable_page_track.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_disable_page_track`:

intel_gvt_hypervisor_disable_page_track
=======================================

.. c:function:: int intel_gvt_hypervisor_disable_page_track(struct intel_vgpu *vgpu, unsigned long gfn)

    untrack a guest page

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned long gfn:
        the gfn of guest

.. _`intel_gvt_hypervisor_disable_page_track.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_read_gpa`:

intel_gvt_hypervisor_read_gpa
=============================

.. c:function:: int intel_gvt_hypervisor_read_gpa(struct intel_vgpu *vgpu, unsigned long gpa, void *buf, unsigned long len)

    copy data from GPA to host data buffer

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned long gpa:
        guest physical address

    :param void \*buf:
        host data buffer

    :param unsigned long len:
        data length

.. _`intel_gvt_hypervisor_read_gpa.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_write_gpa`:

intel_gvt_hypervisor_write_gpa
==============================

.. c:function:: int intel_gvt_hypervisor_write_gpa(struct intel_vgpu *vgpu, unsigned long gpa, void *buf, unsigned long len)

    copy data from host data buffer to GPA

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned long gpa:
        guest physical address

    :param void \*buf:
        host data buffer

    :param unsigned long len:
        data length

.. _`intel_gvt_hypervisor_write_gpa.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_gfn_to_mfn`:

intel_gvt_hypervisor_gfn_to_mfn
===============================

.. c:function:: unsigned long intel_gvt_hypervisor_gfn_to_mfn(struct intel_vgpu *vgpu, unsigned long gfn)

    translate a GFN to MFN

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned long gfn:
        *undescribed*

.. _`intel_gvt_hypervisor_gfn_to_mfn.return`:

Return
------

MFN on success, INTEL_GVT_INVALID_ADDR if failed.

.. _`intel_gvt_hypervisor_dma_map_guest_page`:

intel_gvt_hypervisor_dma_map_guest_page
=======================================

.. c:function:: int intel_gvt_hypervisor_dma_map_guest_page(struct intel_vgpu *vgpu, unsigned long gfn, dma_addr_t *dma_addr)

    setup dma map for guest page

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned long gfn:
        *undescribed*

    :param dma_addr_t \*dma_addr:
        retrieve allocated dma addr

.. _`intel_gvt_hypervisor_dma_map_guest_page.return`:

Return
------

0 on success, negative error code if failed.

.. _`intel_gvt_hypervisor_dma_unmap_guest_page`:

intel_gvt_hypervisor_dma_unmap_guest_page
=========================================

.. c:function:: void intel_gvt_hypervisor_dma_unmap_guest_page(struct intel_vgpu *vgpu, dma_addr_t dma_addr)

    cancel dma map for guest page

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param dma_addr_t dma_addr:
        the mapped dma addr

.. _`intel_gvt_hypervisor_map_gfn_to_mfn`:

intel_gvt_hypervisor_map_gfn_to_mfn
===================================

.. c:function:: int intel_gvt_hypervisor_map_gfn_to_mfn(struct intel_vgpu *vgpu, unsigned long gfn, unsigned long mfn, unsigned int nr, bool map)

    map a GFN region to MFN

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned long gfn:
        guest PFN

    :param unsigned long mfn:
        host PFN

    :param unsigned int nr:
        amount of PFNs

    :param bool map:
        map or unmap

.. _`intel_gvt_hypervisor_map_gfn_to_mfn.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_set_trap_area`:

intel_gvt_hypervisor_set_trap_area
==================================

.. c:function:: int intel_gvt_hypervisor_set_trap_area(struct intel_vgpu *vgpu, u64 start, u64 end, bool map)

    Trap a guest PA region

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param u64 start:
        the beginning of the guest physical address region

    :param u64 end:
        the end of the guest physical address region

    :param bool map:
        map or unmap

.. _`intel_gvt_hypervisor_set_trap_area.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_set_opregion`:

intel_gvt_hypervisor_set_opregion
=================================

.. c:function:: int intel_gvt_hypervisor_set_opregion(struct intel_vgpu *vgpu)

    Set opregion for guest

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. _`intel_gvt_hypervisor_set_opregion.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_get_vfio_device`:

intel_gvt_hypervisor_get_vfio_device
====================================

.. c:function:: int intel_gvt_hypervisor_get_vfio_device(struct intel_vgpu *vgpu)

    increase vfio device ref count

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. _`intel_gvt_hypervisor_get_vfio_device.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_put_vfio_device`:

intel_gvt_hypervisor_put_vfio_device
====================================

.. c:function:: void intel_gvt_hypervisor_put_vfio_device(struct intel_vgpu *vgpu)

    decrease vfio device ref count

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. _`intel_gvt_hypervisor_put_vfio_device.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_is_valid_gfn`:

intel_gvt_hypervisor_is_valid_gfn
=================================

.. c:function:: bool intel_gvt_hypervisor_is_valid_gfn(struct intel_vgpu *vgpu, unsigned long gfn)

    check if a visible gfn

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned long gfn:
        guest PFN

.. _`intel_gvt_hypervisor_is_valid_gfn.return`:

Return
------

true on valid gfn, false on not.

.. This file was automatic generated / don't edit.

