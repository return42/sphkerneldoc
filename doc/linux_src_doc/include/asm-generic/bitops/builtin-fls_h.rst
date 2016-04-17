.. -*- coding: utf-8; mode: rst -*-

=============
builtin-fls.h
=============


.. _`fls`:

fls
===

.. c:function:: int fls (int x)

    find last (most-significant) bit set

    :param int x:
        the word to search



.. _`fls.description`:

Description
-----------

This is defined the same way as ffs.
Note fls(0) = 0, fls(1) = 1, fls(0x80000000) = 32.

