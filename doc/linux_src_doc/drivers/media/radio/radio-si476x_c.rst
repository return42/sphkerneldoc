.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/radio/radio-si476x.c

.. _`si476x_radio_ops`:

struct si476x_radio_ops
=======================

.. c:type:: struct si476x_radio_ops

    vtable of tuner functions

.. _`si476x_radio_ops.definition`:

Definition
----------

.. code-block:: c

    struct si476x_radio_ops {
        int (*tune_freq)(struct si476x_core *, struct si476x_tune_freq_args *);
        int (*seek_start)(struct si476x_core *, bool, bool);
        int (*rsq_status)(struct si476x_core *, struct si476x_rsq_status_args *,struct si476x_rsq_status_report *);
        int (*rds_blckcnt)(struct si476x_core *, bool,struct si476x_rds_blockcount_report *);
        int (*phase_diversity)(struct si476x_core *,enum si476x_phase_diversity_mode);
        int (*phase_div_status)(struct si476x_core *);
        int (*acf_status)(struct si476x_core *,struct si476x_acf_status_report *);
        int (*agc_status)(struct si476x_core *,struct si476x_agc_status_report *);
    }

.. _`si476x_radio_ops.members`:

Members
-------

tune_freq
    Tune chip to a specific frequency

seek_start
    Star station seeking

rsq_status
    Get Received Signal Quality(RSQ) status

rds_blckcnt
    Get received RDS blocks count

phase_diversity
    Change phase diversity mode of the tuner

phase_div_status
    Get phase diversity mode status

acf_status
    Get the status of Automatically Controlled
    Features(ACF)

agc_status
    Get Automatic Gain Control(AGC) status

.. _`si476x_radio_ops.description`:

Description
-----------

This table holds pointers to functions implementing particular
operations depending on the mode in which the tuner chip was
configured to start in. If the function is not supported
corresponding element is set to #NULL.

.. _`si476x_radio`:

struct si476x_radio
===================

.. c:type:: struct si476x_radio

    radio device

.. _`si476x_radio.definition`:

Definition
----------

.. code-block:: c

    struct si476x_radio {
        struct v4l2_device v4l2dev;
        struct video_device videodev;
        struct v4l2_ctrl_handler ctrl_handler;
        struct si476x_core *core;
        const struct si476x_radio_ops *ops;
        struct dentry *debugfs;
        u32 audmode;
    }

.. _`si476x_radio.members`:

Members
-------

v4l2dev
    *undescribed*

videodev
    Pointer to video device created by V4L2 subsystem

ctrl_handler
    *undescribed*

core
    Pointer to underlying core device

ops
    Vtable of functions. See struct si476x_radio_ops for details

debugfs
    *undescribed*

audmode
    *undescribed*

.. This file was automatic generated / don't edit.

