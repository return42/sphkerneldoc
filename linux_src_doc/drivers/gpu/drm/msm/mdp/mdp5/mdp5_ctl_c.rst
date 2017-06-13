.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/mdp/mdp5/mdp5_ctl.c

.. _`mdp5_ctl_set_encoder_state`:

mdp5_ctl_set_encoder_state
==========================

.. c:function:: int mdp5_ctl_set_encoder_state(struct mdp5_ctl *ctl, struct mdp5_pipeline *pipeline, bool enabled)

    set the encoder state

    :param struct mdp5_ctl \*ctl:
        *undescribed*

    :param struct mdp5_pipeline \*pipeline:
        *undescribed*

    :param bool enabled:
        *undescribed*

.. _`mdp5_ctl_set_encoder_state.note`:

Note
----

This encoder state is needed to trigger START signal (data path kickoff).

.. _`mdp5_ctl_commit`:

mdp5_ctl_commit
===============

.. c:function:: u32 mdp5_ctl_commit(struct mdp5_ctl *ctl, struct mdp5_pipeline *pipeline, u32 flush_mask)

    Register Flush

    :param struct mdp5_ctl \*ctl:
        *undescribed*

    :param struct mdp5_pipeline \*pipeline:
        *undescribed*

    :param u32 flush_mask:
        *undescribed*

.. _`mdp5_ctl_commit.description`:

Description
-----------

The flush register is used to indicate several registers are all
programmed, and are safe to update to the back copy of the double
buffered registers.

Some registers FLUSH bits are shared when the hardware does not have
dedicated bits for them; handling these is the job of \ :c:func:`fix_sw_flush`\ .

CTL registers need to be flushed in some circumstances; if that is the
case, some trigger bits will be present in both flush mask and
ctl->pending_ctl_trigger.

Return H/W flushed bit mask.

.. This file was automatic generated / don't edit.

