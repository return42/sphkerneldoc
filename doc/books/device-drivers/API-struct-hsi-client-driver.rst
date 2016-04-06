
.. _API-struct-hsi-client-driver:

========================
struct hsi_client_driver
========================

*man struct hsi_client_driver(9)*

*4.6.0-rc1*

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
