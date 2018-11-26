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

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param gvt:
        *undescribed*
    :type gvt: void \*

    :param ops:
        *undescribed*
    :type ops: const void \*

.. _`intel_gvt_hypervisor_host_init.return`:

Return
------

Zero on success, negative error code if failed

.. _`intel_gvt_hypervisor_host_exit`:

intel_gvt_hypervisor_host_exit
==============================

.. c:function:: void intel_gvt_hypervisor_host_exit(struct device *dev, void *gvt)

    exit GVT-g host side

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param gvt:
        *undescribed*
    :type gvt: void \*

.. _`intel_gvt_hypervisor_attach_vgpu`:

intel_gvt_hypervisor_attach_vgpu
================================

.. c:function:: int intel_gvt_hypervisor_attach_vgpu(struct intel_vgpu *vgpu)

    call hypervisor to initialize vGPU related stuffs inside hypervisor.

    :param vgpu:
        *undescribed*
    :type vgpu: struct intel_vgpu \*

.. _`intel_gvt_hypervisor_attach_vgpu.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_detach_vgpu`:

intel_gvt_hypervisor_detach_vgpu
================================

.. c:function:: void intel_gvt_hypervisor_detach_vgpu(struct intel_vgpu *vgpu)

    call hypervisor to release vGPU related stuffs inside hypervisor.

    :param vgpu:
        *undescribed*
    :type vgpu: struct intel_vgpu \*

.. _`intel_gvt_hypervisor_detach_vgpu.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_inject_msi`:

intel_gvt_hypervisor_inject_msi
===============================

.. c:function:: int intel_gvt_hypervisor_inject_msi(struct intel_vgpu *vgpu)

    inject a MSI interrupt into vGPU

    :param vgpu:
        *undescribed*
    :type vgpu: struct intel_vgpu \*

.. _`intel_gvt_hypervisor_inject_msi.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_virt_to_mfn`:

intel_gvt_hypervisor_virt_to_mfn
================================

.. c:function:: unsigned long intel_gvt_hypervisor_virt_to_mfn(void *p)

    translate a host VA into MFN

    :param p:
        host kernel virtual address
    :type p: void \*

.. _`intel_gvt_hypervisor_virt_to_mfn.return`:

Return
------

MFN on success, INTEL_GVT_INVALID_ADDR if failed.

.. _`intel_gvt_hypervisor_enable_page_track`:

intel_gvt_hypervisor_enable_page_track
======================================

.. c:function:: int intel_gvt_hypervisor_enable_page_track(struct intel_vgpu *vgpu, unsigned long gfn)

    track a guest page

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gfn:
        the gfn of guest
    :type gfn: unsigned long

.. _`intel_gvt_hypervisor_enable_page_track.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_disable_page_track`:

intel_gvt_hypervisor_disable_page_track
=======================================

.. c:function:: int intel_gvt_hypervisor_disable_page_track(struct intel_vgpu *vgpu, unsigned long gfn)

    untrack a guest page

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gfn:
        the gfn of guest
    :type gfn: unsigned long

.. _`intel_gvt_hypervisor_disable_page_track.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_read_gpa`:

intel_gvt_hypervisor_read_gpa
=============================

.. c:function:: int intel_gvt_hypervisor_read_gpa(struct intel_vgpu *vgpu, unsigned long gpa, void *buf, unsigned long len)

    copy data from GPA to host data buffer

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gpa:
        guest physical address
    :type gpa: unsigned long

    :param buf:
        host data buffer
    :type buf: void \*

    :param len:
        data length
    :type len: unsigned long

.. _`intel_gvt_hypervisor_read_gpa.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_write_gpa`:

intel_gvt_hypervisor_write_gpa
==============================

.. c:function:: int intel_gvt_hypervisor_write_gpa(struct intel_vgpu *vgpu, unsigned long gpa, void *buf, unsigned long len)

    copy data from host data buffer to GPA

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gpa:
        guest physical address
    :type gpa: unsigned long

    :param buf:
        host data buffer
    :type buf: void \*

    :param len:
        data length
    :type len: unsigned long

.. _`intel_gvt_hypervisor_write_gpa.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_gfn_to_mfn`:

