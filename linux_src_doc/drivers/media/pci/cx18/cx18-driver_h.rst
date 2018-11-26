.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/pci/cx18/cx18-driver.h

.. _`list_entry_is_past_end`:

list_entry_is_past_end
======================

.. c:function::  list_entry_is_past_end( pos,  head,  member)

    check if a previous loop cursor is off list end

    :param pos:
        the type \* previously used as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_entry_is_past_end.description`:

Description
-----------

Check if the entry's list_head is the head of the list, thus it's not a
real entry but was the loop cursor that walked past the end

.. This file was automatic generated / don't edit.

