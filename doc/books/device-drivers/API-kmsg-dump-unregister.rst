.. -*- coding: utf-8; mode: rst -*-

.. _API-kmsg-dump-unregister:

====================
kmsg_dump_unregister
====================

*man kmsg_dump_unregister(9)*

*4.6.0-rc5*

unregister a kmsg dumper.


Synopsis
========

.. c:function:: int kmsg_dump_unregister( struct kmsg_dumper * dumper )

Arguments
=========

``dumper``
    pointer to the kmsg_dumper structure


Description
===========

Removes a dump device from the system. Returns zero on success and
``-EINVAL`` otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
