.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/matrix-keymap.c

.. _`matrix_keypad_parse_properties`:

matrix_keypad_parse_properties
==============================

.. c:function:: int matrix_keypad_parse_properties(struct device *dev, unsigned int *rows, unsigned int *cols)

    Read properties of matrix keypad

    :param dev:
        Device containing properties
    :type dev: struct device \*

    :param rows:
        Returns number of matrix rows
    :type rows: unsigned int \*

    :param cols:
        Returns number of matrix columns
        \ ``return``\  0 if OK, <0 on error
    :type cols: unsigned int \*

.. _`matrix_keypad_build_keymap`:

matrix_keypad_build_keymap
==========================

.. c:function:: int matrix_keypad_build_keymap(const struct matrix_keymap_data *keymap_data, const char *keymap_name, unsigned int rows, unsigned int cols, unsigned short *keymap, struct input_dev *input_dev)

    convert platform keymap into matrix keymap

    :param keymap_data:
        keymap supplied by the platform code
    :type keymap_data: const struct matrix_keymap_data \*

    :param keymap_name:
        name of device tree property containing keymap (if device
        tree support is enabled).
    :type keymap_name: const char \*

    :param rows:
        number of rows in target keymap array
    :type rows: unsigned int

    :param cols:
        number of cols in target keymap array
    :type cols: unsigned int

    :param keymap:
        expanded version of keymap that is suitable for use by
        matrix keyboard driver
    :type keymap: unsigned short \*

    :param input_dev:
        input devices for which we are setting up the keymap
    :type input_dev: struct input_dev \*

.. _`matrix_keypad_build_keymap.description`:

Description
-----------

This function converts platform keymap (encoded with \ :c:func:`KEY`\  macro) into
an array of keycodes that is suitable for using in a standard matrix
keyboard driver that uses row and col as indices.

If \ ``keymap_data``\  is not supplied and device tree support is enabled
it will attempt load the keymap from property specified by \ ``keymap_name``\ 
argument (or "linux,keymap" if \ ``keymap_name``\  is \ ``NULL``\ ).

If \ ``keymap``\  is \ ``NULL``\  the function will automatically allocate managed
block of memory to store the keymap. This memory will be associated with
the parent device and automatically freed when device unbinds from the
driver.

Callers are expected to set up input_dev->dev.parent before calling this
function.

.. This file was automatic generated / don't edit.

