.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-dev-info-list-add:

======================
scsi_dev_info_list_add
======================

*man scsi_dev_info_list_add(9)*

*4.6.0-rc5*

add one dev_info list entry.


Synopsis
========

.. c:function:: int scsi_dev_info_list_add( int compatible, char * vendor, char * model, char * strflags, int flags )

Arguments
=========

``compatible``
    if true, null terminate short strings. Otherwise space pad.

``vendor``
    vendor string

``model``
    model (product) string

``strflags``
    integer string

``flags``
    if strflags NULL, use this flag value


Description
===========

Create and add one dev_info entry for ``vendor``, ``model``,
``strflags`` or ``flag``. If ``compatible``, add to the tail of the
list, do not space pad, and set devinfo->compatible. The
scsi_static_device_list entries are added with ``compatible`` 1 and
``clfags`` NULL.


Returns
=======

0 OK, -error on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
