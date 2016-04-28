.. -*- coding: utf-8; mode: rst -*-

.. _API-kmsg-dump-rewind:

================
kmsg_dump_rewind
================

*man kmsg_dump_rewind(9)*

*4.6.0-rc5*

reset the interator


Synopsis
========

.. c:function:: void kmsg_dump_rewind( struct kmsg_dumper * dumper )

Arguments
=========

``dumper``
    registered kmsg dumper


Description
===========

Reset the dumper's iterator so that ``kmsg_dump_get_line`` and
``kmsg_dump_get_buffer`` can be called again and used multiple times
within the same dumper.\ ``dump`` callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
