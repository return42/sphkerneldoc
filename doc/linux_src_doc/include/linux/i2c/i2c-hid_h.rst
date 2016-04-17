.. -*- coding: utf-8; mode: rst -*-

=========
i2c-hid.h
=========


.. _`i2c_hid_platform_data`:

struct i2c_hid_platform_data
============================

.. c:type:: i2c_hid_platform_data

    used by hid over i2c implementation.


.. _`i2c_hid_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct i2c_hid_platform_data {
    u16 hid_descriptor_address;
  };


.. _`i2c_hid_platform_data.members`:

Members
-------

:``hid_descriptor_address``:
    i2c register where the HID descriptor is stored.




.. _`i2c_hid_platform_data.description`:

Description
-----------

Note that it is the responsibility of the platform driver (or the acpi 5.0
driver, or the flattened device tree) to setup the irq related to the gpio in
the struct i2c_board_info.



.. _`i2c_hid_platform_data.a-typical-example-is-the-following`:

A typical example is the following
----------------------------------

.. code-block:: c

	irq = gpio_to_irq(intr_gpio);
	hkdk4412_i2c_devs5[0].irq = irq; // store the irq in i2c_board_info
	gpio_request(intr_gpio, "elan-irq");
	s3c_gpio_setpull(intr_gpio, S3C_GPIO_PULL_UP);

