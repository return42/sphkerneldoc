.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/math-emu/math.c

.. _`denormal_to_double`:

denormal_to_double
==================

.. c:function:: void denormal_to_double(struct sh_fpu_soft_struct *fpu, int n)

    Given denormalized float number, store double float

    :param fpu:
        Pointer to sh_fpu_soft structure
    :type fpu: struct sh_fpu_soft_struct \*

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

.. _`fpu_init`:

fpu_init
========

.. c:function:: void fpu_init(struct sh_fpu_soft_struct *fpu)

    Initialize FPU registers

    :param fpu:
        Pointer to software emulated FPU registers.
    :type fpu: struct sh_fpu_soft_struct \*

.. _`do_fpu_inst`:

do_fpu_inst
===========

.. c:function:: int do_fpu_inst(unsigned short inst, struct pt_regs *regs)

    Handle reserved instructions for FPU emulation

    :param inst:
        instruction code.
    :type inst: unsigned short

    :param regs:
        registers on stack.
    :type regs: struct pt_regs \*

.. This file was automatic generated / don't edit.

