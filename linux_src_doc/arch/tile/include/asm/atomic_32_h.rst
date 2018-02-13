.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/tile/include/asm/atomic_32.h

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

.. _`__atomic_add_unless`:

\__atomic_add_unless
====================

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

.. _`atomic_set`:

atomic_set
==========

.. c:function:: void atomic_set(atomic_t *v, int n)

    set atomic variable

    :param atomic_t \*v:
        pointer of type atomic_t

    :param int n:
        *undescribed*

.. _`atomic_set.description`:

Description
-----------

Atomically sets the value of \ ``v``\  to \ ``i``\ .

\ :c:func:`atomic_set`\  can't be just a raw store, since it would be lost if it
fell between the load and store of one of the other atomic ops.

.. _`atomic64_read`:

atomic64_read
=============

.. c:function:: long long atomic64_read(const atomic64_t *v)

    read atomic variable

    :param const atomic64_t \*v:
        pointer of type atomic64_t

.. _`atomic64_read.description`:

Description
-----------

Atomically reads the value of \ ``v``\ .

.. _`atomic64_add`:

atomic64_add
============

.. c:function:: void atomic64_add(long long i, atomic64_t *v)

    add integer to atomic variable

    :param long long i:
        integer value to add

    :param atomic64_t \*v:
        pointer of type atomic64_t

.. _`atomic64_add.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\ .

.. _`atomic64_add_return`:

atomic64_add_return
===================

.. c:function:: long long atomic64_add_return(long long i, atomic64_t *v)

    add integer and return

    :param long long i:
        integer value to add

    :param atomic64_t \*v:
        pointer of type atomic64_t

.. _`atomic64_add_return.description`:

Description
-----------

Atomically adds \ ``i``\  to \ ``v``\  and returns \ ``i``\  + \ ``v``\ 

.. _`atomic64_add_unless`:

atomic64_add_unless
===================

.. c:function:: long long atomic64_add_unless(atomic64_t *v, long long a, long long u)

    add unless the number is already a given value

    :param atomic64_t \*v:
        pointer of type atomic64_t

    :param long long a:
        the amount to add to v...

    :param long long u:
        ...unless v is equal to u.

.. _`atomic64_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , so long as \ ``v``\  was not already \ ``u``\ .
Returns non-zero if \ ``v``\  was not \ ``u``\ , and zero otherwise.

.. _`atomic64_set`:

atomic64_set
============

.. c:function:: void atomic64_set(atomic64_t *v, long long n)

    set atomic variable

    :param atomic64_t \*v:
        pointer of type atomic64_t

    :param long long n:
        *undescribed*

.. _`atomic64_set.description`:

Description
-----------

Atomically sets the value of \ ``v``\  to \ ``i``\ .

\ :c:func:`atomic64_set`\  can't be just a raw store, since it would be lost if it
fell between the load and store of one of the other atomic ops.

.. This file was automatic generated / don't edit.

