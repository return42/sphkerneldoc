
.. _API-fc-remote-port-add:

==================
fc_remote_port_add
==================

*man fc_remote_port_add(9)*

*4.6.0-rc1*

notify fc transport of the existence of a remote FC port.


Synopsis
========

.. c:function:: struct fc_rport ⋆ fc_remote_port_add( struct Scsi_Host * shost, int channel, struct fc_rport_identifiers * ids )

Arguments
=========

``shost``
    scsi host the remote port is connected to.

``channel``
    Channel on shost port connected to.

``ids``
    The world wide names, fc address, and FC4 port roles for the remote port.


Description
===========

The LLDD calls this routine to notify the transport of the existence of a remote port. The LLDD provides the unique identifiers (wwpn,wwn) of the port, it's FC address (port_id),
and the FC4 roles that are active for the port.

For ports that are FCP targets (aka scsi targets), the FC transport maintains consistent target id bindings on behalf of the LLDD. A consistent target id binding is an assignment
of a target id to a remote port identifier, which persists while the scsi host is attached. The remote port can disappear, then later reappear, and it's target id assignment
remains the same. This allows for shifts in FC addressing (if binding by wwpn or wwnn) with no apparent changes to the scsi subsystem which is based on scsi host number and target
id values. Bindings are only valid during the attachment of the scsi host. If the host detaches, then later re-attaches, target id bindings may change.

This routine is responsible for returning a remote port structure. The routine will search the list of remote ports it maintains internally on behalf of consistent target id
mappings. If found, the remote port structure will be reused. Otherwise, a new remote port structure will be allocated.

Whenever a remote port is allocated, a new fc_remote_port class device is created.

Should not be called from interrupt context.


Notes
=====

This routine assumes no locks are held on entry.
