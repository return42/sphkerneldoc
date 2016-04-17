.. -*- coding: utf-8; mode: rst -*-

==========
compiler.h
==========


.. _`smp_cond_acquire`:

smp_cond_acquire
================

.. c:function:: smp_cond_acquire ( cond)

    Spin wait for cond with ACQUIRE ordering

    :param cond:
        boolean expression to wait for



.. _`smp_cond_acquire.description`:

Description
-----------

Equivalent to using :c:func:`smp_load_acquire` on the condition variable but employs
the control dependency of the wait to reduce the barrier on many platforms.

The control dependency provides a LOAD->STORE order, the additional RMB
provides LOAD->LOAD order, together they provide LOAD->{LOAD,STORE} order,
aka. ACQUIRE.



.. _`compiletime_assert`:

compiletime_assert
==================

.. c:function:: compiletime_assert ( condition,  msg)

    break build and emit msg if condition is false

    :param condition:
        a compile-time constant condition to check

    :param msg:
        a message to emit if condition is false



.. _`compiletime_assert.description`:

Description
-----------

In tradition of POSIX assert, this macro will break the build if the
supplied condition is \*false\*, emitting the supplied error message if the
compiler has support to do so.



.. _`lockless_dereference`:

lockless_dereference
====================

.. c:function:: lockless_dereference ( p)

    safely load a pointer for later dereference

    :param p:
        The pointer to load



.. _`lockless_dereference.description`:

Description
-----------

Similar to :c:func:`rcu_dereference`, but for situations where the pointed-to
object's lifetime is managed by something other than RCU.  That
"something other" might be reference counting or simple immortality.

