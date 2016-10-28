.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/mediatek/pinctrl-mtk-common.h

.. _`mtk_drv_group_desc`:

struct mtk_drv_group_desc
=========================

.. c:type:: struct mtk_drv_group_desc

    Provide driving group data.

.. _`mtk_drv_group_desc.definition`:

Definition
----------

.. code-block:: c

    struct mtk_drv_group_desc {
        unsigned char min_drv;
        unsigned char max_drv;
        unsigned char low_bit;
        unsigned char high_bit;
        unsigned char step;
    }

.. _`mtk_drv_group_desc.members`:

Members
-------

min_drv
    The minimum current of this group.

max_drv
    The maximum current of this group.

low_bit
    The lowest bit of this group.

high_bit
    The highest bit of this group.

step
    The step current of this group.

.. _`mtk_pin_drv_grp`:

struct mtk_pin_drv_grp
======================

.. c:type:: struct mtk_pin_drv_grp

    Provide each pin driving info.

.. _`mtk_pin_drv_grp.definition`:

Definition
----------

.. code-block:: c

    struct mtk_pin_drv_grp {
        unsigned short pin;
        unsigned short offset;
        unsigned char bit;
        unsigned char grp;
    }

.. _`mtk_pin_drv_grp.members`:

Members
-------

pin
    The pin number.

offset
    The offset of driving register for this pin.

bit
    The bit of driving register for this pin.

grp
    The group for this pin belongs to.

.. _`mtk_pin_spec_pupd_set_samereg`:

struct mtk_pin_spec_pupd_set_samereg
====================================

.. c:type:: struct mtk_pin_spec_pupd_set_samereg

    - For special pins' pull up/down setting which resides in same register

.. _`mtk_pin_spec_pupd_set_samereg.definition`:

Definition
----------

.. code-block:: c

    struct mtk_pin_spec_pupd_set_samereg {
        unsigned short pin;
        unsigned short offset;
        unsigned char pupd_bit;
        unsigned char r1_bit;
        unsigned char r0_bit;
    }

.. _`mtk_pin_spec_pupd_set_samereg.members`:

Members
-------

pin
    The pin number.

offset
    The offset of special pull up/down setting register.

pupd_bit
    The pull up/down bit in this register.

r1_bit
    The r1 bit of pull resistor.

r0_bit
    The r0 bit of pull resistor.

.. _`mtk_pin_ies_smt_set`:

struct mtk_pin_ies_smt_set
==========================

.. c:type:: struct mtk_pin_ies_smt_set

    For special pins' ies and smt setting.

.. _`mtk_pin_ies_smt_set.definition`:

Definition
----------

.. code-block:: c

    struct mtk_pin_ies_smt_set {
        unsigned short start;
        unsigned short end;
        unsigned short offset;
        unsigned char bit;
    }

.. _`mtk_pin_ies_smt_set.members`:

Members
-------

start
    The start pin number of those special pins.

end
    The end pin number of those special pins.

offset
    The offset of special setting register.

bit
    The bit of special setting register.

.. _`mtk_pinctrl_devdata`:

struct mtk_pinctrl_devdata
==========================

.. c:type:: struct mtk_pinctrl_devdata

    Provide HW GPIO related data.

.. _`mtk_pinctrl_devdata.definition`:

Definition
----------

.. code-block:: c

    struct mtk_pinctrl_devdata {
        const struct mtk_desc_pin *pins;
        unsigned int npins;
        const struct mtk_drv_group_desc *grp_desc;
        unsigned int n_grp_cls;
        const struct mtk_pin_drv_grp *pin_drv_grp;
        unsigned int n_pin_drv_grps;
        int (*spec_pull_set)(struct regmap *reg, unsigned int pin,unsigned char align, bool isup, unsigned int arg);
        int (*spec_ies_smt_set)(struct regmap *reg, unsigned int pin,unsigned char align, int value, enum pin_config_param arg);
        void (*spec_pinmux_set)(struct regmap *reg, unsigned int pin,unsigned int mode);
        void (*spec_dir_set)(unsigned int *reg_addr, unsigned int pin);
        unsigned int dir_offset;
        unsigned int ies_offset;
        unsigned int smt_offset;
        unsigned int pullen_offset;
        unsigned int pullsel_offset;
        unsigned int drv_offset;
        unsigned int dout_offset;
        unsigned int din_offset;
        unsigned int pinmux_offset;
        unsigned short type1_start;
        unsigned short type1_end;
        unsigned char port_shf;
        unsigned char port_mask;
        unsigned char port_align;
        struct mtk_eint_offsets eint_offsets;
        unsigned int ap_num;
        unsigned int db_cnt;
    }

.. _`mtk_pinctrl_devdata.members`:

Members
-------

pins
    An array describing all pins the pin controller affects.

npins
    The number of entries in \ ``pins``\ .

grp_desc
    The driving group info.

n_grp_cls
    *undescribed*

pin_drv_grp
    The driving group for all pins.

n_pin_drv_grps
    *undescribed*

spec_pull_set
    Each SoC may have special pins for pull up/down setting,
    these pins' pull setting are very different, they have separate pull
    up/down bit, R0 and R1 resistor bit, so they need special pull setting.
    If special setting is success, this should return 0, otherwise it should
    return non-zero value.

spec_ies_smt_set
    Some pins are irregular, their input enable and smt
    control register are discontinuous, but they are mapping together. That
    means when user set smt, input enable is set at the same time. So they
    also need special control. If special control is success, this should
    return 0, otherwise return non-zero value.

spec_pinmux_set
    In some cases, there are two pinmux functions share
    the same value in the same segment of pinmux control register. If user
    want to use one of the two functions, they need an extra bit setting to
    select the right one.

spec_dir_set
    In very few SoCs, direction control registers are not
    arranged continuously, they may be cut to parts. So they need special
    dir setting.

dir_offset
    The direction register offset.

ies_offset
    *undescribed*

smt_offset
    *undescribed*

pullen_offset
    The pull-up/pull-down enable register offset.

pullsel_offset
    *undescribed*

drv_offset
    *undescribed*

dout_offset
    *undescribed*

din_offset
    *undescribed*

pinmux_offset
    The pinmux register offset.

type1_start
    Some chips have two base addresses for pull select register,
    that means some pins use the first address and others use the second. This
    member record the start of pin number to use the second address.

type1_end
    The end of pin number to use the second address.

port_shf
    The shift between two registers.

port_mask
    The mask of register.

port_align
    Provide clear register and set register step.

eint_offsets
    *undescribed*

ap_num
    *undescribed*

db_cnt
    *undescribed*

.. This file was automatic generated / don't edit.

