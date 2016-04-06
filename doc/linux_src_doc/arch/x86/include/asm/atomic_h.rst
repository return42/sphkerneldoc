.. -*- coding: utf-8; mode: rst -*-

========
atomic.h
========



.. _xref_atomic_read:

atomic_read
===========

.. c:function:: int atomic_read (const atomic_t * v)

    read atomic variable

    :param const atomic_t * v:
        pointer of type atomic_t



Description
-----------

Atomically reads the value of **v**.




.. _xref_atomic_set:

atomic_set
==========

.. c:function:: void atomic_set (atomic_t * v, int i)

    set atomic variable

    :param atomic_t * v:
        pointer of type atomic_t

    :param int i:
        required value



Description
-----------

Atomically sets the value of **v** to **i**.




.. _xref_atomic_add:

atomic_add
==========

.. c:function:: void atomic_add (int i, atomic_t * v)

    add integer to atomic variable

    :param int i:
        integer value to add

    :param atomic_t * v:
        pointer of type atomic_t



Description
-----------

Atomically adds **i** to **v**.




.. _xref_atomic_sub:

atomic_sub
==========

.. c:function:: void atomic_sub (int i, atomic_t * v)

    subtract integer from atomic variable

    :param int i:
        integer value to subtract

    :param atomic_t * v:
        pointer of type atomic_t



Description
-----------

Atomically subtracts **i** from **v**.




.. _xref_atomic_sub_and_test:

atomic_sub_and_test
===================

.. c:function:: int atomic_sub_and_test (int i, atomic_t * v)

    subtract value from variable and test result

    :param int i:
        integer value to subtract

    :param atomic_t * v:
        pointer of type atomic_t



Description
-----------

Atomically subtracts **i** from **v** and returns
true if the result is zero, or false for all
other cases.




.. _xref_atomic_inc:

atomic_inc
==========

.. c:function:: void atomic_inc (atomic_t * v)

    increment atomic variable

    :param atomic_t * v:
        pointer of type atomic_t



Description
-----------

Atomically increments **v** by 1.




.. _xref_atomic_dec:

atomic_dec
==========

.. c:function:: void atomic_dec (atomic_t * v)

    decrement atomic variable

    :param atomic_t * v:
        pointer of type atomic_t



Description
-----------

Atomically decrements **v** by 1.




.. _xref_atomic_dec_and_test:

atomic_dec_and_test
===================

.. c:function:: int atomic_dec_and_test (atomic_t * v)

    decrement and test

    :param atomic_t * v:
        pointer of type atomic_t



Description
-----------

Atomically decrements **v** by 1 and
returns true if the result is 0, or false for all other
cases.




.. _xref_atomic_inc_and_test:

atomic_inc_and_test
===================

.. c:function:: int atomic_inc_and_test (atomic_t * v)

    increment and test

    :param atomic_t * v:
        pointer of type atomic_t



Description
-----------

Atomically increments **v** by 1
and returns true if the result is zero, or false for all
other cases.




.. _xref_atomic_add_negative:

atomic_add_negative
===================

.. c:function:: int atomic_add_negative (int i, atomic_t * v)

    add and test if negative

    :param int i:
        integer value to add

    :param atomic_t * v:
        pointer of type atomic_t



Description
-----------

Atomically adds **i** to **v** and returns true
if the result is negative, or false when
result is greater than or equal to zero.




.. _xref_atomic_add_return:

atomic_add_return
=================

.. c:function:: int atomic_add_return (int i, atomic_t * v)

    add integer and return

    :param int i:
        integer value to add

    :param atomic_t * v:
        pointer of type atomic_t



Description
-----------

Atomically adds **i** to **v** and returns **i** + **v**




.. _xref_atomic_sub_return:

atomic_sub_return
=================

.. c:function:: int atomic_sub_return (int i, atomic_t * v)

    subtract integer and return

    :param int i:
        integer value to subtract

    :param atomic_t * v:
        pointer of type atomic_t



Description
-----------

Atomically subtracts **i** from **v** and returns **v** - **i**




.. _xref___atomic_add_unless:

__atomic_add_unless
===================

.. c:function:: int __atomic_add_unless (atomic_t * v, int a, int u)

    add unless the number is already a given value

    :param atomic_t * v:
        pointer of type atomic_t

    :param int a:
        the amount to add to v...

    :param int u:
        ...unless v is equal to u.



Description
-----------

Atomically adds **a** to **v**, so long as **v** was not already **u**.
Returns the old value of **v**.




.. _xref_atomic_inc_short:

atomic_inc_short
================

.. c:function:: short int atomic_inc_short (short int * v)

    increment of a short integer

    :param short int * v:
        pointer to type int



Description
-----------

Atomically adds 1 to **v**
Returns the new value of **u**


