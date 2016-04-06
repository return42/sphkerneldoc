
.. _API-srp-stop-rport-timers:

=====================
srp_stop_rport_timers
=====================

*man srp_stop_rport_timers(9)*

*4.6.0-rc1*

stop the transport layer recovery timers


Synopsis
========

.. c:function:: void srp_stop_rport_timers( struct srp_rport * rport )

Arguments
=========

``rport``
    SRP remote port for which to stop the timers.


Description
===========

Must be called after ``srp_remove_host`` and ``scsi_remove_host``. The caller must hold a reference on the rport (rport->dev) and on the SCSI host (rport->dev.parent).
