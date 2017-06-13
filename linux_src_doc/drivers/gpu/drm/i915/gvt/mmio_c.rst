.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/mmio.c

.. _`intel_vgpu_gpa_to_mmio_offset`:

intel_vgpu_gpa_to_mmio_offset
=============================

.. c:function:: int intel_vgpu_gpa_to_mmio_offset(struct intel_vgpu *vgpu, u64 gpa)

    translate a GPA to MMIO offset

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param u64 gpa:
        *undescribed*

.. _`intel_vgpu_gpa_to_mmio_offset.return`:

Return
------

Zero on success, negative error code if failed

.. _`intel_vgpu_emulate_mmio_read`:

intel_vgpu_emulate_mmio_read
============================

.. c:function:: int intel_vgpu_emulate_mmio_read(struct intel_vgpu *vgpu, uint64_t pa, void *p_data, unsigned int bytes)

    emulate MMIO read

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param uint64_t pa:
        guest physical address

    :param void \*p_data:
        data return buffer

    :param unsigned int bytes:
        access data length

.. _`intel_vgpu_emulate_mmio_read.return`:

Return
------

Zero on success, negative error code if failed

.. _`intel_vgpu_emulate_mmio_write`:

intel_vgpu_emulate_mmio_write
=============================

.. c:function:: int intel_vgpu_emulate_mmio_write(struct intel_vgpu *vgpu, uint64_t pa, void *p_data, unsigned int bytes)

    emulate MMIO write

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param uint64_t pa:
        guest physical address

    :param void \*p_data:
        write data buffer

    :param unsigned int bytes:
        access data length

.. _`intel_vgpu_emulate_mmio_write.return`:

Return
------

Zero on success, negative error code if failed

.. _`intel_vgpu_reset_mmio`:

intel_vgpu_reset_mmio
=====================

.. c:function:: void intel_vgpu_reset_mmio(struct intel_vgpu *vgpu)

    reset virtual MMIO space

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. _`intel_vgpu_init_mmio`:

intel_vgpu_init_mmio
====================

.. c:function:: int intel_vgpu_init_mmio(struct intel_vgpu *vgpu)

    init MMIO  space

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. _`intel_vgpu_init_mmio.return`:

Return
------

Zero on success, negative error code if failed

.. _`intel_vgpu_clean_mmio`:

intel_vgpu_clean_mmio
=====================

.. c:function:: void intel_vgpu_clean_mmio(struct intel_vgpu *vgpu)

    clean MMIO space

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. This file was automatic generated / don't edit.

