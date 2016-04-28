.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-msleep:

==========
ata_msleep
==========

*man ata_msleep(9)*

*4.6.0-rc5*

ATA EH owner aware msleep


Synopsis
========

.. c:function:: void ata_msleep( struct ata_port * ap, unsigned int msecs )

Arguments
=========

``ap``
    ATA port to attribute the sleep to

``msecs``
    duration to sleep in milliseconds


Description
===========

Sleeps ``msecs``. If the current task is owner of ``ap``'s EH, the
ownership is released before going to sleep and reacquired after the
sleep is complete. IOW, other ports sharing the ``ap``->host will be
allowed to own the EH while this task is sleeping.


LOCKING
=======

Might sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
