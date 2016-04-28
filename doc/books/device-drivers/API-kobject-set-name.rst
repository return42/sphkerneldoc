.. -*- coding: utf-8; mode: rst -*-

.. _API-kobject-set-name:

================
kobject_set_name
================

*man kobject_set_name(9)*

*4.6.0-rc5*

Set the name of a kobject


Synopsis
========

.. c:function:: int kobject_set_name( struct kobject * kobj, const char * fmt, ... )

Arguments
=========

``kobj``
    struct kobject to set the name of

``fmt``
    format string used to build the name

``...``
    variable arguments


Description
===========

This sets the name of the kobject. If you have already added the kobject
to the system, you must call ``kobject_rename`` in order to change the
name of the kobject.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
