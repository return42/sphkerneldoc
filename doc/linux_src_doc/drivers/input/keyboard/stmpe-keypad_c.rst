.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/keyboard/stmpe-keypad.c

.. _`stmpe_keypad_variant`:

struct stmpe_keypad_variant
===========================

.. c:type:: struct stmpe_keypad_variant

    model-specific attributes

.. _`stmpe_keypad_variant.definition`:

Definition
----------

.. code-block:: c

    struct stmpe_keypad_variant {
        bool auto_increment;
        bool set_pullup;
        int num_data;
        int num_normal_data;
        int max_cols;
        int max_rows;
        unsigned int col_gpios;
        unsigned int row_gpios;
    }

.. _`stmpe_keypad_variant.members`:

Members
-------

auto_increment
    whether the KPC_DATA_BYTE register address
    auto-increments on multiple read

set_pullup
    whether the pins need to have their pull-ups set

num_data
    number of data bytes

num_normal_data
    number of normal keys' data bytes

max_cols
    maximum number of columns supported

max_rows
    maximum number of rows supported

col_gpios
    bitmask of gpios which can be used for columns

row_gpios
    bitmask of gpios which can be used for rows

.. _`stmpe_keypad`:

struct stmpe_keypad
===================

.. c:type:: struct stmpe_keypad

    STMPE keypad state container

.. _`stmpe_keypad.definition`:

Definition
----------

.. code-block:: c

    struct stmpe_keypad {
        struct stmpe *stmpe;
        struct input_dev *input;
        const struct stmpe_keypad_variant *variant;
        unsigned int debounce_ms;
        unsigned int scan_count;
        bool no_autorepeat;
        unsigned int rows;
        unsigned int cols;
        unsigned short keymap[STMPE_KEYPAD_KEYMAP_MAX_SIZE];
    }

.. _`stmpe_keypad.members`:

Members
-------

stmpe
    pointer to parent STMPE device

input
    spawned input device

variant
    STMPE variant

debounce_ms
    debounce interval, in ms.  Maximum is
    \ ``STMPE_KEYPAD_MAX_DEBOUNCE``\ .

scan_count
    number of key scanning cycles to confirm key data.
    Maximum is \ ``STMPE_KEYPAD_MAX_SCAN_COUNT``\ .

no_autorepeat
    disable key autorepeat

rows
    bitmask for the rows

cols
    bitmask for the columns

keymap
    the keymap

.. This file was automatic generated / don't edit.

