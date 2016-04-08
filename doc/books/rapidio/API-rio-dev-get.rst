
.. _API-rio-dev-get:

===========
rio_dev_get
===========

*man rio_dev_get(9)*

*4.6.0-rc1*

Increments the reference count of the RIO device structure


Synopsis
========

.. c:function:: struct rio_dev ⋆ rio_dev_get( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device being referenced


Description
===========

Each live reference to a device should be refcounted.

Drivers for RIO devices should normally record such references in their ``probe`` methods, when they bind to a device, and release them by calling ``rio_dev_put``, in their
``disconnect`` methods.
