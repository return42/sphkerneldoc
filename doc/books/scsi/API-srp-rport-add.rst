
.. _API-srp-rport-add:

=============
srp_rport_add
=============

*man srp_rport_add(9)*

*4.6.0-rc1*

add a SRP remote port to the device hierarchy


Synopsis
========

.. c:function:: struct srp_rport ⋆ srp_rport_add( struct Scsi_Host * shost, struct srp_rport_identifiers * ids )

Arguments
=========

``shost``
    scsi host the remote port is connected to.

``ids``
    The port id for the remote port.


Description
===========

Publishes a port to the rest of the system.
