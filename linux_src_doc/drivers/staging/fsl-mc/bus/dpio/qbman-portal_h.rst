.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/dpio/qbman-portal.h

.. _`qbman_result_is_dq`:

qbman_result_is_DQ
==================

.. c:function:: int qbman_result_is_DQ(const struct dpaa2_dq *dq)

    check if the dequeue result is a dequeue response

    :param const struct dpaa2_dq \*dq:
        the dequeue result to be checked

.. _`qbman_result_is_dq.description`:

Description
-----------

DQRR entries may contain non-dequeue results, ie. notifications

.. _`qbman_result_is_scn`:

qbman_result_is_SCN
===================

.. c:function:: int qbman_result_is_SCN(const struct dpaa2_dq *dq)

    Check the dequeue result is notification or not

    :param const struct dpaa2_dq \*dq:
        the dequeue result to be checked

.. _`qbman_result_scn_state`:

qbman_result_SCN_state
======================

.. c:function:: u8 qbman_result_SCN_state(const struct dpaa2_dq *scn)

    Get the state field in State-change notification

    :param const struct dpaa2_dq \*scn:
        *undescribed*

.. _`qbman_result_scn_rid`:

qbman_result_SCN_rid
====================

.. c:function:: u32 qbman_result_SCN_rid(const struct dpaa2_dq *scn)

    Get the resource id in State-change notification

    :param const struct dpaa2_dq \*scn:
        *undescribed*

.. _`qbman_result_scn_ctx`:

qbman_result_SCN_ctx
====================

.. c:function:: u64 qbman_result_SCN_ctx(const struct dpaa2_dq *scn)

    Get the context data in State-change notification

    :param const struct dpaa2_dq \*scn:
        *undescribed*

.. _`qbman_swp_fq_schedule`:

qbman_swp_fq_schedule
=====================

.. c:function:: int qbman_swp_fq_schedule(struct qbman_swp *s, u32 fqid)

    Move the fq to the scheduled state

    :param struct qbman_swp \*s:
        the software portal object

    :param u32 fqid:
        the index of frame queue to be scheduled

.. _`qbman_swp_fq_schedule.description`:

Description
-----------

There are a couple of different ways that a FQ can end up parked state,
This schedules it.

Return 0 for success, or negative error code for failure.

.. _`qbman_swp_fq_force`:

qbman_swp_fq_force
==================

.. c:function:: int qbman_swp_fq_force(struct qbman_swp *s, u32 fqid)

    Force the FQ to fully scheduled state

    :param struct qbman_swp \*s:
        the software portal object

    :param u32 fqid:
        the index of frame queue to be forced

.. _`qbman_swp_fq_force.description`:

Description
-----------

Force eligible will force a tentatively-scheduled FQ to be fully-scheduled
and thus be available for selection by any channel-dequeuing behaviour (push
or pull). If the FQ is subsequently "dequeued" from the channel and is still
empty at the time this happens, the resulting dq_entry will have no FD.
(qbman_result_DQ_fd() will return NULL.)

Return 0 for success, or negative error code for failure.

.. _`qbman_swp_fq_xon`:

qbman_swp_fq_xon
================

.. c:function:: int qbman_swp_fq_xon(struct qbman_swp *s, u32 fqid)

    sets FQ flow-control to XON

    :param struct qbman_swp \*s:
        the software portal object

    :param u32 fqid:
        the index of frame queue

.. _`qbman_swp_fq_xon.description`:

Description
-----------

This setting doesn't affect enqueues to the FQ, just dequeues.

Return 0 for success, or negative error code for failure.

.. _`qbman_swp_fq_xoff`:

qbman_swp_fq_xoff
=================

.. c:function:: int qbman_swp_fq_xoff(struct qbman_swp *s, u32 fqid)

    sets FQ flow-control to XOFF

    :param struct qbman_swp \*s:
        the software portal object

    :param u32 fqid:
        the index of frame queue

.. _`qbman_swp_fq_xoff.description`:

Description
-----------

This setting doesn't affect enqueues to the FQ, just dequeues.
XOFF FQs will remain in the tenatively-scheduled state, even when
non-empty, meaning they won't be selected for scheduled dequeuing.
If a FQ is changed to XOFF after it had already become truly-scheduled
to a channel, and a pull dequeue of that channel occurs that selects
that FQ for dequeuing, then the resulting dq_entry will have no FD.
(qbman_result_DQ_fd() will return NULL.)

Return 0 for success, or negative error code for failure.

.. _`qbman_swp_cdan_set_context`:

qbman_swp_CDAN_set_context
==========================

.. c:function:: int qbman_swp_CDAN_set_context(struct qbman_swp *s, u16 channelid, u64 ctx)

    Set CDAN context

    :param struct qbman_swp \*s:
        the software portal object

    :param u16 channelid:
        the channel index

    :param u64 ctx:
        the context to be set in CDAN

.. _`qbman_swp_cdan_set_context.description`:

Description
-----------

Return 0 for success, or negative error code for failure.

.. _`qbman_swp_cdan_enable`:

qbman_swp_CDAN_enable
=====================

.. c:function:: int qbman_swp_CDAN_enable(struct qbman_swp *s, u16 channelid)

    Enable CDAN for the channel

    :param struct qbman_swp \*s:
        the software portal object

    :param u16 channelid:
        the index of the channel to generate CDAN

.. _`qbman_swp_cdan_enable.description`:

Description
-----------

Return 0 for success, or negative error code for failure.

.. _`qbman_swp_cdan_disable`:

qbman_swp_CDAN_disable
======================

.. c:function:: int qbman_swp_CDAN_disable(struct qbman_swp *s, u16 channelid)

    disable CDAN for the channel

    :param struct qbman_swp \*s:
        the software portal object

    :param u16 channelid:
        the index of the channel to generate CDAN

.. _`qbman_swp_cdan_disable.description`:

Description
-----------

Return 0 for success, or negative error code for failure.

.. _`qbman_swp_cdan_set_context_enable`:

qbman_swp_CDAN_set_context_enable
=================================

.. c:function:: int qbman_swp_CDAN_set_context_enable(struct qbman_swp *s, u16 channelid, u64 ctx)

    Set CDAN contest and enable CDAN

    :param struct qbman_swp \*s:
        the software portal object

    :param u16 channelid:
        the index of the channel to generate CDAN

    :param u64 ctx:
        i      the context set in CDAN

.. _`qbman_swp_cdan_set_context_enable.description`:

Description
-----------

Return 0 for success, or negative error code for failure.

.. This file was automatic generated / don't edit.

