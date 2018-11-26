.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/kernel/cpu/sh4/fpu.c

.. _`denormal_to_double`:

denormal_to_double
==================

.. c:function:: void denormal_to_double(struct sh_fpu_hard_struct *fpu, int n)

    Given denormalized float number, store double float

    :param fpu:
        Pointer to sh_fpu_hard structure
    :type fpu: struct sh_fpu_hard_struct \*

    :param n:
        Index to FP register
    :type n: int

.. _`ieee_fpe_handler`:

ieee_fpe_handler
================

.. c:function:: int ieee_fpe_handler(struct pt_regs *regs)

    Handle denormalized number exception

    :param regs:
        Pointer to register structure
    :type regs: struct pt_regs \*

.. _`ieee_fpe_handler.description`:

Description
-----------

Returns 1 when it's handled (should not cause exception).

.. This file was automatic generated / don't edit.

