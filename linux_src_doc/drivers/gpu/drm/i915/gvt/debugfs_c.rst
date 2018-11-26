.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/debugfs.c

.. _`intel_gvt_debugfs_add_vgpu`:

intel_gvt_debugfs_add_vgpu
==========================

.. c:function:: int intel_gvt_debugfs_add_vgpu(struct intel_vgpu *vgpu)

    register debugfs entries for a vGPU

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_gvt_debugfs_add_vgpu.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_debugfs_remove_vgpu`:

intel_gvt_debugfs_remove_vgpu
=============================

.. c:function:: void intel_gvt_debugfs_remove_vgpu(struct intel_vgpu *vgpu)

    remove debugfs entries of a vGPU

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_gvt_debugfs_init`:

intel_gvt_debugfs_init
======================

.. c:function:: int intel_gvt_debugfs_init(struct intel_gvt *gvt)

    register gvt debugfs root entry

    :param gvt:
        GVT device
    :type gvt: struct intel_gvt \*

.. _`intel_gvt_debugfs_init.return`:

Return
------

zero on success, negative if failed.

.. _`intel_gvt_debugfs_clean`:

intel_gvt_debugfs_clean
=======================

.. c:function:: void intel_gvt_debugfs_clean(struct intel_gvt *gvt)

    remove debugfs entries

    :param gvt:
        GVT device
    :type gvt: struct intel_gvt \*

.. This file was automatic generated / don't edit.

