.. -*- coding: utf-8; mode: rst -*-

.. _API-request-dma:

===========
request_dma
===========

*man request_dma(9)*

*4.6.0-rc5*

request and reserve a system DMA channel


Synopsis
========

.. c:function:: int request_dma( unsigned int dmanr, const char * device_id )

Arguments
=========

``dmanr``
    DMA channel number

``device_id``
    reserving device ID string, used in /proc/dma


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
