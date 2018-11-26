.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/strlist.h

.. _`strlist__for_each_entry`:

strlist__for_each_entry
=======================

.. c:function::  strlist__for_each_entry( pos,  slist)

    iterate over a strlist

    :param pos:
        the \ :c:type:`struct str_node <str_node>`\  to use as a loop cursor.
    :type pos: 

    :param slist:
        the \ :c:type:`struct strlist <strlist>`\  for loop.
    :type slist: 

.. _`strlist__for_each_entry_safe`:

strlist__for_each_entry_safe
============================

.. c:function::  strlist__for_each_entry_safe( pos,  n,  slist)

    iterate over a strlist safe against removal of str_node

    :param pos:
        the \ :c:type:`struct str_node <str_node>`\  to use as a loop cursor.
    :type pos: 

    :param n:
        another \ :c:type:`struct str_node <str_node>`\  to use as temporary storage.
    :type n: 

    :param slist:
        the \ :c:type:`struct strlist <strlist>`\  for loop.
    :type slist: 

.. This file was automatic generated / don't edit.

