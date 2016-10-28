.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/kernel/cpu/sh2a/fpu.c

.. _`denormal_to_double`:

denormal_to_double
==================

.. c:function:: void denormal_to_double(struct sh_fpu_hard_struct *fpu, int n)

    Given denormalized float number, store double float

    :param struct sh_fpu_hard_struct \*fpu:
        Pointer to sh_fpu_hard structure

    :param int n:
        Index to FP register

.. _`ieee_fpe_handler`:

ieee_fpe_handler
================

.. c:function:: int ieee_fpe_handler(struct pt_regs *regs)

    Handle denormalized number exception

    :param struct pt_regs \*regs:
        Pointer to register structure

.. _`ieee_fpe_handler.description`:

Description
-----------

Returns 1 when it's handled (should not cause exception).

.. This file was automatic generated / don't edit.

