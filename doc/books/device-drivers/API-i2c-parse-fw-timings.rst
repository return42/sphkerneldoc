.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-parse-fw-timings:

====================
i2c_parse_fw_timings
====================

*man i2c_parse_fw_timings(9)*

*4.6.0-rc5*

get I2C related timing parameters from firmware


Synopsis
========

.. c:function:: void i2c_parse_fw_timings( struct device * dev, struct i2c_timings * t, bool use_defaults )

Arguments
=========

``dev``
    The device to scan for I2C timing properties

``t``
    the i2c_timings struct to be filled with values

``use_defaults``
    bool to use sane defaults derived from the I2C specification when
    properties are not found, otherwise use 0


Description
===========

Scan the device for the generic I2C properties describing timing
parameters for the signal and fill the given struct with the results. If
a property was not found and use_defaults was true, then maximum
timings are assumed which are derived from the I2C specification. If
use_defaults is not used, the results will be 0, so drivers can apply
their own defaults later. The latter is mainly intended for avoiding
regressions of existing drivers which want to switch to this function.
New drivers almost always should use the defaults.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
