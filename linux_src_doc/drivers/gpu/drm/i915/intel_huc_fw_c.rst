.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_huc_fw.c

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

.. _`intel_huc_fw_init_early`:

intel_huc_fw_init_early
=======================

.. c:function:: void intel_huc_fw_init_early(struct intel_huc *huc)

    initializes HuC firmware struct

    :param struct intel_huc \*huc:
        intel_huc struct

.. _`intel_huc_fw_init_early.description`:

Description
-----------

On platforms with HuC selects firmware for uploading

.. _`huc_fw_xfer`:

huc_fw_xfer
===========

.. c:function:: int huc_fw_xfer(struct intel_uc_fw *huc_fw, struct i915_vma *vma)

    DMA's the firmware

    :param struct intel_uc_fw \*huc_fw:
        the firmware descriptor

    :param struct i915_vma \*vma:
        the firmware image (bound into the GGTT)

.. _`huc_fw_xfer.description`:

Description
-----------

Transfer the firmware image to RAM for execution by the microcontroller.

.. _`huc_fw_xfer.return`:

Return
------

0 on success, non-zero on failure

.. _`intel_huc_fw_upload`:

intel_huc_fw_upload
===================

.. c:function:: int intel_huc_fw_upload(struct intel_huc *huc)

    load HuC uCode to device

    :param struct intel_huc \*huc:
        intel_huc structure

.. _`intel_huc_fw_upload.description`:

Description
-----------

Called from \ :c:func:`intel_uc_init_hw`\  during driver load, resume from sleep and
after a GPU reset. Note that HuC must be loaded before GuC.

The firmware image should have already been fetched into memory, so only
check that fetch succeeded, and then transfer the image to the h/w.

.. _`intel_huc_fw_upload.return`:

Return
------

non-zero code on error

.. This file was automatic generated / don't edit.

