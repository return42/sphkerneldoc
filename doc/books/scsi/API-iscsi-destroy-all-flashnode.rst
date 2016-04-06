
.. _API-iscsi-destroy-all-flashnode:

===========================
iscsi_destroy_all_flashnode
===========================

*man iscsi_destroy_all_flashnode(9)*

*4.6.0-rc1*

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

Destroys all the flashnode session entries and all corresponding children flashnode connection entries from sysfs
