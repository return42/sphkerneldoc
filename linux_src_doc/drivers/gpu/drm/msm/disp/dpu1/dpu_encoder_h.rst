.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_encoder.h

.. _`dpu_encoder_get_hw_resources`:

dpu_encoder_get_hw_resources
============================

.. c:function:: void dpu_encoder_get_hw_resources(struct drm_encoder *encoder, struct dpu_encoder_hw_resources *hw_res)

    Populate table of required hardware resources

    :param encoder:
        encoder pointer
    :type encoder: struct drm_encoder \*

    :param hw_res:
        resource table to populate with encoder required resources
    :type hw_res: struct dpu_encoder_hw_resources \*

.. _`dpu_encoder_register_vblank_callback`:

dpu_encoder_register_vblank_callback
====================================

.. c:function:: void dpu_encoder_register_vblank_callback(struct drm_encoder *encoder, void (*cb)(void *), void *data)

    provide callback to encoder that will be called on the next vblank.

    :param encoder:
        encoder pointer
    :type encoder: struct drm_encoder \*

    :param void (\*cb)(void \*):
        callback pointer, provide NULL to deregister and disable IRQs

    :param data:
        user data provided to callback
    :type data: void \*

.. _`dpu_encoder_register_frame_event_callback`:

dpu_encoder_register_frame_event_callback
=========================================

.. c:function:: void dpu_encoder_register_frame_event_callback(struct drm_encoder *encoder, void (*cb)(void *, u32), void *data)

    provide callback to encoder that will be called after the request is complete, or other events.

    :param encoder:
        encoder pointer
    :type encoder: struct drm_encoder \*

    :param void (\*cb)(void \*, u32):
        callback pointer, provide NULL to deregister

    :param data:
        user data provided to callback
    :type data: void \*

.. _`dpu_encoder_prepare_for_kickoff`:

dpu_encoder_prepare_for_kickoff
===============================

.. c:function:: void dpu_encoder_prepare_for_kickoff(struct drm_encoder *encoder, struct dpu_encoder_kickoff_params *params)

    schedule double buffer flip of the ctl path (i.e. ctl flush and start) at next appropriate time.

    :param encoder:
        encoder pointer
    :type encoder: struct drm_encoder \*

    :param params:
        kickoff time parameters
    :type params: struct dpu_encoder_kickoff_params \*

.. _`dpu_encoder_prepare_for_kickoff.immediately`:

Immediately
-----------

if no previous commit is outstanding.

.. _`dpu_encoder_prepare_for_kickoff.delayed`:

Delayed
-------

Block until next trigger can be issued.

.. _`dpu_encoder_trigger_kickoff_pending`:

dpu_encoder_trigger_kickoff_pending
===================================

.. c:function:: void dpu_encoder_trigger_kickoff_pending(struct drm_encoder *encoder)

    Clear the flush bits from previous kickoff and trigger the ctl prepare progress for command mode display.

    :param encoder:
        encoder pointer
    :type encoder: struct drm_encoder \*

.. _`dpu_encoder_kickoff`:

dpu_encoder_kickoff
===================

.. c:function:: void dpu_encoder_kickoff(struct drm_encoder *encoder)

    trigger a double buffer flip of the ctl path (i.e. ctl flush and start) immediately.

    :param encoder:
        encoder pointer
    :type encoder: struct drm_encoder \*

.. _`dpu_encoder_wait_for_event`:

dpu_encoder_wait_for_event
==========================

.. c:function:: int dpu_encoder_wait_for_event(struct drm_encoder *drm_encoder, enum msm_event_wait event)

    Waits for encoder events

    :param drm_encoder:
        *undescribed*
    :type drm_encoder: struct drm_encoder \*

    :param event:
        event to wait for
        MSM_ENC_COMMIT_DONE -  Wait for hardware to have flushed the current pending
        frames to hardware at a vblank or ctl_start
        Encoders will map this differently depending on the
        panel type.
        vid mode -> vsync_irq
        cmd mode -> ctl_start
        MSM_ENC_TX_COMPLETE -  Wait for the hardware to transfer all the pixels to
        the panel. Encoders will map this differently
        depending on the panel type.
        vid mode -> vsync_irq
        cmd mode -> pp_done
    :type event: enum msm_event_wait

.. _`dpu_encoder_wait_for_event.return`:

Return
------

0 on success, -EWOULDBLOCK if already signaled, error otherwise

.. _`dpu_encoder_virt_restore`:

dpu_encoder_virt_restore
========================

.. c:function:: void dpu_encoder_virt_restore(struct drm_encoder *encoder)

    restore the encoder configs

    :param encoder:
        encoder pointer
    :type encoder: struct drm_encoder \*

.. _`dpu_encoder_init`:

dpu_encoder_init
================

.. c:function:: struct drm_encoder *dpu_encoder_init(struct drm_device *dev, int drm_enc_mode)

    initialize virtual encoder object

    :param dev:
        Pointer to drm device structure
    :type dev: struct drm_device \*

    :param drm_enc_mode:
        *undescribed*
    :type drm_enc_mode: int

.. _`dpu_encoder_init.return`:

Return
------

Pointer to newly created drm encoder

.. _`dpu_encoder_setup`:

dpu_encoder_setup
=================

.. c:function:: int dpu_encoder_setup(struct drm_device *dev, struct drm_encoder *enc, struct msm_display_info *disp_info)

    setup dpu_encoder for the display probed

    :param dev:
        Pointer to drm device structure
    :type dev: struct drm_device \*

    :param enc:
        Pointer to the drm_encoder
    :type enc: struct drm_encoder \*

    :param disp_info:
        Pointer to the display info
    :type disp_info: struct msm_display_info \*

.. _`dpu_encoder_prepare_commit`:

dpu_encoder_prepare_commit
==========================

.. c:function:: void dpu_encoder_prepare_commit(struct drm_encoder *drm_enc)

    prepare encoder at the very beginning of an atomic commit, before any registers are written

    :param drm_enc:
        Pointer to previously created drm encoder structure
    :type drm_enc: struct drm_encoder \*

.. _`dpu_encoder_set_idle_timeout`:

dpu_encoder_set_idle_timeout
============================

.. c:function:: void dpu_encoder_set_idle_timeout(struct drm_encoder *drm_enc, u32 idle_timeout)

    set the idle timeout for video and command mode encoders.

    :param drm_enc:
        Pointer to previously created drm encoder structure
    :type drm_enc: struct drm_encoder \*

    :param idle_timeout:
        idle timeout duration in milliseconds
    :type idle_timeout: u32

.. This file was automatic generated / don't edit.

