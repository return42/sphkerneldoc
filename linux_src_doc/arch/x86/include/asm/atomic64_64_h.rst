.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/atomic64_64.h

.. _`arch_atomic64_read`:

arch_atomic64_read
==================

.. c:function:: long arch_atomic64_read(const atomic64_t *v)

    read atomic64 variable

    :param v:
        pointer of type atomic64_t
    :type v: const atomic64_t \*

.. _`arch_atomic64_read.description`:

Description
-----------

Atomically reads the value of \ ``v``\ .
Doesn't imply a read memory barrier.

.. _`arch_atomic64_set`:

arch_atomic64_set
=================

.. c:function:: void arch_atomic64_set(atomic64_t *v, long i)

    set atomic64 variable

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

    :param i:
        required value
    :type i: long

.. _`arch_atomic64_set.description`:

Description
-----------

Atomically sets the value of \ ``v``\  to \ ``i``\ .

.. _`arch_atomic64_add`:

arch_atomic64_add
=================

.. c:function:: void arch_atomic64_add(long i, atomic64_t *v)

    add integer to atomic64 variable

    :param i:
        integer value to add
    :type i: long

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

.. c:function:: void arch_atomic64_sub(long i, atomic64_t *v)

    subtract the atomic64 variable

    :param i:
        integer value to subtract
    :type i: long

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

.. _`arch_atomic64_sub.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\ .

.. _`arch_atomic64_sub_and_test`:

arch_atomic64_sub_and_test
==========================

.. c:function:: bool arch_atomic64_sub_and_test(long i, atomic64_t *v)

    subtract value from variable and test result

    :param i:
        integer value to subtract
    :type i: long

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

.. _`arch_atomic64_sub_and_test.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\  and returns
true if the result is zero, or false for all
other cases.

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

.. _`arch_atomic64_dec_and_test`:

arch_atomic64_dec_and_test
==========================

.. c:function:: bool arch_atomic64_dec_and_test(atomic64_t *v)

    decrement and test

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

.. _`arch_atomic64_dec_and_test.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1 and
returns true if the result is 0, or false for all other
cases.

.. _`arch_atomic64_inc_and_test`:

arch_atomic64_inc_and_test
==========================

.. c:function:: bool arch_atomic64_inc_and_test(atomic64_t *v)

    increment and test

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

.. _`arch_atomic64_inc_and_test.description`:

Description
-----------

Atomically increments \ ``v``\  by 1
and returns true if the result is zero, or false for all
other cases.

.. _`arch_atomic64_add_negative`:

arch_atomic64_add_negative
==========================

.. c:function:: bool arch_atomic64_add_negative(long i, atomic64_t *v)

    add and test if negative

    :param i:
        integer value to add
    :type i: long

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

.. _`arch_atomic64_add_negative.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns true
if the result is negative, or false when
result is greater than or equal to zero.

.. _`arch_atomic64_add_return`:

arch_atomic64_add_return
========================

.. c:function:: long arch_atomic64_add_return(long i, atomic64_t *v)

    add and return

    :param i:
        integer value to add
    :type i: long

    :param v:
        pointer to type atomic64_t
    :type v: atomic64_t \*

.. _`arch_atomic64_add_return.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns \ ``i``\  + \ ``v``\ 

.. This file was automatic generated / don't edit.

