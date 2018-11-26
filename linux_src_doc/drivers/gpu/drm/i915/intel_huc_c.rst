.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_huc.c

.. _`intel_huc_auth`:

intel_huc_auth
==============

.. c:function:: int intel_huc_auth(struct intel_huc *huc)

    Authenticate HuC uCode

    :param huc:
        intel_huc structure
    :type huc: struct intel_huc \*

.. _`intel_huc_auth.description`:

Description
-----------

Called after HuC and GuC firmware loading during \ :c:func:`intel_uc_init_hw`\ .

This function pins HuC firmware image object into GGTT.
Then it invokes GuC action to authenticate passing the offset to RSA
signature through \ :c:func:`intel_guc_auth_huc`\ . It then waits for 50ms for
firmware verification ACK and unpins the object.

.. _`intel_huc_check_status`:

intel_huc_check_status
======================

.. c:function:: int intel_huc_check_status(struct intel_huc *huc)

    check HuC status

    :param huc:
        intel_huc structure
    :type huc: struct intel_huc \*

.. _`intel_huc_check_status.description`:

Description
-----------

This function reads status register to verify if HuC
firmware was successfully loaded.

Returns positive value if HuC firmware is loaded and verified
and -ENODEV if HuC is not present.

.. This file was automatic generated / don't edit.

