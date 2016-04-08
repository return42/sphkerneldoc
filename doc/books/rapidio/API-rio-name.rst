
.. _API-rio-name:

========
rio_name
========

*man rio_name(9)*

*4.6.0-rc1*

Get the unique RIO device identifier


Synopsis
========

.. c:function:: const char ⋆ rio_name( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device


Description
===========

Get the unique RIO device identifier. Returns the device identifier string.
