
.. _API-rio-dev-put:

===========
rio_dev_put
===========

*man rio_dev_put(9)*

*4.6.0-rc1*

Release a use of the RIO device structure


Synopsis
========

.. c:function:: void rio_dev_put( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device being disconnected


Description
===========

Must be called when a user of a device is finished with it. When the last user of the device calls this function, the memory of the device is freed.
