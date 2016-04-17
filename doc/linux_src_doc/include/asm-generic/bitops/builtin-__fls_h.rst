.. -*- coding: utf-8; mode: rst -*-

===============
builtin-__fls.h
===============


.. _`__fls`:

__fls
=====

.. c:function:: unsigned long __fls (unsigned long word)

    find last (most-significant) set bit in a long word

    :param unsigned long word:
        the word to search



.. _`__fls.description`:

Description
-----------

Undefined if no set bit exists, so code should check against 0 first.

