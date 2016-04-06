
.. _API-iscsi-create-session:

====================
iscsi_create_session
====================

*man iscsi_create_session(9)*

*4.6.0-rc1*

create iscsi class session


Synopsis
========

.. c:function:: struct iscsi_cls_session ⋆ iscsi_create_session( struct Scsi_Host * shost, struct iscsi_transport * transport, int dd_size, unsigned int target_id )

Arguments
=========

``shost``
    scsi host

``transport``
    iscsi transport

``dd_size``
    private driver data size

``target_id``
    which target


Description
===========

This can be called from a LLD or iscsi_transport.
