.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/iio/accel/sca3000_core.c

.. _`sca3000_reg_lock_on`:

sca3000_reg_lock_on
===================

.. c:function:: int sca3000_reg_lock_on(struct sca3000_state *st)

    :param struct sca3000_state \*st:
        *undescribed*

.. _`sca3000_reg_lock_on.description`:

Description
-----------

Lock must be held.

.. _`__sca3000_unlock_reg_lock`:

__sca3000_unlock_reg_lock
=========================

.. c:function:: int __sca3000_unlock_reg_lock(struct sca3000_state *st)

    :param struct sca3000_state \*st:
        *undescribed*

.. _`__sca3000_unlock_reg_lock.description`:

Description
-----------

Note the device does not appear to support doing this in a single transfer.
This should only ever be used as part of ctrl reg read.
Lock must be held before calling this

.. _`sca3000_write_ctrl_reg`:

sca3000_write_ctrl_reg
======================

.. c:function:: int sca3000_write_ctrl_reg(struct sca3000_state *st, u8 sel, uint8_t val)

    :param struct sca3000_state \*st:
        *undescribed*

    :param u8 sel:
        selects which registers we wish to write to

    :param uint8_t val:
        the value to be written

.. _`sca3000_write_ctrl_reg.description`:

Description
-----------

Certain control registers are protected against overwriting by the lock
register and use a shared write address. This function allows writing of
these registers.
Lock must be held.

.. _`sca3000_read_ctrl_reg`:

sca3000_read_ctrl_reg
=====================

.. c:function:: int sca3000_read_ctrl_reg(struct sca3000_state *st, u8 ctrl_reg)

    :param struct sca3000_state \*st:
        *undescribed*

    :param u8 ctrl_reg:
        *undescribed*

.. _`sca3000_read_ctrl_reg.description`:

Description
-----------

Lock must be held.

.. _`sca3000_show_rev`:

sca3000_show_rev
================

.. c:function:: ssize_t sca3000_show_rev(struct device *dev, struct device_attribute *attr, char *buf)

    sysfs interface to read the chip revision number

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`sca3000_show_available_measurement_modes`:

sca3000_show_available_measurement_modes
========================================

.. c:function:: ssize_t sca3000_show_available_measurement_modes(struct device *dev, struct device_attribute *attr, char *buf)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`sca3000_show_available_measurement_modes.description`:

Description
-----------

This is all read from chip specific data in the driver. Not all
of the sca3000 series support modes other than normal.

.. _`sca3000_show_measurement_mode`:

sca3000_show_measurement_mode
=============================

.. c:function:: ssize_t sca3000_show_measurement_mode(struct device *dev, struct device_attribute *attr, char *buf)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`sca3000_store_measurement_mode`:

sca3000_store_measurement_mode
==============================

.. c:function:: ssize_t sca3000_store_measurement_mode(struct device *dev, struct device_attribute *attr, const char *buf, size_t len)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param const char \*buf:
        *undescribed*

    :param size_t len:
        *undescribed*

.. _`__sca3000_get_base_freq`:

__sca3000_get_base_freq
=======================

.. c:function:: int __sca3000_get_base_freq(struct sca3000_state *st, const struct sca3000_chip_info *info, int *base_freq)

    :param struct sca3000_state \*st:
        *undescribed*

    :param const struct sca3000_chip_info \*info:
        *undescribed*

    :param int \*base_freq:
        *undescribed*

.. _`__sca3000_get_base_freq.description`:

Description
-----------

lock must be held

.. _`read_raw_samp_freq`:

read_raw_samp_freq
==================

.. c:function:: int read_raw_samp_freq(struct sca3000_state *st, int *val)

    :param struct sca3000_state \*st:
        *undescribed*

    :param int \*val:
        *undescribed*

.. _`read_raw_samp_freq.description`:

Description
-----------

lock must be held

.. _`write_raw_samp_freq`:

write_raw_samp_freq
===================

.. c:function:: int write_raw_samp_freq(struct sca3000_state *st, int val)

    :param struct sca3000_state \*st:
        *undescribed*

    :param int val:
        *undescribed*

.. _`write_raw_samp_freq.description`:

Description
-----------

lock must be held

.. _`sca3000_read_av_freq`:

sca3000_read_av_freq
====================

.. c:function:: ssize_t sca3000_read_av_freq(struct device *dev, struct device_attribute *attr, char *buf)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`sca3000_read_av_freq.description`:

Description
-----------

