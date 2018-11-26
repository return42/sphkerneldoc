.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_uc_fw.h

.. _`intel_uc_fw_get_upload_size`:

intel_uc_fw_get_upload_size
===========================

.. c:function:: u32 intel_uc_fw_get_upload_size(struct intel_uc_fw *uc_fw)

    Get size of firmware needed to be uploaded.

    :param uc_fw:
        uC firmware.
    :type uc_fw: struct intel_uc_fw \*

.. _`intel_uc_fw_get_upload_size.description`:

Description
-----------

Get the size of the firmware and header that will be uploaded to WOPCM.

.. _`intel_uc_fw_get_upload_size.return`:

Return
------

Upload firmware size, or zero on firmware fetch failure.

.. This file was automatic generated / don't edit.

