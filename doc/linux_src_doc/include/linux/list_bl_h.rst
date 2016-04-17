.. -*- coding: utf-8; mode: rst -*-

=========
list_bl.h
=========


.. _`hlist_bl_for_each_entry`:

hlist_bl_for_each_entry
=======================

.. c:function:: hlist_bl_for_each_entry ( tpos,  pos,  head,  member)

    iterate over list of given type

    :param tpos:
        the type * to use as a loop cursor.

    :param pos:
        the :c:type:`struct hlist_node <hlist_node>` to use as a loop cursor.

    :param head:
        the head for your list.

    :param member:
        the name of the hlist_node within the struct.



.. _`hlist_bl_for_each_entry_safe`:

hlist_bl_for_each_entry_safe
============================

.. c:function:: hlist_bl_for_each_entry_safe ( tpos,  pos,  n,  head,  member)

    iterate over list of given type safe against removal of list entry

    :param tpos:
        the type * to use as a loop cursor.

    :param pos:
        the :c:type:`struct hlist_node <hlist_node>` to use as a loop cursor.

    :param n:
        another :c:type:`struct hlist_node <hlist_node>` to use as temporary storage

    :param head:
        the head for your list.

    :param member:
        the name of the hlist_node within the struct.

