.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/accel/mma9551_core.c

.. _`mma9551_read_config_byte`:

mma9551_read_config_byte
========================

.. c:function:: int mma9551_read_config_byte(struct i2c_client *client, u8 app_id, u16 reg, u8 *val)

    read 1 configuration byte

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param app_id:
        Application ID
    :type app_id: u8

    :param reg:
        Application register
    :type reg: u16

    :param val:
        Pointer to store value read
    :type val: u8 \*

.. _`mma9551_read_config_byte.description`:

Description
-----------

Read one configuration byte from the device using MMA955xL command format.
Commands to the MMA955xL platform consist of a write followed
by one or more reads.

.. _`mma9551_read_config_byte.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_read_config_byte.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_write_config_byte`:

mma9551_write_config_byte
=========================

.. c:function:: int mma9551_write_config_byte(struct i2c_client *client, u8 app_id, u16 reg, u8 val)

    write 1 configuration byte

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param app_id:
        Application ID
    :type app_id: u8

    :param reg:
        Application register
    :type reg: u16

    :param val:
        Value to write
    :type val: u8

.. _`mma9551_write_config_byte.description`:

Description
-----------

Write one configuration byte from the device using MMA955xL command format.
Commands to the MMA955xL platform consist of a write followed by one or
more reads.

.. _`mma9551_write_config_byte.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_write_config_byte.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_read_status_byte`:

mma9551_read_status_byte
========================

.. c:function:: int mma9551_read_status_byte(struct i2c_client *client, u8 app_id, u16 reg, u8 *val)

    read 1 status byte

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param app_id:
        Application ID
    :type app_id: u8

    :param reg:
        Application register
    :type reg: u16

    :param val:
        Pointer to store value read
    :type val: u8 \*

.. _`mma9551_read_status_byte.description`:

Description
-----------

Read one status byte from the device using MMA955xL command format.
Commands to the MMA955xL platform consist of a write followed by one or
more reads.

.. _`mma9551_read_status_byte.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_read_status_byte.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_read_config_word`:

mma9551_read_config_word
========================

.. c:function:: int mma9551_read_config_word(struct i2c_client *client, u8 app_id, u16 reg, u16 *val)

    read 1 config word

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param app_id:
        Application ID
    :type app_id: u8

    :param reg:
        Application register
    :type reg: u16

    :param val:
        Pointer to store value read
    :type val: u16 \*

.. _`mma9551_read_config_word.description`:

Description
-----------

Read one configuration word from the device using MMA955xL command format.
Commands to the MMA955xL platform consist of a write followed by one or
more reads.

.. _`mma9551_read_config_word.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_read_config_word.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_write_config_word`:

mma9551_write_config_word
=========================

.. c:function:: int mma9551_write_config_word(struct i2c_client *client, u8 app_id, u16 reg, u16 val)

    write 1 config word

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param app_id:
        Application ID
    :type app_id: u8

    :param reg:
        Application register
    :type reg: u16

    :param val:
        Value to write
    :type val: u16

.. _`mma9551_write_config_word.description`:

Description
-----------

Write one configuration word from the device using MMA955xL command format.
Commands to the MMA955xL platform consist of a write followed by one or
more reads.

.. _`mma9551_write_config_word.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_write_config_word.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_read_status_word`:

mma9551_read_status_word
========================

.. c:function:: int mma9551_read_status_word(struct i2c_client *client, u8 app_id, u16 reg, u16 *val)

    read 1 status word

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param app_id:
        Application ID
    :type app_id: u8

    :param reg:
        Application register
    :type reg: u16

    :param val:
        Pointer to store value read
    :type val: u16 \*

.. _`mma9551_read_status_word.description`:

Description
-----------

Read one status word from the device using MMA955xL command format.
Commands to the MMA955xL platform consist of a write followed by one or
more reads.

.. _`mma9551_read_status_word.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_read_status_word.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_read_config_words`:

mma9551_read_config_words
=========================

.. c:function:: int mma9551_read_config_words(struct i2c_client *client, u8 app_id, u16 reg, u8 len, u16 *buf)

    read multiple config words

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param app_id:
        Application ID
    :type app_id: u8

    :param reg:
        Application register
    :type reg: u16

    :param len:
        Length of array to read (in words)
    :type len: u8

    :param buf:
        Array of words to read
    :type buf: u16 \*

.. _`mma9551_read_config_words.description`:

Description
-----------

Read multiple configuration registers (word-sized registers).

.. _`mma9551_read_config_words.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_read_config_words.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_read_status_words`:

mma9551_read_status_words
=========================

.. c:function:: int mma9551_read_status_words(struct i2c_client *client, u8 app_id, u16 reg, u8 len, u16 *buf)

    read multiple status words

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param app_id:
        Application ID
    :type app_id: u8

    :param reg:
        Application register
    :type reg: u16

    :param len:
        Length of array to read (in words)
    :type len: u8

    :param buf:
        Array of words to read
    :type buf: u16 \*

.. _`mma9551_read_status_words.description`:

Description
-----------

Read multiple status registers (word-sized registers).

.. _`mma9551_read_status_words.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_read_status_words.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_write_config_words`:

mma9551_write_config_words
==========================

.. c:function:: int mma9551_write_config_words(struct i2c_client *client, u8 app_id, u16 reg, u8 len, u16 *buf)

    write multiple config words

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param app_id:
        Application ID
    :type app_id: u8

    :param reg:
        Application register
    :type reg: u16

    :param len:
        Length of array to write (in words)
    :type len: u8

    :param buf:
        Array of words to write
    :type buf: u16 \*

