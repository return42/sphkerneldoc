.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/cfg_space.c

.. _`vgpu_pci_cfg_mem_write`:

vgpu_pci_cfg_mem_write
======================

.. c:function:: void vgpu_pci_cfg_mem_write(struct intel_vgpu *vgpu, unsigned int off, u8 *src, unsigned int bytes)

    write virtual cfg space memory

    :param struct intel_vgpu \*vgpu:
        *undescribed*

    :param unsigned int off:
        *undescribed*

    :param u8 \*src:
        *undescribed*

    :param unsigned int bytes:
        *undescribed*

.. _`vgpu_pci_cfg_mem_write.description`:

Description
-----------

Use this function to write virtual cfg space memory.
For standard cfg space, only RW bits can be changed,
and we emulates the RW1C behavior of PCI_STATUS register.

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

.. _`intel_vgpu_init_cfg_space`:

intel_vgpu_init_cfg_space
=========================

.. c:function:: void intel_vgpu_init_cfg_space(struct intel_vgpu *vgpu, bool primary)

    init vGPU configuration space when create vGPU

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param bool primary:
        is the vGPU presented as primary

.. _`intel_vgpu_reset_cfg_space`:

intel_vgpu_reset_cfg_space
==========================

.. c:function:: void intel_vgpu_reset_cfg_space(struct intel_vgpu *vgpu)

    reset vGPU configuration space

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. This file was automatic generated / don't edit.

