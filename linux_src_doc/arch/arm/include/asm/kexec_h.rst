.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/include/asm/kexec.h

.. _`crash_setup_regs`:

crash_setup_regs
================

.. c:function:: void crash_setup_regs(struct pt_regs *newregs, struct pt_regs *oldregs)

    save registers for the panic kernel

    :param struct pt_regs \*newregs:
        registers are saved here

    :param struct pt_regs \*oldregs:
        registers to be saved (may be \ ``NULL``\ )

.. _`crash_setup_regs.description`:

Description
-----------

Function copies machine registers from \ ``oldregs``\  to \ ``newregs``\ . If \ ``oldregs``\  is
\ ``NULL``\  then current registers are stored there.

.. This file was automatic generated / don't edit.

