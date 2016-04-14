.. -*- coding: utf-8; mode: rst -*-

===============
matrix_keypad.h
===============

.. _`matrix_keymap_data`:

struct matrix_keymap_data
=========================

.. c:type:: struct matrix_keymap_data

    keymap for matrix keyboards



Definition
----------

.. code-block:: c

  struct matrix_keymap_data {
    const uint32_t * keymap;
    unsigned int keymap_size;
  };



Members
-------

:``keymap``:
    pointer to array of uint32 values encoded with :c:func:`KEY` macro
    representing keymap

:``keymap_size``:
    number of entries (initialized) in this keymap



Description
-----------

This structure is supposed to be used by platform code to supply
keymaps to drivers that implement matrix-like keypads/keyboards.


.. _`matrix_keypad_platform_data`:

struct matrix_keypad_platform_data
==================================

.. c:type:: struct matrix_keypad_platform_data

    platform-dependent keypad data



Definition
----------

.. code-block:: c

  struct matrix_keypad_platform_data {
    const struct matrix_keymap_data * keymap_data;
    const unsigned int * row_gpios;
    const unsigned int * col_gpios;
    unsigned int num_row_gpios;
    unsigned int num_col_gpios;
    unsigned int col_scan_delay_us;
    unsigned int debounce_ms;
    unsigned int clustered_irq;
    unsigned int clustered_irq_flags;
    bool active_low;
    bool wakeup;
    bool no_autorepeat;
  };



Members
-------

:``keymap_data``:
    pointer to :c:type:`struct matrix_keymap_data <matrix_keymap_data>`

:``row_gpios``:
    pointer to array of gpio numbers representing rows

:``col_gpios``:
    pointer to array of gpio numbers reporesenting colums

:``num_row_gpios``:
    actual number of row gpios used by device

:``num_col_gpios``:
    actual number of col gpios used by device

:``col_scan_delay_us``:
    delay, measured in microseconds, that is
    needed before we can keypad after activating column gpio

:``debounce_ms``:
    debounce interval in milliseconds

:``clustered_irq``:
    may be specified if interrupts of all row/column GPIOs
    are bundled to one single irq

:``clustered_irq_flags``:
    flags that are needed for the clustered irq

:``active_low``:
    gpio polarity

:``wakeup``:
    controls whether the device should be set up as wakeup
    source

:``no_autorepeat``:
    disable key autorepeat



Description
-----------

This structure represents platform-specific data that use used by
matrix_keypad driver to perform proper initialization.


.. _`matrix_keypad_parse_of_params`:

matrix_keypad_parse_of_params
=============================

.. c:function:: int matrix_keypad_parse_of_params (struct device *dev, unsigned int *rows, unsigned int *cols)

    Read parameters from matrix-keypad node

    :param struct device \*dev:
        Device containing of_node

    :param unsigned int \*rows:
        Returns number of matrix rows

    :param unsigned int \*cols:
        Returns number of matrix columns
        ``return`` 0 if OK, <0 on error