The later modes are only relevant to the ring buffer - and depend on current
mode. Note that data sheet gives rather wide tolerances for these so integer
division will give good enough answer and not all chips have them specified
at all.

.. _`sca3000_read_thresh`:

sca3000_read_thresh
===================

.. c:function:: int sca3000_read_thresh(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, enum iio_event_type type, enum iio_event_direction dir, enum iio_event_info info, int *val, int *val2)

    query of a threshold

    :param struct iio_dev \*indio_dev:
        *undescribed*

    :param const struct iio_chan_spec \*chan:
        *undescribed*

    :param enum iio_event_type type:
        *undescribed*

    :param enum iio_event_direction dir:
        *undescribed*

    :param enum iio_event_info info:
        *undescribed*

    :param int \*val:
        *undescribed*

    :param int \*val2:
        *undescribed*

.. _`sca3000_write_thresh`:

sca3000_write_thresh
====================

.. c:function:: int sca3000_write_thresh(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, enum iio_event_type type, enum iio_event_direction dir, enum iio_event_info info, int val, int val2)

    :param struct iio_dev \*indio_dev:
        *undescribed*

    :param const struct iio_chan_spec \*chan:
        *undescribed*

    :param enum iio_event_type type:
        *undescribed*

    :param enum iio_event_direction dir:
        *undescribed*

    :param enum iio_event_info info:
        *undescribed*

    :param int val:
        *undescribed*

    :param int val2:
        *undescribed*

.. _`sca3000_event_handler`:

sca3000_event_handler
=====================

.. c:function:: irqreturn_t sca3000_event_handler(int irq, void *private)

    handling ring and non ring events

    :param int irq:
        *undescribed*

    :param void \*private:
        *undescribed*

.. _`sca3000_event_handler.description`:

Description
-----------

Ring related interrupt handler. Depending on event, push to
the ring buffer event chrdev or the event one.

This function is complicated by the fact that the devices can signify ring
and non ring events via the same interrupt line and they can only
be distinguished via a read of the relevant status register.

.. _`sca3000_read_event_config`:

sca3000_read_event_config
=========================

.. c:function:: int sca3000_read_event_config(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, enum iio_event_type type, enum iio_event_direction dir)

    :param struct iio_dev \*indio_dev:
        *undescribed*

    :param const struct iio_chan_spec \*chan:
        *undescribed*

    :param enum iio_event_type type:
        *undescribed*

    :param enum iio_event_direction dir:
        *undescribed*

.. _`sca3000_query_free_fall_mode`:

sca3000_query_free_fall_mode
============================

.. c:function:: ssize_t sca3000_query_free_fall_mode(struct device *dev, struct device_attribute *attr, char *buf)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`sca3000_set_free_fall_mode`:

sca3000_set_free_fall_mode
==========================

.. c:function:: ssize_t sca3000_set_free_fall_mode(struct device *dev, struct device_attribute *attr, const char *buf, size_t len)

    :param struct device \*dev:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param const char \*buf:
        *undescribed*

    :param size_t len:
        *undescribed*

.. _`sca3000_set_free_fall_mode.description`:

Description
-----------

In these chips the free fall detector should send an interrupt if
the device falls more than 25cm.  This has not been tested due
to fragile wiring.

.. _`sca3000_write_event_config`:

sca3000_write_event_config
==========================

.. c:function:: int sca3000_write_event_config(struct iio_dev *indio_dev, const struct iio_chan_spec *chan, enum iio_event_type type, enum iio_event_direction dir, int state)

    :param struct iio_dev \*indio_dev:
        *undescribed*

    :param const struct iio_chan_spec \*chan:
        *undescribed*

    :param enum iio_event_type type:
        *undescribed*

    :param enum iio_event_direction dir:
        *undescribed*

    :param int state:
        *undescribed*

.. _`sca3000_write_event_config.description`:

Description
-----------

This is a per axis control, but enabling any will result in the
motion detector unit being enabled.
N.B. enabling motion detector stops normal data acquisition.
There is a complexity in knowing which mode to return to when
this mode is disabled.  Currently normal mode is assumed.

.. _`sca3000_clean_setup`:

sca3000_clean_setup
===================

.. c:function:: int sca3000_clean_setup(struct sca3000_state *st)

    :param struct sca3000_state \*st:
        *undescribed*

.. _`sca3000_clean_setup.description`:

Description
-----------

Devices use flash memory to store many of the register values
and hence can come up in somewhat unpredictable states.
Hence reset everything on driver load.

.. This file was automatic generated / don't edit.

