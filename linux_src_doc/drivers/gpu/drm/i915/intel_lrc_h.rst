.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_lrc.h

.. _`intel_logical_ring_advance`:

intel_logical_ring_advance
==========================

.. c:function:: void intel_logical_ring_advance(struct intel_ringbuffer *ringbuf)

    advance the ringbuffer tail

    :param struct intel_ringbuffer \*ringbuf:
        Ringbuffer to advance.

.. _`intel_logical_ring_advance.description`:

Description
-----------

The tail is only updated in our logical ringbuffer struct.

.. _`intel_logical_ring_emit`:

intel_logical_ring_emit
=======================

.. c:function:: void intel_logical_ring_emit(struct intel_ringbuffer *ringbuf, u32 data)

    write a DWORD to the ringbuffer.

    :param struct intel_ringbuffer \*ringbuf:
        Ringbuffer to write to.

    :param u32 data:
        DWORD to write.

.. This file was automatic generated / don't edit.

