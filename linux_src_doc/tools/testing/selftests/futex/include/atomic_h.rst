.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/testing/selftests/futex/include/atomic.h

.. _`atomic_cmpxchg`:

atomic_cmpxchg
==============

.. c:function:: int atomic_cmpxchg(atomic_t *addr, int oldval, int newval)

    Atomic compare and exchange

    :param addr:
        *undescribed*
    :type addr: atomic_t \*

    :param oldval:
        The expected value of the futex
    :type oldval: int

    :param newval:
        The new value to try and assign the futex
    :type newval: int

.. _`atomic_cmpxchg.description`:

Description
-----------

Return the old value of addr->val.

.. _`atomic_inc`:

atomic_inc
==========

.. c:function:: int atomic_inc(atomic_t *addr)

    Atomic incrememnt

    :param addr:
        Address of the variable to increment
    :type addr: atomic_t \*

.. _`atomic_inc.description`:

Description
-----------

Return the new value of addr->val.

.. _`atomic_dec`:

atomic_dec
==========

.. c:function:: int atomic_dec(atomic_t *addr)

    Atomic decrement

    :param addr:
        Address of the variable to decrement
    :type addr: atomic_t \*

.. _`atomic_dec.description`:

Description
-----------

Return the new value of addr-val.

.. _`atomic_set`:

atomic_set
==========

.. c:function:: int atomic_set(atomic_t *addr, int newval)

    Atomic set

    :param addr:
        Address of the variable to set
    :type addr: atomic_t \*

    :param newval:
        New value for the atomic_t
    :type newval: int

.. _`atomic_set.description`:

Description
-----------

Return the new value of addr->val.

.. This file was automatic generated / don't edit.

