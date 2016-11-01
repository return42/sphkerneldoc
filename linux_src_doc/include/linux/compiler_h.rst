.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/compiler.h

.. _`compiletime_assert`:

compiletime_assert
==================

.. c:function::  compiletime_assert( condition,  msg)

    break build and emit msg if condition is false

    :param  condition:
        a compile-time constant condition to check

    :param  msg:
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

.. c:function::  lockless_dereference( p)

    safely load a pointer for later dereference

    :param  p:
        The pointer to load

.. _`lockless_dereference.description`:

Description
-----------

Similar to \ :c:func:`rcu_dereference`\ , but for situations where the pointed-to
object's lifetime is managed by something other than RCU.  That
"something other" might be reference counting or simple immortality.

The seemingly unused variable \___typecheck_p validates that \ ``p``\  is
indeed a pointer type by using a pointer to typeof(\*p) as the type.
Taking a pointer to typeof(\*p) again is needed in case p is void \*.

.. This file was automatic generated / don't edit.

