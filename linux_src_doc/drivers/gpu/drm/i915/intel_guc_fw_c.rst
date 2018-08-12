.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_guc_fw.c

.. _`intel_guc_fw_init_early`:

intel_guc_fw_init_early
=======================

.. c:function:: void intel_guc_fw_init_early(struct intel_guc *guc)

    initializes GuC firmware struct

    :param struct intel_guc \*guc:
        intel_guc struct

.. _`intel_guc_fw_init_early.description`:

Description
-----------

On platforms with GuC selects firmware for uploading

.. _`intel_guc_fw_upload`:

intel_guc_fw_upload
===================

.. c:function:: int intel_guc_fw_upload(struct intel_guc *guc)

    load GuC uCode to device

    :param struct intel_guc \*guc:
        intel_guc structure

.. _`intel_guc_fw_upload.description`:

Description
-----------

Called from \ :c:func:`intel_uc_init_hw`\  during driver load, resume from sleep and
after a GPU reset.

The firmware image should have already been fetched into memory, so only
check that fetch succeeded, and then transfer the image to the h/w.

.. _`intel_guc_fw_upload.return`:

Return
------

non-zero code on error

.. This file was automatic generated / don't edit.

