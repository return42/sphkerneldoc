.. -*- coding: utf-8; mode: rst -*-

.. _API-set-wiphy-dev:

=============
set_wiphy_dev
=============

*man set_wiphy_dev(9)*

*4.6.0-rc5*

set device pointer for wiphy


Synopsis
========

.. c:function:: void set_wiphy_dev( struct wiphy * wiphy, struct device * dev )

Arguments
=========

``wiphy``
    The wiphy whose device to bind

``dev``
    The device to parent it to


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
