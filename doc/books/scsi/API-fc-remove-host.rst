
.. _API-fc-remove-host:

==============
fc_remove_host
==============

*man fc_remove_host(9)*

*4.6.0-rc1*

called to terminate any fc_transport-related elements for a scsi host.


Synopsis
========

.. c:function:: void fc_remove_host( struct Scsi_Host * shost )

Arguments
=========

``shost``
    Which ``Scsi_Host``


Description
===========

This routine is expected to be called immediately preceding the a driver's call to ``scsi_remove_host``.


WARNING
=======

A driver utilizing the fc_transport, which fails to call this routine prior to ``scsi_remove_host``, will leave dangling objects in /sys/class/fc_remote_ports. Access to any of
these objects can result in a system crash !!!


Notes
=====

This routine assumes no locks are held on entry.
