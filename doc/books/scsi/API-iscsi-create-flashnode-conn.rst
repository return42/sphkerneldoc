
.. _API-iscsi-create-flashnode-conn:

===========================
iscsi_create_flashnode_conn
===========================

*man iscsi_create_flashnode_conn(9)*

*4.6.0-rc1*

Add flashnode conn entry in sysfs


Synopsis
========

.. c:function:: struct iscsi_bus_flash_conn ⋆ iscsi_create_flashnode_conn( struct Scsi_Host * shost, struct iscsi_bus_flash_session * fnode_sess, struct iscsi_transport * transport, int dd_size )

Arguments
=========

``shost``
    pointer to host data

``fnode_sess``
    pointer to the parent flashnode session entry

``transport``
    pointer to transport data

``dd_size``
    total size to allocate


Description
===========

Adds a sysfs entry for the flashnode connection attributes


Returns
=======

pointer to allocated flashnode conn on success ``NULL`` on failure
