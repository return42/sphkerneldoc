.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/m32r/include/asm/local.h

.. _`local_read`:

local_read
==========

.. c:function::  local_read( l)

    read local variable

    :param  l:
        pointer of type local_t

.. _`local_read.description`:

Description
-----------

Atomically reads the value of \ ``l``\ .

.. _`local_set`:

local_set
=========

.. c:function::  local_set( l,  i)

    set local variable

    :param  l:
        pointer of type local_t

    :param  i:
        required value

.. _`local_set.description`:

Description
-----------

Atomically sets the value of \ ``l``\  to \ ``i``\ .

.. _`local_add_return`:

local_add_return
================

.. c:function:: long local_add_return(long i, local_t *l)

    add long to local variable and return it

    :param long i:
        long value to add

    :param local_t \*l:
        pointer of type local_t

.. _`local_add_return.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``l``\  and return (@i + \ ``l``\ ).

.. _`local_sub_return`:

local_sub_return
================

.. c:function:: long local_sub_return(long i, local_t *l)

    subtract long from local variable and return it

    :param long i:
        long value to subtract

    :param local_t \*l:
        pointer of type local_t

.. _`local_sub_return.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``l``\  and return (@l - \ ``i``\ ).

.. _`local_add`:

local_add
=========

.. c:function::  local_add( i,  l)

    add long to local variable

    :param  i:
        long value to add

    :param  l:
        pointer of type local_t

.. _`local_add.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``l``\ .

.. _`local_sub`:

local_sub
=========

.. c:function::  local_sub( i,  l)

    subtract the local variable

    :param  i:
        long value to subtract

    :param  l:
        pointer of type local_t

.. _`local_sub.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``l``\ .

.. _`local_sub_and_test`:

local_sub_and_test
==================

.. c:function::  local_sub_and_test( i,  l)

    subtract value from variable and test result

    :param  i:
        integer value to subtract

    :param  l:
        pointer of type local_t

.. _`local_sub_and_test.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``l``\  and returns
true if the result is zero, or false for all
other cases.

.. _`local_inc_return`:

local_inc_return
================

.. c:function:: long local_inc_return(local_t *l)

    increment local variable and return it

    :param local_t \*l:
        pointer of type local_t

.. _`local_inc_return.description`:

Description
-----------

Atomically increments \ ``l``\  by 1 and returns the result.

.. _`local_dec_return`:

local_dec_return
================

.. c:function:: long local_dec_return(local_t *l)

    decrement local variable and return it

    :param local_t \*l:
        pointer of type local_t

.. _`local_dec_return.description`:

Description
-----------

Atomically decrements \ ``l``\  by 1 and returns the result.

.. _`local_inc`:

local_inc
=========

.. c:function::  local_inc( l)

    increment local variable

    :param  l:
        pointer of type local_t

.. _`local_inc.description`:

Description
-----------

Atomically increments \ ``l``\  by 1.

.. _`local_dec`:

local_dec
=========

.. c:function::  local_dec( l)

    decrement local variable

    :param  l:
        pointer of type local_t

.. _`local_dec.description`:

Description
-----------

Atomically decrements \ ``l``\  by 1.

.. _`local_inc_and_test`:

local_inc_and_test
==================

.. c:function::  local_inc_and_test( l)

    increment and test

    :param  l:
        pointer of type local_t

.. _`local_inc_and_test.description`:

Description
-----------

Atomically increments \ ``l``\  by 1
and returns true if the result is zero, or false for all
other cases.

.. _`local_dec_and_test`:

local_dec_and_test
==================

.. c:function::  local_dec_and_test( l)

    decrement and test

    :param  l:
        pointer of type local_t

.. _`local_dec_and_test.description`:

Description
-----------

Atomically decrements \ ``l``\  by 1 and
returns true if the result is 0, or false for all
other cases.

.. _`local_add_negative`:

local_add_negative
==================

.. c:function::  local_add_negative( i,  l)

    add and test if negative

    :param  i:
        integer value to add

    :param  l:
        pointer of type local_t

.. _`local_add_negative.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``l``\  and returns true
if the result is negative, or false when
result is greater than or equal to zero.

.. _`local_add_unless`:

local_add_unless
================

.. c:function:: int local_add_unless(local_t *l, long a, long u)

    add unless the number is a given value

    :param local_t \*l:
        pointer of type local_t

    :param long a:
        the amount to add to l...

    :param long u:
        ...unless l is equal to u.

.. _`local_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``l``\ , so long as it was not \ ``u``\ .
Returns non-zero if \ ``l``\  was not \ ``u``\ , and zero otherwise.

.. This file was automatic generated / don't edit.

