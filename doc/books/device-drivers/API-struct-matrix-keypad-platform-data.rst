
.. _API-struct-matrix-keypad-platform-data:

==================================
struct matrix_keypad_platform_data
==================================

*man struct matrix_keypad_platform_data(9)*

*4.6.0-rc1*

platform-dependent keypad data


Synopsis
========

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
=======

keymap_data
    pointer to ``matrix_keymap_data``

row_gpios
    pointer to array of gpio numbers representing rows

col_gpios
    pointer to array of gpio numbers reporesenting colums

num_row_gpios
    actual number of row gpios used by device

num_col_gpios
    actual number of col gpios used by device

col_scan_delay_us
    delay, measured in microseconds, that is needed before we can keypad after activating column gpio

debounce_ms
    debounce interval in milliseconds

clustered_irq
    may be specified if interrupts of all row/column GPIOs are bundled to one single irq

clustered_irq_flags
    flags that are needed for the clustered irq

active_low
    gpio polarity

wakeup
    controls whether the device should be set up as wakeup source

no_autorepeat
    disable key autorepeat


Description
===========

This structure represents platform-specific data that use used by matrix_keypad driver to perform proper initialization.
