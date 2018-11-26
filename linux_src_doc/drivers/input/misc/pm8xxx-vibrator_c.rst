.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/misc/pm8xxx-vibrator.c

.. _`pm8xxx_vib`:

struct pm8xxx_vib
=================

.. c:type:: struct pm8xxx_vib

    structure to hold vibrator data

.. _`pm8xxx_vib.definition`:

Definition
----------

.. code-block:: c

    struct pm8xxx_vib {
        struct input_dev *vib_input_dev;
        struct work_struct work;
        struct regmap *regmap;
        const struct pm8xxx_regs *regs;
        int speed;
        int level;
        bool active;
        u8 reg_vib_drv;
    }

.. _`pm8xxx_vib.members`:

Members
-------

vib_input_dev
    input device supporting force feedback

work
    work structure to set the vibration parameters

regmap
    regmap for register read/write

regs
    registers' info

speed
    speed of vibration set from userland

level
    level of vibration to set in the chip

active
    state of vibrator

reg_vib_drv
    regs->drv_addr register value

.. _`pm8xxx_vib_set`:

pm8xxx_vib_set
==============

.. c:function:: int pm8xxx_vib_set(struct pm8xxx_vib *vib, bool on)

    handler to start/stop vibration

    :param vib:
        pointer to vibrator structure
    :type vib: struct pm8xxx_vib \*

    :param on:
        state to set
    :type on: bool

.. _`pm8xxx_work_handler`:

pm8xxx_work_handler
===================

.. c:function:: void pm8xxx_work_handler(struct work_struct *work)

    worker to set vibration level

    :param work:
        pointer to work_struct
    :type work: struct work_struct \*

.. _`pm8xxx_vib_close`:

pm8xxx_vib_close
================

.. c:function:: void pm8xxx_vib_close(struct input_dev *dev)

    callback of input close callback

    :param dev:
        input device pointer
    :type dev: struct input_dev \*

.. _`pm8xxx_vib_close.description`:

Description
-----------

Turns off the vibrator.

.. _`pm8xxx_vib_play_effect`:

pm8xxx_vib_play_effect
======================

.. c:function:: int pm8xxx_vib_play_effect(struct input_dev *dev, void *data, struct ff_effect *effect)

    function to handle vib effects.

    :param dev:
        input device pointer
    :type dev: struct input_dev \*

    :param data:
        data of effect
    :type data: void \*

    :param effect:
        effect to play
    :type effect: struct ff_effect \*

.. _`pm8xxx_vib_play_effect.description`:

Description
-----------

Currently this driver supports only rumble effects.

.. This file was automatic generated / don't edit.

