
.. _API-wiphy-rfkill-set-hw-state:

=========================
wiphy_rfkill_set_hw_state
=========================

*man wiphy_rfkill_set_hw_state(9)*

*4.6.0-rc1*

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
