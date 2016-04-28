.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-info-create-module-entry:

============================
snd_info_create_module_entry
============================

*man snd_info_create_module_entry(9)*

*4.6.0-rc5*

create an info entry for the given module


Synopsis
========

.. c:function:: struct snd_info_entry * snd_info_create_module_entry( struct module * module, const char * name, struct snd_info_entry * parent )

Arguments
=========

``module``
    the module pointer

``name``
    the file name

``parent``
    the parent directory


Description
===========

Creates a new info entry and assigns it to the given module.


Return
======

The pointer of the new instance, or ``NULL`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
