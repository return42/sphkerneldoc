.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_bios.c

.. _`intel_bios_is_valid_vbt`:

intel_bios_is_valid_vbt
=======================

.. c:function:: bool intel_bios_is_valid_vbt(const void *buf, size_t size)

    does the given buffer contain a valid VBT

    :param const void \*buf:
        pointer to a buffer to validate

    :param size_t size:
        size of the buffer

.. _`intel_bios_is_valid_vbt.description`:

Description
-----------

Returns true on valid VBT.

.. _`intel_bios_init`:

intel_bios_init
===============

.. c:function:: void intel_bios_init(struct drm_i915_private *dev_priv)

    find VBT and initialize settings from the BIOS

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

.. _`intel_bios_init.description`:

Description
-----------

Parse and initialize settings from the Video BIOS Tables (VBT). If the VBT
was not found in ACPI OpRegion, try to find it in PCI ROM first. Also
initialize some defaults if the VBT is not present at all.

.. _`intel_bios_is_tv_present`:

intel_bios_is_tv_present
========================

.. c:function:: bool intel_bios_is_tv_present(struct drm_i915_private *dev_priv)

    is integrated TV present in VBT

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

.. _`intel_bios_is_tv_present.description`:

Description
-----------

Return true if TV is present. If no child devices were parsed from VBT,
assume TV is present.

.. _`intel_bios_is_lvds_present`:

intel_bios_is_lvds_present
==========================

.. c:function:: bool intel_bios_is_lvds_present(struct drm_i915_private *dev_priv, u8 *i2c_pin)

    is LVDS present in VBT

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param u8 \*i2c_pin:
        i2c pin for LVDS if present

.. _`intel_bios_is_lvds_present.description`:

Description
-----------

Return true if LVDS is present. If no child devices were parsed from VBT,
assume LVDS is present.

.. _`intel_bios_is_port_present`:

intel_bios_is_port_present
==========================

.. c:function:: bool intel_bios_is_port_present(struct drm_i915_private *dev_priv, enum port port)

    is the specified digital port present

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum port port:
        port to check

.. _`intel_bios_is_port_present.description`:

Description
-----------

Return true if the device in \ ``port``\  is present.

.. _`intel_bios_is_port_edp`:

intel_bios_is_port_edp
======================

.. c:function:: bool intel_bios_is_port_edp(struct drm_i915_private *dev_priv, enum port port)

    is the device in given port eDP

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum port port:
        port to check

.. _`intel_bios_is_port_edp.description`:

Description
-----------

Return true if the device in \ ``port``\  is eDP.

.. _`intel_bios_is_dsi_present`:

intel_bios_is_dsi_present
=========================

.. c:function:: bool intel_bios_is_dsi_present(struct drm_i915_private *dev_priv, enum port *port)

    is DSI present in VBT

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum port \*port:
        port for DSI if present

.. _`intel_bios_is_dsi_present.description`:

Description
-----------

Return true if DSI is present, and return the port in \ ``port``\ .

.. _`intel_bios_is_port_hpd_inverted`:

intel_bios_is_port_hpd_inverted
===============================

.. c:function:: bool intel_bios_is_port_hpd_inverted(struct drm_i915_private *dev_priv, enum port port)

    is HPD inverted for \ ``port``\ 

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum port port:
        port to check

.. _`intel_bios_is_port_hpd_inverted.description`:

Description
-----------

Return true if HPD should be inverted for \ ``port``\ .

.. _`intel_bios_is_lspcon_present`:

intel_bios_is_lspcon_present
============================

.. c:function:: bool intel_bios_is_lspcon_present(struct drm_i915_private *dev_priv, enum port port)

    if LSPCON is attached on \ ``port``\ 

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum port port:
        port to check

.. _`intel_bios_is_lspcon_present.description`:

Description
-----------

Return true if LSPCON is present on this port

.. This file was automatic generated / don't edit.

