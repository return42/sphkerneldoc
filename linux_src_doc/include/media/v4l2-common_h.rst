.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-common.h

.. _`v4l2_ctrl_query_fill`:

v4l2_ctrl_query_fill
====================

.. c:function:: int v4l2_ctrl_query_fill(struct v4l2_queryctrl *qctrl, s32 min, s32 max, s32 step, s32 def)

    Fill in a struct v4l2_queryctrl

    :param qctrl:
        pointer to the \ :c:type:`struct v4l2_queryctrl <v4l2_queryctrl>`\  to be filled
    :type qctrl: struct v4l2_queryctrl \*

    :param min:
        minimum value for the control
    :type min: s32

    :param max:
        maximum value for the control
    :type max: s32

    :param step:
        control step
    :type step: s32

    :param def:
        default value for the control
    :type def: s32

.. _`v4l2_ctrl_query_fill.description`:

Description
-----------

Fills the \ :c:type:`struct v4l2_queryctrl <v4l2_queryctrl>`\  fields for the query control.

.. note::

   This function assumes that the @qctrl->id field is filled.

Returns -EINVAL if the control is not known by the V4L2 core, 0 on success.

.. _`v4l2_i2c_new_subdev`:

v4l2_i2c_new_subdev
===================

.. c:function:: struct v4l2_subdev *v4l2_i2c_new_subdev(struct v4l2_device *v4l2_dev, struct i2c_adapter *adapter, const char *client_type, u8 addr, const unsigned short *probe_addrs)

    Load an i2c module and return an initialized \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ .

    :param v4l2_dev:
        pointer to \ :c:type:`struct v4l2_device <v4l2_device>`\ 
    :type v4l2_dev: struct v4l2_device \*

    :param adapter:
        pointer to struct i2c_adapter
    :type adapter: struct i2c_adapter \*

    :param client_type:
        name of the chip that's on the adapter.
    :type client_type: const char \*

    :param addr:
        I2C address. If zero, it will use \ ``probe_addrs``\ 
    :type addr: u8

    :param probe_addrs:
        array with a list of address. The last entry at such
        array should be \ ``I2C_CLIENT_END``\ .
    :type probe_addrs: const unsigned short \*

.. _`v4l2_i2c_new_subdev.description`:

Description
-----------

returns a \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  pointer.

.. _`v4l2_i2c_new_subdev_board`:

v4l2_i2c_new_subdev_board
=========================

.. c:function:: struct v4l2_subdev *v4l2_i2c_new_subdev_board(struct v4l2_device *v4l2_dev, struct i2c_adapter *adapter, struct i2c_board_info *info, const unsigned short *probe_addrs)

    Load an i2c module and return an initialized \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ .

    :param v4l2_dev:
        pointer to \ :c:type:`struct v4l2_device <v4l2_device>`\ 
    :type v4l2_dev: struct v4l2_device \*

    :param adapter:
        pointer to struct i2c_adapter
    :type adapter: struct i2c_adapter \*

    :param info:
        pointer to struct i2c_board_info used to replace the irq,
        platform_data and addr arguments.
    :type info: struct i2c_board_info \*

    :param probe_addrs:
        array with a list of address. The last entry at such
        array should be \ ``I2C_CLIENT_END``\ .
    :type probe_addrs: const unsigned short \*

.. _`v4l2_i2c_new_subdev_board.description`:

Description
-----------

returns a \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  pointer.

.. _`v4l2_i2c_subdev_set_name`:

v4l2_i2c_subdev_set_name
========================

.. c:function:: void v4l2_i2c_subdev_set_name(struct v4l2_subdev *sd, struct i2c_client *client, const char *devname, const char *postfix)

    Set name for an I²C sub-device

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

    :param client:
        pointer to struct i2c_client
    :type client: struct i2c_client \*

    :param devname:
        the name of the device; if NULL, the I²C device's name will be used
    :type devname: const char \*

    :param postfix:
        sub-device specific string to put right after the I²C device name;
        may be NULL
    :type postfix: const char \*

.. _`v4l2_i2c_subdev_init`:

v4l2_i2c_subdev_init
====================

