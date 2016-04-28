.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-hsi-client:

=================
struct hsi_client
=================

*man struct hsi_client(9)*

*4.6.0-rc5*

HSI client attached to an HSI port


Synopsis
========

.. code-block:: c

    struct hsi_client {
      struct device device;
      struct hsi_config tx_cfg;
      struct hsi_config rx_cfg;
    };


Members
=======

device
    Driver model representation of the device

tx_cfg
    HSI TX configuration

rx_cfg
    HSI RX configuration


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
