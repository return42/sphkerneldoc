.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/keyboard/tc3589x-keypad.c

.. _`tc3589x_keypad_platform_data`:

struct tc3589x_keypad_platform_data
===================================

.. c:type:: struct tc3589x_keypad_platform_data

    platform specific keypad data

.. _`tc3589x_keypad_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct tc3589x_keypad_platform_data {
        const struct matrix_keymap_data *keymap_data;
        u8 krow;
        u8 kcol;
        u8 debounce_period;
        u8 settle_time;
        unsigned long irqtype;
        bool enable_wakeup;
        bool no_autorepeat;
    }

.. _`tc3589x_keypad_platform_data.members`:

Members
-------

keymap_data
    matrix scan code table for keycodes

krow
    mask for available rows, value is 0xFF

kcol
    mask for available columns, value is 0xFF

debounce_period
    platform specific debounce time

settle_time
    platform specific settle down time

irqtype
    type of interrupt, falling or rising edge

enable_wakeup
    specifies if keypad event can wake up system from sleep

no_autorepeat
    flag for auto repetition

.. _`tc_keypad`:

struct tc_keypad
================

.. c:type:: struct tc_keypad

    data structure used by keypad driver

.. _`tc_keypad.definition`:

Definition
----------

.. code-block:: c

    struct tc_keypad {
        struct tc3589x *tc3589x;
        struct input_dev *input;
        const struct tc3589x_keypad_platform_data *board;
        unsigned int krow;
        unsigned int kcol;
        unsigned short *keymap;
        bool keypad_stopped;
    }

.. _`tc_keypad.members`:

Members
-------

tc3589x
    pointer to tc35893

input
    pointer to input device object

board
    keypad platform device

krow
    number of rows

kcol
    number of columns

keymap
    matrix scan code table for keycodes

keypad_stopped
    holds keypad status

.. This file was automatic generated / don't edit.

