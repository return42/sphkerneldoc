.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/9p/util.c

.. _`p9_idpool`:

struct p9_idpool
================

.. c:type:: struct p9_idpool

    per-connection accounting for tag idpool

.. _`p9_idpool.definition`:

Definition
----------

.. code-block:: c

    struct p9_idpool {
        spinlock_t lock;
        struct idr pool;
    }

.. _`p9_idpool.members`:

Members
-------

lock
    protects the pool

pool
    idr to allocate tag id from

.. _`p9_idpool_create`:

p9_idpool_create
================

.. c:function:: struct p9_idpool *p9_idpool_create( void)

    create a new per-connection id pool

    :param  void:
        no arguments

.. _`p9_idpool_destroy`:

p9_idpool_destroy
=================

.. c:function:: void p9_idpool_destroy(struct p9_idpool *p)

    create a new per-connection id pool

    :param struct p9_idpool \*p:
        idpool to destroy

.. _`p9_idpool_get`:

p9_idpool_get
=============

.. c:function:: int p9_idpool_get(struct p9_idpool *p)

    allocate numeric id from pool

    :param struct p9_idpool \*p:
        pool to allocate from

.. _`p9_idpool_get.bugs`:

Bugs
----

This seems to be an awful generic function, should it be in idr.c with
the lock included in struct idr?

.. _`p9_idpool_put`:

p9_idpool_put
=============

.. c:function:: void p9_idpool_put(int id, struct p9_idpool *p)

    release numeric id from pool

    :param int id:
        numeric id which is being released

    :param struct p9_idpool \*p:
        pool to release id into

.. _`p9_idpool_put.bugs`:

Bugs
----

This seems to be an awful generic function, should it be in idr.c with
the lock included in struct idr?

.. _`p9_idpool_check`:

p9_idpool_check
===============

.. c:function:: int p9_idpool_check(int id, struct p9_idpool *p)

    check if the specified id is available

    :param int id:
        id to check

    :param struct p9_idpool \*p:
        pool to check

.. This file was automatic generated / don't edit.

