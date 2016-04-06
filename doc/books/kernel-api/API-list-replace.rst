
.. _API-list-replace:

============
list_replace
============

*man list_replace(9)*

*4.6.0-rc1*

replace old entry by new one


Synopsis
========

.. c:function:: void list_replace( struct list_head * old, struct list_head * new )

Arguments
=========

``old``
    the element to be replaced

``new``
    the new element to insert


Description
===========

If ``old`` was empty, it will be overwritten.
