.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/numa/toptree.c

.. _`toptree_alloc`:

toptree_alloc
=============

.. c:function:: struct toptree *toptree_alloc(int level, int id)

    Allocate and initialize a new tree node.

    :param int level:
        The node's vertical level; level 0 contains the leaves.

    :param int id:
        ID number, explicitly not unique beyond scope of node's siblings

.. _`toptree_alloc.description`:

Description
-----------

Allocate a new tree node and initialize it.

.. _`toptree_alloc.return`:

Return
------

Pointer to the new tree node or NULL on error

.. _`toptree_remove`:

toptree_remove
==============

.. c:function:: void toptree_remove(struct toptree *cand)

    Remove a tree node from a tree

    :param struct toptree \*cand:
        Pointer to the node to remove

.. _`toptree_remove.description`:

Description
-----------

The node is detached from its parent node. The parent node's
masks will be updated to reflect the loss of the child.

.. _`toptree_free`:

toptree_free
============

.. c:function:: void toptree_free(struct toptree *cand)

    discard a tree node

    :param struct toptree \*cand:
        Pointer to the tree node to discard

.. _`toptree_free.description`:

Description
-----------

Checks if \ ``cand``\  is attached to a parent node. Detaches it
cleanly using toptree_remove. Possible children are freed
recursively. In the end \ ``cand``\  itself is freed.

.. _`toptree_update_mask`:

toptree_update_mask
===================

.. c:function:: void toptree_update_mask(struct toptree *cand)

    Update node bitmasks

    :param struct toptree \*cand:
        Pointer to a tree node

.. _`toptree_update_mask.description`:

Description
-----------

The node's cpumask will be updated by combining all children's
masks. Then toptree_update_mask is called recursively for the
parent if applicable.

.. _`toptree_update_mask.note`:

NOTE
----

This must not be called on leaves. If called on a leaf, its
CPU mask is cleared and lost.

.. _`toptree_insert`:

toptree_insert
==============

.. c:function:: int toptree_insert(struct toptree *cand, struct toptree *target)

    Insert a tree node into tree

    :param struct toptree \*cand:
        Pointer to the node to insert

    :param struct toptree \*target:
        Pointer to the node to which \ ``cand``\  will added as a child

.. _`toptree_insert.description`:

Description
-----------

Insert a tree node into a tree. Masks will be updated automatically.

.. _`toptree_insert.return`:

Return
------

0 on success, -1 if NULL is passed as argument or the node levels
don't fit.

.. _`toptree_move_children`:

toptree_move_children
=====================

.. c:function:: void toptree_move_children(struct toptree *cand, struct toptree *target)

    Move all child nodes of a node to a new place

    :param struct toptree \*cand:
        Pointer to the node whose children are to be moved

    :param struct toptree \*target:
        Pointer to the node to which \ ``cand``\ 's children will be attached

.. _`toptree_move_children.description`:

Description
-----------

Take all child nodes of \ ``cand``\  and move them using toptree_move.

.. _`toptree_unify`:

toptree_unify
=============

.. c:function:: void toptree_unify(struct toptree *cand)

    Merge children with same ID

    :param struct toptree \*cand:
        Pointer to node whose direct children should be made unique

.. _`toptree_unify.description`:

Description
-----------

When mangling the tree it is possible that a node has two or more children
which have the same ID. This routine merges these children into one and
moves all children of the merged nodes into the unified node.

.. _`toptree_move`:

toptree_move
============

.. c:function:: void toptree_move(struct toptree *cand, struct toptree *target)

    Move a node to another context

    :param struct toptree \*cand:
        Pointer to the node to move

    :param struct toptree \*target:
        Pointer to the node where \ ``cand``\  should go

.. _`toptree_move.description`:

Description
-----------

In the easiest case \ ``cand``\  is exactly on the level below \ ``target``\ 
and will be immediately moved to the target.

If \ ``target``\ 's level is not the direct parent level of \ ``cand``\ ,
nodes for the missing levels are created and put between
\ ``cand``\  and \ ``target``\ . The "stacking" nodes' IDs are taken from
\ ``cand``\ 's parents.

After this it is likely to have redundant nodes in the tree
which are addressed by means of toptree_unify.

.. _`toptree_get_child`:

toptree_get_child
=================

.. c:function:: struct toptree *toptree_get_child(struct toptree *cand, int id)

    Access a tree node's child by its ID

    :param struct toptree \*cand:
        Pointer to tree node whose child is to access

    :param int id:
        The desired child's ID

.. _`toptree_get_child.description`:

Description
-----------

@cand's children are searched for a child with matching ID.
If no match can be found, a new child with the desired ID
is created and returned.

.. _`toptree_first`:

toptree_first
=============

.. c:function:: struct toptree *toptree_first(struct toptree *context, int level)

    Find the first descendant on specified level

    :param struct toptree \*context:
        Pointer to tree node whose descendants are to be used

    :param int level:
        The level of interest

.. _`toptree_first.return`:

Return
------

@context's first descendant on the specified level, or NULL
if there is no matching descendant

.. _`toptree_next_sibling`:

toptree_next_sibling
====================

.. c:function:: struct toptree *toptree_next_sibling(struct toptree *cur)

    Return next sibling

    :param struct toptree \*cur:
        Pointer to a tree node

.. _`toptree_next_sibling.return`:

Return
------

If \ ``cur``\  has a parent and is not the last in the parent's children list,
the next sibling is returned. Or NULL when there are no siblings left.

.. _`toptree_next`:

toptree_next
============

.. c:function:: struct toptree *toptree_next(struct toptree *cur, struct toptree *context, int level)

    Tree traversal function

    :param struct toptree \*cur:
        Pointer to current element

    :param struct toptree \*context:
        Pointer to the root node of the tree or subtree to
        be traversed.

    :param int level:
        The level of interest.

.. _`toptree_next.return`:

Return
------

Pointer to the next node on level \ ``level``\ 
or NULL when there is no next node.

.. _`toptree_count`:

toptree_count
=============

.. c:function:: int toptree_count(struct toptree *context, int level)

    Count descendants on specified level

    :param struct toptree \*context:
        Pointer to node whose descendants are to be considered

    :param int level:
        Only descendants on the specified level will be counted

.. _`toptree_count.return`:

Return
------

Number of descendants on the specified level

.. This file was automatic generated / don't edit.

