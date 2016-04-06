
.. _API-matrix-keypad-parse-of-params:

=============================
matrix_keypad_parse_of_params
=============================

*man matrix_keypad_parse_of_params(9)*

*4.6.0-rc1*

Read parameters from matrix-keypad node


Synopsis
========

.. c:function:: int matrix_keypad_parse_of_params( struct device * dev, unsigned int * rows, unsigned int * cols )

Arguments
=========

``dev``
    Device containing of_node

``rows``
    Returns number of matrix rows

``cols``
    Returns number of matrix columns ``return`` 0 if OK, <0 on error
