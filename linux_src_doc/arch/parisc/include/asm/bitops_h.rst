.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/parisc/include/asm/bitops.h

.. _`__ffs`:

\__ffs
======

.. c:function:: unsigned long __ffs(unsigned long x)

    find first bit in word. returns 0 to "BITS_PER_LONG-1".

    :param unsigned long x:
        *undescribed*

.. _`__ffs.description`:

Description
-----------

\__ffs() return is undefined if no bit is set.

32-bit fast \__ffs by LaMont Jones "lamont At hp com".
64-bit enhancement by Grant Grundler "grundler At parisc-linux org".
(with help from willy/jejb to get the semantics right)

This algorithm avoids branches by making use of nullification.
One side effect of "extr" instructions is it sets PSW[N] bit.
How PSW[N] (nullify next insn) gets set is determined by the
"condition" field (eg "<>" or "TR" below) in the extr\* insn.
Only the 1st and one of either the 2cd or 3rd insn will get executed.
Each set of 3 insn will get executed in 2 cycles on PA8x00 vs 16 or so
cycles for each mispredicted branch.

.. This file was automatic generated / don't edit.

