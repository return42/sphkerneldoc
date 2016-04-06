
.. _API-kobject-move:

============
kobject_move
============

*man kobject_move(9)*

*4.6.0-rc1*

move object to another parent


Synopsis
========

.. c:function:: int kobject_move( struct kobject * kobj, struct kobject * new_parent )

Arguments
=========

``kobj``
    object in question.

``new_parent``
    object's new parent (can be NULL)
