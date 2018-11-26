.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/intlist.h

.. _`intlist__for_each_entry`:

intlist__for_each_entry
=======================

.. c:function::  intlist__for_each_entry( pos,  ilist)

    iterate over a intlist

    :param pos:
        the \ :c:type:`struct int_node <int_node>`\  to use as a loop cursor.
    :type pos: 

    :param ilist:
        the \ :c:type:`struct intlist <intlist>`\  for loop.
    :type ilist: 

.. _`intlist__for_each_entry_safe`:

intlist__for_each_entry_safe
============================

.. c:function::  intlist__for_each_entry_safe( pos,  n,  ilist)

    iterate over a intlist safe against removal of int_node

    :param pos:
        the \ :c:type:`struct int_node <int_node>`\  to use as a loop cursor.
    :type pos: 

    :param n:
        another \ :c:type:`struct int_node <int_node>`\  to use as temporary storage.
    :type n: 

    :param ilist:
        the \ :c:type:`struct intlist <intlist>`\  for loop.
    :type ilist: 

.. This file was automatic generated / don't edit.

