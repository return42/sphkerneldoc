.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-read-mmd-indirect:

=====================
phy_read_mmd_indirect
=====================

*man phy_read_mmd_indirect(9)*

*4.6.0-rc5*

reads data from the MMD registers


Synopsis
========

.. c:function:: int phy_read_mmd_indirect( struct phy_device * phydev, int prtad, int devad )

Arguments
=========

``phydev``
    The PHY device bus

``prtad``
    MMD Address

``devad``
    MMD DEVAD


Description
===========

it reads data from the MMD registers (clause 22 to access to clause 45)
of the specified phy address.


To read these register we have
==============================

1) Write reg 13 // DEVAD 2) Write reg 14 // MMD Address 3) Write reg 13
// MMD Data Command for MMD DEVAD 3) Read reg 14 // Read MMD data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
