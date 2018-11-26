.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/atomic.h

.. _`atomic_fetch_add_unless`:

atomic_fetch_add_unless
=======================

.. c:function:: int atomic_fetch_add_unless(atomic_t *v, int a, int u)

    add unless the number is already a given value

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

    :param a:
        the amount to add to v...
    :type a: int

    :param u:
        ...unless v is equal to u.
    :type u: int

.. _`atomic_fetch_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , if \ ``v``\  was not already \ ``u``\ .
Returns the original value of \ ``v``\ .

.. _`atomic_add_unless`:

atomic_add_unless
=================

.. c:function:: bool atomic_add_unless(atomic_t *v, int a, int u)

    add unless the number is already a given value

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

    :param a:
        the amount to add to v...
    :type a: int

    :param u:
        ...unless v is equal to u.
    :type u: int

.. _`atomic_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , if \ ``v``\  was not already \ ``u``\ .
Returns true if the addition was done.

.. _`atomic_inc_not_zero`:

atomic_inc_not_zero
===================

.. c:function::  atomic_inc_not_zero( v)

    increment unless the number is zero

    :param v:
        pointer of type atomic_t
    :type v: 

.. _`atomic_inc_not_zero.description`:

Description
-----------

Atomically increments \ ``v``\  by 1, if \ ``v``\  is non-zero.
Returns true if the increment was done.

.. _`atomic_inc_and_test`:

atomic_inc_and_test
===================

.. c:function:: bool atomic_inc_and_test(atomic_t *v)

    increment and test

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`atomic_inc_and_test.description`:

Description
-----------

Atomically increments \ ``v``\  by 1
and returns true if the result is zero, or false for all
other cases.

.. _`atomic_dec_and_test`:

atomic_dec_and_test
===================

.. c:function:: bool atomic_dec_and_test(atomic_t *v)

    decrement and test

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`atomic_dec_and_test.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1 and
returns true if the result is 0, or false for all other
cases.

.. _`atomic_sub_and_test`:

atomic_sub_and_test
===================

.. c:function:: bool atomic_sub_and_test(int i, atomic_t *v)

    subtract value from variable and test result

    :param i:
        integer value to subtract
    :type i: int

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`atomic_sub_and_test.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\  and returns
true if the result is zero, or false for all
other cases.

.. _`atomic_add_negative`:

atomic_add_negative
===================

.. c:function:: bool atomic_add_negative(int i, atomic_t *v)

    add and test if negative

    :param i:
        integer value to add
    :type i: int

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`atomic_add_negative.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns true
if the result is negative, or false when
result is greater than or equal to zero.

.. _`atomic64_fetch_add_unless`:

atomic64_fetch_add_unless
=========================

.. c:function:: long long atomic64_fetch_add_unless(atomic64_t *v, long long a, long long u)

    add unless the number is already a given value

    :param v:
        pointer of type atomic64_t
    :type v: atomic64_t \*

    :param a:
        the amount to add to v...
    :type a: long long

    :param u:
        ...unless v is equal to u.
    :type u: long long

.. _`atomic64_fetch_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , if \ ``v``\  was not already \ ``u``\ .
Returns the original value of \ ``v``\ .

.. _`atomic64_add_unless`:

atomic64_add_unless
===================

.. c:function:: bool atomic64_add_unless(atomic64_t *v, long long a, long long u)

    add unless the number is already a given value

    :param v:
        pointer of type atomic_t
    :type v: atomic64_t \*

    :param a:
        the amount to add to v...
    :type a: long long

    :param u:
        ...unless v is equal to u.
    :type u: long long

.. _`atomic64_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , if \ ``v``\  was not already \ ``u``\ .
Returns true if the addition was done.

.. _`atomic64_inc_not_zero`:

atomic64_inc_not_zero
=====================

.. c:function::  atomic64_inc_not_zero( v)

    increment unless the number is zero

    :param v:
        pointer of type atomic64_t
    :type v: 

.. _`atomic64_inc_not_zero.description`:

Description
-----------

Atomically increments \ ``v``\  by 1, if \ ``v``\  is non-zero.
Returns true if the increment was done.

.. _`atomic64_inc_and_test`:

atomic64_inc_and_test
=====================

.. c:function:: bool atomic64_inc_and_test(atomic64_t *v)

    increment and test

    :param v:
        pointer of type atomic64_t
    :type v: atomic64_t \*

.. _`atomic64_inc_and_test.description`:

Description
-----------

Atomically increments \ ``v``\  by 1
and returns true if the result is zero, or false for all
other cases.

.. _`atomic64_dec_and_test`:

atomic64_dec_and_test
=====================

.. c:function:: bool atomic64_dec_and_test(atomic64_t *v)

    decrement and test

    :param v:
        pointer of type atomic64_t
    :type v: atomic64_t \*

.. _`atomic64_dec_and_test.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1 and
returns true if the result is 0, or false for all other
cases.

.. _`atomic64_sub_and_test`:

atomic64_sub_and_test
=====================

.. c:function:: bool atomic64_sub_and_test(long long i, atomic64_t *v)

    subtract value from variable and test result

    :param i:
        integer value to subtract
    :type i: long long

    :param v:
        pointer of type atomic64_t
    :type v: atomic64_t \*

.. _`atomic64_sub_and_test.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\  and returns
true if the result is zero, or false for all
other cases.

.. _`atomic64_add_negative`:

atomic64_add_negative
=====================

.. c:function:: bool atomic64_add_negative(long long i, atomic64_t *v)

    add and test if negative

    :param i:
        integer value to add
    :type i: long long

    :param v:
        pointer of type atomic64_t
    :type v: atomic64_t \*

.. _`atomic64_add_negative.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns true
if the result is negative, or false when
result is greater than or equal to zero.

.. This file was automatic generated / don't edit.

