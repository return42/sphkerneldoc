.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_scdc_helper.h

.. _`drm_scdc_readb`:

drm_scdc_readb
==============

.. c:function:: int drm_scdc_readb(struct i2c_adapter *adapter, u8 offset, u8 *value)

    read a single byte from SCDC

    :param struct i2c_adapter \*adapter:
        I2C adapter

    :param u8 offset:
        offset of register to read

    :param u8 \*value:
        return location for the register value

.. _`drm_scdc_readb.description`:

Description
-----------

Reads a single byte from SCDC. This is a convenience wrapper around the
\ :c:func:`drm_scdc_read`\  function.

.. _`drm_scdc_readb.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_scdc_writeb`:

drm_scdc_writeb
===============

.. c:function:: int drm_scdc_writeb(struct i2c_adapter *adapter, u8 offset, u8 value)

    write a single byte to SCDC

    :param struct i2c_adapter \*adapter:
        I2C adapter

    :param u8 offset:
        offset of register to read

    :param u8 value:
        return location for the register value

.. _`drm_scdc_writeb.description`:

Description
-----------

Writes a single byte to SCDC. This is a convenience wrapper around the
\ :c:func:`drm_scdc_write`\  function.

.. _`drm_scdc_writeb.return`:

Return
------

0 on success or a negative error code on failure.

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

.. _`drm_scdc_set_high_tmds_clock_ratio.description`:

Description
-----------

Writes to the TMDS config register over SCDC channel, and:
sets TMDS clock ratio to 1/40 when set = 1
sets TMDS clock ratio to 1/10 when set = 0

.. _`drm_scdc_set_high_tmds_clock_ratio.return`:

Return
------

True if write is successful, false otherwise.

.. This file was automatic generated / don't edit.

