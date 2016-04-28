.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-hsi-client-driver:

========================
struct hsi_client_driver
========================

*man struct hsi_client_driver(9)*

*4.6.0-rc5*

Driver associated to an HSI client


Synopsis
========

.. code-block:: c

    struct hsi_client_driver {
      struct device_driver driver;
    };


Members
=======

driver
    Driver model representation of the driver


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
