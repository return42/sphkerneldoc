.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/atomic.h

.. _`arch_atomic_read`:

arch_atomic_read
================

.. c:function:: int arch_atomic_read(const atomic_t *v)

    read atomic variable

    :param const atomic_t \*v:
        pointer of type atomic_t

.. _`arch_atomic_read.description`:

Description
-----------

Atomically reads the value of \ ``v``\ .

.. _`arch_atomic_set`:

arch_atomic_set
===============

.. c:function:: void arch_atomic_set(atomic_t *v, int i)

    set atomic variable

    :param atomic_t \*v:
        pointer of type atomic_t

    :param int i:
        required value

.. _`arch_atomic_set.description`:

Description
-----------

Atomically sets the value of \ ``v``\  to \ ``i``\ .

.. _`arch_atomic_add`:

arch_atomic_add
===============

.. c:function:: void arch_atomic_add(int i, atomic_t *v)

    add integer to atomic variable

    :param int i:
        integer value to add

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`arch_atomic_add.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\ .

.. _`arch_atomic_sub`:

arch_atomic_sub
===============

.. c:function:: void arch_atomic_sub(int i, atomic_t *v)

    subtract integer from atomic variable

    :param int i:
        integer value to subtract

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`arch_atomic_sub.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\ .

.. _`arch_atomic_sub_and_test`:

arch_atomic_sub_and_test
========================

.. c:function:: bool arch_atomic_sub_and_test(int i, atomic_t *v)

    subtract value from variable and test result

    :param int i:
        integer value to subtract

    :param atomic_t \*v:
        pointer of type atomic_t

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

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`arch_atomic_inc.description`:

Description
-----------

Atomically increments \ ``v``\  by 1.

.. _`arch_atomic_dec`:

arch_atomic_dec
===============

.. c:function:: void arch_atomic_dec(atomic_t *v)

    decrement atomic variable

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`arch_atomic_dec.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1.

.. _`arch_atomic_dec_and_test`:

arch_atomic_dec_and_test
========================

.. c:function:: bool arch_atomic_dec_and_test(atomic_t *v)

    decrement and test

    :param atomic_t \*v:
        pointer of type atomic_t

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

    :param atomic_t \*v:
        pointer of type atomic_t

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

    :param int i:
        integer value to add

    :param atomic_t \*v:
        pointer of type atomic_t

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

    :param int i:
        integer value to add

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`arch_atomic_add_return.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns \ ``i``\  + \ ``v``\ 

.. _`arch_atomic_sub_return`:

arch_atomic_sub_return
======================

.. c:function:: int arch_atomic_sub_return(int i, atomic_t *v)

    subtract integer and return

    :param int i:
        integer value to subtract

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`arch_atomic_sub_return.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\  and returns \ ``v``\  - \ ``i``\ 

.. _`__arch_atomic_add_unless`:

__arch_atomic_add_unless
========================

.. c:function:: int __arch_atomic_add_unless(atomic_t *v, int a, int u)

    add unless the number is already a given value

    :param atomic_t \*v:
        pointer of type atomic_t

    :param int a:
        the amount to add to v...

    :param int u:
        ...unless v is equal to u.

.. _`__arch_atomic_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , so long as \ ``v``\  was not already \ ``u``\ .
Returns the old value of \ ``v``\ .

.. This file was automatic generated / don't edit.

