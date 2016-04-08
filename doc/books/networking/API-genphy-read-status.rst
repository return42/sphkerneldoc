
.. _API-genphy-read-status:

==================
genphy_read_status
==================

*man genphy_read_status(9)*

*4.6.0-rc1*

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

Check the link, then figure out the current state by comparing what we advertise with what the link partner advertises. Start by checking the gigabit possibilities, then move on to
10/100.
