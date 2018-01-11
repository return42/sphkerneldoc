.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/handlers.c

.. _`intel_gvt_render_mmio_to_ring_id`:

intel_gvt_render_mmio_to_ring_id
================================

.. c:function:: int intel_gvt_render_mmio_to_ring_id(struct intel_gvt *gvt, unsigned int offset)

    convert a mmio offset into ring id

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_render_mmio_to_ring_id.return`:

Return
------

Ring ID on success, negative error code if failed.

.. _`intel_gvt_clean_mmio_info`:

intel_gvt_clean_mmio_info
=========================

.. c:function:: void intel_gvt_clean_mmio_info(struct intel_gvt *gvt)

    clean up MMIO information table for GVT device

    :param struct intel_gvt \*gvt:
        GVT device

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

    :param struct intel_gvt \*gvt:
        GVT device

.. _`intel_gvt_setup_mmio_info.description`:

Description
-----------

This function is called at the initialization stage, to setup the MMIO
information table for GVT device

.. _`intel_gvt_setup_mmio_info.return`:

Return
------

zero on success, negative if failed.

.. _`intel_vgpu_default_mmio_read`:

intel_vgpu_default_mmio_read
============================

.. c:function:: int intel_vgpu_default_mmio_read(struct intel_vgpu *vgpu, unsigned int offset, void *p_data, unsigned int bytes)

    default MMIO read handler

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned int offset:
        access offset

    :param void \*p_data:
        data return buffer

    :param unsigned int bytes:
        access data length

.. _`intel_vgpu_default_mmio_read.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_default_mmio_write`:

intel_vgpu_default_mmio_write
=============================

.. c:function:: int intel_vgpu_default_mmio_write(struct intel_vgpu *vgpu, unsigned int offset, void *p_data, unsigned int bytes)

    default MMIO write handler

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned int offset:
        access offset

    :param void \*p_data:
        write data buffer

    :param unsigned int bytes:
        access data length

.. _`intel_vgpu_default_mmio_write.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_in_force_nonpriv_whitelist`:

intel_gvt_in_force_nonpriv_whitelist
====================================

.. c:function:: bool intel_gvt_in_force_nonpriv_whitelist(struct intel_gvt *gvt, unsigned int offset)

    if a mmio is in whitelist to be force-nopriv register

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

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

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned int offset:
        register offset

    :param void \*pdata:
        data buffer

    :param unsigned int bytes:
        data length

    :param bool is_read:
        *undescribed*

.. _`intel_vgpu_mmio_reg_rw.return`:

Return
------

Zero on success, negative error code if failed.

.. This file was automatic generated / don't edit.

