.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_rm.h

.. _`dpu_rm`:

struct dpu_rm
=============

.. c:type:: struct dpu_rm

    DPU dynamic hardware resource manager

.. _`dpu_rm.definition`:

Definition
----------

.. code-block:: c

    struct dpu_rm {
        struct drm_device *dev;
        struct list_head rsvps;
        struct list_head hw_blks[DPU_HW_BLK_MAX];
        struct dpu_hw_mdp *hw_mdp;
        uint32_t lm_max_width;
        uint32_t rsvp_next_seq;
        struct mutex rm_lock;
    }

.. _`dpu_rm.members`:

Members
-------

dev
    device handle for event logging purposes

rsvps
    list of hardware reservations by each crtc->encoder->connector

hw_blks
    array of lists of hardware resources present in the system, one
    list per type of hardware block

hw_mdp
    hardware object for mdp_top

lm_max_width
    cached layer mixer maximum width

rsvp_next_seq
    sequence number for next reservation for debugging purposes

rm_lock
    resource manager mutex

.. _`dpu_rm_hw_iter`:

struct dpu_rm_hw_iter
=====================

.. c:type:: struct dpu_rm_hw_iter

    iterator for use with dpu_rm

.. _`dpu_rm_hw_iter.definition`:

Definition
----------

.. code-block:: c

    struct dpu_rm_hw_iter {
        void *hw;
        struct dpu_rm_hw_blk *blk;
        uint32_t enc_id;
        enum dpu_hw_blk_type type;
    }

.. _`dpu_rm_hw_iter.members`:

Members
-------

hw
    dpu_hw object requested, or NULL on failure

blk
    dpu_rm internal block representation. Clients ignore. Used as iterator.

enc_id
    DRM ID of Encoder client wishes to search for, or 0 for Any Encoder

type
    Hardware Block Type client wishes to search for.

.. _`dpu_rm_init`:

dpu_rm_init
===========

.. c:function:: int dpu_rm_init(struct dpu_rm *rm, struct dpu_mdss_cfg *cat, void __iomem *mmio, struct drm_device *dev)

    Read hardware catalog and create reservation tracking objects for all HW blocks.

    :param rm:
        DPU Resource Manager handle
    :type rm: struct dpu_rm \*

    :param cat:
        Pointer to hardware catalog
    :type cat: struct dpu_mdss_cfg \*

    :param mmio:
        mapped register io address of MDP
    :type mmio: void __iomem \*

    :param dev:
        device handle for event logging purposes
    :type dev: struct drm_device \*

.. _`dpu_rm_destroy`:

dpu_rm_destroy
==============

.. c:function:: int dpu_rm_destroy(struct dpu_rm *rm)

    Free all memory allocated by dpu_rm_init

    :param rm:
        DPU Resource Manager handle
    :type rm: struct dpu_rm \*

.. _`dpu_rm_reserve`:

dpu_rm_reserve
==============

.. c:function:: int dpu_rm_reserve(struct dpu_rm *rm, struct drm_encoder *drm_enc, struct drm_crtc_state *crtc_state, struct msm_display_topology topology, bool test_only)

    Given a CRTC->Encoder->Connector display chain, analyze the use connections and user requirements, specified through related topology control properties, and reserve hardware blocks to that display chain. HW blocks can then be accessed through dpu_rm_get\_\* functions. HW Reservations should be released via dpu_rm_release_hw.

    :param rm:
        DPU Resource Manager handle
    :type rm: struct dpu_rm \*

    :param drm_enc:
        DRM Encoder handle
    :type drm_enc: struct drm_encoder \*

    :param crtc_state:
        Proposed Atomic DRM CRTC State handle
    :type crtc_state: struct drm_crtc_state \*

    :param topology:
        Pointer to topology info for the display
    :type topology: struct msm_display_topology

    :param test_only:
        Atomic-Test phase, discard results (unless property overrides)
    :type test_only: bool

.. _`dpu_rm_release`:

dpu_rm_release
==============

.. c:function:: void dpu_rm_release(struct dpu_rm *rm, struct drm_encoder *enc)

    Given the encoder for the display chain, release any HW blocks previously reserved for that use case.

    :param rm:
        DPU Resource Manager handle
    :type rm: struct dpu_rm \*

    :param enc:
        DRM Encoder handle
    :type enc: struct drm_encoder \*

.. _`dpu_rm_get_mdp`:

dpu_rm_get_mdp
==============

.. c:function:: struct dpu_hw_mdp *dpu_rm_get_mdp(struct dpu_rm *rm)

    Retrieve HW block for MDP TOP. This is never reserved, and is usable by any display.

    :param rm:
        DPU Resource Manager handle
    :type rm: struct dpu_rm \*

.. _`dpu_rm_init_hw_iter`:

dpu_rm_init_hw_iter
===================

.. c:function:: void dpu_rm_init_hw_iter(struct dpu_rm_hw_iter *iter, uint32_t enc_id, enum dpu_hw_blk_type type)

    setup given iterator for new iteration over hw list using dpu_rm_get_hw

    :param iter:
        iter object to initialize
    :type iter: struct dpu_rm_hw_iter \*

    :param enc_id:
        DRM ID of Encoder client wishes to search for, or 0 for Any Encoder
    :type enc_id: uint32_t

    :param type:
        Hardware Block Type client wishes to search for.
    :type type: enum dpu_hw_blk_type

.. _`dpu_rm_get_hw`:

dpu_rm_get_hw
=============

.. c:function:: bool dpu_rm_get_hw(struct dpu_rm *rm, struct dpu_rm_hw_iter *iter)

    retrieve reserved hw object given encoder and hw type Meant to do a single pass through the hardware list to iteratively retrieve hardware blocks of a given type for a given encoder. Initialize an iterator object. Set hw block type of interest. Set encoder id of interest, 0 for any. Function returns first hw of type for that encoder. Subsequent calls will return the next reserved hw of that type in-order. Iterator HW pointer will be null on failure to find hw.

    :param rm:
        DPU Resource Manager handle
    :type rm: struct dpu_rm \*

    :param iter:
        iterator object
    :type iter: struct dpu_rm_hw_iter \*

.. _`dpu_rm_check_property_topctl`:

dpu_rm_check_property_topctl
============================

.. c:function:: int dpu_rm_check_property_topctl(uint64_t val)

    validate property bitmask before it is set

    :param val:
        user's proposed topology control bitmask
    :type val: uint64_t

.. This file was automatic generated / don't edit.

