.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/opregion.c

.. _`intel_vgpu_init_opregion`:

intel_vgpu_init_opregion
========================

.. c:function:: int intel_vgpu_init_opregion(struct intel_vgpu *vgpu)

    initialize the stuff used to emulate opregion

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_init_opregion.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_opregion_base_write_handler`:

intel_vgpu_opregion_base_write_handler
======================================

.. c:function:: int intel_vgpu_opregion_base_write_handler(struct intel_vgpu *vgpu, u32 gpa)

    Opregion base register write handler

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param gpa:
        guest physical address of opregion
    :type gpa: u32

.. _`intel_vgpu_opregion_base_write_handler.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_clean_opregion`:

intel_vgpu_clean_opregion
=========================

.. c:function:: void intel_vgpu_clean_opregion(struct intel_vgpu *vgpu)

    clean the stuff used to emulate opregion

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_emulate_opregion_request`:

intel_vgpu_emulate_opregion_request
===================================

.. c:function:: int intel_vgpu_emulate_opregion_request(struct intel_vgpu *vgpu, u32 swsci)

    emulating OpRegion request

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param swsci:
        SWSCI request
    :type swsci: u32

.. _`intel_vgpu_emulate_opregion_request.return`:

Return
------

Zero on success, negative error code if failed

.. This file was automatic generated / don't edit.

