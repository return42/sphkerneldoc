.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_scdc_helper.h

.. _`drm_scdc_readb`:

drm_scdc_readb
==============

.. c:function:: int drm_scdc_readb(struct i2c_adapter *adapter, u8 offset, u8 *value)

    read a single byte from SCDC

    :param adapter:
        I2C adapter
    :type adapter: struct i2c_adapter \*

    :param offset:
        offset of register to read
    :type offset: u8

    :param value:
        return location for the register value
    :type value: u8 \*

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

    :param adapter:
        I2C adapter
    :type adapter: struct i2c_adapter \*

    :param offset:
        offset of register to read
    :type offset: u8

    :param value:
        return location for the register value
    :type value: u8

.. _`drm_scdc_writeb.description`:

Description
-----------

Writes a single byte to SCDC. This is a convenience wrapper around the
\ :c:func:`drm_scdc_write`\  function.

.. _`drm_scdc_writeb.return`:

Return
------

0 on success or a negative error code on failure.

.. This file was automatic generated / don't edit.

