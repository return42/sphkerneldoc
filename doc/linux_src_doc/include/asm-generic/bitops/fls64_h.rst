.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/bitops/fls64.h

.. _`fls64`:

fls64
=====

.. c:function:: int fls64(__u64 x)

    find last set bit in a 64-bit word

    :param __u64 x:
        the word to search

.. _`fls64.description`:

Description
-----------

This is defined in a similar way as the libc and compiler builtin
ffsll, but returns the position of the most significant set bit.

fls64(value) returns 0 if value is 0 or the position of the last
set bit if value is nonzero. The last (most significant) bit is
at position 64.

.. This file was automatic generated / don't edit.

