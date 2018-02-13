.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/x25/x25_link.c

.. _`__x25_remove_neigh`:

\__x25_remove_neigh
===================

.. c:function:: void __x25_remove_neigh(struct x25_neigh *nb)

    remove neighbour from x25_neigh_list \ ``nb``\  - neigh to remove

    :param struct x25_neigh \*nb:
        *undescribed*

.. _`__x25_remove_neigh.description`:

Description
-----------

Remove neighbour from x25_neigh_list. If it was there.
Caller must hold x25_neigh_list_lock.

.. This file was automatic generated / don't edit.

