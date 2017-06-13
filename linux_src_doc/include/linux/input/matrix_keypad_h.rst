.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/input/matrix_keypad.h

.. _`matrix_keymap_data`:

struct matrix_keymap_data
=========================

.. c:type:: struct matrix_keymap_data

    keymap for matrix keyboards

.. _`matrix_keymap_data.definition`:

Definition
----------

.. code-block:: c

    struct matrix_keymap_data {
        const uint32_t *keymap;
        unsigned int keymap_size;
    }

.. _`matrix_keymap_data.members`:

Members
-------

keymap
    pointer to array of uint32 values encoded with \ :c:func:`KEY`\  macro
    representing keymap

keymap_size
    number of entries (initialized) in this keymap

.. _`matrix_keymap_data.description`:

Description
-----------

This structure is supposed to be used by platform code to supply
keymaps to drivers that implement matrix-like keypads/keyboards.

.. _`matrix_keypad_platform_data`:

struct matrix_keypad_platform_data
==================================

.. c:type:: struct matrix_keypad_platform_data

    platform-dependent keypad data

.. _`matrix_keypad_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct matrix_keypad_platform_data {
        const struct matrix_keymap_data *keymap_data;
        const unsigned int *row_gpios;
        const unsigned int *col_gpios;
        unsigned int num_row_gpios;
        unsigned int num_col_gpios;
        unsigned int col_scan_delay_us;
        unsigned int debounce_ms;
        unsigned int clustered_irq;
        unsigned int clustered_irq_flags;
        bool active_low;
        bool wakeup;
        bool no_autorepeat;
        bool drive_inactive_cols;
    }

.. _`matrix_keypad_platform_data.members`:

Members
-------

keymap_data
    pointer to \ :c:type:`struct matrix_keymap_data <matrix_keymap_data>`\ 

row_gpios
    pointer to array of gpio numbers representing rows

col_gpios
    pointer to array of gpio numbers reporesenting colums

num_row_gpios
    actual number of row gpios used by device

num_col_gpios
    actual number of col gpios used by device

col_scan_delay_us
    delay, measured in microseconds, that is
    needed before we can keypad after activating column gpio

debounce_ms
    debounce interval in milliseconds

clustered_irq
    may be specified if interrupts of all row/column GPIOs
    are bundled to one single irq

clustered_irq_flags
    flags that are needed for the clustered irq

active_low
    gpio polarity

wakeup
    controls whether the device should be set up as wakeup
    source

no_autorepeat
    disable key autorepeat

drive_inactive_cols
    drive inactive columns during scan, rather than
    making them inputs.

.. _`matrix_keypad_platform_data.description`:

Description
-----------

This structure represents platform-specific data that use used by
matrix_keypad driver to perform proper initialization.

.. This file was automatic generated / don't edit.

