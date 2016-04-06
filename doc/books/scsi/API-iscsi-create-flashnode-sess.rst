
.. _API-iscsi-create-flashnode-sess:

===========================
iscsi_create_flashnode_sess
===========================

*man iscsi_create_flashnode_sess(9)*

*4.6.0-rc1*

Add flashnode session entry in sysfs


Synopsis
========

.. c:function:: struct iscsi_bus_flash_session ⋆ iscsi_create_flashnode_sess( struct Scsi_Host * shost, int index, struct iscsi_transport * transport, int dd_size )

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
