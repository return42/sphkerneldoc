.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/local.h

.. _`local_sub_and_test`:

local_sub_and_test
==================

.. c:function:: bool local_sub_and_test(long i, local_t *l)

    subtract value from variable and test result

    :param i:
        integer value to subtract
    :type i: long

    :param l:
        pointer to type local_t
    :type l: local_t \*

.. _`local_sub_and_test.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``l``\  and returns
true if the result is zero, or false for all
other cases.

.. _`local_dec_and_test`:

local_dec_and_test
==================

.. c:function:: bool local_dec_and_test(local_t *l)

    decrement and test

    :param l:
        pointer to type local_t
    :type l: local_t \*

.. _`local_dec_and_test.description`:

Description
-----------

Atomically decrements \ ``l``\  by 1 and
returns true if the result is 0, or false for all other
cases.

.. _`local_inc_and_test`:

local_inc_and_test
==================

.. c:function:: bool local_inc_and_test(local_t *l)

    increment and test

    :param l:
        pointer to type local_t
    :type l: local_t \*

.. _`local_inc_and_test.description`:

Description
-----------

Atomically increments \ ``l``\  by 1
and returns true if the result is zero, or false for all
other cases.

.. _`local_add_negative`:

local_add_negative
==================

.. c:function:: bool local_add_negative(long i, local_t *l)

    add and test if negative

    :param i:
        integer value to add
    :type i: long

    :param l:
        pointer to type local_t
    :type l: local_t \*

.. _`local_add_negative.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``l``\  and returns true
if the result is negative, or false when
result is greater than or equal to zero.

.. _`local_add_return`:

local_add_return
================

.. c:function:: long local_add_return(long i, local_t *l)

    add and return

    :param i:
        integer value to add
    :type i: long

    :param l:
        pointer to type local_t
    :type l: local_t \*

.. _`local_add_return.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``l``\  and returns \ ``i``\  + \ ``l``\ 

.. _`local_add_unless`:

local_add_unless
================

.. c:function::  local_add_unless( l,  a,  u)

    add unless the number is a given value

    :param l:
        pointer of type local_t
    :type l: 

    :param a:
        the amount to add to l...
    :type a: 

    :param u:
        ...unless l is equal to u.
    :type u: 

.. _`local_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``l``\ , so long as it was not \ ``u``\ .
Returns non-zero if \ ``l``\  was not \ ``u``\ , and zero otherwise.

.. This file was automatic generated / don't edit.

