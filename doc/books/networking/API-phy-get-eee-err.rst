.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-get-eee-err:

===============
phy_get_eee_err
===============

*man phy_get_eee_err(9)*

*4.6.0-rc5*

report the EEE wake error count


Synopsis
========

.. c:function:: int phy_get_eee_err( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

it is to report the number of time where the PHY failed to complete its
normal wake sequence.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
