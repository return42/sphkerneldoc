.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_huc.c

.. _`huc-firmware`:

HuC Firmware
============

Motivation:
GEN9 introduces a new dedicated firmware for usage in media HEVC (High
Efficiency Video Coding) operations. Userspace can use the firmware
capabilities by adding HuC specific commands to batch buffers.

Implementation:
The same firmware loader is used as the GuC. However, the actual
loading to HW is deferred until GEM initialization is done.

Note that HuC firmware loading must be done before GuC loading.

.. _`huc_ucode_xfer`:

huc_ucode_xfer
==============

.. c:function:: int huc_ucode_xfer(struct drm_i915_private *dev_priv)

    DMA's the firmware

    :param struct drm_i915_private \*dev_priv:
        the drm_i915_private device

.. _`huc_ucode_xfer.description`:

Description
-----------

Transfer the firmware image to RAM for execution by the microcontroller.

.. _`huc_ucode_xfer.return`:

Return
------

0 on success, non-zero on failure

.. _`intel_huc_select_fw`:

intel_huc_select_fw
===================

.. c:function:: void intel_huc_select_fw(struct intel_huc *huc)

    selects HuC firmware for loading

    :param struct intel_huc \*huc:
        intel_huc struct

.. _`intel_huc_init_hw`:

intel_huc_init_hw
=================

.. c:function:: int intel_huc_init_hw(struct intel_huc *huc)

    load HuC uCode to device

    :param struct intel_huc \*huc:
        intel_huc structure

.. _`intel_huc_init_hw.description`:

Description
-----------

Called from \ :c:func:`guc_setup`\  during driver loading and also after a GPU reset.
Be note that HuC loading must be done before GuC loading.

The firmware image should have already been fetched into memory by the
earlier call to \ :c:func:`intel_huc_init`\ , so here we need only check that
is succeeded, and then transfer the image to the h/w.

.. _`intel_huc_init_hw.return`:

Return
------

non-zero code on error

.. _`intel_guc_auth_huc`:

intel_guc_auth_huc
==================

.. c:function:: void intel_guc_auth_huc(struct drm_i915_private *dev_priv)

    authenticate ucode

    :param struct drm_i915_private \*dev_priv:
        the drm_i915_device

.. _`intel_guc_auth_huc.description`:

Description
-----------

Triggers a HuC fw authentication request to the GuC via intel_guc_action\_
authenticate_huc interface.

.. This file was automatic generated / don't edit.

