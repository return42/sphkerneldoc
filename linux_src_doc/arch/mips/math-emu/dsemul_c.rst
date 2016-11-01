.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/math-emu/dsemul.c

.. _`emuframe`:

struct emuframe
===============

.. c:type:: struct emuframe

    The 'emulation' frame structure

.. _`emuframe.definition`:

Definition
----------

.. code-block:: c

    struct emuframe {
        mips_instruction emul;
        mips_instruction badinst;
    }

.. _`emuframe.members`:

Members
-------

emul
    The instruction to 'emulate'.

badinst
    A break instruction to cause a return to the kernel.

.. _`emuframe.description`:

Description
-----------

This structure defines the frames placed within the delay slot emulation
page in response to a call to \ :c:func:`mips_dsemul`\ . Each thread may be allocated
only one frame at any given time. The kernel stores within it the
instruction to be 'emulated' followed by a break instruction, then
executes the frame in user mode. The break causes a trap to the kernel
which leads to \ :c:func:`do_dsemulret`\  being called unless the instruction in
\ ``emul``\  causes a trap itself, is a branch, or a signal is delivered to
the thread. In these cases the allocated frame will either be reused by
a subsequent delay slot 'emulation', or be freed during signal delivery or
upon thread exit.

.. _`emuframe.this-approach-is-used-because`:

This approach is used because
-----------------------------


- Actually emulating all instructions isn't feasible. We would need to
be able to handle instructions from all revisions of the MIPS ISA,
all ASEs & all vendor instruction set extensions. This would be a
whole lot of work & continual maintenance burden as new instructions
are introduced, and in the case of some vendor extensions may not
even be possible. Thus we need to take the approach of actually
executing the instruction.

- We must execute the instruction within user context. If we were to
execute the instruction in kernel mode then it would have access to
kernel resources without very careful checks, leaving us with a
high potential for security or stability issues to arise.

- We used to place the frame on the users stack, but this requires
that the stack be executable. This is bad for security so the
per-process page is now used instead.

- The instruction in \ ``emul``\  may be something entirely invalid for a
delay slot. The user may (intentionally or otherwise) place a branch
in a delay slot, or a kernel mode instruction, or something else
which generates an exception. Thus we can't rely upon the break in
\ ``badinst``\  always being hit. For this reason we track the index of the
frame allocated to each thread, allowing us to clean it up at later
points such as signal delivery or thread exit.

- The user may generate a fake struct emuframe if they wish, invoking
the BRK_MEMU break instruction themselves. We must therefore not
trust that BRK_MEMU means there's actually a valid frame allocated
to the thread, and must not allow the user to do anything they
couldn't already.

.. This file was automatic generated / don't edit.

