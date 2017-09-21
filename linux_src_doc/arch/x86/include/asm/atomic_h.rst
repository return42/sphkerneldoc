.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/atomic.h

.. _`atomic_read`:

atomic_read
===========

.. c:function:: int atomic_read(const atomic_t *v)

    read atomic variable

    :param const atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_read.description`:

Description
-----------

Atomically reads the value of \ ``v``\ .

.. _`atomic_set`:

atomic_set
==========

.. c:function:: void atomic_set(atomic_t *v, int i)

    set atomic variable

    :param atomic_t \*v:
        pointer of type atomic_t

    :param int i:
        required value

.. _`atomic_set.description`:

Description
-----------

Atomically sets the value of \ ``v``\  to \ ``i``\ .

.. _`atomic_add`:

atomic_add
==========

.. c:function:: void atomic_add(int i, atomic_t *v)

    add integer to atomic variable

    :param int i:
        integer value to add

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_add.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\ .

.. _`atomic_sub`:

atomic_sub
==========

.. c:function:: void atomic_sub(int i, atomic_t *v)

    subtract integer from atomic variable

    :param int i:
        integer value to subtract

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_sub.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\ .

.. _`atomic_sub_and_test`:

atomic_sub_and_test
===================

.. c:function:: bool atomic_sub_and_test(int i, atomic_t *v)

    subtract value from variable and test result

    :param int i:
        integer value to subtract

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_sub_and_test.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\  and returns
true if the result is zero, or false for all
other cases.

.. _`atomic_inc`:

atomic_inc
==========

.. c:function:: void atomic_inc(atomic_t *v)

    increment atomic variable

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_inc.description`:

Description
-----------

Atomically increments \ ``v``\  by 1.

.. _`atomic_dec`:

atomic_dec
==========

.. c:function:: void atomic_dec(atomic_t *v)

    decrement atomic variable

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_dec.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1.

.. _`atomic_dec_and_test`:

atomic_dec_and_test
===================

.. c:function:: bool atomic_dec_and_test(atomic_t *v)

    decrement and test

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_dec_and_test.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1 and
returns true if the result is 0, or false for all other
cases.

.. _`atomic_inc_and_test`:

atomic_inc_and_test
===================

.. c:function:: bool atomic_inc_and_test(atomic_t *v)

    increment and test

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_inc_and_test.description`:

Description
-----------

Atomically increments \ ``v``\  by 1
and returns true if the result is zero, or false for all
other cases.

.. _`atomic_add_negative`:

atomic_add_negative
===================

.. c:function:: bool atomic_add_negative(int i, atomic_t *v)

    add and test if negative

    :param int i:
        integer value to add

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_add_negative.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns true
if the result is negative, or false when
result is greater than or equal to zero.

.. _`atomic_add_return`:

atomic_add_return
=================

.. c:function:: int atomic_add_return(int i, atomic_t *v)

    add integer and return

    :param int i:
        integer value to add

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_add_return.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns \ ``i``\  + \ ``v``\ 

.. _`atomic_sub_return`:

atomic_sub_return
=================

.. c:function:: int atomic_sub_return(int i, atomic_t *v)

    subtract integer and return

    :param int i:
        integer value to subtract

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_sub_return.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\  and returns \ ``v``\  - \ ``i``\ 

.. _`__atomic_add_unless`:

__atomic_add_unless
===================

.. c:function:: int __atomic_add_unless(atomic_t *v, int a, int u)

    add unless the number is already a given value

    :param atomic_t \*v:
        pointer of type atomic_t

    :param int a:
        the amount to add to v...

    :param int u:
        ...unless v is equal to u.

.. _`__atomic_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , so long as \ ``v``\  was not already \ ``u``\ .
Returns the old value of \ ``v``\ .

.. This file was automatic generated / don't edit.

