
.. _API-fence-put:

=========
fence_put
=========

*man fence_put(9)*

*4.6.0-rc1*

decreases refcount of the fence


Synopsis
========

.. c:function:: void fence_put( struct fence * fence )

Arguments
=========

``fence``
    [in] fence to reduce refcount of
