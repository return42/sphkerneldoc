.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/refcount.h

.. _`refcount_t`:

typedef refcount_t
==================

.. c:type:: typedef refcount_t

    variant of atomic_t specialized for reference counts

.. _`refcount_t.description`:

Description
-----------

The counter saturates at UINT_MAX and will not move once
there. This avoids wrapping the counter and causing 'spurious'
use-after-free bugs.

.. _`refcount_set`:

refcount_set
============

.. c:function:: void refcount_set(refcount_t *r, unsigned int n)

    set a refcount's value

    :param refcount_t \*r:
        the refcount

    :param unsigned int n:
        value to which the refcount will be set

.. _`refcount_read`:

refcount_read
=============

.. c:function:: unsigned int refcount_read(const refcount_t *r)

    get a refcount's value

    :param const refcount_t \*r:
        the refcount

.. _`refcount_read.return`:

Return
------

the refcount's value

.. This file was automatic generated / don't edit.

