.. -*- coding: utf-8; mode: rst -*-

============
list_nulls.h
============


.. _`is_a_nulls`:

is_a_nulls
==========

.. c:function:: int is_a_nulls (const struct hlist_nulls_node *ptr)

    Test if a ptr is a nulls

    :param const struct hlist_nulls_node \*ptr:
        ptr to be tested



.. _`get_nulls_value`:

get_nulls_value
===============

.. c:function:: unsigned long get_nulls_value (const struct hlist_nulls_node *ptr)

    Get the 'nulls' value of the end of chain

    :param const struct hlist_nulls_node \*ptr:
        end of chain



.. _`get_nulls_value.description`:

Description
-----------

Should be called only if is_a_nulls(ptr);



.. _`hlist_nulls_for_each_entry`:

hlist_nulls_for_each_entry
==========================

.. c:function:: hlist_nulls_for_each_entry ( tpos,  pos,  head,  member)

    iterate over list of given type

    :param tpos:
        the type * to use as a loop cursor.

    :param pos:
        the :c:type:`struct hlist_node <hlist_node>` to use as a loop cursor.

    :param head:
        the head for your list.

    :param member:
        the name of the hlist_node within the struct.



.. _`hlist_nulls_for_each_entry_from`:

hlist_nulls_for_each_entry_from
===============================

.. c:function:: hlist_nulls_for_each_entry_from ( tpos,  pos,  member)

    iterate over a hlist continuing from current point

    :param tpos:
        the type * to use as a loop cursor.

    :param pos:
        the :c:type:`struct hlist_node <hlist_node>` to use as a loop cursor.

    :param member:
        the name of the hlist_node within the struct.

