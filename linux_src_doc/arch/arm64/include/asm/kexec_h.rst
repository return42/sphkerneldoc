.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/include/asm/kexec.h

.. _`crash_setup_regs`:

crash_setup_regs
================

.. c:function:: void crash_setup_regs(struct pt_regs *newregs, struct pt_regs *oldregs)

    save registers for the panic kernel

    :param newregs:
        registers are saved here
    :type newregs: struct pt_regs \*

    :param oldregs:
        registers to be saved (may be \ ``NULL``\ )
    :type oldregs: struct pt_regs \*

.. This file was automatic generated / don't edit.

