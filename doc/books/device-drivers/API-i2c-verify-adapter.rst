
.. _API-i2c-verify-adapter:

==================
i2c_verify_adapter
==================

*man i2c_verify_adapter(9)*

*4.6.0-rc1*

return parameter as i2c_adapter or NULL


Synopsis
========

.. c:function:: struct i2c_adapter ⋆ i2c_verify_adapter( struct device * dev )

Arguments
=========

``dev``
    device, probably from some driver model iterator


Description
===========

When traversing the driver model tree, perhaps using driver model iterators like ``device_for_each_child``\ (), you can't assume very much about the nodes you find. Use this
function to avoid oopses caused by wrongly treating some non-I2C device as an i2c_adapter.
