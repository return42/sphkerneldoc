.. -*- coding: utf-8; mode: rst -*-

.. _API-kobject-move:

============
kobject_move
============

*man kobject_move(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
