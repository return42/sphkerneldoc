.. -*- coding: utf-8; mode: rst -*-

.. _API-wiphy-register:

==============
wiphy_register
==============

*man wiphy_register(9)*

*4.6.0-rc5*

register a wiphy with cfg80211


Synopsis
========

.. c:function:: int wiphy_register( struct wiphy * wiphy )

Arguments
=========

``wiphy``
    The wiphy to register.


Return
======

A non-negative wiphy index or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