.. c:function:: void v4l2_i2c_subdev_init(struct v4l2_subdev *sd, struct i2c_client *client, const struct v4l2_subdev_ops *ops)

    Initializes a \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  with data from an i2c_client struct.

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

    :param client:
        pointer to struct i2c_client
    :type client: struct i2c_client \*

    :param ops:
        pointer to \ :c:type:`struct v4l2_subdev_ops <v4l2_subdev_ops>`\ 
    :type ops: const struct v4l2_subdev_ops \*

.. _`v4l2_i2c_subdev_addr`:

v4l2_i2c_subdev_addr
====================

.. c:function:: unsigned short v4l2_i2c_subdev_addr(struct v4l2_subdev *sd)

    returns i2c client address of \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ .

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

.. _`v4l2_i2c_subdev_addr.description`:

Description
-----------

Returns the address of an I2C sub-device

.. _`v4l2_i2c_tuner_type`:

enum v4l2_i2c_tuner_type
========================

.. c:type:: enum v4l2_i2c_tuner_type

    specifies the range of tuner address that should be used when seeking for I2C devices.

.. _`v4l2_i2c_tuner_type.definition`:

Definition
----------

.. code-block:: c

    enum v4l2_i2c_tuner_type {
        ADDRS_RADIO,
        ADDRS_DEMOD,
        ADDRS_TV,
        ADDRS_TV_WITH_DEMOD
    };

.. _`v4l2_i2c_tuner_type.constants`:

Constants
---------

ADDRS_RADIO
    Radio tuner addresses.
    Represent the following I2C addresses:
    0x10 (if compiled with tea5761 support)
    and 0x60.

ADDRS_DEMOD
    Demod tuner addresses.
    Represent the following I2C addresses:
    0x42, 0x43, 0x4a and 0x4b.

ADDRS_TV
    TV tuner addresses.
    Represent the following I2C addresses:
    0x42, 0x43, 0x4a, 0x4b, 0x60, 0x61, 0x62,
    0x63 and 0x64.

ADDRS_TV_WITH_DEMOD
    TV tuner addresses if demod is present, this
    excludes addresses used by the demodulator
    from the list of candidates.
    Represent the following I2C addresses:
    0x60, 0x61, 0x62, 0x63 and 0x64.

.. _`v4l2_i2c_tuner_type.note`:

NOTE
----

All I2C addresses above use the 7-bit notation.

.. _`v4l2_i2c_tuner_addrs`:

v4l2_i2c_tuner_addrs
====================

.. c:function:: const unsigned short *v4l2_i2c_tuner_addrs(enum v4l2_i2c_tuner_type type)

    Return a list of I2C tuner addresses to probe.

    :param type:
        type of the tuner to seek, as defined by
        \ :c:type:`enum v4l2_i2c_tuner_type <v4l2_i2c_tuner_type>`\ .
    :type type: enum v4l2_i2c_tuner_type

.. _`v4l2_i2c_tuner_addrs.note`:

NOTE
----

Use only if the tuner addresses are unknown.

.. _`v4l2_spi_new_subdev`:

v4l2_spi_new_subdev
===================

.. c:function:: struct v4l2_subdev *v4l2_spi_new_subdev(struct v4l2_device *v4l2_dev, struct spi_master *master, struct spi_board_info *info)

    Load an spi module and return an initialized \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ .

    :param v4l2_dev:
        pointer to \ :c:type:`struct v4l2_device <v4l2_device>`\ .
    :type v4l2_dev: struct v4l2_device \*

    :param master:
        pointer to struct spi_master.
    :type master: struct spi_master \*

    :param info:
        pointer to struct spi_board_info.
    :type info: struct spi_board_info \*

.. _`v4l2_spi_new_subdev.description`:

Description
-----------

returns a \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  pointer.

.. _`v4l2_spi_subdev_init`:

v4l2_spi_subdev_init
====================

.. c:function:: void v4l2_spi_subdev_init(struct v4l2_subdev *sd, struct spi_device *spi, const struct v4l2_subdev_ops *ops)

    Initialize a v4l2_subdev with data from an spi_device struct.

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

    :param spi:
        pointer to struct spi_device.
    :type spi: struct spi_device \*

    :param ops:
        pointer to \ :c:type:`struct v4l2_subdev_ops <v4l2_subdev_ops>`\ 
    :type ops: const struct v4l2_subdev_ops \*

