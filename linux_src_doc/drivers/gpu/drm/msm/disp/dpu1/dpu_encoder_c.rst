.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_encoder.c

.. _`dpu_enc_rc_events`:

enum dpu_enc_rc_events
======================

.. c:type:: enum dpu_enc_rc_events

    events for resource control state machine

.. _`dpu_enc_rc_events.definition`:

Definition
----------

.. code-block:: c

    enum dpu_enc_rc_events {
        DPU_ENC_RC_EVENT_KICKOFF,
        DPU_ENC_RC_EVENT_FRAME_DONE,
        DPU_ENC_RC_EVENT_PRE_STOP,
        DPU_ENC_RC_EVENT_STOP,
        DPU_ENC_RC_EVENT_ENTER_IDLE
    };

.. _`dpu_enc_rc_events.constants`:

Constants
---------

DPU_ENC_RC_EVENT_KICKOFF
    This event happens at NORMAL priority.
    Event that signals the start of the transfer. When this event is
    received, enable MDP/DSI core clocks. Regardless of the previous
    state, the resource should be in ON state at the end of this event.

DPU_ENC_RC_EVENT_FRAME_DONE
    This event happens at INTERRUPT level.
    Event signals the end of the data transfer after the PP FRAME_DONE
    event. At the end of this event, a delayed work is scheduled to go to
    IDLE_PC state after IDLE_TIMEOUT time.

DPU_ENC_RC_EVENT_PRE_STOP
    This event happens at NORMAL priority.
    This event, when received during the ON state, leave the RC STATE
    in the PRE_OFF state. It should be followed by the STOP event as
    part of encoder disable.
    If received during IDLE or OFF states, it will do nothing.

DPU_ENC_RC_EVENT_STOP
    This event happens at NORMAL priority.
    When this event is received, disable all the MDP/DSI core clocks, and
    disable IRQs. It should be called from the PRE_OFF or IDLE states.
    IDLE is expected when IDLE_PC has run, and PRE_OFF did nothing.
    PRE_OFF is expected when PRE_STOP was executed during the ON state.
    Resource state should be in OFF at the end of the event.

DPU_ENC_RC_EVENT_ENTER_IDLE
    This event happens at NORMAL priority from a work item.
    Event signals that there were no frame updates for IDLE_TIMEOUT time.
    This would disable MDP/DSI core clocks and change the resource state
    to IDLE.

.. _`dpu_encoder_virt`:

struct dpu_encoder_virt
=======================

.. c:type:: struct dpu_encoder_virt

    virtual encoder. Container of one or more physical encoders. Virtual encoder manages one "logical" display. Physical encoders manage one intf block, tied to a specific panel/sub-panel. Virtual encoder defers as much as possible to the physical encoders. Virtual encoder registers itself with the DRM Framework as the encoder.

.. _`dpu_encoder_virt.definition`:

Definition
----------

.. code-block:: c

    struct dpu_encoder_virt {
        struct drm_encoder base;
        spinlock_t enc_spinlock;
        uint32_t bus_scaling_client;
        unsigned int num_phys_encs;
        struct dpu_encoder_phys *phys_encs[MAX_PHYS_ENCODERS_PER_VIRTUAL];
        struct dpu_encoder_phys *cur_master;
        struct dpu_encoder_phys *cur_slave;
        struct dpu_hw_pingpong *hw_pp[MAX_CHANNELS_PER_ENC];
        bool intfs_swapped;
        void (*crtc_vblank_cb)(void *);
        void *crtc_vblank_cb_data;
        struct dentry *debugfs_root;
        struct mutex enc_lock;
        DECLARE_BITMAP(frame_busy_mask, MAX_PHYS_ENCODERS_PER_VIRTUAL);
        void (*crtc_frame_event_cb)(void *, u32 event);
        void *crtc_frame_event_cb_data;
        atomic_t frame_done_timeout;
        struct timer_list frame_done_timer;
        struct timer_list vsync_event_timer;
        struct msm_display_info disp_info;
        bool idle_pc_supported;
        struct mutex rc_lock;
        enum dpu_enc_rc_states rc_state;
        struct kthread_delayed_work delayed_off_work;
        struct kthread_work vsync_event_work;
        struct msm_display_topology topology;
        bool mode_set_complete;
        u32 idle_timeout;
    }

