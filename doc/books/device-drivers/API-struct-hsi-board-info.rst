
.. _API-struct-hsi-board-info:

=====================
struct hsi_board_info
=====================

*man struct hsi_board_info(9)*

*4.6.0-rc1*

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
