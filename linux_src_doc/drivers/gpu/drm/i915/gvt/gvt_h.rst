.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/gvt.h

.. _`intel_gvt_mmio_set_accessed`:

intel_gvt_mmio_set_accessed
===========================

.. c:function:: void intel_gvt_mmio_set_accessed(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO has been accessed

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_mmio_is_cmd_access`:

intel_gvt_mmio_is_cmd_access
============================

.. c:function:: bool intel_gvt_mmio_is_cmd_access(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO could be accessed by command

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_mmio_is_unalign`:

intel_gvt_mmio_is_unalign
=========================

.. c:function:: bool intel_gvt_mmio_is_unalign(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO could be accessed unaligned

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_mmio_set_cmd_accessed`:

intel_gvt_mmio_set_cmd_accessed
===============================

.. c:function:: void intel_gvt_mmio_set_cmd_accessed(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO has been accessed by command

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_mmio_has_mode_mask`:

intel_gvt_mmio_has_mode_mask
============================

.. c:function:: bool intel_gvt_mmio_has_mode_mask(struct intel_gvt *gvt, unsigned int offset)

    if a MMIO has a mode mask

    :param struct intel_gvt \*gvt:
        a GVT device

    :param unsigned int offset:
        register offset

.. _`intel_gvt_mmio_has_mode_mask.return`:

Return
------

True if a MMIO has a mode mask in its higher 16 bits, false if it isn't.

.. This file was automatic generated / don't edit.

