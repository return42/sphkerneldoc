
.. _API-fence-later:

===========
fence_later
===========

*man fence_later(9)*

*4.6.0-rc1*

return the chronologically later fence


Synopsis
========

.. c:function:: struct fence ⋆ fence_later( struct fence * f1, struct fence * f2 )

Arguments
=========

``f1``
    [in] the first fence from the same context

``f2``
    [in] the second fence from the same context


Description
===========

Returns NULL if both fences are signaled, otherwise the fence that would be signaled last. Both fences must be from the same context, since a seqno is not re-used across contexts.
