
.. _API-sata-lpm-ignore-phy-events:

==========================
sata_lpm_ignore_phy_events
==========================

*man sata_lpm_ignore_phy_events(9)*

*4.6.0-rc1*

test if PHY event should be ignored


Synopsis
========

.. c:function:: bool sata_lpm_ignore_phy_events( struct ata_link * link )

Arguments
=========

``link``
    Link receiving the event


Description
===========

Test whether the received PHY event has to be ignored or not.


RETURNS
=======

True if the event has to be ignored.
