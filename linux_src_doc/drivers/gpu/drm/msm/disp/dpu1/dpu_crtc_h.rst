.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_crtc.h

.. _`dpu_crtc_client_type`:

enum dpu_crtc_client_type
=========================

.. c:type:: enum dpu_crtc_client_type

    crtc client type

.. _`dpu_crtc_client_type.definition`:

Definition
----------

.. code-block:: c

    enum dpu_crtc_client_type {
        RT_CLIENT,
        NRT_CLIENT
    };

.. _`dpu_crtc_client_type.constants`:

Constants
---------

RT_CLIENT
    RealTime client like video/cmd mode display
    voting through apps rsc

NRT_CLIENT
    Non-RealTime client like WB display
    voting through apps rsc

.. _`dpu_crtc_smmu_state`:

enum dpu_crtc_smmu_state
========================

.. c:type:: enum dpu_crtc_smmu_state

    smmu state

.. _`dpu_crtc_smmu_state.definition`:

Definition
----------

.. code-block:: c

    enum dpu_crtc_smmu_state {
        ATTACHED,
        DETACHED,
        ATTACH_ALL_REQ,
        DETACH_ALL_REQ
    };

.. _`dpu_crtc_smmu_state.constants`:

Constants
---------

ATTACHED
    all the context banks are attached.

DETACHED
    all the context banks are detached.

ATTACH_ALL_REQ
    transient state of attaching context banks.

DETACH_ALL_REQ
    transient state of detaching context banks.

.. _`dpu_crtc_smmu_state_transition_type`:

enum dpu_crtc_smmu_state_transition_type
========================================

.. c:type:: enum dpu_crtc_smmu_state_transition_type

    state transition type

.. _`dpu_crtc_smmu_state_transition_type.definition`:

Definition
----------

.. code-block:: c

    enum dpu_crtc_smmu_state_transition_type {
        NONE,
        PRE_COMMIT,
        POST_COMMIT
    };

.. _`dpu_crtc_smmu_state_transition_type.constants`:

Constants
---------

NONE
    no pending state transitions

PRE_COMMIT
    state transitions should be done before processing the commit

POST_COMMIT
    state transitions to be done after processing the commit.

.. _`dpu_crtc_smmu_state_data`:

struct dpu_crtc_smmu_state_data
===============================

.. c:type:: struct dpu_crtc_smmu_state_data

    stores the smmu state and transition type

.. _`dpu_crtc_smmu_state_data.definition`:

Definition
----------

.. code-block:: c

    struct dpu_crtc_smmu_state_data {
        uint32_t state;
        uint32_t transition_type;
        uint32_t transition_error;
    }

.. _`dpu_crtc_smmu_state_data.members`:

Members
-------

state
    current state of smmu context banks

transition_type
    transition request type

transition_error
    whether there is error while transitioning the state

.. _`dpu_crtc_mixer`:

struct dpu_crtc_mixer
=====================

.. c:type:: struct dpu_crtc_mixer

    stores the map for each virtual pipeline in the CRTC

.. _`dpu_crtc_mixer.definition`:

Definition
----------

.. code-block:: c

    struct dpu_crtc_mixer {
        struct dpu_hw_mixer *hw_lm;
        struct dpu_hw_ctl *lm_ctl;
        struct drm_encoder *encoder;
        u32 mixer_op_mode;
        u32 flush_mask;
    }

.. _`dpu_crtc_mixer.members`:

Members
-------

hw_lm
    LM HW Driver context

lm_ctl
    CTL Path HW driver context

encoder
    Encoder attached to this lm & ctl

mixer_op_mode
    mixer blending operation mode

flush_mask
    mixer flush mask for ctl, mixer and pipe

.. _`dpu_crtc_frame_event`:

struct dpu_crtc_frame_event
===========================

.. c:type:: struct dpu_crtc_frame_event

    stores crtc frame event for crtc processing

.. _`dpu_crtc_frame_event.definition`:

Definition
----------

.. code-block:: c

    struct dpu_crtc_frame_event {
        struct kthread_work work;
        struct drm_crtc *crtc;
        struct list_head list;
        ktime_t ts;
        u32 event;
    }

.. _`dpu_crtc_frame_event.members`:

Members
-------

work
    base work structure

crtc
    Pointer to crtc handling this event

list
    event list

ts
    timestamp at queue entry

event
    event identifier

.. _`dpu_crtc`:

struct dpu_crtc
===============

