.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/klist.c

.. _`klist_init`:

klist_init
==========

.. c:function:: void klist_init(struct klist *k, void (*get)(struct klist_node *), void (*put)(struct klist_node *))

    Initialize a klist structure.

    :param k:
        The klist we're initializing.
    :type k: struct klist \*

    :param void (\*get)(struct klist_node \*):
        The get function for the embedding object (NULL if none)

    :param void (\*put)(struct klist_node \*):
        The put function for the embedding object (NULL if none)

.. _`klist_init.description`:

Description
-----------

Initialises the klist structure.  If the klist_node structures are
going to be embedded in refcounted objects (necessary for safe
deletion) then the get/put arguments are used to initialise
functions that take and release references on the embedding
objects.

.. _`klist_add_head`:

klist_add_head
==============

.. c:function:: void klist_add_head(struct klist_node *n, struct klist *k)

    Initialize a klist_node and add it to front.

    :param n:
        node we're adding.
    :type n: struct klist_node \*

    :param k:
        klist it's going on.
    :type k: struct klist \*

.. _`klist_add_tail`:

klist_add_tail
==============

.. c:function:: void klist_add_tail(struct klist_node *n, struct klist *k)

    Initialize a klist_node and add it to back.

    :param n:
        node we're adding.
    :type n: struct klist_node \*

    :param k:
        klist it's going on.
    :type k: struct klist \*

.. _`klist_add_behind`:

klist_add_behind
================

.. c:function:: void klist_add_behind(struct klist_node *n, struct klist_node *pos)

    Init a klist_node and add it after an existing node

    :param n:
        node we're adding.
    :type n: struct klist_node \*

    :param pos:
        node to put \ ``n``\  after
    :type pos: struct klist_node \*

.. _`klist_add_before`:

klist_add_before
================

.. c:function:: void klist_add_before(struct klist_node *n, struct klist_node *pos)

    Init a klist_node and add it before an existing node

    :param n:
        node we're adding.
    :type n: struct klist_node \*

    :param pos:
        node to put \ ``n``\  after
    :type pos: struct klist_node \*

.. _`klist_del`:

klist_del
=========

.. c:function:: void klist_del(struct klist_node *n)

    Decrement the reference count of node and try to remove.

    :param n:
        node we're deleting.
    :type n: struct klist_node \*

.. _`klist_remove`:

klist_remove
============

.. c:function:: void klist_remove(struct klist_node *n)

    Decrement the refcount of node and wait for it to go away.

    :param n:
        node we're removing.
    :type n: struct klist_node \*

.. _`klist_node_attached`:

klist_node_attached
===================

.. c:function:: int klist_node_attached(struct klist_node *n)

    Say whether a node is bound to a list or not.

    :param n:
        Node that we're testing.
    :type n: struct klist_node \*

.. _`klist_iter_init_node`:

klist_iter_init_node
====================

.. c:function:: void klist_iter_init_node(struct klist *k, struct klist_iter *i, struct klist_node *n)

    Initialize a klist_iter structure.

    :param k:
        klist we're iterating.
    :type k: struct klist \*

    :param i:
        klist_iter we're filling.
    :type i: struct klist_iter \*

    :param n:
        node to start with.
    :type n: struct klist_node \*

.. _`klist_iter_init_node.description`:

Description
-----------

Similar to \ :c:func:`klist_iter_init`\ , but starts the action off with \ ``n``\ ,
instead of with the list head.

.. _`klist_iter_init`:

klist_iter_init
===============

.. c:function:: void klist_iter_init(struct klist *k, struct klist_iter *i)

    Iniitalize a klist_iter structure.

    :param k:
        klist we're iterating.
    :type k: struct klist \*

    :param i:
        klist_iter structure we're filling.
    :type i: struct klist_iter \*

.. _`klist_iter_init.description`:

Description
-----------

Similar to \ :c:func:`klist_iter_init_node`\ , but start with the list head.

.. _`klist_iter_exit`:

klist_iter_exit
===============

.. c:function:: void klist_iter_exit(struct klist_iter *i)

    Finish a list iteration.

    :param i:
        Iterator structure.
    :type i: struct klist_iter \*

.. _`klist_iter_exit.description`:

Description
-----------

Must be called when done iterating over list, as it decrements the
refcount of the current node. Necessary in case iteration exited before
the end of the list was reached, and always good form.

.. _`klist_prev`:

klist_prev
==========

.. c:function:: struct klist_node *klist_prev(struct klist_iter *i)

    Ante up prev node in list.

    :param i:
        Iterator structure.
    :type i: struct klist_iter \*

.. _`klist_prev.description`:

Description
-----------

First grab list lock. Decrement the reference count of the previous
node, if there was one. Grab the prev node, increment its reference
count, drop the lock, and return that prev node.

.. _`klist_next`:

klist_next
==========

.. c:function:: struct klist_node *klist_next(struct klist_iter *i)

    Ante up next node in list.

    :param i:
        Iterator structure.
    :type i: struct klist_iter \*

.. _`klist_next.description`:

Description
-----------

First grab list lock. Decrement the reference count of the previous
node, if there was one. Grab the next node, increment its reference
count, drop the lock, and return that next node.

.. This file was automatic generated / don't edit.

