.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/xtensa/include/asm/atomic.h

.. _`atomic_read`:

atomic_read
===========

.. c:function::  atomic_read( v)

    read atomic variable

    :param  v:
        pointer of type atomic_t

.. _`atomic_read.description`:

Description
-----------

Atomically reads the value of \ ``v``\ .

.. _`atomic_set`:

atomic_set
==========

.. c:function::  atomic_set( v,  i)

    set atomic variable

    :param  v:
        pointer of type atomic_t

    :param  i:
        required value

.. _`atomic_set.description`:

Description
-----------

Atomically sets the value of \ ``v``\  to \ ``i``\ .

.. _`atomic_sub_and_test`:

atomic_sub_and_test
===================

.. c:function::  atomic_sub_and_test( i,  v)

    subtract value from variable and test result

    :param  i:
        integer value to subtract

    :param  v:
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

.. c:function::  atomic_inc( v)

    increment atomic variable

    :param  v:
        pointer of type atomic_t

.. _`atomic_inc.description`:

Description
-----------

Atomically increments \ ``v``\  by 1.

.. _`atomic_inc_return`:

atomic_inc_return
=================

.. c:function::  atomic_inc_return( v)

    increment atomic variable

    :param  v:
        pointer of type atomic_t

.. _`atomic_inc_return.description`:

Description
-----------

Atomically increments \ ``v``\  by 1.

.. _`atomic_dec`:

atomic_dec
==========

.. c:function::  atomic_dec( v)

    decrement atomic variable

    :param  v:
        pointer of type atomic_t

.. _`atomic_dec.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1.

.. _`atomic_dec_return`:

atomic_dec_return
=================

.. c:function::  atomic_dec_return( v)

    decrement atomic variable

    :param  v:
        pointer of type atomic_t

.. _`atomic_dec_return.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1.

.. _`atomic_dec_and_test`:

atomic_dec_and_test
===================

.. c:function::  atomic_dec_and_test( v)

    decrement and test

    :param  v:
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

.. c:function::  atomic_inc_and_test( v)

    increment and test

    :param  v:
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

.. c:function::  atomic_add_negative( i,  v)

    add and test if negative

    :param  i:
        integer value to add

    :param  v:
        pointer of type atomic_t

.. _`atomic_add_negative.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns true
if the result is negative, or false when
result is greater than or equal to zero.

.. _`__atomic_add_unless`:

__atomic_add_unless
===================

.. c:function:: int __atomic_add_unless(atomic_t *v, int a, int u)

    add unless the number is a given value

    :param atomic_t \*v:
        pointer of type atomic_t

    :param int a:
        the amount to add to v...

    :param int u:
        ...unless v is equal to u.

.. _`__atomic_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , so long as it was not \ ``u``\ .
Returns the old value of \ ``v``\ .

.. This file was automatic generated / don't edit.

