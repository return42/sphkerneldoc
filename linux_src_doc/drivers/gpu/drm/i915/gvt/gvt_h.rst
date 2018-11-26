.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/gvt.h

.. _`intel_gvt_mmio_set_accessed`:

intel_gvt_mmio_set_accessed
===========================

.. c:function:: void intel_gvt_mmio_set_accessed(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO has been accessed

    :param gvt:
        a GVT device
    :type gvt: struct intel_gvt \*

    :param offset:
        register offset
    :type offset: unsigned int

.. _`intel_gvt_mmio_is_cmd_access`:

intel_gvt_mmio_is_cmd_access
============================

.. c:function:: bool intel_gvt_mmio_is_cmd_access(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO could be accessed by command

    :param gvt:
        a GVT device
    :type gvt: struct intel_gvt \*

    :param offset:
        register offset
    :type offset: unsigned int

.. _`intel_gvt_mmio_is_unalign`:

intel_gvt_mmio_is_unalign
=========================

.. c:function:: bool intel_gvt_mmio_is_unalign(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO could be accessed unaligned

    :param gvt:
        a GVT device
    :type gvt: struct intel_gvt \*

    :param offset:
        register offset
    :type offset: unsigned int

.. _`intel_gvt_mmio_set_cmd_accessed`:

intel_gvt_mmio_set_cmd_accessed
===============================

.. c:function:: void intel_gvt_mmio_set_cmd_accessed(struct intel_gvt *gvt, unsigned int offset)

    mark a MMIO has been accessed by command

    :param gvt:
        a GVT device
    :type gvt: struct intel_gvt \*

    :param offset:
        register offset
    :type offset: unsigned int

.. _`intel_gvt_mmio_has_mode_mask`:

intel_gvt_mmio_has_mode_mask
============================

.. c:function:: bool intel_gvt_mmio_has_mode_mask(struct intel_gvt *gvt, unsigned int offset)

    if a MMIO has a mode mask

    :param gvt:
        a GVT device
    :type gvt: struct intel_gvt \*

    :param offset:
        register offset
    :type offset: unsigned int

.. _`intel_gvt_mmio_has_mode_mask.return`:

Return
------

True if a MMIO has a mode mask in its higher 16 bits, false if it isn't.

.. _`intel_gvt_mmio_is_in_ctx`:

intel_gvt_mmio_is_in_ctx
========================

.. c:function:: bool intel_gvt_mmio_is_in_ctx(struct intel_gvt *gvt, unsigned int offset)

    check if a MMIO has in-ctx mask

    :param gvt:
        a GVT device
    :type gvt: struct intel_gvt \*

    :param offset:
        register offset
    :type offset: unsigned int

.. _`intel_gvt_mmio_is_in_ctx.return`:

Return
------

True if a MMIO has a in-context mask, false if it isn't.

.. _`intel_gvt_mmio_set_in_ctx`:

intel_gvt_mmio_set_in_ctx
=========================

.. c:function:: void intel_gvt_mmio_set_in_ctx(struct intel_gvt *gvt, unsigned int offset)

    mask a MMIO in logical context

    :param gvt:
        a GVT device
    :type gvt: struct intel_gvt \*

    :param offset:
        register offset
    :type offset: unsigned int

.. This file was automatic generated / don't edit.

