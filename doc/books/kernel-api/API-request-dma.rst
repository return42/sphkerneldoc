
.. _API-request-dma:

===========
request_dma
===========

*man request_dma(9)*

*4.6.0-rc1*

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
