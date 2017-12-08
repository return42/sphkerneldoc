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

.. _`intel_huc_select_fw`:

intel_huc_select_fw
===================

.. c:function:: void intel_huc_select_fw(struct intel_huc *huc)

    selects HuC firmware for loading

    :param struct intel_huc \*huc:
        intel_huc struct

.. _`huc_ucode_xfer`:

huc_ucode_xfer
==============

.. c:function:: int huc_ucode_xfer(struct intel_uc_fw *huc_fw, struct i915_vma *vma)

    DMA's the firmware

    :param struct intel_uc_fw \*huc_fw:
        *undescribed*

    :param struct i915_vma \*vma:
        *undescribed*

.. _`huc_ucode_xfer.description`:

Description
-----------

Transfer the firmware image to RAM for execution by the microcontroller.

.. _`huc_ucode_xfer.return`:

Return
------

0 on success, non-zero on failure

.. _`intel_huc_init_hw`:

intel_huc_init_hw
=================

.. c:function:: void intel_huc_init_hw(struct intel_huc *huc)

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

.. _`intel_huc_auth`:

intel_huc_auth
==============

.. c:function:: void intel_huc_auth(struct intel_huc *huc)

    Authenticate HuC uCode

    :param struct intel_huc \*huc:
        intel_huc structure

.. _`intel_huc_auth.description`:

Description
-----------

Called after HuC and GuC firmware loading during \ :c:func:`intel_uc_init_hw`\ .

This function pins HuC firmware image object into GGTT.
Then it invokes GuC action to authenticate passing the offset to RSA
signature through \ :c:func:`intel_guc_auth_huc`\ . It then waits for 50ms for
firmware verification ACK and unpins the object.

.. This file was automatic generated / don't edit.

