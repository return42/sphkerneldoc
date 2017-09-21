.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_guc_ct.c

.. _`intel_guc_enable_ct`:

intel_guc_enable_ct
===================

.. c:function:: int intel_guc_enable_ct(struct intel_guc *guc)

    Shall only be called for platforms with HAS_GUC_CT.

    :param struct intel_guc \*guc:
        the guc

.. _`intel_guc_enable_ct.return`:

Return
------

0 on success
non-zero on failure

.. _`intel_guc_disable_ct`:

intel_guc_disable_ct
====================

.. c:function:: void intel_guc_disable_ct(struct intel_guc *guc)

    Shall only be called for platforms with HAS_GUC_CT.

    :param struct intel_guc \*guc:
        the guc

.. This file was automatic generated / don't edit.

