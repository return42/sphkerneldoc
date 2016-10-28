.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/m5mols/m5mols_core.c

.. _`m5mols_swap_byte`:

m5mols_swap_byte
================

.. c:function:: u32 m5mols_swap_byte(u8 *data, u8 length)

    an byte array to integer conversion function

    :param u8 \*data:
        *undescribed*

    :param u8 length:
        *undescribed*

.. _`m5mols_swap_byte.description`:

Description
-----------

Convert I2C data byte array with performing any required byte
reordering to assure proper values for each data type, regardless
of the architecture endianness.

.. _`m5mols_read`:

m5mols_read
===========

.. c:function:: int m5mols_read(struct v4l2_subdev *sd, u32 size, u32 reg, u32 *val)

    I2C read function

    :param struct v4l2_subdev \*sd:
        *undescribed*

    :param u32 size:
        desired size of I2C packet

    :param u32 reg:
        combination of size, category and command for the I2C packet

    :param u32 \*val:
        read value

.. _`m5mols_read.description`:

Description
-----------

Returns 0 on success, or else negative errno.

.. _`m5mols_write`:

m5mols_write
============

.. c:function:: int m5mols_write(struct v4l2_subdev *sd, u32 reg, u32 val)

    I2C command write function

    :param struct v4l2_subdev \*sd:
        *undescribed*

    :param u32 reg:
        combination of size, category and command for the I2C packet

    :param u32 val:
        value to write

.. _`m5mols_write.description`:

Description
-----------

Returns 0 on success, or else negative errno.

.. _`m5mols_busy_wait`:

m5mols_busy_wait
================

.. c:function:: int m5mols_busy_wait(struct v4l2_subdev *sd, u32 reg, u32 value, u32 mask, int timeout)

    Busy waiting with I2C register polling

    :param struct v4l2_subdev \*sd:
        *undescribed*

    :param u32 reg:
        the \ :c:func:`I2C_REG`\  address of an 8-bit status register to check

    :param u32 value:
        expected status register value

    :param u32 mask:
        bit mask for the read status register value

    :param int timeout:
        timeout in miliseconds, or -1 for default timeout

.. _`m5mols_busy_wait.description`:

Description
-----------

The \ ``reg``\  register value is ORed with \ ``mask``\  before comparing with \ ``value``\ .

.. _`m5mols_busy_wait.return`:

Return
------

0 if the requested condition became true within less than
\ ``timeout``\  ms, or else negative errno.

.. _`m5mols_enable_interrupt`:

m5mols_enable_interrupt
=======================

.. c:function:: int m5mols_enable_interrupt(struct v4l2_subdev *sd, u8 reg)

    Clear interrupt pending bits and unmask interrupts

    :param struct v4l2_subdev \*sd:
        *undescribed*

    :param u8 reg:
        *undescribed*

.. _`m5mols_enable_interrupt.description`:

Description
-----------

Before writing desired interrupt value the INT_FACTOR register should
be read to clear pending interrupts.

.. _`m5mols_reg_mode`:

m5mols_reg_mode
===============

.. c:function:: int m5mols_reg_mode(struct v4l2_subdev *sd, u8 mode)

    Write the mode and check busy status

    :param struct v4l2_subdev \*sd:
        *undescribed*

    :param u8 mode:
        *undescribed*

.. _`m5mols_reg_mode.description`:

Description
-----------

It always accompanies a little delay changing the M-5MOLS mode, so it is
needed checking current busy status to guarantee right mode.

.. _`m5mols_set_mode`:

m5mols_set_mode
===============

.. c:function:: int m5mols_set_mode(struct m5mols_info *info, u8 mode)

    set the M-5MOLS controller mode

    :param struct m5mols_info \*info:
        *undescribed*

    :param u8 mode:
        the required operation mode

.. _`m5mols_set_mode.description`:

Description
-----------

The commands of M-5MOLS are grouped into specific modes. Each functionality
can be guaranteed only when the sensor is operating in mode which a command
belongs to.

.. _`m5mols_get_version`:

m5mols_get_version
==================

.. c:function:: int m5mols_get_version(struct v4l2_subdev *sd)

    retrieve full revisions information of M-5MOLS

    :param struct v4l2_subdev \*sd:
        *undescribed*

.. _`m5mols_get_version.description`:

Description
-----------

The version information includes revisions of hardware and firmware,
AutoFocus alghorithm version and the version string.

.. _`__find_restype`:

__find_restype
==============

.. c:function:: enum m5mols_restype __find_restype(u32 code)

    Lookup M-5MOLS resolution type according to pixel code

    :param u32 code:
        pixel code

.. _`__find_resolution`:

__find_resolution
=================

.. c:function:: int __find_resolution(struct v4l2_subdev *sd, struct v4l2_mbus_framefmt *mf, enum m5mols_restype *type, u32 *resolution)

    Lookup preset and type of M-5MOLS's resolution

    :param struct v4l2_subdev \*sd:
        *undescribed*

    :param struct v4l2_mbus_framefmt \*mf:
        pixel format to find/negotiate the resolution preset for

    :param enum m5mols_restype \*type:
        M-5MOLS resolution type

    :param u32 \*resolution:
        M-5MOLS resolution preset register value

.. _`__find_resolution.description`:

Description
-----------

Find nearest resolution matching resolution preset and adjust mf
to supported values.

.. _`m5mols_restore_controls`:

m5mols_restore_controls
=======================

.. c:function:: int m5mols_restore_controls(struct m5mols_info *info)

    Apply current control values to the registers

    :param struct m5mols_info \*info:
        *undescribed*

.. _`m5mols_restore_controls.description`:

Description
-----------

\ :c:func:`m5mols_do_scenemode`\  handles all parameters for which there is yet no
individual control. It should be replaced at some point by setting each
control individually, in required register set up order.

.. _`m5mols_start_monitor`:

m5mols_start_monitor
====================

.. c:function:: int m5mols_start_monitor(struct m5mols_info *info)

    Start the monitor mode

    :param struct m5mols_info \*info:
        *undescribed*

.. _`m5mols_start_monitor.description`:

Description
-----------

Before applying the controls setup the resolution and frame rate
in PARAMETER mode, and then switch over to MONITOR mode.

.. _`m5mols_fw_start`:

m5mols_fw_start
===============

.. c:function:: int m5mols_fw_start(struct v4l2_subdev *sd)

    M-5MOLS internal ARM controller initialization

    :param struct v4l2_subdev \*sd:
        *undescribed*

.. _`m5mols_fw_start.description`:

Description
-----------

Execute the M-5MOLS internal ARM controller initialization sequence.
This function should be called after the supply voltage has been
applied and before any requests to the device are made.

.. _`m5mols_s_power`:

m5mols_s_power
==============

.. c:function:: int m5mols_s_power(struct v4l2_subdev *sd, int on)

    Main sensor power control function

    :param struct v4l2_subdev \*sd:
        *undescribed*

    :param int on:
        *undescribed*

.. _`m5mols_s_power.description`:

Description
-----------

To prevent breaking the lens when the sensor is powered off the Soft-Landing
algorithm is called where available. The Soft-Landing algorithm availability
dependends on the firmware provider.

.. This file was automatic generated / don't edit.

