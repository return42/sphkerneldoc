.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-verify-client:

=================
i2c_verify_client
=================

*man i2c_verify_client(9)*

*4.6.0-rc5*

return parameter as i2c_client, or NULL


Synopsis
========

.. c:function:: struct i2c_client * i2c_verify_client( struct device * dev )

Arguments
=========

``dev``
    device, probably from some driver model iterator


Description
===========

When traversing the driver model tree, perhaps using driver model
iterators like ``device_for_each_child``\ (), you can't assume very much
about the nodes you find. Use this function to avoid oopses caused by
wrongly treating some non-I2C device as an i2c_client.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
