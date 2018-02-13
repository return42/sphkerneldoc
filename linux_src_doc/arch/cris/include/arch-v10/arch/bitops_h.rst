.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/cris/include/arch-v10/arch/bitops.h

.. _`__ffs`:

\__ffs
======

.. c:function:: unsigned long __ffs(unsigned long word)

    find first bit in word.

    :param unsigned long word:
        The word to search

.. _`__ffs.description`:

Description
-----------

Undefined if no bit exists, so code should check against 0 first.

.. _`kernel_ffs`:

kernel_ffs
==========

.. c:function:: unsigned long kernel_ffs(unsigned long w)

    find first bit set

    :param unsigned long w:
        *undescribed*

.. _`kernel_ffs.description`:

Description
-----------

This is defined the same way as
the libc and compiler builtin ffs routines, therefore
differs in spirit from the above ffz (man ffs).

.. This file was automatic generated / don't edit.

