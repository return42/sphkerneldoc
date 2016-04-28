.. -*- coding: utf-8; mode: rst -*-

.. _API-genphy-update-link:

==================
genphy_update_link
==================

*man genphy_update_link(9)*

*4.6.0-rc5*

update link status in ``phydev``


Synopsis
========

.. c:function:: int genphy_update_link( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Update the value in phydev->link to reflect the current link value. In
order to do this, we need to read the status register twice, keeping the
second value.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
