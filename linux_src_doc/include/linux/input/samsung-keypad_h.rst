.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/input/samsung-keypad.h

.. _`samsung_keypad_platdata`:

struct samsung_keypad_platdata
==============================

.. c:type:: struct samsung_keypad_platdata

    Platform device data for Samsung Keypad.

.. _`samsung_keypad_platdata.definition`:

Definition
----------

.. code-block:: c

    struct samsung_keypad_platdata {
        const struct matrix_keymap_data *keymap_data;
        unsigned int rows;
        unsigned int cols;
        bool no_autorepeat;
        bool wakeup;
        void (*cfg_gpio)(unsigned int rows, unsigned int cols);
    }

.. _`samsung_keypad_platdata.members`:

Members
-------

keymap_data
    pointer to \ :c:type:`struct matrix_keymap_data <matrix_keymap_data>`.

rows
    number of keypad row supported.

cols
    number of keypad col supported.

no_autorepeat
    disable key autorepeat.

wakeup
    controls whether the device should be set up as wakeup source.

cfg_gpio
    configure the GPIO.

.. _`samsung_keypad_platdata.description`:

Description
-----------

Initialisation data specific to either the machine or the platform
for the device driver to use or call-back when configuring gpio.

.. This file was automatic generated / don't edit.

