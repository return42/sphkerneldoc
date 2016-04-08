
.. _API-ata-msense-ctl-mode:

===================
ata_msense_ctl_mode
===================

*man ata_msense_ctl_mode(9)*

*4.6.0-rc1*

Simulate MODE SENSE control mode page


Synopsis
========

.. c:function:: unsigned int ata_msense_ctl_mode( u8 * buf, bool changeable )

Arguments
=========

``buf``
    output buffer

``changeable``
    whether changeable parameters are requested


Description
===========

Generate a generic MODE SENSE control mode page.


LOCKING
=======

None.