.. _`v4l_bound_align_image`:

v4l_bound_align_image
=====================

.. c:function:: void v4l_bound_align_image(unsigned int *width, unsigned int wmin, unsigned int wmax, unsigned int walign, unsigned int *height, unsigned int hmin, unsigned int hmax, unsigned int halign, unsigned int salign)

    adjust video dimensions according to a given constraints.

    :param width:
        pointer to width that will be adjusted if needed.
    :type width: unsigned int \*

    :param wmin:
        minimum width.
    :type wmin: unsigned int

    :param wmax:
        maximum width.
    :type wmax: unsigned int

    :param walign:
        least significant bit on width.
    :type walign: unsigned int

    :param height:
        pointer to height that will be adjusted if needed.
    :type height: unsigned int \*

    :param hmin:
        minimum height.
    :type hmin: unsigned int

    :param hmax:
        maximum height.
    :type hmax: unsigned int

    :param halign:
        least significant bit on height.
    :type halign: unsigned int

    :param salign:
        least significant bit for the image size (e. g.
        :math:`width * height`).
    :type salign: unsigned int

.. _`v4l_bound_align_image.description`:

Description
-----------

Clip an image to have \ ``width``\  between \ ``wmin``\  and \ ``wmax``\ , and \ ``height``\  between
\ ``hmin``\  and \ ``hmax``\ , inclusive.

Additionally, the \ ``width``\  will be a multiple of :math:`2^{walign}`,
the \ ``height``\  will be a multiple of :math:`2^{halign}`, and the overall
size :math:`width * height` will be a multiple of :math:`2^{salign}`.

.. note::

   #. The clipping rectangle may be shrunk or enlarged to fit the alignment
      constraints.
   #. @wmax must not be smaller than @wmin.
   #. @hmax must not be smaller than @hmin.
   #. The alignments must not be so high there are no possible image
      sizes within the allowed bounds.
   #. @wmin and @hmin must be at least 1 (don't use 0).
   #. For @walign, @halign and @salign, if you don't care about a certain
      alignment, specify ``0``, as :math:`2^0 = 1` and one byte alignment
      is equivalent to no alignment.
   #. If you only want to adjust downward, specify a maximum that's the
      same as the initial value.

.. _`v4l2_get_timestamp`:

v4l2_get_timestamp
==================

.. c:function:: void v4l2_get_timestamp(struct timeval *tv)

    helper routine to get a timestamp to be used when filling streaming metadata. Internally, it uses \ :c:func:`ktime_get_ts`\ , which is the recommended way to get it.

    :param tv:
        pointer to \ :c:type:`struct timeval <timeval>`\  to be filled.
    :type tv: struct timeval \*

.. _`v4l2_g_parm_cap`:

v4l2_g_parm_cap
===============

.. c:function:: int v4l2_g_parm_cap(struct video_device *vdev, struct v4l2_subdev *sd, struct v4l2_streamparm *a)

    helper routine for vidioc_g_parm to fill this in by calling the g_frame_interval op of the given subdev. It only works for V4L2_BUF_TYPE_VIDEO_CAPTURE(_MPLANE), hence the _cap in the function name.

    :param vdev:
        the struct video_device pointer. Used to determine the device caps.
    :type vdev: struct video_device \*

    :param sd:
        the sub-device pointer.
    :type sd: struct v4l2_subdev \*

    :param a:
        the VIDIOC_G_PARM argument.
    :type a: struct v4l2_streamparm \*

.. _`v4l2_s_parm_cap`:

v4l2_s_parm_cap
===============

.. c:function:: int v4l2_s_parm_cap(struct video_device *vdev, struct v4l2_subdev *sd, struct v4l2_streamparm *a)

    helper routine for vidioc_s_parm to fill this in by calling the s_frame_interval op of the given subdev. It only works for V4L2_BUF_TYPE_VIDEO_CAPTURE(_MPLANE), hence the _cap in the function name.

    :param vdev:
        the struct video_device pointer. Used to determine the device caps.
    :type vdev: struct video_device \*

    :param sd:
        the sub-device pointer.
    :type sd: struct v4l2_subdev \*

    :param a:
        the VIDIOC_S_PARM argument.
    :type a: struct v4l2_streamparm \*

.. This file was automatic generated / don't edit.

