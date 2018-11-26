.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/c6x/include/asm/bitops.h

.. _`__ffs`:

\__ffs
======

.. c:function:: unsigned long __ffs(unsigned long x)

    find first bit in word.

    :param x:
        *undescribed*
    :type x: unsigned long

.. _`__ffs.description`:

Description
-----------

Undefined if no bit exists, so code should check against 0 first.
Note \__ffs(0) = undef, \__ffs(1) = 0, \__ffs(0x80000000) = 31.

.. _`fls`:

fls
===

.. c:function:: int fls(int x)

    find last (most-significant) bit set

    :param x:
        the word to search
    :type x: int

.. _`fls.description`:

Description
-----------

This is defined the same way as ffs.
Note fls(0) = 0, fls(1) = 1, fls(0x80000000) = 32.

.. _`ffs`:

ffs
===

.. c:function:: int ffs(int x)

    find first bit set

    :param x:
        the word to search
    :type x: int

.. _`ffs.description`:

Description
-----------

This is defined the same way as
the libc and compiler builtin ffs routines, therefore
differs in spirit from the above ffz (man ffs).
Note ffs(0) = 0, ffs(1) = 1, ffs(0x80000000) = 32.

.. This file was automatic generated / don't edit.

