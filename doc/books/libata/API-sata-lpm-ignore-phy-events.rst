.. -*- coding: utf-8; mode: rst -*-

.. _API-sata-lpm-ignore-phy-events:

==========================
sata_lpm_ignore_phy_events
==========================

*man sata_lpm_ignore_phy_events(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
