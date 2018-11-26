.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/atomic.h

.. _`arch_atomic_read`:

arch_atomic_read
================

.. c:function:: int arch_atomic_read(const atomic_t *v)

    read atomic variable

    :param v:
        pointer of type atomic_t
    :type v: const atomic_t \*

.. _`arch_atomic_read.description`:

Description
-----------

Atomically reads the value of \ ``v``\ .

.. _`arch_atomic_set`:

arch_atomic_set
===============

.. c:function:: void arch_atomic_set(atomic_t *v, int i)

    set atomic variable

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

    :param i:
        required value
    :type i: int

.. _`arch_atomic_set.description`:

Description
-----------

Atomically sets the value of \ ``v``\  to \ ``i``\ .

.. _`arch_atomic_add`:

arch_atomic_add
===============

.. c:function:: void arch_atomic_add(int i, atomic_t *v)

    add integer to atomic variable

    :param i:
        integer value to add
    :type i: int

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`arch_atomic_add.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\ .

.. _`arch_atomic_sub`:

arch_atomic_sub
===============

.. c:function:: void arch_atomic_sub(int i, atomic_t *v)

    subtract integer from atomic variable

    :param i:
        integer value to subtract
    :type i: int

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`arch_atomic_sub.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\ .

.. _`arch_atomic_sub_and_test`:

arch_atomic_sub_and_test
========================

.. c:function:: bool arch_atomic_sub_and_test(int i, atomic_t *v)

    subtract value from variable and test result

    :param i:
        integer value to subtract
    :type i: int

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`arch_atomic_sub_and_test.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\  and returns
true if the result is zero, or false for all
other cases.

.. _`arch_atomic_inc`:

arch_atomic_inc
===============

.. c:function:: void arch_atomic_inc(atomic_t *v)

    increment atomic variable

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`arch_atomic_inc.description`:

Description
-----------

Atomically increments \ ``v``\  by 1.

.. _`arch_atomic_dec`:

arch_atomic_dec
===============

.. c:function:: void arch_atomic_dec(atomic_t *v)

    decrement atomic variable

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`arch_atomic_dec.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1.

.. _`arch_atomic_dec_and_test`:

arch_atomic_dec_and_test
========================

.. c:function:: bool arch_atomic_dec_and_test(atomic_t *v)

    decrement and test

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`arch_atomic_dec_and_test.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1 and
returns true if the result is 0, or false for all other
cases.

.. _`arch_atomic_inc_and_test`:

arch_atomic_inc_and_test
========================

.. c:function:: bool arch_atomic_inc_and_test(atomic_t *v)

    increment and test

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`arch_atomic_inc_and_test.description`:

Description
-----------

Atomically increments \ ``v``\  by 1
and returns true if the result is zero, or false for all
other cases.

.. _`arch_atomic_add_negative`:

arch_atomic_add_negative
========================

.. c:function:: bool arch_atomic_add_negative(int i, atomic_t *v)

    add and test if negative

    :param i:
        integer value to add
    :type i: int

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`arch_atomic_add_negative.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns true
if the result is negative, or false when
result is greater than or equal to zero.

.. _`arch_atomic_add_return`:

arch_atomic_add_return
======================

.. c:function:: int arch_atomic_add_return(int i, atomic_t *v)

    add integer and return

    :param i:
        integer value to add
    :type i: int

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`arch_atomic_add_return.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns \ ``i``\  + \ ``v``\ 

.. _`arch_atomic_sub_return`:

arch_atomic_sub_return
======================

.. c:function:: int arch_atomic_sub_return(int i, atomic_t *v)

    subtract integer and return

    :param i:
        integer value to subtract
    :type i: int

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

.. _`arch_atomic_sub_return.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\  and returns \ ``v``\  - \ ``i``\ 

.. This file was automatic generated / don't edit.

