.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/arch/x86/include/asm/atomic.h

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

.. _`atomic_dec_and_test`:

atomic_dec_and_test
===================

.. c:function:: int atomic_dec_and_test(atomic_t *v)

    decrement and test

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_dec_and_test.description`:

Description
-----------

Atomically decrements \ ``v``\  by 1 and
returns true if the result is 0, or false for all other
cases.

.. This file was automatic generated / don't edit.

