.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/handlers.c

.. _`intel_gvt_find_mmio_info`:

intel_gvt_find_mmio_info
========================

.. c:function:: struct intel_gvt_mmio_info *intel_gvt_find_mmio_info(struct intel_gvt *gvt, unsigned int offset)

    find MMIO information entry by aligned offset

    :param struct intel_gvt \*gvt:
        GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_find_mmio_info.description`:

Description
-----------

This function is used to find the MMIO information entry from hash table

.. _`intel_gvt_find_mmio_info.return`:

Return
------

pointer to MMIO information entry, NULL if not exists

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

.. _`intel_gvt_mmio_set_accessed`:

intel_gvt_mmio_set_accessed
===========================

.. c:function:: void intel_gvt_mmio_set_accessed(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO has been accessed

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_mmio_is_cmd_access`:

intel_gvt_mmio_is_cmd_access
============================

.. c:function:: bool intel_gvt_mmio_is_cmd_access(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO could be accessed by command

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_mmio_is_unalign`:

intel_gvt_mmio_is_unalign
=========================

.. c:function:: bool intel_gvt_mmio_is_unalign(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO could be accessed unaligned

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_mmio_set_cmd_accessed`:

intel_gvt_mmio_set_cmd_accessed
===============================

.. c:function:: void intel_gvt_mmio_set_cmd_accessed(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO has been accessed by command

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_mmio_has_mode_mask`:

intel_gvt_mmio_has_mode_mask
============================

.. c:function:: bool intel_gvt_mmio_has_mode_mask(struct intel_gvt *gvt, unsigned int offset)

    if a MMIO has a mode mask

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_mmio_has_mode_mask.return`:

Return
------

True if a MMIO has a mode mask in its higher 16 bits, false if it isn't.

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

.. This file was automatic generated / don't edit.

