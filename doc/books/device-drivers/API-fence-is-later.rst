
.. _API-fence-is-later:

==============
fence_is_later
==============

*man fence_is_later(9)*

*4.6.0-rc1*

return if f1 is chronologically later than f2


Synopsis
========

.. c:function:: bool fence_is_later( struct fence * f1, struct fence * f2 )

Arguments
=========

``f1``
    [in] the first fence from the same context

``f2``
    [in] the second fence from the same context


Description
===========

Returns true if f1 is chronologically later than f2. Both fences must be from the same context, since a seqno is not re-used across contexts.
