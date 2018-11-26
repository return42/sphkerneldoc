.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_dp_dual_mode_helper.c

.. _`dp-dual-mode-helpers`:

dp dual mode helpers
====================

Helper functions to deal with DP dual mode (aka. DP++) adaptors.

Type 1:
Adaptor registers (if any) and the sink DDC bus may be accessed via I2C.

Type 2:
Adaptor registers and sink DDC bus can be accessed either via I2C or
I2C-over-AUX. Source devices may choose to implement either of these
access methods.

.. _`drm_dp_dual_mode_read`:

drm_dp_dual_mode_read
=====================

.. c:function:: ssize_t drm_dp_dual_mode_read(struct i2c_adapter *adapter, u8 offset, void *buffer, size_t size)

    Read from the DP dual mode adaptor register(s)

    :param adapter:
        I2C adapter for the DDC bus
    :type adapter: struct i2c_adapter \*

    :param offset:
        register offset
    :type offset: u8

    :param buffer:
        buffer for return data
    :type buffer: void \*

    :param size:
        sizo of the buffer
    :type size: size_t

.. _`drm_dp_dual_mode_read.description`:

Description
-----------

Reads \ ``size``\  bytes from the DP dual mode adaptor registers
starting at \ ``offset``\ .

.. _`drm_dp_dual_mode_read.return`:

Return
------

0 on success, negative error code on failure

.. _`drm_dp_dual_mode_write`:

drm_dp_dual_mode_write
======================

.. c:function:: ssize_t drm_dp_dual_mode_write(struct i2c_adapter *adapter, u8 offset, const void *buffer, size_t size)

    Write to the DP dual mode adaptor register(s)

    :param adapter:
        I2C adapter for the DDC bus
    :type adapter: struct i2c_adapter \*

    :param offset:
        register offset
    :type offset: u8

    :param buffer:
        buffer for write data
    :type buffer: const void \*

    :param size:
        sizo of the buffer
    :type size: size_t

.. _`drm_dp_dual_mode_write.description`:

Description
-----------

Writes \ ``size``\  bytes to the DP dual mode adaptor registers
starting at \ ``offset``\ .

.. _`drm_dp_dual_mode_write.return`:

Return
------

0 on success, negative error code on failure

.. _`drm_dp_dual_mode_detect`:

drm_dp_dual_mode_detect
=======================

.. c:function:: enum drm_dp_dual_mode_type drm_dp_dual_mode_detect(struct i2c_adapter *adapter)

    Identify the DP dual mode adaptor

    :param adapter:
        I2C adapter for the DDC bus
    :type adapter: struct i2c_adapter \*

.. _`drm_dp_dual_mode_detect.description`:

Description
-----------

Attempt to identify the type of the DP dual mode adaptor used.

Note that when the answer is \ ``DRM_DP_DUAL_MODE_UNKNOWN``\  it's not
certain whether we're dealing with a native HDMI port or
a type 1 DVI dual mode adaptor. The driver will have to use
some other hardware/driver specific mechanism to make that
distinction.

.. _`drm_dp_dual_mode_detect.return`:

Return
------

The type of the DP dual mode adaptor used

.. _`drm_dp_dual_mode_max_tmds_clock`:

drm_dp_dual_mode_max_tmds_clock
===============================

.. c:function:: int drm_dp_dual_mode_max_tmds_clock(enum drm_dp_dual_mode_type type, struct i2c_adapter *adapter)

    Max TMDS clock for DP dual mode adaptor

    :param type:
        DP dual mode adaptor type
    :type type: enum drm_dp_dual_mode_type

    :param adapter:
        I2C adapter for the DDC bus
    :type adapter: struct i2c_adapter \*

.. _`drm_dp_dual_mode_max_tmds_clock.description`:

Description
-----------

Determine the max TMDS clock the adaptor supports based on the
type of the dual mode adaptor and the DP_DUAL_MODE_MAX_TMDS_CLOCK
register (on type2 adaptors). As some type 1 adaptors have
problems with registers (see comments in \ :c:func:`drm_dp_dual_mode_detect`\ )
we don't read the register on those, instead we simply assume
a 165 MHz limit based on the specification.

.. _`drm_dp_dual_mode_max_tmds_clock.return`:

Return
------

