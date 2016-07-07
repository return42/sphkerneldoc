.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/include/asm-generic/bitops/__ffs.h

.. _`__ffs`:

__ffs
=====

.. c:function:: unsigned long __ffs(unsigned long word)

    find first bit in word.

    :param unsigned long word:
        The word to search

.. _`__ffs.description`:

Description
-----------

Undefined if no bit exists, so code should check against 0 first.

.. This file was automatic generated / don't edit.

