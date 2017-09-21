.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_scdc_helper.c

.. _`scdc-helpers`:

scdc helpers
============

Status and Control Data Channel (SCDC) is a mechanism introduced by the
HDMI 2.0 specification. It is a point-to-point protocol that allows the
HDMI source and HDMI sink to exchange data. The same I2C interface that
is used to access EDID serves as the transport mechanism for SCDC.

.. _`drm_scdc_read`:

drm_scdc_read
=============

.. c:function:: ssize_t drm_scdc_read(struct i2c_adapter *adapter, u8 offset, void *buffer, size_t size)

    read a block of data from SCDC

    :param struct i2c_adapter \*adapter:
        I2C controller

    :param u8 offset:
        start offset of block to read

    :param void \*buffer:
        return location for the block to read

    :param size_t size:
        size of the block to read

.. _`drm_scdc_read.description`:

Description
-----------

Reads a block of data from SCDC, starting at a given offset.

.. _`drm_scdc_read.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_scdc_write`:

drm_scdc_write
==============

.. c:function:: ssize_t drm_scdc_write(struct i2c_adapter *adapter, u8 offset, const void *buffer, size_t size)

    write a block of data to SCDC

    :param struct i2c_adapter \*adapter:
        I2C controller

    :param u8 offset:
        start offset of block to write

    :param const void \*buffer:
        block of data to write

    :param size_t size:
        size of the block to write

.. _`drm_scdc_write.description`:

Description
-----------

Writes a block of data to SCDC, starting at a given offset.

.. _`drm_scdc_write.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_scdc_get_scrambling_status`:

drm_scdc_get_scrambling_status
==============================

.. c:function:: bool drm_scdc_get_scrambling_status(struct i2c_adapter *adapter)

    what is status of scrambling?

    :param struct i2c_adapter \*adapter:
        I2C adapter for DDC channel

.. _`drm_scdc_get_scrambling_status.description`:

Description
-----------

Reads the scrambler status over SCDC, and checks the
scrambling status.

.. _`drm_scdc_get_scrambling_status.return`:

Return
------

True if the scrambling is enabled, false otherwise.

.. _`drm_scdc_set_scrambling`:

drm_scdc_set_scrambling
=======================

.. c:function:: bool drm_scdc_set_scrambling(struct i2c_adapter *adapter, bool enable)

    enable scrambling

    :param struct i2c_adapter \*adapter:
        I2C adapter for DDC channel

    :param bool enable:
        bool to indicate if scrambling is to be enabled/disabled

.. _`drm_scdc_set_scrambling.description`:

Description
-----------

Writes the TMDS config register over SCDC channel, and:
enables scrambling when enable = 1
disables scrambling when enable = 0

.. _`drm_scdc_set_scrambling.return`:

Return
------

True if scrambling is set/reset successfully, false otherwise.

.. _`drm_scdc_set_high_tmds_clock_ratio`:

drm_scdc_set_high_tmds_clock_ratio
==================================

.. c:function:: bool drm_scdc_set_high_tmds_clock_ratio(struct i2c_adapter *adapter, bool set)

    set TMDS clock ratio

    :param struct i2c_adapter \*adapter:
        I2C adapter for DDC channel

    :param bool set:
        ret or reset the high clock ratio

.. _`drm_scdc_set_high_tmds_clock_ratio.tmds-clock-ratio-calculations-go-like-this`:

TMDS clock ratio calculations go like this
------------------------------------------


             TMDS character = 10 bit TMDS encoded value

             TMDS character rate = The rate at which TMDS characters are
             transmitted (Mcsc)

             TMDS bit rate = 10x TMDS character rate

.. _`drm_scdc_set_high_tmds_clock_ratio.as-per-the-spec`:

As per the spec
---------------

             TMDS clock rate for pixel clock < 340 MHz = 1x the character
             rate = 1/10 pixel clock rate

             TMDS clock rate for pixel clock > 340 MHz = 0.25x the character
             rate = 1/40 pixel clock rate

     Writes to the TMDS config register over SCDC channel, and:
             sets TMDS clock ratio to 1/40 when set = 1

             sets TMDS clock ratio to 1/10 when set = 0

.. _`drm_scdc_set_high_tmds_clock_ratio.return`:

Return
------

True if write is successful, false otherwise.

.. This file was automatic generated / don't edit.

