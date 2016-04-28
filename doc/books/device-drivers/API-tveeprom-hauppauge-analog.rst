.. -*- coding: utf-8; mode: rst -*-

.. _API-tveeprom-hauppauge-analog:

=========================
tveeprom_hauppauge_analog
=========================

*man tveeprom_hauppauge_analog(9)*

*4.6.0-rc5*

Fill struct tveeprom using the contents of the eeprom previously filled
at ``eeprom_data`` field.


Synopsis
========

.. c:function:: void tveeprom_hauppauge_analog( struct i2c_client * c, struct tveeprom * tvee, unsigned char * eeprom_data )

Arguments
=========

``c``
    I2C client struct

``tvee``
    Struct to where the eeprom parsed data will be filled;

``eeprom_data``
    Array with the contents of the eeprom_data. It should contain 256
    bytes filled with the contents of the eeprom read from the Hauppauge
    device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
