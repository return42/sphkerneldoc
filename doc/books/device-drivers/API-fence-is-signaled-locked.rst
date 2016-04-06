
.. _API-fence-is-signaled-locked:

========================
fence_is_signaled_locked
========================

*man fence_is_signaled_locked(9)*

*4.6.0-rc1*

Return an indication if the fence is signaled yet.


Synopsis
========

.. c:function:: bool fence_is_signaled_locked( struct fence * fence )

Arguments
=========

``fence``
    [in] the fence to check


Description
===========

Returns true if the fence was already signaled, false if not. Since this function doesn't enable signaling, it is not guaranteed to ever return true if fence_add_callback,
fence_wait or fence_enable_sw_signaling haven't been called before.

This function requires fence->lock to be held.
