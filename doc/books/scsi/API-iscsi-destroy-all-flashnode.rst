.. -*- coding: utf-8; mode: rst -*-

.. _API-iscsi-destroy-all-flashnode:

===========================
iscsi_destroy_all_flashnode
===========================

*man iscsi_destroy_all_flashnode(9)*

*4.6.0-rc5*

destroy all flashnode session entries


Synopsis
========

.. c:function:: void iscsi_destroy_all_flashnode( struct Scsi_Host * shost )

Arguments
=========

``shost``
    pointer to host data


Description
===========

Destroys all the flashnode session entries and all corresponding
children flashnode connection entries from sysfs


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
