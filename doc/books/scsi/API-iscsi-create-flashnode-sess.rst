.. -*- coding: utf-8; mode: rst -*-

.. _API-iscsi-create-flashnode-sess:

===========================
iscsi_create_flashnode_sess
===========================

*man iscsi_create_flashnode_sess(9)*

*4.6.0-rc5*

Add flashnode session entry in sysfs


Synopsis
========

.. c:function:: struct iscsi_bus_flash_session * iscsi_create_flashnode_sess( struct Scsi_Host * shost, int index, struct iscsi_transport * transport, int dd_size )

Arguments
=========

``shost``
    pointer to host data

``index``
    index of flashnode to add in sysfs

``transport``
    pointer to transport data

``dd_size``
    total size to allocate


Description
===========

Adds a sysfs entry for the flashnode session attributes


Returns
=======

pointer to allocated flashnode sess on success ``NULL`` on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
