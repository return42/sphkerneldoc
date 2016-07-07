.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/list_debug.c

.. _`list_del`:

list_del
========

.. c:function:: void list_del(struct list_head *entry)

    deletes entry from list.

    :param struct list_head \*entry:
        the element to delete from the list.

.. _`list_del.note`:

Note
----

list_empty on entry does not return true after this, the entry is
in an undefined state.

.. This file was automatic generated / don't edit.

