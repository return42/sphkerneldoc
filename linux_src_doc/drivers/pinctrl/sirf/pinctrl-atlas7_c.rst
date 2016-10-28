.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/sirf/pinctrl-atlas7.c

.. _`atlas7_pad_config`:

struct atlas7_pad_config
========================

.. c:type:: struct atlas7_pad_config

    Atlas7 Pad Configuration \ ``id``\                   The ID of this Pad.

.. _`atlas7_pad_config.definition`:

Definition
----------

.. code-block:: c

    struct atlas7_pad_config {
        const u32 id;
        u32 type;
        u32 mux_reg;
        u32 pupd_reg;
        u32 drvstr_reg;
        u32 ad_ctrl_reg;
        u8 mux_bit;
        u8 pupd_bit;
        u8 drvstr_bit;
        u8 ad_ctrl_bit;
    }

.. _`atlas7_pad_config.members`:

Members
-------

id
    *undescribed*

type
    The type of this Pad.

mux_reg
    The mux register offset.
    This register contains the mux.

pupd_reg
    The pull-up/down register offset.

drvstr_reg
    The drive-strength register offset.

ad_ctrl_reg
    The Analogue/Digital Control register.

mux_bit
    The start bit of mux register.

pupd_bit
    The start bit of pull-up/down register.

drvstr_bit
    The start bit of drive-strength register.

ad_ctrl_bit
    The start bit of analogue/digital register.

.. _`atlas7_pad_status`:

struct atlas7_pad_status
========================

.. c:type:: struct atlas7_pad_status

    Atlas7 Pad status

.. _`atlas7_pad_status.definition`:

Definition
----------

.. code-block:: c

    struct atlas7_pad_status {
        u8 func;
        u8 pull;
        u8 dstr;
        u8 reserved;
    }

.. _`atlas7_pad_status.members`:

Members
-------

func
    *undescribed*

pull
    *undescribed*

dstr
    *undescribed*

reserved
    *undescribed*

.. _`atlas7_pad_mux`:

struct atlas7_pad_mux
=====================

.. c:type:: struct atlas7_pad_mux

    Atlas7 mux

.. _`atlas7_pad_mux.definition`:

Definition
----------

.. code-block:: c

    struct atlas7_pad_mux {
        u32 bank;
        u32 pin;
        u32 func;
        u32 dinput_reg;
        u32 dinput_bit;
        u32 dinput_val_reg;
        u32 dinput_val_bit;
    }

.. _`atlas7_pad_mux.members`:

Members
-------

bank
    The bank of this pad's registers on.

pin
    The ID of this Pad.

func
    The mux func on this Pad.

dinput_reg
    The Input-Disable register offset.

dinput_bit
    The start bit of Input-Disable register.

dinput_val_reg
    The Input-Disable-value register offset.
    This register is used to set the value of this pad
    if this pad was disabled.

dinput_val_bit
    The start bit of Input-Disable Value register.

.. _`ngpio_of_bank`:

NGPIO_OF_BANK
=============

.. c:function::  NGPIO_OF_BANK()

.. _`atlas7_pull_info`:

struct atlas7_pull_info
=======================

.. c:type:: struct atlas7_pull_info

    Atlas7 Pad pull info

.. _`atlas7_pull_info.definition`:

Definition
----------

.. code-block:: c

    struct atlas7_pull_info {
        u8 pad_type;
        u8 mask;
        const struct map_data *v2s;
        const struct map_data *s2v;
    }

.. _`atlas7_pull_info.members`:

Members
-------

pad_type
    *undescribed*

mask
    The mas value of this pin's pull bits.

v2s
    The map of pull register value to pull status.

s2v
    The map of pull status to pull register value.

.. _`atlas7_ds_ma_info`:

struct atlas7_ds_ma_info
========================

.. c:type:: struct atlas7_ds_ma_info

    Atlas7 Pad DriveStrength & currents info

.. _`atlas7_ds_ma_info.definition`:

Definition
----------

.. code-block:: c

    struct atlas7_ds_ma_info {
        u32 ma;
        u32 ds_16st;
        u32 ds_4we;
        u32 ds_0204m31;
        u32 ds_0610m31;
    }

.. _`atlas7_ds_ma_info.members`:

Members
-------

ma
    The Drive Strength in current value .

ds_16st
    The correspond raw value of 16st pad.

ds_4we
    The correspond raw value of 4we pad.

ds_0204m31
    The correspond raw value of 0204m31 pad.

ds_0610m31
    The correspond raw value of 0610m31 pad.

.. _`atlas7_ds_info`:

struct atlas7_ds_info
=====================

.. c:type:: struct atlas7_ds_info

    Atlas7 Pad DriveStrength info

.. _`atlas7_ds_info.definition`:

Definition
----------

.. code-block:: c

    struct atlas7_ds_info {
        u8 type;
        u8 mask;
        u8 imval;
        u8 reserved;
    }

.. _`atlas7_ds_info.members`:

Members
-------

type
    The type of this Pad.

mask
    The mask value of this pin's pull bits.

imval
    The immediate value of drives trength register.

reserved
    *undescribed*

.. _`atlas7_gpio_to_bank`:

atlas7_gpio_to_bank
===================

.. c:function:: struct atlas7_gpio_bank *atlas7_gpio_to_bank(struct atlas7_gpio_chip *a7gc, u32 gpio)

    :param struct atlas7_gpio_chip \*a7gc:
        *undescribed*

    :param u32 gpio:
        *undescribed*

.. This file was automatic generated / don't edit.

