
.. _API-fc-remote-port-rolechg:

======================
fc_remote_port_rolechg
======================

*man fc_remote_port_rolechg(9)*

*4.6.0-rc1*

notifies the fc transport that the roles on a remote may have changed.


Synopsis
========

.. c:function:: void fc_remote_port_rolechg( struct fc_rport * rport, u32 roles )

Arguments
=========

``rport``
    The remote port that changed.

``roles``
    New roles for this port.


Description
===========

The LLDD calls this routine to notify the transport that the roles on a remote port may have changed. The largest effect of this is if a port now becomes a FCP Target, it must be
allocated a scsi target id. If the port is no longer a FCP target, any scsi target id value assigned to it will persist in case the role changes back to include FCP Target. No
changes in the scsi midlayer will be invoked if the role changes (in the expectation that the role will be resumed. If it doesn't normal error processing will take place).

Should not be called from interrupt context.


Notes
=====

This routine assumes no locks are held on entry.
