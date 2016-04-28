.. -*- coding: utf-8; mode: rst -*-

.. _API-wiphy-rfkill-set-hw-state:

=========================
wiphy_rfkill_set_hw_state
=========================

*man wiphy_rfkill_set_hw_state(9)*

*4.6.0-rc5*

notify cfg80211 about hw block state


Synopsis
========

.. c:function:: void wiphy_rfkill_set_hw_state( struct wiphy * wiphy, bool blocked )

Arguments
=========

``wiphy``
    the wiphy

``blocked``
    block status


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
