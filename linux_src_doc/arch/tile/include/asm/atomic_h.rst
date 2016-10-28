.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/tile/include/asm/atomic.h

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

.. _`atomic_sub_return`:

atomic_sub_return
=================

.. c:function::  atomic_sub_return( i,  v)

    subtract integer and return

    :param  i:
        integer value to subtract

    :param  v:
        pointer of type atomic_t

.. _`atomic_sub_return.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\  and returns \ ``v``\  - \ ``i``\ 

.. _`atomic_sub`:

atomic_sub
==========

.. c:function::  atomic_sub( i,  v)

    subtract integer from atomic variable

    :param  i:
        integer value to subtract

    :param  v:
        pointer of type atomic_t

.. _`atomic_sub.description`:

Description
-----------

Atomically subtracts \ ``i``\  from \ ``v``\ .

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

Atomically subtracts \ ``i``\  from \ ``v``\  and returns true if the result is
zero, or false for all other cases.

.. _`atomic_inc_return`:

atomic_inc_return
=================

.. c:function::  atomic_inc_return( v)

    increment memory and return

    :param  v:
        pointer of type atomic_t

.. _`atomic_inc_return.description`:

Description
-----------

Atomically increments \ ``v``\  by 1 and returns the new value.

.. _`atomic_dec_return`:

atomic_dec_return
=================

.. c:function::  atomic_dec_return( v)

    decrement memory and return

    :param  v:
        pointer of type atomic_t

.. _`atomic_dec_return.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1 and returns the new value.

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

Atomically decrements \ ``v``\  by 1 and returns true if the result is 0.

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

Atomically increments \ ``v``\  by 1 and returns true if the result is 0.

.. _`atomic_xchg`:

atomic_xchg
===========

.. c:function:: int atomic_xchg(atomic_t *v, int n)

    atomically exchange contents of memory with a new value

    :param atomic_t \*v:
        pointer of type atomic_t

    :param int n:
        *undescribed*

.. _`atomic_xchg.description`:

Description
-----------

Atomically sets \ ``v``\  to \ ``i``\  and returns old \ ``v``\ 

.. _`atomic_cmpxchg`:

atomic_cmpxchg
==============

.. c:function:: int atomic_cmpxchg(atomic_t *v, int o, int n)

    atomically exchange contents of memory if it matches

    :param atomic_t \*v:
        pointer of type atomic_t

    :param int o:
        old value that memory should have

    :param int n:
        new value to write to memory if it matches

.. _`atomic_cmpxchg.description`:

Description
-----------

Atomically checks if \ ``v``\  holds \ ``o``\  and replaces it with \ ``n``\  if so.
Returns the old value at \ ``v``\ .

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

Atomically adds \ ``i``\  to \ ``v``\  and returns true if the result is
negative, or false when result is greater than or equal to zero.

.. _`atomic64_xchg`:

atomic64_xchg
=============

.. c:function:: long long atomic64_xchg(atomic64_t *v, long long n)

    atomically exchange contents of memory with a new value

    :param atomic64_t \*v:
        pointer of type atomic64_t

    :param long long n:
        *undescribed*

.. _`atomic64_xchg.description`:

Description
-----------

Atomically sets \ ``v``\  to \ ``i``\  and returns old \ ``v``\ 

.. _`atomic64_cmpxchg`:

atomic64_cmpxchg
================

.. c:function:: long long atomic64_cmpxchg(atomic64_t *v, long long o, long long n)

    atomically exchange contents of memory if it matches

    :param atomic64_t \*v:
        pointer of type atomic64_t

    :param long long o:
        old value that memory should have

    :param long long n:
        new value to write to memory if it matches

.. _`atomic64_cmpxchg.description`:

Description
-----------

Atomically checks if \ ``v``\  holds \ ``o``\  and replaces it with \ ``n``\  if so.
Returns the old value at \ ``v``\ .

.. This file was automatic generated / don't edit.

