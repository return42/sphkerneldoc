.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/omapdrm/dss/omapdss.h

.. _`omap_dss_device_ops_flag`:

enum omap_dss_device_ops_flag
=============================

.. c:type:: enum omap_dss_device_ops_flag

    Indicates which device ops are supported

.. _`omap_dss_device_ops_flag.definition`:

Definition
----------

.. code-block:: c

    enum omap_dss_device_ops_flag {
        OMAP_DSS_DEVICE_OP_DETECT,
        OMAP_DSS_DEVICE_OP_HPD,
        OMAP_DSS_DEVICE_OP_EDID
    };

.. _`omap_dss_device_ops_flag.constants`:

Constants
---------

OMAP_DSS_DEVICE_OP_DETECT
    The device supports output connection detection

OMAP_DSS_DEVICE_OP_HPD
    The device supports all hot-plug-related operations

OMAP_DSS_DEVICE_OP_EDID
    The device supports readind EDID

.. This file was automatic generated / don't edit.

