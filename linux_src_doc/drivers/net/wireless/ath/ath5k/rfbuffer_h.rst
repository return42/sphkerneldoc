.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/rfbuffer.h

.. _`rf-buffer-registers`:

RF Buffer registers
===================

There are some special registers on the RF chip
that control various operation settings related mostly to
the analog parts (channel, gain adjustment etc).

We don't write on those registers directly but
we send a data packet on the chip, using a special register,
that holds all the settings we need. After we've sent the
data packet, we write on another special register to notify hw
to apply the settings. This is done so that control registers
can be dynamically programmed during operation and the settings
are applied faster on the hw.

We call each data packet an "RF Bank" and all the data we write
(all RF Banks) "RF Buffer". This file holds initial RF Buffer
data for the different RF chips, and various info to match RF
Buffer offsets with specific RF registers so that we can access
them. We tweak these settings on rfregs_init function.

Also check out reg.h and U.S. Patent 6677779 B1 (about buffer
registers and control registers):

http://www.google.com/patents?id=qNURAAAAEBAJ

.. _`ath5k_ini_rfbuffer`:

struct ath5k_ini_rfbuffer
=========================

.. c:type:: struct ath5k_ini_rfbuffer

    Initial RF Buffer settings

.. _`ath5k_ini_rfbuffer.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_ini_rfbuffer {
        u8 rfb_bank;
        u16 rfb_ctrl_register;
        u32 rfb_mode_data;
    }

.. _`ath5k_ini_rfbuffer.members`:

Members
-------

rfb_bank
    RF Bank number

rfb_ctrl_register
    RF Buffer control register

rfb_mode_data
    RF Buffer data for each mode

.. _`ath5k_ini_rfbuffer.description`:

Description
-----------

Struct to hold default mode specific RF
register values (RF Banks) for each chip.

.. _`ath5k_rfb_field`:

struct ath5k_rfb_field
======================

.. c:type:: struct ath5k_rfb_field

    An RF Buffer field (register/value)

.. _`ath5k_rfb_field.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_rfb_field {
        u8 len;
        u16 pos;
        u8 col;
    }

.. _`ath5k_rfb_field.members`:

Members
-------

len
    Field length

pos
    Offset on the raw packet

col
    Used for shifting

.. _`ath5k_rfb_field.description`:

Description
-----------

Struct to hold RF Buffer field
infos used to access certain RF
analog registers

.. _`ath5k_rf_reg`:

struct ath5k_rf_reg
===================

.. c:type:: struct ath5k_rf_reg

    RF analog register definition

