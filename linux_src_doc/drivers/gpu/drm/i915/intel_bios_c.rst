.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_bios.c

.. _`video-bios-table--vbt-`:

Video BIOS Table (VBT)
======================

The Video BIOS Table, or VBT, provides platform and board specific
configuration information to the driver that is not discoverable or available
through other means. The configuration is mostly related to display
hardware. The VBT is available via the ACPI OpRegion or, on older systems, in
the PCI ROM.

The VBT consists of a VBT Header (defined as \ :c:type:`struct vbt_header <vbt_header>`\ ), a BDB
Header (&struct bdb_header), and a number of BIOS Data Blocks (BDB) that
contain the actual configuration information. The VBT Header, and thus the
VBT, begins with "$VBT" signature. The VBT Header contains the offset of the
BDB Header. The data blocks are concatenated after the BDB Header. The data
blocks have a 1-byte Block ID, 2-byte Block Size, and Block Size bytes of
data. (Block 53, the MIPI Sequence Block is an exception.)

The driver parses the VBT during load. The relevant information is stored in
driver private data for ease of use, and the actual VBT is not read after
that.

.. _`intel_bios_is_valid_vbt`:

intel_bios_is_valid_vbt
=======================

.. c:function:: bool intel_bios_is_valid_vbt(const void *buf, size_t size)

    does the given buffer contain a valid VBT

    :param buf:
        pointer to a buffer to validate
    :type buf: const void \*

    :param size:
        size of the buffer
    :type size: size_t

.. _`intel_bios_is_valid_vbt.description`:

Description
-----------

Returns true on valid VBT.

.. _`intel_bios_init`:

intel_bios_init
===============

.. c:function:: void intel_bios_init(struct drm_i915_private *dev_priv)

    find VBT and initialize settings from the BIOS

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_bios_init.description`:

Description
-----------

Parse and initialize settings from the Video BIOS Tables (VBT). If the VBT
was not found in ACPI OpRegion, try to find it in PCI ROM first. Also
initialize some defaults if the VBT is not present at all.

.. _`intel_bios_cleanup`:

intel_bios_cleanup
==================

.. c:function:: void intel_bios_cleanup(struct drm_i915_private *dev_priv)

    Free any resources allocated by \ :c:func:`intel_bios_init`\ 

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_bios_is_tv_present`:

intel_bios_is_tv_present
========================

.. c:function:: bool intel_bios_is_tv_present(struct drm_i915_private *dev_priv)

    is integrated TV present in VBT

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

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

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param i2c_pin:
        i2c pin for LVDS if present
    :type i2c_pin: u8 \*

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

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param port:
        port to check
    :type port: enum port

.. _`intel_bios_is_port_present.description`:

Description
-----------

Return true if the device in \ ``port``\  is present.

.. _`intel_bios_is_port_edp`:

intel_bios_is_port_edp
======================

.. c:function:: bool intel_bios_is_port_edp(struct drm_i915_private *dev_priv, enum port port)

    is the device in given port eDP

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param port:
        port to check
    :type port: enum port

.. _`intel_bios_is_port_edp.description`:

Description
-----------

Return true if the device in \ ``port``\  is eDP.

.. _`intel_bios_is_dsi_present`:

intel_bios_is_dsi_present
=========================

.. c:function:: bool intel_bios_is_dsi_present(struct drm_i915_private *dev_priv, enum port *port)

    is DSI present in VBT

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param port:
        port for DSI if present
    :type port: enum port \*

.. _`intel_bios_is_dsi_present.description`:

Description
-----------

Return true if DSI is present, and return the port in \ ``port``\ .

.. _`intel_bios_is_port_hpd_inverted`:

intel_bios_is_port_hpd_inverted
===============================

.. c:function:: bool intel_bios_is_port_hpd_inverted(struct drm_i915_private *dev_priv, enum port port)

    is HPD inverted for \ ``port``\ 

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param port:
        port to check
    :type port: enum port

.. _`intel_bios_is_port_hpd_inverted.description`:

Description
-----------

Return true if HPD should be inverted for \ ``port``\ .

.. _`intel_bios_is_lspcon_present`:

intel_bios_is_lspcon_present
============================

.. c:function:: bool intel_bios_is_lspcon_present(struct drm_i915_private *dev_priv, enum port port)

    if LSPCON is attached on \ ``port``\ 

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param port:
        port to check
    :type port: enum port

.. _`intel_bios_is_lspcon_present.description`:

Description
-----------

Return true if LSPCON is present on this port

.. This file was automatic generated / don't edit.