.. c:type:: struct dpu_crtc

    virtualized CRTC data structure

.. _`dpu_crtc.definition`:

Definition
----------

.. code-block:: c

    struct dpu_crtc {
        struct drm_crtc base;
        char name[DPU_CRTC_NAME_SIZE];
        struct drm_pending_vblank_event *event;
        u32 vsync_count;
        struct dpu_hw_stage_cfg stage_cfg;
        struct dentry *debugfs_root;
        u32 vblank_cb_count;
        u64 play_count;
        ktime_t vblank_cb_time;
        bool vblank_requested;
        bool suspend;
        bool enabled;
        struct list_head feature_list;
        struct list_head active_list;
        struct list_head dirty_list;
        struct list_head ad_dirty;
        struct list_head ad_active;
        struct mutex crtc_lock;
        atomic_t frame_pending;
        struct dpu_crtc_frame_event frame_events[DPU_CRTC_FRAME_EVENT_SIZE];
        struct list_head frame_event_list;
        spinlock_t spin_lock;
        struct completion frame_done_comp;
        spinlock_t event_lock;
        struct dpu_power_handle *phandle;
        struct dpu_power_event *power_event;
        struct dpu_core_perf_params cur_perf;
        struct dpu_crtc_smmu_state_data smmu_state;
    }

.. _`dpu_crtc.members`:

Members
-------

base
    Base drm crtc structure

name
    ASCII description of this crtc

event
    Pointer to last received drm vblank event. If there is a
    pending vblank event, this will be non-null.

vsync_count
    Running count of received vsync events

stage_cfg
    H/w mixer stage configuration

debugfs_root
    Parent of debugfs node

vblank_cb_count
    count of vblank callback since last reset

play_count
    frame count between crtc enable and disable

vblank_cb_time
    ktime at vblank count reset

vblank_requested
    whether the user has requested vblank events

suspend
    whether or not a suspend operation is in progress

enabled
    whether the DPU CRTC is currently enabled. updated in the
    commit-thread, not state-swap time which is earlier, so
    safe to make decisions on during VBLANK on/off work

feature_list
    list of color processing features supported on a crtc

active_list
    list of color processing features are active

dirty_list
    list of color processing features are dirty

ad_dirty
    list containing ad properties that are dirty

ad_active
    list containing ad properties that are active

crtc_lock
    crtc lock around create, destroy and access.

frame_pending
    Whether or not an update is pending

frame_events
    static allocation of in-flight frame events

frame_event_list
    available frame event list

spin_lock
    spin lock for frame event, transaction status, etc...

frame_done_comp
    for frame_event_done synchronization

event_lock
    Spinlock around event handling code

phandle
    Pointer to power handler

power_event
    registered power event handle

cur_perf
    current performance committed to clock/bandwidth driver

smmu_state
    *undescribed*

.. _`dpu_crtc_state`:

struct dpu_crtc_state
=====================

.. c:type:: struct dpu_crtc_state

    dpu container for atomic crtc state

.. _`dpu_crtc_state.definition`:

Definition
----------

.. code-block:: c

    struct dpu_crtc_state {
        struct drm_crtc_state base;
        bool bw_control;
        bool bw_split_vote;
        struct drm_rect lm_bounds[CRTC_DUAL_MIXERS];
        uint64_t input_fence_timeout_ns;
        struct dpu_core_perf_params new_perf;
        u32 num_mixers;
        struct dpu_crtc_mixer mixers[CRTC_DUAL_MIXERS];
        u32 num_ctls;
        struct dpu_hw_ctl *hw_ctls[CRTC_DUAL_MIXERS];
    }

.. _`dpu_crtc_state.members`:

Members
-------

base
    Base drm crtc state structure

bw_control
    true if bw/clk controlled by core bw/clk properties

bw_split_vote
    true if bw controlled by llcc/dram bw properties

lm_bounds
    LM boundaries based on current mode full resolution, no ROI.
    Origin top left of CRTC.

input_fence_timeout_ns
    Cached input fence timeout, in ns

new_perf
    new performance state being requested

num_mixers
    Number of mixers in use

mixers
    List of active mixers

num_ctls
    Number of ctl paths in use

hw_ctls
    List of active ctl paths

.. _`dpu_crtc_state_is_stereo`:

dpu_crtc_state_is_stereo
========================