.. _`ath5k_rf_reg.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_rf_reg {
        u8 bank;
        u8 index;
        struct ath5k_rfb_field field;
    }

.. _`ath5k_rf_reg.members`:

Members
-------

bank
    RF Buffer Bank number

index
    Register's index on ath5k_rf_regx_idx

field
    The \ :c:type:`struct ath5k_rfb_field <ath5k_rfb_field>`\ 

.. _`ath5k_rf_reg.description`:

Description
-----------

We use this struct to define the set of RF registers
on each chip that we want to tweak. Some RF registers
are common between different chip versions so this saves
us space and complexity because we can refer to an rf
register by it's index no matter what chip we work with
as long as it has that register.

.. _`ath5k_rf_regs_idx`:

enum ath5k_rf_regs_idx
======================

.. c:type:: enum ath5k_rf_regs_idx

    Map RF registers to indexes

.. _`ath5k_rf_regs_idx.definition`:

Definition
----------

.. code-block:: c

    enum ath5k_rf_regs_idx {
        AR5K_RF_TURBO,
        AR5K_RF_OB_2GHZ,
        AR5K_RF_OB_5GHZ,
        AR5K_RF_DB_2GHZ,
        AR5K_RF_DB_5GHZ,
        AR5K_RF_FIXED_BIAS_A,
        AR5K_RF_FIXED_BIAS_B,
        AR5K_RF_PWD_XPD,
        AR5K_RF_XPD_SEL,
        AR5K_RF_XPD_GAIN,
        AR5K_RF_PD_GAIN_LO,
        AR5K_RF_PD_GAIN_HI,
        AR5K_RF_HIGH_VC_CP,
        AR5K_RF_MID_VC_CP,
        AR5K_RF_LOW_VC_CP,
        AR5K_RF_PUSH_UP,
        AR5K_RF_PAD2GND,
        AR5K_RF_XB2_LVL,
        AR5K_RF_XB5_LVL,
        AR5K_RF_PWD_ICLOBUF_2G,
        AR5K_RF_PWD_84,
        AR5K_RF_PWD_90,
        AR5K_RF_PWD_130,
        AR5K_RF_PWD_131,
        AR5K_RF_PWD_132,
        AR5K_RF_PWD_136,
        AR5K_RF_PWD_137,
        AR5K_RF_PWD_138,
        AR5K_RF_PWD_166,
        AR5K_RF_PWD_167,
        AR5K_RF_DERBY_CHAN_SEL_MODE,
        AR5K_RF_GAIN_I,
        AR5K_RF_PLO_SEL,
        AR5K_RF_RFGAIN_SEL,
        AR5K_RF_RFGAIN_STEP,
        AR5K_RF_WAIT_S,
        AR5K_RF_WAIT_I,
        AR5K_RF_MAX_TIME,
        AR5K_RF_MIXVGA_OVR,
        AR5K_RF_MIXGAIN_OVR,
        AR5K_RF_MIXGAIN_STEP,
        AR5K_RF_PD_DELAY_A,
        AR5K_RF_PD_DELAY_B,
        AR5K_RF_PD_DELAY_XR,
        AR5K_RF_PD_PERIOD_A,
        AR5K_RF_PD_PERIOD_B,
        AR5K_RF_PD_PERIOD_XR
    };

.. _`ath5k_rf_regs_idx.constants`:

Constants
---------

AR5K_RF_TURBO
    *undescribed*

AR5K_RF_OB_2GHZ
    *undescribed*

AR5K_RF_OB_5GHZ
    *undescribed*

AR5K_RF_DB_2GHZ
    *undescribed*

AR5K_RF_DB_5GHZ
    *undescribed*

AR5K_RF_FIXED_BIAS_A
    *undescribed*

AR5K_RF_FIXED_BIAS_B
    *undescribed*

AR5K_RF_PWD_XPD
    *undescribed*

AR5K_RF_XPD_SEL
    *undescribed*

AR5K_RF_XPD_GAIN
    *undescribed*

AR5K_RF_PD_GAIN_LO
    *undescribed*

AR5K_RF_PD_GAIN_HI
    *undescribed*

AR5K_RF_HIGH_VC_CP
    *undescribed*

AR5K_RF_MID_VC_CP
    *undescribed*

AR5K_RF_LOW_VC_CP
    *undescribed*

AR5K_RF_PUSH_UP
    *undescribed*

AR5K_RF_PAD2GND
    *undescribed*

AR5K_RF_XB2_LVL
    *undescribed*

AR5K_RF_XB5_LVL
    *undescribed*

AR5K_RF_PWD_ICLOBUF_2G
    *undescribed*

AR5K_RF_PWD_84
    *undescribed*

AR5K_RF_PWD_90
    *undescribed*

AR5K_RF_PWD_130
    *undescribed*

AR5K_RF_PWD_131
    *undescribed*

AR5K_RF_PWD_132
    *undescribed*

AR5K_RF_PWD_136
    *undescribed*

AR5K_RF_PWD_137
    *undescribed*

AR5K_RF_PWD_138
    *undescribed*

AR5K_RF_PWD_166
    *undescribed*

AR5K_RF_PWD_167
    *undescribed*

AR5K_RF_DERBY_CHAN_SEL_MODE
    *undescribed*

AR5K_RF_GAIN_I
    *undescribed*

AR5K_RF_PLO_SEL
    *undescribed*

AR5K_RF_RFGAIN_SEL
    *undescribed*

AR5K_RF_RFGAIN_STEP
    *undescribed*

AR5K_RF_WAIT_S
    *undescribed*

AR5K_RF_WAIT_I
    *undescribed*

AR5K_RF_MAX_TIME
    *undescribed*

AR5K_RF_MIXVGA_OVR
    *undescribed*

AR5K_RF_MIXGAIN_OVR
    *undescribed*

AR5K_RF_MIXGAIN_STEP
    *undescribed*

AR5K_RF_PD_DELAY_A
    *undescribed*

AR5K_RF_PD_DELAY_B
    *undescribed*

AR5K_RF_PD_DELAY_XR
    *undescribed*

AR5K_RF_PD_PERIOD_A
    *undescribed*

AR5K_RF_PD_PERIOD_B
    *undescribed*

AR5K_RF_PD_PERIOD_XR
    *undescribed*

.. _`ath5k_rf_regs_idx.description`:

Description
-----------

We do this to handle common bits and make our
life easier by using an index for each register
instead of a full rfb_field

.. This file was automatic generated / don't edit.

