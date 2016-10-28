.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/intlist.h

.. _`intlist__for_each`:

intlist__for_each
=================

.. c:function::  intlist__for_each( pos,  ilist)

    iterate over a intlist

    :param  pos:
        the \ :c:type:`struct int_node <int_node>`\  to use as a loop cursor.

    :param  ilist:
        the \ :c:type:`struct intlist <intlist>`\  for loop.

.. _`intlist__for_each_safe`:

intlist__for_each_safe
======================

.. c:function::  intlist__for_each_safe( pos,  n,  ilist)

    iterate over a intlist safe against removal of int_node

    :param  pos:
        the \ :c:type:`struct int_node <int_node>`\  to use as a loop cursor.

    :param  n:
        another \ :c:type:`struct int_node <int_node>`\  to use as temporary storage.

    :param  ilist:
        the \ :c:type:`struct intlist <intlist>`\  for loop.

.. This file was automatic generated / don't edit.

