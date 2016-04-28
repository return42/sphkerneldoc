.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-enable-rx-tx-port:

=====================
rio_enable_rx_tx_port
=====================

*man rio_enable_rx_tx_port(9)*

*4.6.0-rc5*

enable input receiver and output transmitter of given port


Synopsis
========

.. c:function:: int rio_enable_rx_tx_port( struct rio_mport * port, int local, u16 destid, u8 hopcount, u8 port_num )

Arguments
=========

``port``
    Master port associated with the RIO network

``local``
    local=1 select local port otherwise a far device is reached

``destid``
    Destination ID of the device to check host bit

``hopcount``
    Number of hops to reach the target

``port_num``
    Port (-number on switch) to enable on a far end device


Description
===========

Returns 0 or 1 from on General Control Command and Status Register
(EXT_PTR+0x3C)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
