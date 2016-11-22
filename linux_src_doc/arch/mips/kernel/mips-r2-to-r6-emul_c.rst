.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/mips-r2-to-r6-emul.c

.. _`mipsr6_emul`:

mipsr6_emul
===========

.. c:function:: int mipsr6_emul(struct pt_regs *regs, u32 ir)

    Emulate some frequent R2/R5/R6 instructions in delay slot for performance instead of the traditional way of using a stack trampoline which is rather slow.

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`movf_func`:

movf_func
=========

.. c:function:: int movf_func(struct pt_regs *regs, u32 ir)

    Emulate a MOVF instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`movf_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`movt_func`:

movt_func
=========

.. c:function:: int movt_func(struct pt_regs *regs, u32 ir)

    Emulate a MOVT instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`movt_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`jr_func`:

jr_func
=======

.. c:function:: int jr_func(struct pt_regs *regs, u32 ir)

    Emulate a JR instruction.

    :param struct pt_regs \*regs:
        *undescribed*

    :param u32 ir:
        Instruction

.. _`jr_func.description`:

Description
-----------

Returns SIGILL if JR was in delay slot, SIGEMT if we
can't compute the EPC, SIGSEGV if we can't access the
userland instruction or 0 on success.

.. _`movz_func`:

movz_func
=========

.. c:function:: int movz_func(struct pt_regs *regs, u32 ir)

    Emulate a MOVZ instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`movz_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`movn_func`:

movn_func
=========

.. c:function:: int movn_func(struct pt_regs *regs, u32 ir)

    Emulate a MOVZ instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`movn_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`mfhi_func`:

mfhi_func
=========

.. c:function:: int mfhi_func(struct pt_regs *regs, u32 ir)

    Emulate a MFHI instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`mfhi_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`mthi_func`:

mthi_func
=========

.. c:function:: int mthi_func(struct pt_regs *regs, u32 ir)

    Emulate a MTHI instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`mthi_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`mflo_func`:

mflo_func
=========

.. c:function:: int mflo_func(struct pt_regs *regs, u32 ir)

    Emulate a MFLO instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`mflo_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`mtlo_func`:

mtlo_func
=========

.. c:function:: int mtlo_func(struct pt_regs *regs, u32 ir)

    Emulate a MTLO instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`mtlo_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`mult_func`:

mult_func
=========

.. c:function:: int mult_func(struct pt_regs *regs, u32 ir)

    Emulate a MULT instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`mult_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`multu_func`:

multu_func
==========

.. c:function:: int multu_func(struct pt_regs *regs, u32 ir)

    Emulate a MULTU instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`multu_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`div_func`:

div_func
========

.. c:function:: int div_func(struct pt_regs *regs, u32 ir)

    Emulate a DIV instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`div_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`divu_func`:

divu_func
=========

.. c:function:: int divu_func(struct pt_regs *regs, u32 ir)

    Emulate a DIVU instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`divu_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`dmult_func`:

dmult_func
==========

.. c:function:: int dmult_func(struct pt_regs *regs, u32 ir)

    Emulate a DMULT instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`dmult_func.description`:

Description
-----------

Returns 0 on success or SIGILL for 32-bit kernels.

.. _`dmultu_func`:

dmultu_func
===========

.. c:function:: int dmultu_func(struct pt_regs *regs, u32 ir)

    Emulate a DMULTU instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`dmultu_func.description`:

Description
-----------

Returns 0 on success or SIGILL for 32-bit kernels.

.. _`ddiv_func`:

ddiv_func
=========

.. c:function:: int ddiv_func(struct pt_regs *regs, u32 ir)

    Emulate a DDIV instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`ddiv_func.description`:

Description
-----------

Returns 0 on success or SIGILL for 32-bit kernels.

.. _`ddivu_func`:

ddivu_func
==========

.. c:function:: int ddivu_func(struct pt_regs *regs, u32 ir)

    Emulate a DDIVU instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`ddivu_func.description`:

Description
-----------

Returns 0 on success or SIGILL for 32-bit kernels.

.. _`madd_func`:

madd_func
=========

.. c:function:: int madd_func(struct pt_regs *regs, u32 ir)

    Emulate a MADD instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`madd_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`maddu_func`:

maddu_func
==========

.. c:function:: int maddu_func(struct pt_regs *regs, u32 ir)

    Emulate a MADDU instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`maddu_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`msub_func`:

msub_func
=========

.. c:function:: int msub_func(struct pt_regs *regs, u32 ir)

    Emulate a MSUB instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`msub_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`msubu_func`:

msubu_func
==========

.. c:function:: int msubu_func(struct pt_regs *regs, u32 ir)

    Emulate a MSUBU instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`msubu_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`mul_func`:

mul_func
========

.. c:function:: int mul_func(struct pt_regs *regs, u32 ir)

    Emulate a MUL instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`mul_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`clz_func`:

clz_func
========

.. c:function:: int clz_func(struct pt_regs *regs, u32 ir)

    Emulate a CLZ instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`clz_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`clo_func`:

clo_func
========

.. c:function:: int clo_func(struct pt_regs *regs, u32 ir)

    Emulate a CLO instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`clo_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`dclz_func`:

dclz_func
=========

.. c:function:: int dclz_func(struct pt_regs *regs, u32 ir)

    Emulate a DCLZ instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`dclz_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`dclo_func`:

dclo_func
=========

.. c:function:: int dclo_func(struct pt_regs *regs, u32 ir)

    Emulate a DCLO instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 ir:
        Instruction

.. _`dclo_func.description`:

Description
-----------

Returns 0 since it always succeeds.

.. _`mipsr2_decoder`:

mipsr2_decoder
==============

.. c:function:: int mipsr2_decoder(struct pt_regs *regs, u32 inst, unsigned long *fcr31)

    Decode and emulate a MIPS R2 instruction

    :param struct pt_regs \*regs:
        Process register set

    :param u32 inst:
        Instruction to decode and emulate

    :param unsigned long \*fcr31:
        Floating Point Control and Status Register Cause bits returned

.. This file was automatic generated / don't edit.