.. _`dpu_encoder_virt.members`:

Members
-------

base
    drm_encoder base class for registration with DRM

enc_spinlock
    *undescribed*

bus_scaling_client
    Client handle to the bus scaling interface

num_phys_encs
    Actual number of physical encoders contained.

phys_encs
    Container of physical encoders managed.

cur_master
    Pointer to the current master in this mode. Optimization
    Only valid after enable. Cleared as disable.
    \ ``hw_pp``\                Handle to the pingpong blocks used for the display. No.
    pingpong blocks can be different than num_phys_encs.
    \ ``intfs_swapped``\        Whether or not the phys_enc interfaces have been swapped
    for partial update right-only cases, such as pingpong
    split where virtual pingpong does not generate IRQs

cur_slave
    *undescribed*

hw_pp
    *undescribed*

intfs_swapped
    *undescribed*

crtc_vblank_cb
    Callback into the upper layer / CRTC for
    notification of the VBLANK

crtc_vblank_cb_data
    Data from upper layer for VBLANK notification

debugfs_root
    Debug file system root file node

enc_lock
    Lock around physical encoder create/destroy and

frame_busy_mask
    Bitmask tracking which phys_enc we are still
    busy processing current command.
    Bit0 = phys_encs[0] etc.

crtc_frame_event_cb
    callback handler for frame event

crtc_frame_event_cb_data
    callback handler private data

frame_done_timeout
    frame done timeout in Hz

frame_done_timer
    watchdog timer for frame done event

vsync_event_timer
    vsync timer

disp_info
    local copy of msm_display_info struct

idle_pc_supported
    indicate if idle power collaps is supported

rc_lock
    resource control mutex lock to protect
    virt encoder over various state changes

rc_state
    resource controller state

delayed_off_work
    delayed worker to schedule disabling of
    clks and resources after IDLE_TIMEOUT time.

vsync_event_work
    worker to handle vsync event for autorefresh

topology
    topology of the display

mode_set_complete
    flag to indicate modeset completion

idle_timeout
    idle timeout duration in milliseconds

.. _`_dpu_encoder_trigger_flush`:

\_dpu_encoder_trigger_flush
===========================

.. c:function:: void _dpu_encoder_trigger_flush(struct drm_encoder *drm_enc, struct dpu_encoder_phys *phys, uint32_t extra_flush_bits)

    trigger flush for a physical encoder

    :param drm_enc:
        *undescribed*
    :type drm_enc: struct drm_encoder \*

    :param phys:
        *undescribed*
    :type phys: struct dpu_encoder_phys \*

    :param extra_flush_bits:
        *undescribed*
    :type extra_flush_bits: uint32_t

.. _`_dpu_encoder_trigger_flush.drm_enc`:

drm_enc
-------

Pointer to drm encoder structure

.. _`_dpu_encoder_trigger_flush.phys`:

phys
----

Pointer to physical encoder structure

.. _`_dpu_encoder_trigger_flush.extra_flush_bits`:

extra_flush_bits
----------------

Additional bit mask to include in flush trigger

.. _`_dpu_encoder_trigger_start`:

\_dpu_encoder_trigger_start
===========================

.. c:function:: void _dpu_encoder_trigger_start(struct dpu_encoder_phys *phys)

    trigger start for a physical encoder

    :param phys:
        *undescribed*
    :type phys: struct dpu_encoder_phys \*

.. _`_dpu_encoder_trigger_start.phys`:

phys
----

Pointer to physical encoder structure

.. _`_dpu_encoder_kickoff_phys`:

\_dpu_encoder_kickoff_phys
==========================

.. c:function:: void _dpu_encoder_kickoff_phys(struct dpu_encoder_virt *dpu_enc)

    handle physical encoder kickoff Iterate through the physical encoders and perform consolidated flush and/or control start triggering as needed. This is done in the virtual encoder rather than the individual physical ones in order to handle use cases that require visibility into multiple physical encoders at a time.

    :param dpu_enc:
        *undescribed*
    :type dpu_enc: struct dpu_encoder_virt \*

.. _`_dpu_encoder_kickoff_phys.dpu_enc`:

dpu_enc
-------

Pointer to virtual encoder structure

.. This file was automatic generated / don't edit.