Maximum supported TMDS clock rate for the DP dual mode adaptor in kHz.

.. _`drm_dp_dual_mode_get_tmds_output`:

drm_dp_dual_mode_get_tmds_output
================================

.. c:function:: int drm_dp_dual_mode_get_tmds_output(enum drm_dp_dual_mode_type type, struct i2c_adapter *adapter, bool *enabled)

    Get the state of the TMDS output buffers in the DP dual mode adaptor

    :param type:
        DP dual mode adaptor type
    :type type: enum drm_dp_dual_mode_type

    :param adapter:
        I2C adapter for the DDC bus
    :type adapter: struct i2c_adapter \*

    :param enabled:
        current state of the TMDS output buffers
    :type enabled: bool \*

.. _`drm_dp_dual_mode_get_tmds_output.description`:

Description
-----------

Get the state of the TMDS output buffers in the adaptor. For
type2 adaptors this is queried from the DP_DUAL_MODE_TMDS_OEN
register. As some type 1 adaptors have problems with registers
(see comments in \ :c:func:`drm_dp_dual_mode_detect`\ ) we don't read the
register on those, instead we simply assume that the buffers
are always enabled.

.. _`drm_dp_dual_mode_get_tmds_output.return`:

Return
------

0 on success, negative error code on failure

.. _`drm_dp_dual_mode_set_tmds_output`:

drm_dp_dual_mode_set_tmds_output
================================

.. c:function:: int drm_dp_dual_mode_set_tmds_output(enum drm_dp_dual_mode_type type, struct i2c_adapter *adapter, bool enable)

    Enable/disable TMDS output buffers in the DP dual mode adaptor

    :param type:
        DP dual mode adaptor type
    :type type: enum drm_dp_dual_mode_type

    :param adapter:
        I2C adapter for the DDC bus
    :type adapter: struct i2c_adapter \*

    :param enable:
        enable (as opposed to disable) the TMDS output buffers
    :type enable: bool

.. _`drm_dp_dual_mode_set_tmds_output.description`:

Description
-----------

Set the state of the TMDS output buffers in the adaptor. For
type2 this is set via the DP_DUAL_MODE_TMDS_OEN register. As
some type 1 adaptors have problems with registers (see comments
in \ :c:func:`drm_dp_dual_mode_detect`\ ) we avoid touching the register,
making this function a no-op on type 1 adaptors.

.. _`drm_dp_dual_mode_set_tmds_output.return`:

Return
------

0 on success, negative error code on failure

.. _`drm_dp_get_dual_mode_type_name`:

drm_dp_get_dual_mode_type_name
==============================

.. c:function:: const char *drm_dp_get_dual_mode_type_name(enum drm_dp_dual_mode_type type)

    Get the name of the DP dual mode adaptor type as a string

    :param type:
        DP dual mode adaptor type
    :type type: enum drm_dp_dual_mode_type

.. _`drm_dp_get_dual_mode_type_name.return`:

Return
------

String representation of the DP dual mode adaptor type

.. _`drm_lspcon_get_mode`:

drm_lspcon_get_mode
===================

.. c:function:: int drm_lspcon_get_mode(struct i2c_adapter *adapter, enum drm_lspcon_mode *mode)

    Get LSPCON's current mode of operation by reading offset (0x80, 0x41)

    :param adapter:
        I2C-over-aux adapter
    :type adapter: struct i2c_adapter \*

    :param mode:
        current lspcon mode of operation output variable
    :type mode: enum drm_lspcon_mode \*

.. _`drm_lspcon_get_mode.return`:

Return
------

0 on success, sets the current_mode value to appropriate mode
-error on failure

.. _`drm_lspcon_set_mode`:

drm_lspcon_set_mode
===================

.. c:function:: int drm_lspcon_set_mode(struct i2c_adapter *adapter, enum drm_lspcon_mode mode)

    Change LSPCON's mode of operation by writing offset (0x80, 0x40)

    :param adapter:
        I2C-over-aux adapter
    :type adapter: struct i2c_adapter \*

    :param mode:
        required mode of operation
    :type mode: enum drm_lspcon_mode

.. _`drm_lspcon_set_mode.return`:

Return
------

0 on success, -error on failure/timeout

.. This file was automatic generated / don't edit.

