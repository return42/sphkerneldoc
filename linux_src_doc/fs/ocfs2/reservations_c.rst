.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ocfs2/reservations.c

.. _`ocfs2_find_resv_lhs`:

ocfs2_find_resv_lhs
===================

.. c:function:: struct ocfs2_alloc_reservation *ocfs2_find_resv_lhs(struct ocfs2_reservation_map *resmap, unsigned int goal)

    find the window which contains goal

    :param resmap:
        reservation map to search
    :type resmap: struct ocfs2_reservation_map \*

    :param goal:
        which bit to search for
    :type goal: unsigned int

.. _`ocfs2_find_resv_lhs.description`:

Description
-----------

If a window containing that goal is not found, we return the window
which comes before goal. Returns NULL on empty rbtree or no window
before goal.

.. This file was automatic generated / don't edit.

