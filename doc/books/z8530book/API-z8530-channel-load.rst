.. -*- coding: utf-8; mode: rst -*-

.. _API-z8530-channel-load:

==================
z8530_channel_load
==================

*man z8530_channel_load(9)*

*4.6.0-rc5*

Load channel data


Synopsis
========

.. c:function:: int z8530_channel_load( struct z8530_channel * c, u8 * rtable )

Arguments
=========

``c``
    Z8530 channel to configure

``rtable``
    table of register, value pairs


FIXME
=====

ioctl to allow user uploaded tables

Load a Z8530 channel up from the system data. We use +16 to indicate the
“prime” registers. The value 255 terminates the table.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
