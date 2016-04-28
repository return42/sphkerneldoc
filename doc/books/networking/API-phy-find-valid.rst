.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-find-valid:

==============
phy_find_valid
==============

*man phy_find_valid(9)*

*4.6.0-rc5*

find a PHY setting that matches the requested features mask


Synopsis
========

.. c:function:: unsigned int phy_find_valid( unsigned int idx, u32 features )

Arguments
=========

``idx``
    The first index in settings[] to search

``features``
    A mask of the valid settings


Description
===========

Returns the index of the first valid setting less than or equal to the
one pointed to by idx, as determined by the mask in features. Returns
the index of the last setting if nothing else matches.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
