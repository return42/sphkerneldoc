.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/bitops/builtin-__ffs.h

.. _`__ffs`:

\__ffs
======

.. c:function:: unsigned long __ffs(unsigned long word)

    find first bit in word.

    :param word:
        The word to search
    :type word: unsigned long

.. _`__ffs.description`:

Description
-----------

Undefined if no bit exists, so code should check against 0 first.

.. This file was automatic generated / don't edit.

