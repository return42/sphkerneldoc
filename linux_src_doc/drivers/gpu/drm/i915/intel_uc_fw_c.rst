.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_uc_fw.c

.. _`intel_uc_fw_fetch`:

intel_uc_fw_fetch
=================

.. c:function:: void intel_uc_fw_fetch(struct drm_i915_private *dev_priv, struct intel_uc_fw *uc_fw)

    fetch uC firmware

    :param struct drm_i915_private \*dev_priv:
        device private

    :param struct intel_uc_fw \*uc_fw:
        uC firmware

.. _`intel_uc_fw_fetch.description`:

Description
-----------

Fetch uC firmware into GEM obj.

.. _`intel_uc_fw_upload`:

intel_uc_fw_upload
==================

.. c:function:: int intel_uc_fw_upload(struct intel_uc_fw *uc_fw, int (*xfer)(struct intel_uc_fw *uc_fw, struct i915_vma *vma))

    load uC firmware using custom loader

    :param struct intel_uc_fw \*uc_fw:
        uC firmware

    :param int (\*xfer)(struct intel_uc_fw \*uc_fw, struct i915_vma \*vma):
        custom uC firmware loader function

.. _`intel_uc_fw_upload.description`:

Description
-----------

Loads uC firmware using custom loader and updates internal flags.

.. _`intel_uc_fw_upload.return`:

Return
------

0 on success, non-zero on failure.

.. _`intel_uc_fw_fini`:

intel_uc_fw_fini
================

.. c:function:: void intel_uc_fw_fini(struct intel_uc_fw *uc_fw)

    cleanup uC firmware

    :param struct intel_uc_fw \*uc_fw:
        uC firmware

.. _`intel_uc_fw_fini.description`:

Description
-----------

Cleans up uC firmware by releasing the firmware GEM obj.

.. _`intel_uc_fw_dump`:

intel_uc_fw_dump
================

.. c:function:: void intel_uc_fw_dump(const struct intel_uc_fw *uc_fw, struct drm_printer *p)

    dump information about uC firmware

    :param const struct intel_uc_fw \*uc_fw:
        uC firmware

    :param struct drm_printer \*p:
        the \ :c:type:`struct drm_printer <drm_printer>`\ 

.. _`intel_uc_fw_dump.description`:

Description
-----------

Pretty printer for uC firmware.

.. This file was automatic generated / don't edit.

