.. -*- coding: utf-8; mode: rst -*-

.. _API-fence-is-signaled:

=================
fence_is_signaled
=================

*man fence_is_signaled(9)*

*4.6.0-rc5*

Return an indication if the fence is signaled yet.


Synopsis
========

.. c:function:: bool fence_is_signaled( struct fence * fence )

Arguments
=========

``fence``
    [in] the fence to check


Description
===========

Returns true if the fence was already signaled, false if not. Since this
function doesn't enable signaling, it is not guaranteed to ever return
true if fence_add_callback, fence_wait or
fence_enable_sw_signaling haven't been called before.

It's recommended for seqno fences to call fence_signal when the
operation is complete, it makes it possible to prevent issues from
wraparound between time of issue and time of use by checking the return
value of this function before calling hardware-specific wait
instructions.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
