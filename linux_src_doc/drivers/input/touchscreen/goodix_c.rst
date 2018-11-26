.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/touchscreen/goodix.c

.. _`goodix_i2c_read`:

goodix_i2c_read
===============

.. c:function:: int goodix_i2c_read(struct i2c_client *client, u16 reg, u8 *buf, int len)

    read data from a register of the i2c slave device.

    :param client:
        i2c device.
    :type client: struct i2c_client \*

    :param reg:
        the register to read from.
    :type reg: u16

    :param buf:
        raw write data buffer.
    :type buf: u8 \*

    :param len:
        length of the buffer to write
    :type len: int

.. _`goodix_i2c_write`:

goodix_i2c_write
================

.. c:function:: int goodix_i2c_write(struct i2c_client *client, u16 reg, const u8 *buf, unsigned len)

    write data to a register of the i2c slave device.

    :param client:
        i2c device.
    :type client: struct i2c_client \*

    :param reg:
        the register to write to.
    :type reg: u16

    :param buf:
        raw data buffer to write.
    :type buf: const u8 \*

    :param len:
        length of the buffer to write
    :type len: unsigned

.. _`goodix_process_events`:

goodix_process_events
=====================

.. c:function:: void goodix_process_events(struct goodix_ts_data *ts)

    Process incoming events

    :param ts:
        our goodix_ts_data pointer
    :type ts: struct goodix_ts_data \*

.. _`goodix_process_events.description`:

Description
-----------

Called when the IRQ is triggered. Read the current device state, and push
the input events to the user space.

.. _`goodix_ts_irq_handler`:

goodix_ts_irq_handler
=====================

.. c:function:: irqreturn_t goodix_ts_irq_handler(int irq, void *dev_id)

    The IRQ handler

    :param irq:
        interrupt number.
    :type irq: int

    :param dev_id:
        private data pointer.
    :type dev_id: void \*

.. _`goodix_check_cfg`:

goodix_check_cfg
================

.. c:function:: int goodix_check_cfg(struct goodix_ts_data *ts, const struct firmware *cfg)

    Checks if config fw is valid

    :param ts:
        goodix_ts_data pointer
    :type ts: struct goodix_ts_data \*

    :param cfg:
        firmware config data
    :type cfg: const struct firmware \*

.. _`goodix_send_cfg`:

goodix_send_cfg
===============

.. c:function:: int goodix_send_cfg(struct goodix_ts_data *ts, const struct firmware *cfg)

    Write fw config to device

    :param ts:
        goodix_ts_data pointer
    :type ts: struct goodix_ts_data \*

    :param cfg:
        config firmware to write to device
    :type cfg: const struct firmware \*

.. _`goodix_reset`:

goodix_reset
============

.. c:function:: int goodix_reset(struct goodix_ts_data *ts)

    Reset device during power on

    :param ts:
        goodix_ts_data pointer
    :type ts: struct goodix_ts_data \*

.. _`goodix_get_gpio_config`:

goodix_get_gpio_config
======================

.. c:function:: int goodix_get_gpio_config(struct goodix_ts_data *ts)

    Get GPIO config from ACPI/DT

    :param ts:
        goodix_ts_data pointer
    :type ts: struct goodix_ts_data \*

.. _`goodix_read_config`:

goodix_read_config
==================

.. c:function:: void goodix_read_config(struct goodix_ts_data *ts)

    Read the embedded configuration of the panel

    :param ts:
        our goodix_ts_data pointer
    :type ts: struct goodix_ts_data \*

.. _`goodix_read_config.description`:

Description
-----------

Must be called during probe

.. _`goodix_read_version`:

goodix_read_version
===================

.. c:function:: int goodix_read_version(struct goodix_ts_data *ts)

    Read goodix touchscreen version

    :param ts:
        our goodix_ts_data pointer
    :type ts: struct goodix_ts_data \*

.. _`goodix_i2c_test`:

goodix_i2c_test
===============

.. c:function:: int goodix_i2c_test(struct i2c_client *client)

    I2C test function to check if the device answers.

    :param client:
        the i2c client
    :type client: struct i2c_client \*

.. _`goodix_configure_dev`:

goodix_configure_dev
====================

.. c:function:: int goodix_configure_dev(struct goodix_ts_data *ts)

    Finish device initialization

    :param ts:
        our goodix_ts_data pointer
    :type ts: struct goodix_ts_data \*

.. _`goodix_configure_dev.description`:

Description
-----------

Must be called from probe to finish initialization of the device.
Contains the common initialization code for both devices that
declare gpio pins and devices that do not. It is either called
directly from probe or from request_firmware_wait callback.

.. _`goodix_config_cb`:

goodix_config_cb
================

.. c:function:: void goodix_config_cb(const struct firmware *cfg, void *ctx)

    Callback to finish device init

    :param cfg:
        *undescribed*
    :type cfg: const struct firmware \*

    :param ctx:
        *undescribed*
    :type ctx: void \*

.. _`goodix_config_cb.description`:

Description
-----------

request_firmware_wait callback that finishes
initialization of the device.

.. This file was automatic generated / don't edit.

