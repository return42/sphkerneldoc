.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_interval.c

.. _`interval_end`:

interval_end
============

.. c:function:: sector_t interval_end(struct rb_node *node)

    return end of \ ``node``\ 

    :param node:
        *undescribed*
    :type node: struct rb_node \*

.. _`compute_subtree_last`:

compute_subtree_last
====================

.. c:function:: sector_t compute_subtree_last(struct drbd_interval *node)

    compute end of \ ``node``\ 

    :param node:
        *undescribed*
    :type node: struct drbd_interval \*

.. _`compute_subtree_last.description`:

Description
-----------

The end of an interval is the highest (start + (size >> 9)) value of this
node and of its children.  Called for \ ``node``\  and its parents whenever the end
may have changed.

.. _`drbd_insert_interval`:

drbd_insert_interval
====================

.. c:function:: bool drbd_insert_interval(struct rb_root *root, struct drbd_interval *this)

    insert a new interval into a tree

    :param root:
        *undescribed*
    :type root: struct rb_root \*

    :param this:
        *undescribed*
    :type this: struct drbd_interval \*

.. _`drbd_contains_interval`:

drbd_contains_interval
======================

.. c:function:: bool drbd_contains_interval(struct rb_root *root, sector_t sector, struct drbd_interval *interval)

    check if a tree contains a given interval

    :param root:
        *undescribed*
    :type root: struct rb_root \*

    :param sector:
        start sector of \ ``interval``\ 
    :type sector: sector_t

    :param interval:
        may not be a valid pointer
    :type interval: struct drbd_interval \*

.. _`drbd_contains_interval.description`:

Description
-----------

Returns if the tree contains the node \ ``interval``\  with start sector \ ``start``\ .
Does not dereference \ ``interval``\  until \ ``interval``\  is known to be a valid object
in \ ``tree``\ .  Returns \ ``false``\  if \ ``interval``\  is in the tree but with a different
sector number.

.. _`drbd_remove_interval`:

drbd_remove_interval
====================

.. c:function:: void drbd_remove_interval(struct rb_root *root, struct drbd_interval *this)

    remove an interval from a tree

    :param root:
        *undescribed*
    :type root: struct rb_root \*

    :param this:
        *undescribed*
    :type this: struct drbd_interval \*

.. _`drbd_find_overlap`:

drbd_find_overlap
=================

.. c:function:: struct drbd_interval *drbd_find_overlap(struct rb_root *root, sector_t sector, unsigned int size)

    search for an interval overlapping with [sector, sector + size)

    :param root:
        *undescribed*
    :type root: struct rb_root \*

    :param sector:
        start sector
    :type sector: sector_t

    :param size:
        size, aligned to 512 bytes
    :type size: unsigned int

.. _`drbd_find_overlap.description`:

Description
-----------

Returns an interval overlapping with [sector, sector + size), or NULL if
there is none.  When there is more than one overlapping interval in the
tree, the interval with the lowest start sector is returned, and all other
overlapping intervals will be on the right side of the tree, reachable with
\ :c:func:`rb_next`\ .

.. This file was automatic generated / don't edit.

