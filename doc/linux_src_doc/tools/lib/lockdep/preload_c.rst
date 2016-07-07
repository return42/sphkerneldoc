.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/lockdep/preload.c

.. _`lock_lookup`:

struct lock_lookup
==================

.. c:type:: struct lock_lookup

    liblockdep's view of a single unique lock

.. _`lock_lookup.definition`:

Definition
----------

.. code-block:: c

    struct lock_lookup {
        void *orig;
        struct lockdep_map dep_map;
        struct lock_class_key key;
        struct rb_node node;
        #define LIBLOCKDEP_MAX_LOCK_NAME 22
        char name[LIBLOCKDEP_MAX_LOCK_NAME];
    }

.. _`lock_lookup.members`:

Members
-------

orig
    pointer to the original pthread lock, used for lookups

dep_map
    lockdep's dep_map structure

key
    lockdep's key structure

node
    rb-tree node used to store the lock in a global tree

name
    a unique name for the lock

.. _`__get_lock`:

__get_lock
==========

.. c:function:: struct lock_lookup *__get_lock(void *lock)

    find or create a lock instance

    :param void \*lock:
        pointer to a pthread lock function

.. _`__get_lock.description`:

Description
-----------

Try to find an existing lock in the rbtree using the provided pointer. If
one wasn't found - create it.

.. This file was automatic generated / don't edit.

