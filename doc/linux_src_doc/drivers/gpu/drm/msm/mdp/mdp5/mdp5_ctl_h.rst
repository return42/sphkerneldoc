.. -*- coding: utf-8; mode: rst -*-

==========
mdp5_ctl.h
==========


.. _`mdp_ctl_flush_mask_lm`:

mdp_ctl_flush_mask_lm
=====================

.. c:function:: u32 mdp_ctl_flush_mask_lm (int lm)

    Register FLUSH masks

    :param int lm:

        *undescribed*



.. _`mdp_ctl_flush_mask_lm.description`:

Description
-----------


These masks are used to specify which block(s) need to be flushed
through ``flush_mask`` parameter in mdp5_ctl_commit(.., flush_mask).

