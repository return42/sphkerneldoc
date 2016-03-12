.. -*- coding: utf-8; mode: rst -*-

==============
radio-si476x.c
==============



.. _xref_struct_si476x_radio_ops:

struct si476x_radio_ops
=======================

.. c:type:: struct si476x_radio_ops

    vtable of tuner functions



Definition
----------

.. code-block:: c

  struct si476x_radio_ops {
    int (* tune_freq) (struct si476x_core *, struct si476x_tune_freq_args *);
    int (* seek_start) (struct si476x_core *, bool, bool);
    int (* rsq_status) (struct si476x_core *, struct si476x_rsq_status_args *,struct si476x_rsq_status_report *);
    int (* rds_blckcnt) (struct si476x_core *, bool,struct si476x_rds_blockcount_report *);
    int (* phase_diversity) (struct si476x_core *,enum si476x_phase_diversity_mode);
    int (* phase_div_status) (struct si476x_core *);
    int (* acf_status) (struct si476x_core *,struct si476x_acf_status_report *);
    int (* agc_status) (struct si476x_core *,struct si476x_agc_status_report *);
  };



Members
-------

:``int (*)(struct si476x_core *, struct si476x_tune_freq_args *) tune_freq``:
    Tune chip to a specific frequency

:``int (*)(struct si476x_core *, bool, bool) seek_start``:
    Star station seeking

:``int (*)(struct si476x_core *, struct si476x_rsq_status_args *,struct si476x_rsq_status_report *) rsq_status``:
    Get Received Signal Quality(RSQ) status

:``int (*)(struct si476x_core *, bool,struct si476x_rds_blockcount_report *) rds_blckcnt``:
    Get received RDS blocks count

:``int (*)(struct si476x_core *,enum si476x_phase_diversity_mode) phase_diversity``:
    Change phase diversity mode of the tuner

:``int (*)(struct si476x_core *) phase_div_status``:
    Get phase diversity mode status

:``int (*)(struct si476x_core *,struct si476x_acf_status_report *) acf_status``:
    Get the status of Automatically Controlled
    Features(ACF)

:``int (*)(struct si476x_core *,struct si476x_agc_status_report *) agc_status``:
    Get Automatic Gain Control(AGC) status




Description
-----------



This table holds pointers to functions implementing particular
operations depending on the mode in which the tuner chip was
configured to start in. If the function is not supported
corresponding element is set to #NULL.




.. _xref_struct_si476x_radio:

struct si476x_radio
===================

.. c:type:: struct si476x_radio

    radio device



Definition
----------

.. code-block:: c

  struct si476x_radio {
    struct video_device videodev;
    struct si476x_core * core;
    const struct si476x_radio_ops * ops;
  };



Members
-------

:``struct video_device videodev``:
    Pointer to video device created by V4L2 subsystem

:``struct si476x_core * core``:
    Pointer to underlying core device

:``const struct si476x_radio_ops * ops``:
    Vtable of functions. See struct si476x_radio_ops for details



