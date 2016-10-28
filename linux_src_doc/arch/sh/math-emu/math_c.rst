.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/math-emu/math.c

.. _`denormal_to_double`:

denormal_to_double
==================

.. c:function:: void denormal_to_double(struct sh_fpu_soft_struct *fpu, int n)

    Given denormalized float number, store double float

    :param struct sh_fpu_soft_struct \*fpu:
        Pointer to sh_fpu_soft structure

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

.. _`fpu_init`:

fpu_init
========

.. c:function:: void fpu_init(struct sh_fpu_soft_struct *fpu)

    Initialize FPU registers

    :param struct sh_fpu_soft_struct \*fpu:
        Pointer to software emulated FPU registers.

.. _`do_fpu_inst`:

do_fpu_inst
===========

.. c:function:: int do_fpu_inst(unsigned short inst, struct pt_regs *regs)

    Handle reserved instructions for FPU emulation

    :param unsigned short inst:
        instruction code.

    :param struct pt_regs \*regs:
        registers on stack.

.. This file was automatic generated / don't edit.

