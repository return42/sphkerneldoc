.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_sprite.c

.. _`intel_pipe_update_start`:

intel_pipe_update_start
=======================

.. c:function:: void intel_pipe_update_start(const struct intel_crtc_state *new_crtc_state)

    start update of a set of display registers

    :param new_crtc_state:
        the new crtc state
    :type new_crtc_state: const struct intel_crtc_state \*

.. _`intel_pipe_update_start.description`:

Description
-----------

Mark the start of an update to pipe registers that should be updated
atomically regarding vblank. If the next vblank will happens within
the next 100 us, this function waits until the vblank passes.

After a successful call to this function, interrupts will be disabled
until a subsequent call to \ :c:func:`intel_pipe_update_end`\ . That is done to
avoid random delays.

.. _`intel_pipe_update_end`:

intel_pipe_update_end
=====================

.. c:function:: void intel_pipe_update_end(struct intel_crtc_state *new_crtc_state)

    end update of a set of display registers

    :param new_crtc_state:
        the new crtc state
    :type new_crtc_state: struct intel_crtc_state \*

.. _`intel_pipe_update_end.description`:

Description
-----------

Mark the end of an update started with \ :c:func:`intel_pipe_update_start`\ . This
re-enables interrupts and verifies the update was actually completed
before a vblank.

.. This file was automatic generated / don't edit.