.. _`mma9551_write_config_words.description`:

Description
-----------

Write multiple configuration registers (word-sized registers).

.. _`mma9551_write_config_words.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_write_config_words.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_update_config_bits`:

mma9551_update_config_bits
==========================

.. c:function:: int mma9551_update_config_bits(struct i2c_client *client, u8 app_id, u16 reg, u8 mask, u8 val)

    update bits in register

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param app_id:
        Application ID
    :type app_id: u8

    :param reg:
        Application register
    :type reg: u16

    :param mask:
        Mask for the bits to update
    :type mask: u8

    :param val:
        Value of the bits to update
    :type val: u8

.. _`mma9551_update_config_bits.description`:

Description
-----------

Update bits in the given register using a bit mask.

.. _`mma9551_update_config_bits.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_update_config_bits.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_gpio_config`:

mma9551_gpio_config
===================

.. c:function:: int mma9551_gpio_config(struct i2c_client *client, enum mma9551_gpio_pin pin, u8 app_id, u8 bitnum, int polarity)

    configure gpio

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param pin:
        GPIO pin to configure
    :type pin: enum mma9551_gpio_pin

    :param app_id:
        Application ID
    :type app_id: u8

    :param bitnum:
        Bit number of status register being assigned to the GPIO pin.
    :type bitnum: u8

    :param polarity:
        The polarity parameter is described in section 6.2.2, page 66,
        of the Software Reference Manual.  Basically, polarity=0 means
        the interrupt line has the same value as the selected bit,
        while polarity=1 means the line is inverted.
    :type polarity: int

.. _`mma9551_gpio_config.description`:

Description
-----------

Assign a bit from an application’s status register to a specific GPIO pin.

.. _`mma9551_gpio_config.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_gpio_config.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_read_version`:

mma9551_read_version
====================

.. c:function:: int mma9551_read_version(struct i2c_client *client)

    read device version information

    :param client:
        I2C client
    :type client: struct i2c_client \*

.. _`mma9551_read_version.description`:

Description
-----------

Read version information and print device id and firmware version.

.. _`mma9551_read_version.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_read_version.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_set_device_state`:

mma9551_set_device_state
========================

.. c:function:: int mma9551_set_device_state(struct i2c_client *client, bool enable)

    sets HW power mode

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param enable:
        Use true to power on device, false to cause the device
        to enter sleep.
    :type enable: bool

.. _`mma9551_set_device_state.description`:

Description
-----------

Set power on/off for device using the Sleep/Wake Application.
When enable is true, power on chip and enable doze mode.
When enable is false, enter sleep mode (device remains in the
lowest-power mode).

.. _`mma9551_set_device_state.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_set_device_state.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_set_power_state`:

mma9551_set_power_state
=======================

.. c:function:: int mma9551_set_power_state(struct i2c_client *client, bool on)

    sets runtime PM state

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param on:
        Use true to power on device, false to power off
    :type on: bool

.. _`mma9551_set_power_state.description`:

Description
-----------

Resume or suspend the device using Runtime PM.
The device will suspend after the autosuspend delay.

.. _`mma9551_set_power_state.return`:

Return
------

0 on success, negative value on failure.

.. _`mma9551_sleep`:

mma9551_sleep
=============

.. c:function:: void mma9551_sleep(int freq)

    sleep

    :param freq:
        Application frequency
    :type freq: int

.. _`mma9551_sleep.description`:

Description
-----------

Firmware applications run at a certain frequency on the
device. Sleep for one application cycle to make sure the
application had time to run once and initialize set values.

.. _`mma9551_read_accel_chan`:

mma9551_read_accel_chan
=======================

.. c:function:: int mma9551_read_accel_chan(struct i2c_client *client, const struct iio_chan_spec *chan, int *val, int *val2)

    read accelerometer channel

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param chan:
        IIO channel
    :type chan: const struct iio_chan_spec \*

    :param val:
        Pointer to the accelerometer value read
    :type val: int \*

    :param val2:
        Unused
    :type val2: int \*

.. _`mma9551_read_accel_chan.description`:

Description
-----------

Read accelerometer value for the specified channel.

.. _`mma9551_read_accel_chan.locking-note`:

Locking note
------------

This function must be called with the device lock held.
Locking is not handled inside the function. Callers should ensure they
serialize access to the HW.

.. _`mma9551_read_accel_chan.return`:

Return
------

IIO_VAL_INT on success, negative value on failure.

.. _`mma9551_read_accel_scale`:

mma9551_read_accel_scale
========================

.. c:function:: int mma9551_read_accel_scale(int *val, int *val2)

    read accelerometer scale

    :param val:
        Pointer to the accelerometer scale (int value)
    :type val: int \*

    :param val2:
        Pointer to the accelerometer scale (micro value)
    :type val2: int \*

.. _`mma9551_read_accel_scale.description`:

Description
-----------

Read accelerometer scale.

.. _`mma9551_read_accel_scale.return`:

Return
------

IIO_VAL_INT_PLUS_MICRO.

.. _`mma9551_app_reset`:

mma9551_app_reset
=================

.. c:function:: int mma9551_app_reset(struct i2c_client *client, u32 app_mask)

    reset application

    :param client:
        I2C client
    :type client: struct i2c_client \*

    :param app_mask:
        Application to reset
    :type app_mask: u32

.. _`mma9551_app_reset.description`:

Description
-----------

Reset the given application (using the Reset/Suspend/Clear
Control Application)

.. _`mma9551_app_reset.return`:

Return
------

0 on success, negative value on failure.

.. This file was automatic generated / don't edit.

