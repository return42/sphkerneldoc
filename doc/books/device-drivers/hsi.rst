.. -*- coding: utf-8; mode: rst -*-

.. _hsi:

=============================================
High Speed Synchronous Serial Interface (HSI)
=============================================

High Speed Synchronous Serial Interface (HSI) is a serial interface
mainly used for connecting application engines (APE) with cellular modem
engines (CMT) in cellular handsets. HSI provides multiplexing for up to
16 logical channels, low-latency and full duplex communication.


.. kernel-doc:: include/linux/hsi/hsi.h
    :internal:

.. kernel-doc:: drivers/hsi/hsi.c
    :export:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
