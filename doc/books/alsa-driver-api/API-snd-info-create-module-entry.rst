
.. _API-snd-info-create-module-entry:

============================
snd_info_create_module_entry
============================

*man snd_info_create_module_entry(9)*

*4.6.0-rc1*

create an info entry for the given module


Synopsis
========

.. c:function:: struct snd_info_entry ⋆ snd_info_create_module_entry( struct module * module, const char * name, struct snd_info_entry * parent )

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
