.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/strlist.h

.. _`strlist__for_each`:

strlist__for_each
=================

.. c:function::  strlist__for_each( pos,  slist)

    iterate over a strlist

    :param  pos:
        the \ :c:type:`struct str_node <str_node>`\  to use as a loop cursor.

    :param  slist:
        the \ :c:type:`struct strlist <strlist>`\  for loop.

.. _`strlist__for_each_safe`:

strlist__for_each_safe
======================

.. c:function::  strlist__for_each_safe( pos,  n,  slist)

    iterate over a strlist safe against removal of str_node

    :param  pos:
        the \ :c:type:`struct str_node <str_node>`\  to use as a loop cursor.

    :param  n:
        another \ :c:type:`struct str_node <str_node>`\  to use as temporary storage.

    :param  slist:
        the \ :c:type:`struct strlist <strlist>`\  for loop.

.. This file was automatic generated / don't edit.

