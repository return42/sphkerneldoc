
.. _API-struct-mipi-dsi-driver:

======================
struct mipi_dsi_driver
======================

*man struct mipi_dsi_driver(9)*

*4.6.0-rc1*

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
