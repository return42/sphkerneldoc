.. -*- coding: utf-8; mode: rst -*-

.. _API-kmsg-dump-register:

==================
kmsg_dump_register
==================

*man kmsg_dump_register(9)*

*4.6.0-rc5*

register a kernel log dumper.


Synopsis
========

.. c:function:: int kmsg_dump_register( struct kmsg_dumper * dumper )

Arguments
=========

``dumper``
    pointer to the kmsg_dumper structure


Description
===========

Adds a kernel log dumper to the system. The dump callback in the
structure will be called when the kernel oopses or panics and must be
set. Returns zero on success and ``-EINVAL`` or ``-EBUSY`` otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
