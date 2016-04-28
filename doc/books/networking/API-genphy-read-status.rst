.. -*- coding: utf-8; mode: rst -*-

.. _API-genphy-read-status:

==================
genphy_read_status
==================

*man genphy_read_status(9)*

*4.6.0-rc5*

check the link status and update current link state


Synopsis
========

.. c:function:: int genphy_read_status( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Check the link, then figure out the current state by comparing what we
advertise with what the link partner advertises. Start by checking the
gigabit possibilities, then move on to 10/100.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
