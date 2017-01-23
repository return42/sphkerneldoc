.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mn10300/include/asm/bitops.h

.. _`__ffs`:

__ffs
=====

.. c:function:: unsigned long __ffs(unsigned long x)

    find first bit set

    :param unsigned long x:
        the word to search

.. _`__ffs.description`:

Description
-----------

- return 31..0 to indicate bit 31..0 most least significant bit set
- if no bits are set in x, the result is undefined

.. _`fls`:

fls
===

.. c:function:: int fls(int x)

    find last bit set

    :param int x:
        the word to search

.. _`fls.this-is-defined-the-same-way-as-ffs`:

This is defined the same way as ffs
-----------------------------------

- return 32..1 to indicate bit 31..0 most significant bit set
- return 0 to indicate no bits set

.. _`__fls`:

__fls
=====

.. c:function:: unsigned long __fls(unsigned long word)

    find last (most-significant) set bit in a long word

    :param unsigned long word:
        the word to search

.. _`__fls.description`:

Description
-----------

Undefined if no set bit exists, so code should check against 0 first.

.. _`ffs`:

ffs
===

.. c:function:: int ffs(int x)

    find first bit set

    :param int x:
        the word to search

.. _`ffs.description`:

Description
-----------

- return 32..1 to indicate bit 31..0 most least significant bit set
- return 0 to indicate no bits set

.. This file was automatic generated / don't edit.

