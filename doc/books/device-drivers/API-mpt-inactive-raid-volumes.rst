.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-inactive-raid-volumes:

=========================
mpt_inactive_raid_volumes
=========================

*man mpt_inactive_raid_volumes(9)*

*4.6.0-rc5*

sets up link list of phy_disk_nums for devices belonging in an
inactive volume


Synopsis
========

.. c:function:: void mpt_inactive_raid_volumes( MPT_ADAPTER * ioc, u8 channel, u8 id )

Arguments
=========

``ioc``
    pointer to per adapter structure

``channel``
    volume channel

``id``
    volume target id


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
