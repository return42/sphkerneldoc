.. -*- coding: utf-8; mode: rst -*-

.. _API-sync-mapping-buffers:

====================
sync_mapping_buffers
====================

*man sync_mapping_buffers(9)*

*4.6.0-rc5*

write out & wait upon a mapping's “associated” buffers


Synopsis
========

.. c:function:: int sync_mapping_buffers( struct address_space * mapping )

Arguments
=========

``mapping``
    the mapping which wants those buffers written


Description
===========

Starts I/O against the buffers at mapping->private_list, and waits upon
that I/O.

Basically, this is a convenience function for ``fsync``. ``mapping`` is
a file or directory which needs those buffers to be written for a
successful ``fsync``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