intel_gvt_hypervisor_gfn_to_mfn
===============================

.. c:function:: unsigned long intel_gvt_hypervisor_gfn_to_mfn(struct intel_vgpu *vgpu, unsigned long gfn)

    translate a GFN to MFN

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gfn:
        *undescribed*
    :type gfn: unsigned long

.. _`intel_gvt_hypervisor_gfn_to_mfn.return`:

Return
------

MFN on success, INTEL_GVT_INVALID_ADDR if failed.

.. _`intel_gvt_hypervisor_dma_map_guest_page`:

intel_gvt_hypervisor_dma_map_guest_page
=======================================

.. c:function:: int intel_gvt_hypervisor_dma_map_guest_page(struct intel_vgpu *vgpu, unsigned long gfn, unsigned long size, dma_addr_t *dma_addr)

    setup dma map for guest page

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gfn:
        guest pfn
    :type gfn: unsigned long

    :param size:
        page size
    :type size: unsigned long

    :param dma_addr:
        retrieve allocated dma addr
    :type dma_addr: dma_addr_t \*

.. _`intel_gvt_hypervisor_dma_map_guest_page.return`:

Return
------

0 on success, negative error code if failed.

.. _`intel_gvt_hypervisor_dma_unmap_guest_page`:

intel_gvt_hypervisor_dma_unmap_guest_page
=========================================

.. c:function:: void intel_gvt_hypervisor_dma_unmap_guest_page(struct intel_vgpu *vgpu, dma_addr_t dma_addr)

    cancel dma map for guest page

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param dma_addr:
        the mapped dma addr
    :type dma_addr: dma_addr_t

.. _`intel_gvt_hypervisor_map_gfn_to_mfn`:

intel_gvt_hypervisor_map_gfn_to_mfn
===================================

.. c:function:: int intel_gvt_hypervisor_map_gfn_to_mfn(struct intel_vgpu *vgpu, unsigned long gfn, unsigned long mfn, unsigned int nr, bool map)

    map a GFN region to MFN

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gfn:
        guest PFN
    :type gfn: unsigned long

    :param mfn:
        host PFN
    :type mfn: unsigned long

    :param nr:
        amount of PFNs
    :type nr: unsigned int

    :param map:
        map or unmap
    :type map: bool

.. _`intel_gvt_hypervisor_map_gfn_to_mfn.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_set_trap_area`:

intel_gvt_hypervisor_set_trap_area
==================================

.. c:function:: int intel_gvt_hypervisor_set_trap_area(struct intel_vgpu *vgpu, u64 start, u64 end, bool map)

    Trap a guest PA region

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param start:
        the beginning of the guest physical address region
    :type start: u64

    :param end:
        the end of the guest physical address region
    :type end: u64

    :param map:
        map or unmap
    :type map: bool

.. _`intel_gvt_hypervisor_set_trap_area.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_set_opregion`:

intel_gvt_hypervisor_set_opregion
=================================

.. c:function:: int intel_gvt_hypervisor_set_opregion(struct intel_vgpu *vgpu)

    Set opregion for guest

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_gvt_hypervisor_set_opregion.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_get_vfio_device`:

intel_gvt_hypervisor_get_vfio_device
====================================

.. c:function:: int intel_gvt_hypervisor_get_vfio_device(struct intel_vgpu *vgpu)

    increase vfio device ref count

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_gvt_hypervisor_get_vfio_device.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_put_vfio_device`:

intel_gvt_hypervisor_put_vfio_device
====================================

.. c:function:: void intel_gvt_hypervisor_put_vfio_device(struct intel_vgpu *vgpu)

    decrease vfio device ref count

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_gvt_hypervisor_put_vfio_device.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_hypervisor_is_valid_gfn`:

intel_gvt_hypervisor_is_valid_gfn
=================================

.. c:function:: bool intel_gvt_hypervisor_is_valid_gfn(struct intel_vgpu *vgpu, unsigned long gfn)

    check if a visible gfn

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gfn:
        guest PFN
    :type gfn: unsigned long

.. _`intel_gvt_hypervisor_is_valid_gfn.return`:

Return
------

true on valid gfn, false on not.

.. This file was automatic generated / don't edit.

