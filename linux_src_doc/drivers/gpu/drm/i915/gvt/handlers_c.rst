.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/handlers.c

.. _`intel_gvt_render_mmio_to_ring_id`:

intel_gvt_render_mmio_to_ring_id
================================

.. c:function:: int intel_gvt_render_mmio_to_ring_id(struct intel_gvt *gvt, unsigned int offset)

    convert a mmio offset into ring id

    :param gvt:
        a GVT device
    :type gvt: struct intel_gvt \*

    :param offset:
        register offset
    :type offset: unsigned int

.. _`intel_gvt_render_mmio_to_ring_id.return`:

Return
------

Ring ID on success, negative error code if failed.

.. _`intel_gvt_clean_mmio_info`:

intel_gvt_clean_mmio_info
=========================

.. c:function:: void intel_gvt_clean_mmio_info(struct intel_gvt *gvt)

    clean up MMIO information table for GVT device

    :param gvt:
        GVT device
    :type gvt: struct intel_gvt \*

.. _`intel_gvt_clean_mmio_info.description`:

Description
-----------

This function is called at the driver unloading stage, to clean up the MMIO
information table of GVT device

.. _`intel_gvt_setup_mmio_info`:

intel_gvt_setup_mmio_info
=========================

.. c:function:: int intel_gvt_setup_mmio_info(struct intel_gvt *gvt)

    setup MMIO information table for GVT device

    :param gvt:
        GVT device
    :type gvt: struct intel_gvt \*

.. _`intel_gvt_setup_mmio_info.description`:

Description
-----------

This function is called at the initialization stage, to setup the MMIO
information table for GVT device

.. _`intel_gvt_setup_mmio_info.return`:

Return
------

zero on success, negative if failed.

.. _`intel_gvt_for_each_tracked_mmio`:

intel_gvt_for_each_tracked_mmio
===============================

.. c:function:: int intel_gvt_for_each_tracked_mmio(struct intel_gvt *gvt, int (*handler)(struct intel_gvt *gvt, u32 offset, void *data), void *data)

    iterate each tracked mmio

    :param gvt:
        a GVT device
    :type gvt: struct intel_gvt \*

    :param int (\*handler)(struct intel_gvt \*gvt, u32 offset, void \*data):
        the handler

    :param data:
        private data given to handler
    :type data: void \*

.. _`intel_gvt_for_each_tracked_mmio.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_default_mmio_read`:

intel_vgpu_default_mmio_read
============================

.. c:function:: int intel_vgpu_default_mmio_read(struct intel_vgpu *vgpu, unsigned int offset, void *p_data, unsigned int bytes)

    default MMIO read handler

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param offset:
        access offset
    :type offset: unsigned int

    :param p_data:
        data return buffer
    :type p_data: void \*

    :param bytes:
        access data length
    :type bytes: unsigned int

.. _`intel_vgpu_default_mmio_read.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_default_mmio_write`:

intel_vgpu_default_mmio_write
=============================

.. c:function:: int intel_vgpu_default_mmio_write(struct intel_vgpu *vgpu, unsigned int offset, void *p_data, unsigned int bytes)

    default MMIO write handler

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param offset:
        access offset
    :type offset: unsigned int

    :param p_data:
        write data buffer
    :type p_data: void \*

    :param bytes:
        access data length
    :type bytes: unsigned int

.. _`intel_vgpu_default_mmio_write.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_mask_mmio_write`:

intel_vgpu_mask_mmio_write
==========================

.. c:function:: int intel_vgpu_mask_mmio_write(struct intel_vgpu *vgpu, unsigned int offset, void *p_data, unsigned int bytes)

    write mask register

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param offset:
        access offset
    :type offset: unsigned int

    :param p_data:
        write data buffer
    :type p_data: void \*

    :param bytes:
        access data length
    :type bytes: unsigned int

.. _`intel_vgpu_mask_mmio_write.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_in_force_nonpriv_whitelist`:

intel_gvt_in_force_nonpriv_whitelist
====================================

.. c:function:: bool intel_gvt_in_force_nonpriv_whitelist(struct intel_gvt *gvt, unsigned int offset)

    if a mmio is in whitelist to be force-nopriv register

    :param gvt:
        a GVT device
    :type gvt: struct intel_gvt \*

    :param offset:
        register offset
    :type offset: unsigned int

.. _`intel_gvt_in_force_nonpriv_whitelist.return`:

Return
------

True if the register is in force-nonpriv whitelist;
False if outside;

.. _`intel_vgpu_mmio_reg_rw`:

intel_vgpu_mmio_reg_rw
======================

.. c:function:: int intel_vgpu_mmio_reg_rw(struct intel_vgpu *vgpu, unsigned int offset, void *pdata, unsigned int bytes, bool is_read)

    emulate tracked mmio registers

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param offset:
        register offset
    :type offset: unsigned int

    :param pdata:
        data buffer
    :type pdata: void \*

    :param bytes:
        data length
    :type bytes: unsigned int

    :param is_read:
        read or write
    :type is_read: bool

.. _`intel_vgpu_mmio_reg_rw.return`:

Return
------

Zero on success, negative error code if failed.

.. This file was automatic generated / don't edit.

