
.. _API-set-wiphy-dev:

=============
set_wiphy_dev
=============

*man set_wiphy_dev(9)*

*4.6.0-rc1*

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
