.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/keyboard/pmic8xxx-keypad.c

.. _`pmic8xxx_kp`:

struct pmic8xxx_kp
==================

.. c:type:: struct pmic8xxx_kp

    internal keypad data structure \ ``num_cols``\  - number of columns of keypad \ ``num_rows``\  - number of row of keypad \ ``input``\  - input device pointer for keypad \ ``regmap``\  - regmap handle \ ``key_sense_irq``\  - key press/release irq number \ ``key_stuck_irq``\  - key stuck notification irq number \ ``keycodes``\  - array to hold the key codes \ ``dev``\  - parent device pointer \ ``keystate``\  - present key press/release state \ ``stuckstate``\  - present state when key stuck irq \ ``ctrl_reg``\  - control register value

.. _`pmic8xxx_kp.definition`:

Definition
----------

.. code-block:: c

    struct pmic8xxx_kp {
        unsigned int num_rows;
        unsigned int num_cols;
        struct input_dev *input;
        struct regmap *regmap;
        int key_sense_irq;
        int key_stuck_irq;
        unsigned short keycodes[PM8XXX_MATRIX_MAX_SIZE];
        struct device *dev;
        u16 keystate[PM8XXX_MAX_ROWS];
        u16 stuckstate[PM8XXX_MAX_ROWS];
        u8 ctrl_reg;
    }

.. _`pmic8xxx_kp.members`:

Members
-------

num_rows
    *undescribed*

num_cols
    *undescribed*

input
    *undescribed*

regmap
    *undescribed*

key_sense_irq
    *undescribed*

key_stuck_irq
    *undescribed*

dev
    *undescribed*

ctrl_reg
    *undescribed*

.. This file was automatic generated / don't edit.

