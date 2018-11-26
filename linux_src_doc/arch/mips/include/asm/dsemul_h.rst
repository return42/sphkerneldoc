.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/dsemul.h

.. _`mips_dsemul`:

mips_dsemul
===========

.. c:function:: int mips_dsemul(struct pt_regs *regs, mips_instruction ir, unsigned long branch_pc, unsigned long cont_pc)

    'Emulate' an instruction from a branch delay slot

    :param regs:
        User thread register context.
    :type regs: struct pt_regs \*

    :param ir:
        The instruction to be 'emulated'.
    :type ir: mips_instruction

    :param branch_pc:
        The PC of the branch instruction.
    :type branch_pc: unsigned long

    :param cont_pc:
        The PC to continue at following 'emulation'.
    :type cont_pc: unsigned long

.. _`mips_dsemul.description`:

Description
-----------

Emulate or execute an arbitrary MIPS instruction within the context of
the current user thread. This is used primarily to handle instructions
in the delay slots of emulated branch instructions, for example FP
branch instructions on systems without an FPU.

.. _`mips_dsemul.return`:

Return
------

Zero on success, negative if ir is a NOP, signal number on failure.

.. _`do_dsemulret`:

do_dsemulret
============

.. c:function:: bool do_dsemulret(struct pt_regs *xcp)

    Return from a delay slot 'emulation' frame

    :param xcp:
        User thread register context.
    :type xcp: struct pt_regs \*

.. _`do_dsemulret.description`:

Description
-----------

Call in response to the BRK_MEMU break instruction used to return to
the kernel from branch delay slot 'emulation' frames following a call
to \ :c:func:`mips_dsemul`\ . Restores the user thread PC to the value that was
passed as the cpc parameter to \ :c:func:`mips_dsemul`\ .

.. _`do_dsemulret.return`:

Return
------

True if an emulation frame was returned from, else false.

.. _`dsemul_thread_cleanup`:

dsemul_thread_cleanup
=====================

.. c:function:: bool dsemul_thread_cleanup(struct task_struct *tsk)

    Cleanup thread 'emulation' frame

    :param tsk:
        The task structure associated with the thread
    :type tsk: struct task_struct \*

.. _`dsemul_thread_cleanup.description`:

Description
-----------

If the thread \ ``tsk``\  has a branch delay slot 'emulation' frame
allocated to it then free that frame.

.. _`dsemul_thread_cleanup.return`:

Return
------

True if a frame was freed, else false.

.. _`dsemul_thread_rollback`:

dsemul_thread_rollback
======================

.. c:function:: bool dsemul_thread_rollback(struct pt_regs *regs)

    Rollback from an 'emulation' frame

    :param regs:
        User thread register context.
    :type regs: struct pt_regs \*

.. _`dsemul_thread_rollback.description`:

Description
-----------

If the current thread, whose register context is represented by \ ``regs``\ ,
is executing within a delay slot 'emulation' frame then exit that
frame. The PC will be rolled back to the branch if the instruction
that was being 'emulated' has not yet executed, or advanced to the
continuation PC if it has.

.. _`dsemul_thread_rollback.return`:

Return
------

True if a frame was exited, else false.

.. _`dsemul_mm_cleanup`:

dsemul_mm_cleanup
=================

.. c:function:: void dsemul_mm_cleanup(struct mm_struct *mm)

    Cleanup per-mm delay slot 'emulation' state

    :param mm:
        The struct mm_struct to cleanup state for.
    :type mm: struct mm_struct \*

.. _`dsemul_mm_cleanup.description`:

Description
-----------

Cleanup state for the given \ ``mm``\ , ensuring that any memory allocated
for delay slot 'emulation' book-keeping is freed. This is to be called
before \ ``mm``\  is freed in order to avoid memory leaks.

.. This file was automatic generated / don't edit.

