.. -*- coding: utf-8; mode: rst -*-

.. _API-sq-remap:

========
sq_remap
========

*man sq_remap(9)*

*4.6.0-rc5*

Map a physical address through the Store Queues


Synopsis
========

.. c:function:: unsigned long sq_remap( unsigned long phys, unsigned int size, const char * name, pgprot_t prot )

Arguments
=========

``phys``
    Physical address of mapping.

``size``
    Length of mapping.

``name``
    User invoking mapping.

``prot``
    Protection bits.


Description
===========

Remaps the physical address ``phys`` through the next available store
queue address of ``size`` length. ``name`` is logged at boot time as
well as through the sysfs interface.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
