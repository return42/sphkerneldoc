.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_modes.c

.. _`intel_connector_update_modes`:

intel_connector_update_modes
============================

.. c:function:: int intel_connector_update_modes(struct drm_connector *connector, struct edid *edid)

    update connector from edid

    :param struct drm_connector \*connector:
        DRM connector device to use

    :param struct edid \*edid:
        previously read EDID information

.. _`intel_ddc_get_modes`:

intel_ddc_get_modes
===================

.. c:function:: int intel_ddc_get_modes(struct drm_connector *connector, struct i2c_adapter *adapter)

    get modelist from monitor

    :param struct drm_connector \*connector:
        DRM connector device to use

    :param struct i2c_adapter \*adapter:
        i2c adapter

.. _`intel_ddc_get_modes.description`:

Description
-----------

Fetch the EDID information from \ ``connector``\  using the DDC bus.

.. This file was automatic generated / don't edit.

