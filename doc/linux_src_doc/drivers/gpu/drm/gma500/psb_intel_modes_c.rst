.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/psb_intel_modes.c

.. _`psb_intel_ddc_probe`:

psb_intel_ddc_probe
===================

.. c:function:: bool psb_intel_ddc_probe(struct i2c_adapter *adapter)

    :param struct i2c_adapter \*adapter:
        *undescribed*

.. _`psb_intel_ddc_get_modes`:

psb_intel_ddc_get_modes
=======================

.. c:function:: int psb_intel_ddc_get_modes(struct drm_connector *connector, struct i2c_adapter *adapter)

    get modelist from monitor

    :param struct drm_connector \*connector:
        DRM connector device to use

    :param struct i2c_adapter \*adapter:
        *undescribed*

.. _`psb_intel_ddc_get_modes.description`:

Description
-----------

Fetch the EDID information from \ ``connector``\  using the DDC bus.

.. This file was automatic generated / don't edit.