.. c:function:: bool dpu_crtc_state_is_stereo(struct dpu_crtc_state *cstate)

    Is crtc virtualized with two mixers?

    :param cstate:
        Pointer to dpu crtc state
    :type cstate: struct dpu_crtc_state \*

.. _`dpu_crtc_get_mixer_height`:

dpu_crtc_get_mixer_height
=========================

.. c:function:: int dpu_crtc_get_mixer_height(struct dpu_crtc *dpu_crtc, struct dpu_crtc_state *cstate, struct drm_display_mode *mode)

    get the mixer height Mixer height will be same as panel height

    :param dpu_crtc:
        *undescribed*
    :type dpu_crtc: struct dpu_crtc \*

    :param cstate:
        *undescribed*
    :type cstate: struct dpu_crtc_state \*

    :param mode:
        *undescribed*
    :type mode: struct drm_display_mode \*

.. _`dpu_crtc_frame_pending`:

dpu_crtc_frame_pending
======================

.. c:function:: int dpu_crtc_frame_pending(struct drm_crtc *crtc)

    retun the number of pending frames

    :param crtc:
        Pointer to drm crtc object
    :type crtc: struct drm_crtc \*

.. _`dpu_crtc_vblank`:

dpu_crtc_vblank
===============

.. c:function:: int dpu_crtc_vblank(struct drm_crtc *crtc, bool en)

    enable or disable vblanks for this crtc

    :param crtc:
        Pointer to drm crtc object
    :type crtc: struct drm_crtc \*

    :param en:
        true to enable vblanks, false to disable
    :type en: bool

.. _`dpu_crtc_commit_kickoff`:

dpu_crtc_commit_kickoff
=======================

.. c:function:: void dpu_crtc_commit_kickoff(struct drm_crtc *crtc)

    trigger kickoff of the commit for this crtc

    :param crtc:
        Pointer to drm crtc object
    :type crtc: struct drm_crtc \*

.. _`dpu_crtc_complete_commit`:

dpu_crtc_complete_commit
========================

.. c:function:: void dpu_crtc_complete_commit(struct drm_crtc *crtc, struct drm_crtc_state *old_state)

    callback signalling completion of current commit

    :param crtc:
        Pointer to drm crtc object
    :type crtc: struct drm_crtc \*

    :param old_state:
        Pointer to drm crtc old state object
    :type old_state: struct drm_crtc_state \*

.. _`dpu_crtc_init`:

dpu_crtc_init
=============

.. c:function:: struct drm_crtc *dpu_crtc_init(struct drm_device *dev, struct drm_plane *plane, struct drm_plane *cursor)

    create a new crtc object

    :param dev:
        dpu device
    :type dev: struct drm_device \*

    :param plane:
        base plane
    :type plane: struct drm_plane \*

    :param cursor:
        cursor plane
    :type cursor: struct drm_plane \*

.. _`dpu_crtc_register_custom_event`:

dpu_crtc_register_custom_event
==============================

.. c:function:: int dpu_crtc_register_custom_event(struct dpu_kms *kms, struct drm_crtc *crtc_drm, u32 event, bool en)

    api for enabling/disabling crtc event

    :param kms:
        Pointer to dpu_kms
    :type kms: struct dpu_kms \*

    :param crtc_drm:
        Pointer to crtc object
    :type crtc_drm: struct drm_crtc \*

    :param event:
        Event that client is interested
    :type event: u32

    :param en:
        Flag to enable/disable the event
    :type en: bool

.. _`dpu_crtc_get_intf_mode`:

dpu_crtc_get_intf_mode
======================

.. c:function:: enum dpu_intf_mode dpu_crtc_get_intf_mode(struct drm_crtc *crtc)

    get interface mode of the given crtc

    :param crtc:
        Pointert to crtc
    :type crtc: struct drm_crtc \*

.. _`dpu_crtc_get_client_type`:

dpu_crtc_get_client_type
========================

.. c:function:: enum dpu_crtc_client_type dpu_crtc_get_client_type(struct drm_crtc *crtc)

    check the crtc type- rt, nrt etc.

    :param crtc:
        Pointer to crtc
    :type crtc: struct drm_crtc \*

.. _`dpu_crtc_is_enabled`:

dpu_crtc_is_enabled
===================

.. c:function:: bool dpu_crtc_is_enabled(struct drm_crtc *crtc)

    check if dpu crtc is enabled or not

    :param crtc:
        Pointer to crtc
    :type crtc: struct drm_crtc \*

.. This file was automatic generated / don't edit.

