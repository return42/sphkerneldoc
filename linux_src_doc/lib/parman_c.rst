.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/parman.c

.. _`parman_create`:

parman_create
=============

.. c:function:: struct parman *parman_create(const struct parman_ops *ops, void *priv)

    creates a new parman instance

    :param const struct parman_ops \*ops:
        caller-specific callbacks

    :param void \*priv:
        pointer to a private data passed to the ops

.. _`parman_create.note`:

Note
----

all locking must be provided by the caller.

Each parman instance manages an array area with chunks of entries
with the same priority. Consider following example:

item 1 with prio 10
item 2 with prio 10
item 3 with prio 10
item 4 with prio 20
item 5 with prio 20
item 6 with prio 30
item 7 with prio 30
item 8 with prio 30

In this example, there are 3 priority chunks. The order of the priorities
matters, however the order of items within a single priority chunk does not
matter. So the same array could be ordered as follows:

item 2 with prio 10
item 3 with prio 10
item 1 with prio 10
item 5 with prio 20
item 4 with prio 20
item 7 with prio 30
item 8 with prio 30
item 6 with prio 30

The goal of parman is to maintain the priority ordering. The caller
provides \ ``ops``\  with callbacks parman uses to move the items
and resize the array area.

Returns a pointer to newly created parman instance in case of success,
otherwise it returns NULL.

.. _`parman_destroy`:

parman_destroy
==============

.. c:function:: void parman_destroy(struct parman *parman)

    destroys existing parman instance

    :param struct parman \*parman:
        parman instance

.. _`parman_destroy.note`:

Note
----

all locking must be provided by the caller.

.. _`parman_prio_init`:

parman_prio_init
================

.. c:function:: void parman_prio_init(struct parman *parman, struct parman_prio *prio, unsigned long priority)

    initializes a parman priority chunk

    :param struct parman \*parman:
        parman instance

    :param struct parman_prio \*prio:
        parman prio structure to be initialized

    :param unsigned long priority:
        *undescribed*

.. _`parman_prio_init.note`:

Note
----

all locking must be provided by the caller.

Before caller could add an item with certain priority, he has to
initialize a priority chunk for it using this function.

.. _`parman_prio_fini`:

parman_prio_fini
================

.. c:function:: void parman_prio_fini(struct parman_prio *prio)

    finalizes use of parman priority chunk

    :param struct parman_prio \*prio:
        parman prio structure

.. _`parman_prio_fini.note`:

Note
----

all locking must be provided by the caller.

.. _`parman_item_add`:

parman_item_add
===============

.. c:function:: int parman_item_add(struct parman *parman, struct parman_prio *prio, struct parman_item *item)

    adds a parman item under defined priority

    :param struct parman \*parman:
        parman instance

    :param struct parman_prio \*prio:
        parman prio instance to add the item to

    :param struct parman_item \*item:
        parman item instance

.. _`parman_item_add.note`:

Note
----

all locking must be provided by the caller.

Adds item to a array managed by parman instance under the specified priority.

Returns 0 in case of success, negative number to indicate an error.

.. _`parman_item_remove`:

parman_item_remove
==================

.. c:function:: void parman_item_remove(struct parman *parman, struct parman_prio *prio, struct parman_item *item)

    deletes parman item

    :param struct parman \*parman:
        parman instance

    :param struct parman_prio \*prio:
        parman prio instance to delete the item from

    :param struct parman_item \*item:
        parman item instance

.. _`parman_item_remove.note`:

Note
----

all locking must be provided by the caller.

.. This file was automatic generated / don't edit.

