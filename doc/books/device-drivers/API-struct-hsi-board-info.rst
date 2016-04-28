.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-hsi-board-info:

=====================
struct hsi_board_info
=====================

*man struct hsi_board_info(9)*

*4.6.0-rc5*

HSI client board info


Synopsis
========

.. code-block:: c

    struct hsi_board_info {
      const char * name;
      unsigned int hsi_id;
      unsigned int port;
      struct hsi_config tx_cfg;
      struct hsi_config rx_cfg;
      void * platform_data;
      struct dev_archdata * archdata;
    };


Members
=======

name
    Name for the HSI device

hsi_id
    HSI controller id where the client sits

port
    Port number in the controller where the client sits

tx_cfg
    HSI TX configuration

rx_cfg
    HSI RX configuration

platform_data
    Platform related data

archdata
    Architecture-dependent device data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
