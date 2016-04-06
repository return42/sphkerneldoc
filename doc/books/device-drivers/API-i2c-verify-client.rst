
.. _API-i2c-verify-client:

=================
i2c_verify_client
=================

*man i2c_verify_client(9)*

*4.6.0-rc1*

return parameter as i2c_client, or NULL


Synopsis
========

.. c:function:: struct i2c_client ⋆ i2c_verify_client( struct device * dev )

Arguments
=========

``dev``
    device, probably from some driver model iterator


Description
===========

When traversing the driver model tree, perhaps using driver model iterators like ``device_for_each_child``\ (), you can't assume very much about the nodes you find. Use this
function to avoid oopses caused by wrongly treating some non-I2C device as an i2c_client.
