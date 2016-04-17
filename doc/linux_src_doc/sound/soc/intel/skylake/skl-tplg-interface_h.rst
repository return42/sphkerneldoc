.. -*- coding: utf-8; mode: rst -*-

====================
skl-tplg-interface.h
====================


.. _`skl_ch_cfg`:

enum skl_ch_cfg
===============

.. c:type:: skl_ch_cfg

    channel configuration


.. _`skl_ch_cfg.definition`:

Definition
----------

.. code-block:: c

    enum skl_ch_cfg {
      SKL_CH_CFG_MONO,
      SKL_CH_CFG_STEREO,
      SKL_CH_CFG_2_1,
      SKL_CH_CFG_3_0,
      SKL_CH_CFG_3_1,
      SKL_CH_CFG_QUATRO,
      SKL_CH_CFG_4_0,
      SKL_CH_CFG_5_0,
      SKL_CH_CFG_5_1,
      SKL_CH_CFG_DUAL_MONO,
      SKL_CH_CFG_I2S_DUAL_STEREO_0,
      SKL_CH_CFG_I2S_DUAL_STEREO_1,
      SKL_CH_CFG_4_CHANNEL,
      SKL_CH_CFG_INVALID
    };


.. _`skl_ch_cfg.constants`:

Constants
---------

:``SKL_CH_CFG_MONO``:
    One channel only

:``SKL_CH_CFG_STEREO``:
    L & R

:``SKL_CH_CFG_2_1``:
    L, R & LFE

:``SKL_CH_CFG_3_0``:
    L, C & R

:``SKL_CH_CFG_3_1``:
    L, C, R & LFE

:``SKL_CH_CFG_QUATRO``:
    L, R, Ls & Rs

:``SKL_CH_CFG_4_0``:
    L, C, R & Cs

:``SKL_CH_CFG_5_0``:
    L, C, R, Ls & Rs

:``SKL_CH_CFG_5_1``:
    L, C, R, Ls, Rs & LFE

:``SKL_CH_CFG_DUAL_MONO``:
    One channel replicated in two

:``SKL_CH_CFG_I2S_DUAL_STEREO_0``:
    Stereo(L,R) in 4 slots, 1st stream:[ L, R, -, - ]

:``SKL_CH_CFG_I2S_DUAL_STEREO_1``:
    Stereo(L,R) in 4 slots, 2nd stream:[ -, -, L, R ]

:``SKL_CH_CFG_4_CHANNEL``:
-- undescribed --

:``SKL_CH_CFG_INVALID``:
    Invalid


.. _`skl_interleaving`:

enum skl_interleaving
=====================

.. c:type:: skl_interleaving

    interleaving style


.. _`skl_interleaving.definition`:

Definition
----------

.. code-block:: c

    enum skl_interleaving {
      SKL_INTERLEAVING_PER_CHANNEL,
      SKL_INTERLEAVING_PER_SAMPLE
    };


.. _`skl_interleaving.constants`:

Constants
---------

:``SKL_INTERLEAVING_PER_CHANNEL``:
    [s1_ch1...s1_chN,...,sM_ch1...sM_chN]

:``SKL_INTERLEAVING_PER_SAMPLE``:
    [s1_ch1...sM_ch1,...,s1_chN...sM_chN]
