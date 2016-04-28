.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-hsi-port:

===============
struct hsi_port
===============

*man struct hsi_port(9)*

*4.6.0-rc5*

HSI port device


Synopsis
========

.. code-block:: c

    struct hsi_port {
      struct device device;
      struct hsi_config tx_cfg;
      struct hsi_config rx_cfg;
      unsigned int num;
      unsigned int shared:1;
      int claimed;
      struct mutex lock;
      int (* async) (struct hsi_msg *msg);
      int (* setup) (struct hsi_client *cl);
      int (* flush) (struct hsi_client *cl);
      int (* start_tx) (struct hsi_client *cl);
      int (* stop_tx) (struct hsi_client *cl);
      int (* release) (struct hsi_client *cl);
      struct atomic_notifier_head n_head;
    };


Members
=======

device
    Driver model representation of the device

tx_cfg
    Current TX path configuration

rx_cfg
    Current RX path configuration

num
    Port number

shared
    Set when port can be shared by different clients

claimed
    Reference count of clients which claimed the port

lock
    Serialize port claim

async
    Asynchronous transfer callback

setup
    Callback to set the HSI client configuration

flush
    Callback to clean the HW state and destroy all pending transfers

start_tx
    Callback to inform that a client wants to TX data

stop_tx
    Callback to inform that a client no longer wishes to TX data

release
    Callback to inform that a client no longer uses the port

n_head
    Notifier chain for signaling port events to the clients.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
