.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-register-device:

===================
dvb_register_device
===================

*man dvb_register_device(9)*

*4.6.0-rc5*

Registers a new DVB device


Synopsis
========

.. c:function:: int dvb_register_device( struct dvb_adapter * adap, struct dvb_device ** pdvbdev, const struct dvb_device * template, void * priv, int type, int demux_sink_pads )

Arguments
=========

``adap``
    pointer to struct dvb_adapter

``pdvbdev``
    pointer to the place where the new struct dvb_device will be stored

``template``
    Template used to create ``pdvbdev``;

``priv``
    private data

``type``
    type of the device: ``DVB_DEVICE_SEC``, ``DVB_DEVICE_FRONTEND``,
    ``DVB_DEVICE_DEMUX``, ``DVB_DEVICE_DVR``, ``DVB_DEVICE_CA``,
    ``DVB_DEVICE_NET``

``demux_sink_pads``
    Number of demux outputs, to be used to create the TS outputs via the
    Media Controller.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
