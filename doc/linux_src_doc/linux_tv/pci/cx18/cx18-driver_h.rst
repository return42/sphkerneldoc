.. -*- coding: utf-8; mode: rst -*-

=============
cx18-driver.h
=============



.. _xref_list_entry_is_past_end:

list_entry_is_past_end
======================

.. c:function:: list_entry_is_past_end ( pos,  head,  member)

    check if a previous loop cursor is off list end

    :param pos:
        the type * previously used as a loop cursor.

    :param head:
        the head for your list.

    :param member:
        the name of the list_head within the struct.



Description
-----------

Check if the entry's list_head is the head of the list, thus it's not a
real entry but was the loop cursor that walked past the end


