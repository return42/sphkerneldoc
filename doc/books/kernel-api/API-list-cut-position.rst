
.. _API-list-cut-position:

=================
list_cut_position
=================

*man list_cut_position(9)*

*4.6.0-rc1*

cut a list into two


Synopsis
========

.. c:function:: void list_cut_position( struct list_head * list, struct list_head * head, struct list_head * entry )

Arguments
=========

``list``
    a new list to add all removed entries

``head``
    a list with entries

``entry``
    an entry within head, could be the head itself and if so we won't cut the list


Description
===========

This helper moves the initial part of ``head``, up to and including ``entry``, from ``head`` to ``list``. You should pass on ``entry`` an element you know is on ``head``. ``list``
should be an empty list or a list you do not care about losing its data.
