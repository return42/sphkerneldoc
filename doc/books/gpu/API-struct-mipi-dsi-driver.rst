.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-mipi-dsi-driver:

======================
struct mipi_dsi_driver
======================

*man struct mipi_dsi_driver(9)*

*4.6.0-rc5*

DSI driver


Synopsis
========

.. code-block:: c

    struct mipi_dsi_driver {
      struct device_driver driver;
      int(* probe) (struct mipi_dsi_device *dsi);
      int(* remove) (struct mipi_dsi_device *dsi);
      void (* shutdown) (struct mipi_dsi_device *dsi);
    };


Members
=======

driver
    device driver model driver

probe
    callback for device binding

remove
    callback for device unbinding

shutdown
    called at shutdown time to quiesce the device


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
