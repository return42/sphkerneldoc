
.. _API-scsi-host-set-state:

===================
scsi_host_set_state
===================

*man scsi_host_set_state(9)*

*4.6.0-rc1*

Take the given host through the host state model.


Synopsis
========

.. c:function:: int scsi_host_set_state( struct Scsi_Host * shost, enum scsi_host_state state )

Arguments
=========

``shost``
    scsi host to change the state of.

``state``
    state to change to.


Description
===========

Returns zero if unsuccessful or an error if the requested transition is illegal.
