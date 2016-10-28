.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/tile/include/asm/bitops.h

.. _`ffz`:

ffz
===

.. c:function:: unsigned long ffz(unsigned long word)

    find first zero bit in word

    :param unsigned long word:
        The word to search

.. _`ffz.description`:

Description
-----------

Undefined if no zero exists, so code should check against ~0UL first.

.. _`fls`:

fls
===

.. c:function:: int fls(int x)

    find last set bit in word

    :param int x:
        the word to search

.. _`fls.description`:

Description
-----------

This is defined in a similar way as the libc and compiler builtin
ffs, but returns the position of the most significant set bit.

fls(value) returns 0 if value is 0 or the position of the last
set bit if value is nonzero. The last (most significant) bit is
at position 32.

.. This file was automatic generated / don't edit.

