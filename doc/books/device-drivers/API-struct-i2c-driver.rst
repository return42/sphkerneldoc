
.. _API-struct-i2c-driver:

=================
struct i2c_driver
=================

*man struct i2c_driver(9)*

*4.6.0-rc1*

represent an I2C device driver


Synopsis
========

.. code-block:: c

    struct i2c_driver {
      unsigned int class;
      int (* attach_adapter) (struct i2c_adapter *);
      int (* probe) (struct i2c_client *, const struct i2c_device_id *);
      int (* remove) (struct i2c_client *);
      void (* shutdown) (struct i2c_client *);
      void (* alert) (struct i2c_client *, unsigned int data);
      int (* command) (struct i2c_client *client, unsigned int cmd, void *arg);
      struct device_driver driver;
      const struct i2c_device_id * id_table;
      int (* detect) (struct i2c_client *, struct i2c_board_info *);
      const unsigned short * address_list;
      struct list_head clients;
    };


Members
=======

class
    What kind of i2c device we instantiate (for detect)

attach_adapter
    Callback for bus addition (deprecated)

probe
    Callback for device binding

remove
    Callback for device unbinding

shutdown
    Callback for device shutdown

alert
    Alert callback, for example for the SMBus alert protocol

command
    Callback for bus-wide signaling (optional)

driver
    Device driver model driver

id_table
    List of I2C devices supported by this driver

detect
    Callback for device detection

address_list
    The I2C addresses to probe (for detect)

clients
    List of detected clients we created (for i2c-core use only)


Description
===========

The driver.owner field should be set to the module owner of this driver. The driver.name field should be set to the name of this driver.

For automatic device detection, both ``detect`` and ``address_list`` must be defined. ``class`` should also be set, otherwise only devices forced with module parameters will be
created. The detect function must fill at least the name field of the i2c_board_info structure it is handed upon successful detection, and possibly also the flags field.

If ``detect`` is missing, the driver will still work fine for enumerated devices. Detected devices simply won't be supported. This is expected for the many I2C/SMBus devices which
can't be detected reliably, and the ones which can always be enumerated in practice.

The i2c_client structure which is handed to the ``detect`` callback is not a real i2c_client. It is initialized just enough so that you can call i2c_smbus_read_byte_data and
friends on it. Don't do anything else with it. In particular, calling dev_dbg and friends on it is not allowed.
