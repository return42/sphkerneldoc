
.. _API-fence-remove-callback:

=====================
fence_remove_callback
=====================

*man fence_remove_callback(9)*

*4.6.0-rc1*

remove a callback from the signaling list


Synopsis
========

.. c:function:: bool fence_remove_callback( struct fence * fence, struct fence_cb * cb )

Arguments
=========

``fence``
    [in] the fence to wait on

``cb``
    [in] the callback to remove


Description
===========

Remove a previously queued callback from the fence. This function returns true if the callback is successfully removed, or false if the fence has already been signaled.

⋆WARNING⋆: Cancelling a callback should only be done if you really know what you're doing, since deadlocks and race conditions could occur all too easily. For this reason, it
should only ever be done on hardware lockup recovery, with a reference held to the fence.
