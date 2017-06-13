.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/keyboard/nomadik-ske-keypad.c

.. _`ske_keypad`:

struct ske_keypad
=================

.. c:type:: struct ske_keypad

    data structure used by keypad driver

.. _`ske_keypad.definition`:

Definition
----------

.. code-block:: c

    struct ske_keypad {
        int irq;
        void __iomem *reg_base;
        struct input_dev *input;
        const struct ske_keypad_platform_data *board;
        unsigned short keymap;
        struct clk *clk;
        struct clk *pclk;
        spinlock_t ske_keypad_lock;
    }

.. _`ske_keypad.members`:

Members
-------

irq
    irq no

reg_base
    ske registers base address

input
    pointer to input device object

board
    keypad platform device

keymap
    matrix scan code table for keycodes

clk
    clock structure pointer

pclk
    *undescribed*

ske_keypad_lock
    *undescribed*

.. This file was automatic generated / don't edit.

