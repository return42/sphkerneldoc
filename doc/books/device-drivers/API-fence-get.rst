
.. _API-fence-get:

=========
fence_get
=========

*man fence_get(9)*

*4.6.0-rc1*

increases refcount of the fence


Synopsis
========

.. c:function:: struct fence ⋆ fence_get( struct fence * fence )

Arguments
=========

``fence``
    [in] fence to increase refcount of


Description
===========

Returns the same fence, with refcount increased by 1.
