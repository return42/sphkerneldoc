.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_modes.c

.. _`intel_connector_update_modes`:

intel_connector_update_modes
============================

.. c:function:: int intel_connector_update_modes(struct drm_connector *connector, struct edid *edid)

    update connector from edid

    :param connector:
        DRM connector device to use
    :type connector: struct drm_connector \*

    :param edid:
        previously read EDID information
    :type edid: struct edid \*

.. _`intel_ddc_get_modes`:

intel_ddc_get_modes
===================

.. c:function:: int intel_ddc_get_modes(struct drm_connector *connector, struct i2c_adapter *adapter)

    get modelist from monitor

    :param connector:
        DRM connector device to use
    :type connector: struct drm_connector \*

    :param adapter:
        i2c adapter
    :type adapter: struct i2c_adapter \*

.. _`intel_ddc_get_modes.description`:

Description
-----------

Fetch the EDID information from \ ``connector``\  using the DDC bus.

.. This file was automatic generated / don't edit.

