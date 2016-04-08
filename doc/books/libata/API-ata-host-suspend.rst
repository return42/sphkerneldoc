
.. _API-ata-host-suspend:

================
ata_host_suspend
================

*man ata_host_suspend(9)*

*4.6.0-rc1*

suspend host


Synopsis
========

.. c:function:: int ata_host_suspend( struct ata_host * host, pm_message_t mesg )

Arguments
=========

``host``
    host to suspend

``mesg``
    PM message


Description
===========

Suspend ``host``. Actual operation is performed by port suspend.
