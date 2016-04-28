.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-create-media-graph:

======================
dvb_create_media_graph
======================

*man dvb_create_media_graph(9)*

*4.6.0-rc5*

Creates media graph for the Digital TV part of the device.


Synopsis
========

.. c:function:: int dvb_create_media_graph( struct dvb_adapter * adap, bool create_rf_connector )

Arguments
=========

``adap``
    pointer to struct dvb_adapter

``create_rf_connector``
    if true, it creates the RF connector too


Description
===========

This function checks all DVB-related functions at the media controller
entities and creates the needed links for the media graph. It is capable
of working with multiple tuners or multiple frontends, but it won't
create links if the device has multiple tuners and multiple frontends or
if the device has multiple muxes. In such case, the caller driver should
manually create the remaining links.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
