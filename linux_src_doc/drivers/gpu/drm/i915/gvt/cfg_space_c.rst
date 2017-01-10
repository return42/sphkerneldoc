.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/cfg_space.c

.. _`intel_vgpu_emulate_cfg_read`:

intel_vgpu_emulate_cfg_read
===========================

.. c:function:: int intel_vgpu_emulate_cfg_read(struct intel_vgpu *vgpu, unsigned int offset, void *p_data, unsigned int bytes)

    emulate vGPU configuration space read

    :param struct intel_vgpu \*vgpu:
        *undescribed*

    :param unsigned int offset:
        *undescribed*

    :param void \*p_data:
        *undescribed*

    :param unsigned int bytes:
        *undescribed*

.. _`intel_vgpu_emulate_cfg_read.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_emulate_cfg_write`:

intel_vgpu_emulate_cfg_write
============================

.. c:function:: int intel_vgpu_emulate_cfg_write(struct intel_vgpu *vgpu, unsigned int offset, void *p_data, unsigned int bytes)

    emulate vGPU configuration space write

    :param struct intel_vgpu \*vgpu:
        *undescribed*

    :param unsigned int offset:
        *undescribed*

    :param void \*p_data:
        *undescribed*

    :param unsigned int bytes:
        *undescribed*

.. _`intel_vgpu_emulate_cfg_write.return`:

Return
------

Zero on success, negative error code if failed.

.. This file was automatic generated / don't edit.

