.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/soc15.c

.. _`soc15_program_register_sequence`:

soc15_program_register_sequence
===============================

.. c:function:: void soc15_program_register_sequence(struct amdgpu_device *adev, const struct soc15_reg_golden *regs, const u32 array_size)

    program an array of registers.

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param regs:
        pointer to the register array
    :type regs: const struct soc15_reg_golden \*

    :param array_size:
        size of the register array
    :type array_size: const u32

.. _`soc15_program_register_sequence.description`:

Description
-----------

Programs an array or registers with and and or masks.
This is a helper for setting golden registers.

.. This file was automatic generated / don't edit.

