.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_rm.c

.. _`dpu_rm_requirements`:

struct dpu_rm_requirements
==========================

.. c:type:: struct dpu_rm_requirements

    Reservation requirements parameter bundle

.. _`dpu_rm_requirements.definition`:

Definition
----------

.. code-block:: c

    struct dpu_rm_requirements {
        struct msm_display_topology topology;
        struct dpu_encoder_hw_resources hw_res;
    }

.. _`dpu_rm_requirements.members`:

Members
-------

topology
    selected topology for the display

hw_res
    Hardware resources required as reported by the encoders

.. _`dpu_rm_rsvp`:

struct dpu_rm_rsvp
==================

.. c:type:: struct dpu_rm_rsvp

    Use Case Reservation tagging structure Used to tag HW blocks as reserved by a CRTC->Encoder->Connector chain By using as a tag, rather than lists of pointers to HW blocks used we can avoid some list management since we don't know how many blocks of each type a given use case may require.

.. _`dpu_rm_rsvp.definition`:

Definition
----------

.. code-block:: c

    struct dpu_rm_rsvp {
        struct list_head list;
        uint32_t seq;
        uint32_t enc_id;
    }

.. _`dpu_rm_rsvp.members`:

Members
-------

list
    List head for list of all reservations

seq
    Global RSVP sequence number for debugging, especially for
    differentiating differenct allocations for same encoder.

enc_id
    Reservations are tracked by Encoder DRM object ID.
    CRTCs may be connected to multiple Encoders.
    An encoder or connector id identifies the display path.

.. _`dpu_rm_hw_blk`:

struct dpu_rm_hw_blk
====================

.. c:type:: struct dpu_rm_hw_blk

    hardware block tracking list member

.. _`dpu_rm_hw_blk.definition`:

Definition
----------

.. code-block:: c

    struct dpu_rm_hw_blk {
        struct list_head list;
        struct dpu_rm_rsvp *rsvp;
        struct dpu_rm_rsvp *rsvp_nxt;
        enum dpu_hw_blk_type type;
        uint32_t id;
        struct dpu_hw_blk *hw;
    }

.. _`dpu_rm_hw_blk.members`:

Members
-------

list
    List head for list of all hardware blocks tracking items

rsvp
    Pointer to use case reservation if reserved by a client

rsvp_nxt
    Temporary pointer used during reservation to the incoming
    request. Will be swapped into rsvp if proposal is accepted

type
    Type of hardware block this structure tracks

id
    Hardware ID number, within it's own space, ie. LM_X

hw
    Pointer to the hardware register access object for this block

.. _`_dpu_rm_check_lm_and_get_connected_blks`:

\_dpu_rm_check_lm_and_get_connected_blks
========================================

.. c:function:: bool _dpu_rm_check_lm_and_get_connected_blks(struct dpu_rm *rm, struct dpu_rm_rsvp *rsvp, struct dpu_rm_requirements *reqs, struct dpu_rm_hw_blk *lm, struct dpu_rm_hw_blk **pp, struct dpu_rm_hw_blk *primary_lm)

    check if proposed layer mixer meets proposed use case requirements, incl. hardwired dependent blocks like pingpong

    :param rm:
        dpu resource manager handle
    :type rm: struct dpu_rm \*

    :param rsvp:
        reservation currently being created
    :type rsvp: struct dpu_rm_rsvp \*

    :param reqs:
        proposed use case requirements
    :type reqs: struct dpu_rm_requirements \*

    :param lm:
        proposed layer mixer, function checks if lm, and all other hardwired
        blocks connected to the lm (pp) is available and appropriate
    :type lm: struct dpu_rm_hw_blk \*

    :param pp:
        output parameter, pingpong block attached to the layer mixer.
        NULL if pp was not available, or not matching requirements.
    :type pp: struct dpu_rm_hw_blk \*\*

    :param primary_lm:
        if non-null, this function check if lm is compatible primary_lm
        as well as satisfying all other requirements
    :type primary_lm: struct dpu_rm_hw_blk \*

.. _`_dpu_rm_release_rsvp`:

\_dpu_rm_release_rsvp
=====================

.. c:function:: void _dpu_rm_release_rsvp(struct dpu_rm *rm, struct dpu_rm_rsvp *rsvp)

    release resources and release a reservation

    :param rm:
        KMS handle
    :type rm: struct dpu_rm \*

    :param rsvp:
        RSVP pointer to release and release resources for
    :type rsvp: struct dpu_rm_rsvp \*

.. This file was automatic generated / don't edit.

