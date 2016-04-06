
.. _API-fence-add-callback:

==================
fence_add_callback
==================

*man fence_add_callback(9)*

*4.6.0-rc1*

add a callback to be called when the fence is signaled


Synopsis
========

.. c:function:: int fence_add_callback( struct fence * fence, struct fence_cb * cb, fence_func_t func )

Arguments
=========

``fence``
    [in] the fence to wait on

``cb``
    [in] the callback to register

``func``
    [in] the function to call


Description
===========

cb will be initialized by fence_add_callback, no initialization by the caller is required. Any number of callbacks can be registered to a fence, but a callback can only be
registered to one fence at a time.

Note that the callback can be called from an atomic context. If fence is already signaled, this function will return -ENOENT (and ⋆not⋆ call the callback)

Add a software callback to the fence. Same restrictions apply to refcount as it does to fence_wait, however the caller doesn't need to


keep a refcount to fence afterwards
===================================

when software access is enabled, the creator of the fence is required to keep the fence alive until after it signals with fence_signal. The callback itself can be called from irq
context.
