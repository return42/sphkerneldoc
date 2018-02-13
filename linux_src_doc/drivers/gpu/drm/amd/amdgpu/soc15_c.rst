.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/soc15.c

.. _`soc15_program_register_sequence`:

soc15_program_register_sequence
===============================

.. c:function:: void soc15_program_register_sequence(struct amdgpu_device *adev, const struct soc15_reg_golden *regs, const u32 array_size)

    program an array of registers.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param const struct soc15_reg_golden \*regs:
        pointer to the register array

    :param const u32 array_size:
        size of the register array

.. _`soc15_program_register_sequence.description`:

Description
-----------

Programs an array or registers with and and or masks.
This is a helper for setting golden registers.

.. This file was automatic generated / don't edit.

