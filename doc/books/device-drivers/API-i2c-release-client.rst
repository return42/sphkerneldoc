
.. _API-i2c-release-client:

==================
i2c_release_client
==================

*man i2c_release_client(9)*

*4.6.0-rc1*

release a use of the i2c client structure


Synopsis
========

.. c:function:: void i2c_release_client( struct i2c_client * client )

Arguments
=========

``client``
    the client being no longer referenced


Description
===========

Must be called when a user of a client is finished with it.
