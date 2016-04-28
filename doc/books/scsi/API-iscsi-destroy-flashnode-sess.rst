.. -*- coding: utf-8; mode: rst -*-

.. _API-iscsi-destroy-flashnode-sess:

============================
iscsi_destroy_flashnode_sess
============================

*man iscsi_destroy_flashnode_sess(9)*

*4.6.0-rc5*

destroy flashnode session entry


Synopsis
========

.. c:function:: void iscsi_destroy_flashnode_sess( struct iscsi_bus_flash_session * fnode_sess )

Arguments
=========

``fnode_sess``
    pointer to flashnode session entry to be destroyed


Description
===========

Deletes the flashnode session entry and all children flashnode
connection entries from sysfs


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
