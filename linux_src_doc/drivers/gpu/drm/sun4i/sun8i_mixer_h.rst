.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/sun4i/sun8i_mixer.h

.. _`sun8i_mixer_cfg`:

struct sun8i_mixer_cfg
======================

.. c:type:: struct sun8i_mixer_cfg

    mixer HW configuration

.. _`sun8i_mixer_cfg.definition`:

Definition
----------

.. code-block:: c

    struct sun8i_mixer_cfg {
        int vi_num;
        int ui_num;
        int scaler_mask;
        int ccsc;
        unsigned long mod_rate;
    }

.. _`sun8i_mixer_cfg.members`:

Members
-------

vi_num
    number of VI channels

ui_num
    number of UI channels

scaler_mask
    bitmask which tells which channel supports scaling
    First, scaler supports for VI channels is defined and after that, scaler
    support for UI channels. For example, if mixer has 2 VI channels without
    scaler and 2 UI channels with scaler, bitmask would be 0xC.

ccsc
    select set of CCSC base addresses
    Set value to 0 if this is first mixer or second mixer with VEP support.
    Set value to 1 if this is second mixer without VEP support. Other values
    are invalid.

mod_rate
    module clock rate that needs to be set in order to have
    a functional block.

.. This file was automatic generated / don't edit.

