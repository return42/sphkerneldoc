.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/hexagon/include/asm/atomic.h

.. _`atomic_read`:

atomic_read
===========

.. c:function::  atomic_read( v)

    reads a word, atomically

    :param  v:
        pointer to atomic value

.. _`atomic_read.description`:

Description
-----------

Assumes all word reads on our architecture are atomic.

.. _`atomic_xchg`:

atomic_xchg
===========

.. c:function::  atomic_xchg( v,  new)

    atomic

    :param  v:
        pointer to memory to change

    :param  new:
        new value (technically passed in a register -- see xchg)

.. _`atomic_cmpxchg`:

atomic_cmpxchg
==============

.. c:function:: int atomic_cmpxchg(atomic_t *v, int old, int new)

    atomic compare-and-exchange values

    :param atomic_t \*v:
        pointer to value to change

    :param int old:
        desired old value to match

    :param int new:
        new value to put in

.. _`atomic_cmpxchg.description`:

Description
-----------

Parameters are then pointer, value-in-register, value-in-register,
and the output is the old value.

Apparently this is complicated for archs that don't support
the memw_locked like we do (or it's broken or whatever).

Kind of the lynchpin of the rest of the generically defined routines.
Remember V2 had that bug with dotnew predicate set by memw_locked.

"old" is "expected" old val, \__oldval is actual old value

.. _`__atomic_add_unless`:

\__atomic_add_unless
====================

.. c:function:: int __atomic_add_unless(atomic_t *v, int a, int u)

    add unless the number is a given value

    :param atomic_t \*v:
        pointer to value

    :param int a:
        amount to add

    :param int u:
        unless value is equal to u

.. _`__atomic_add_unless.description`:

Description
-----------

Returns old value.

.. This file was automatic generated / don't edit.

