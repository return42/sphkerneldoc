
.. _API-ieee80211-iterate-active-interfaces:

===================================
ieee80211_iterate_active_interfaces
===================================

*man ieee80211_iterate_active_interfaces(9)*

*4.6.0-rc1*

iterate active interfaces


Synopsis
========

.. c:function:: void ieee80211_iterate_active_interfaces( struct ieee80211_hw * hw, u32 iter_flags, void (*iterator) void *data, u8 *mac, struct ieee80211_vif *vif, void * data )

Arguments
=========

``hw``
    the hardware struct of which the interfaces should be iterated over

``iter_flags``
    iteration flags, see ``enum`` ieee80211_interface_iteration_flags

``iterator``
    the iterator function to call

``data``
    first argument of the iterator function


Description
===========

This function iterates over the interfaces associated with a given hardware that are currently active and calls the callback for them. This function allows the iterator function to
sleep, when the iterator function is atomic ``ieee80211_iterate_active_interfaces_atomic`` can be used. Does not iterate over a new interface during ``add_interface``.
