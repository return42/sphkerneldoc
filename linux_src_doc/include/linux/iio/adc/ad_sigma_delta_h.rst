.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/adc/ad_sigma_delta.h

.. _`ad_sd_calib_data`:

struct ad_sd_calib_data
=======================

.. c:type:: struct ad_sd_calib_data

    Calibration data for Sigma Delta devices

.. _`ad_sd_calib_data.definition`:

Definition
----------

.. code-block:: c

    struct ad_sd_calib_data {
        unsigned int mode;
        unsigned int channel;
    }

.. _`ad_sd_calib_data.members`:

Members
-------

mode
    Calibration mode.

channel
    Calibration channel.

.. _`ad_sigma_delta_info`:

struct ad_sigma_delta_info
==========================

.. c:type:: struct ad_sigma_delta_info

    Sigma Delta driver specific callbacks and options

.. _`ad_sigma_delta_info.definition`:

Definition
----------

.. code-block:: c

    struct ad_sigma_delta_info {
        int (*set_channel)(struct ad_sigma_delta *, unsigned int channel);
        int (*set_mode)(struct ad_sigma_delta *, enum ad_sigma_delta_mode mode);
        int (*postprocess_sample)(struct ad_sigma_delta *, unsigned int raw_sample);
        bool has_registers;
        unsigned int addr_shift;
        unsigned int read_mask;
    }

.. _`ad_sigma_delta_info.members`:

Members
-------

set_channel
    Will be called to select the current channel, may be NULL.

set_mode
    Will be called to select the current mode, may be NULL.

postprocess_sample
    Is called for each sampled data word, can be used to
    modify or drop the sample data, it, may be NULL.

has_registers
    true if the device has writable and readable registers, false
    if there is just one read-only sample data shift register.

addr_shift
    Shift of the register address in the communications register.

read_mask
    Mask for the communications register having the read bit set.

.. _`ad_sigma_delta`:

struct ad_sigma_delta
=====================

.. c:type:: struct ad_sigma_delta

    Sigma Delta device struct

.. _`ad_sigma_delta.definition`:

Definition
----------

.. code-block:: c

    struct ad_sigma_delta {
        struct spi_device *spi;
        struct iio_trigger *trig;
    }

.. _`ad_sigma_delta.members`:

Members
-------

spi
    The spi device associated with the Sigma Delta device.

trig
    The IIO trigger associated with the Sigma Delta device.

.. _`ad_sigma_delta.description`:

Description
-----------

Most of the fields are private to the sigma delta library code and should not
be accessed by individual drivers.

.. This file was automatic generated / don't edit.

