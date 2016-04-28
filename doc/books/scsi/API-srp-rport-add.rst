.. -*- coding: utf-8; mode: rst -*-

.. _API-srp-rport-add:

=============
srp_rport_add
=============

*man srp_rport_add(9)*

*4.6.0-rc5*

add a SRP remote port to the device hierarchy


Synopsis
========

.. c:function:: struct srp_rport * srp_rport_add( struct Scsi_Host * shost, struct srp_rport_identifiers * ids )

Arguments
=========

``shost``
    scsi host the remote port is connected to.

``ids``
    The port id for the remote port.


Description
===========

Publishes a port to the rest of the system.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
