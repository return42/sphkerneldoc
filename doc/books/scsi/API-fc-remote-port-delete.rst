
.. _API-fc-remote-port-delete:

=====================
fc_remote_port_delete
=====================

*man fc_remote_port_delete(9)*

*4.6.0-rc1*

notifies the fc transport that a remote port is no longer in existence.


Synopsis
========

.. c:function:: void fc_remote_port_delete( struct fc_rport * rport )

Arguments
=========

``rport``
    The remote port that no longer exists


Description
===========

The LLDD calls this routine to notify the transport that a remote port is no longer part of the topology. Note: Although a port may no longer be part of the topology, it may
persist in the remote ports displayed by the fc_host. We do this under 2 conditions: 1) If the port was a scsi target, we delay its deletion by “blocking” it. This allows the port
to temporarily disappear, then reappear without disrupting the SCSI device tree attached to it. During the “blocked” period the port will still exist. 2) If the port was a scsi
target and disappears for longer than we expect, we'll delete the port and the tear down the SCSI device tree attached to it. However, we want to semi-persist the target id
assigned to that port if it eventually does exist. The port structure will remain (although with minimal information) so that the target id bindings remails.

If the remote port is not an FCP Target, it will be fully torn down and deallocated, including the fc_remote_port class device.

If the remote port is an FCP Target, the port will be placed in a temporary blocked state. From the LLDD's perspective, the rport no longer exists. From the SCSI midlayer's
perspective, the SCSI target exists, but all sdevs on it are blocked from further I/O. The following is then expected.

If the remote port does not return (signaled by a LLDD call to ``fc_remote_port_add``) within the dev_loss_tmo timeout, then the scsi target is removed - killing all outstanding
i/o and removing the scsi devices attached ot it. The port structure will be marked Not Present and be partially cleared, leaving only enough information to recognize the remote
port relative to the scsi target id binding if it later appears. The port will remain as long as there is a valid binding (e.g. until the user changes the binding type or unloads
the scsi host with the binding).

If the remote port returns within the dev_loss_tmo value (and matches according to the target id binding type), the port structure will be reused. If it is no longer a SCSI
target, the target will be torn down. If it continues to be a SCSI target, then the target will be unblocked (allowing i/o to be resumed), and a scan will be activated to ensure
that all luns are detected.

Called from normal process context only - cannot be called from interrupt.


Notes
=====

This routine assumes no locks are held on entry.
