.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-host-suspend:

================
ata_host_suspend
================

*man ata_host_suspend(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
