.. -*- coding: utf-8; mode: rst -*-

.. _API-wiphy-dev:

=========
wiphy_dev
=========

*man wiphy_dev(9)*

*4.6.0-rc5*

get wiphy dev pointer


Synopsis
========

.. c:function:: struct device * wiphy_dev( struct wiphy * wiphy )

Arguments
=========

``wiphy``
    The wiphy whose device struct to look up


Return
======

The dev of ``wiphy``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
