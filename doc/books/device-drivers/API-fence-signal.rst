
.. _API-fence-signal:

============
fence_signal
============

*man fence_signal(9)*

*4.6.0-rc1*

signal completion of a fence


Synopsis
========

.. c:function:: int fence_signal( struct fence * fence )

Arguments
=========

``fence``
    the fence to signal


Description
===========

Signal completion for software callbacks on a fence, this will unblock ``fence_wait`` calls and run all the callbacks added with ``fence_add_callback``. Can be called multiple
times, but since a fence can only go from unsignaled to signaled state, it will only be effective the first time.
