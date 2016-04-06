
.. _API-iscsi-destroy-flashnode-sess:

============================
iscsi_destroy_flashnode_sess
============================

*man iscsi_destroy_flashnode_sess(9)*

*4.6.0-rc1*

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

Deletes the flashnode session entry and all children flashnode connection entries from sysfs
