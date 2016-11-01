.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/alpha/include/asm/barrier.h

.. _`read_barrier_depends`:

read_barrier_depends
====================

.. c:function::  read_barrier_depends( void)

    Flush all pending reads that subsequents reads depend on.

    :param  void:
        no arguments

.. _`read_barrier_depends.description`:

Description
-----------

No data-dependent reads from memory-like regions are ever reordered
over this barrier.  All reads preceding this primitive are guaranteed
to access memory (but not necessarily other CPUs' caches) before any
reads following this primitive that depend on the data return by
any of the preceding reads.  This primitive is much lighter weight than
\ :c:func:`rmb`\  on most CPUs, and is never heavier weight than is
\ :c:func:`rmb`\ .

These ordering constraints are respected by both the local CPU
and the compiler.

Ordering is not guaranteed by anything other than these primitives,
not even by data dependencies.  See the documentation for
\ :c:func:`memory_barrier`\  for examples and URLs to more information.

For example, the following code would force ordering (the initial
value of "a" is zero, "b" is one, and "p" is "&a"):

<programlisting>
CPU 0                           CPU 1

b = 2;
\ :c:func:`memory_barrier`\ ;
p = \ :c:type:`struct b <b>`\ ;                         q = p;
\ :c:func:`read_barrier_depends`\ ;
d = \*q;
</programlisting>

because the read of "\*q" depends on the read of "p" and these
two reads are separated by a \ :c:func:`read_barrier_depends`\ .  However,
the following code, with the same initial values for "a" and "b":

<programlisting>
CPU 0                           CPU 1

a = 2;
\ :c:func:`memory_barrier`\ ;
b = 3;                          y = b;
\ :c:func:`read_barrier_depends`\ ;
x = a;
</programlisting>

does not enforce ordering, since there is no data dependency between
the read of "a" and the read of "b".  Therefore, on some CPUs, such
as Alpha, "y" could be set to 3 and "x" to 0.  Use \ :c:func:`rmb`\ 
in cases like this where there are no data dependencies.

.. This file was automatic generated / don't edit.

