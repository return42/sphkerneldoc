.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/bitops.h

.. _`__flogr`:

\__flogr
========

.. c:function:: unsigned char __flogr(unsigned long word)

    find leftmost one \ ``word``\  - The word to search

    :param word:
        *undescribed*
    :type word: unsigned long

.. _`__flogr.description`:

Description
-----------

Returns the bit number of the most significant bit set,
where the most significant bit has bit number 0.
If no bit is set this function returns 64.

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

.. _`ffs`:

ffs
===

.. c:function:: int ffs(int word)

    find first bit set

    :param word:
        the word to search
    :type word: int

.. _`ffs.description`:

Description
-----------

This is defined the same way as the libc and
compiler builtin ffs routines (man ffs).

.. _`__fls`:

\__fls
======

.. c:function:: unsigned long __fls(unsigned long word)

    find last (most-significant) set bit in a long word

    :param word:
        the word to search
    :type word: unsigned long

.. _`__fls.description`:

Description
-----------

Undefined if no set bit exists, so code should check against 0 first.

.. _`fls64`:

fls64
=====

.. c:function:: int fls64(unsigned long word)

    find last set bit in a 64-bit word

    :param word:
        the word to search
    :type word: unsigned long

.. _`fls64.description`:

Description
-----------

This is defined in a similar way as the libc and compiler builtin
ffsll, but returns the position of the most significant set bit.

fls64(value) returns 0 if value is 0 or the position of the last
set bit if value is nonzero. The last (most significant) bit is
at position 64.

.. _`fls`:

fls
===

.. c:function:: int fls(int word)

    find last (most-significant) bit set

    :param word:
        the word to search
    :type word: int

.. _`fls.description`:

Description
-----------

This is defined the same way as ffs.
Note fls(0) = 0, fls(1) = 1, fls(0x80000000) = 32.

.. This file was automatic generated / don't edit.

