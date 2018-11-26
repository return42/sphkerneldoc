.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/atomic64_32.h

.. _`arch_atomic64_cmpxchg`:

arch_atomic64_cmpxchg
=====================

.. c:function:: long long arch_atomic64_cmpxchg(atomic64_t *v, long long o, long long n)

    cmpxchg atomic64 variable

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

    :param o:
        expected value
    :type o: long long

    :param n:
        new value
    :type n: long long

.. _`arch_atomic64_cmpxchg.description`:

Description
-----------

Atomically sets \ ``v``\  to \ ``n``\  if it was equal to \ ``o``\  and returns
the old value.

.. _`arch_atomic64_xchg`:

arch_atomic64_xchg
==================

.. c:function:: long long arch_atomic64_xchg(atomic64_t *v, long long n)

    xchg atomic64 variable

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

    :param n:
        value to assign
    :type n: long long

.. _`arch_atomic64_xchg.description`:

Description
-----------

Atomically xchgs the value of \ ``v``\  to \ ``n``\  and returns
the old value.

.. _`arch_atomic64_set`:

arch_atomic64_set
=================

.. c:function:: void arch_atomic64_set(atomic64_t *v, long long i)

    set atomic64 variable

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

    :param i:
        value to assign
    :type i: long long

.. _`arch_atomic64_set.description`:

Description
-----------

Atomically sets the value of \ ``v``\  to \ ``n``\ .

.. _`arch_atomic64_read`:

arch_atomic64_read
==================

.. c:function:: long long arch_atomic64_read(const atomic64_t *v)

    read atomic64 variable

    :param v:
        pointer to type atomic64_t
    :type v: const atomic64_t \*

.. _`arch_atomic64_read.description`:

Description
-----------

Atomically reads the value of \ ``v``\  and returns it.

.. _`arch_atomic64_add_return`:

arch_atomic64_add_return
========================

.. c:function:: long long arch_atomic64_add_return(long long i, atomic64_t *v)

    add and return

    :param i:
        integer value to add
    :type i: long long

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

.. _`arch_atomic64_add_return.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns \ ``i``\  + \*@v

.. _`arch_atomic64_add`:

arch_atomic64_add
=================

.. c:function:: long long arch_atomic64_add(long long i, atomic64_t *v)

    add integer to atomic64 variable

    :param i:
        integer value to add
    :type i: long long

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

.. _`arch_atomic64_add.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\ .

.. _`arch_atomic64_sub`:

arch_atomic64_sub
=================

.. c:function:: long long arch_atomic64_sub(long long i, atomic64_t *v)

    subtract the atomic64 variable

    :param i:
        integer value to subtract
    :type i: long long

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

.. _`arch_atomic64_sub.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\ .

.. _`arch_atomic64_inc`:

arch_atomic64_inc
=================

.. c:function:: void arch_atomic64_inc(atomic64_t *v)

    increment atomic64 variable

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

.. _`arch_atomic64_inc.description`:

Description
-----------

Atomically increments \ ``v``\  by 1.

.. _`arch_atomic64_dec`:

arch_atomic64_dec
=================

.. c:function:: void arch_atomic64_dec(atomic64_t *v)

    decrement atomic64 variable

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

.. _`arch_atomic64_dec.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1.

.. _`arch_atomic64_add_unless`:

arch_atomic64_add_unless
========================

.. c:function:: int arch_atomic64_add_unless(atomic64_t *v, long long a, long long u)

    add unless the number is a given value

    :param v:
        pointer of type atomic64_t
    :type v: atomic64_t \*

    :param a:
        the amount to add to v...
    :type a: long long

    :param u:
        ...unless v is equal to u.
    :type u: long long

.. _`arch_atomic64_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , so long as it was not \ ``u``\ .
Returns non-zero if the add was done, zero otherwise.

.. This file was automatic generated / don't edit.

