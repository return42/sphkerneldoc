.. -*- coding: utf-8; mode: rst -*-

.. _input_subsystem:

***************
Input Subsystem
***************


Input core
==========


.. kernel-doc:: include/linux/input.h
    :internal:

.. kernel-doc:: drivers/input/input.c
    :export:

.. kernel-doc:: drivers/input/ff-core.c
    :export:

.. kernel-doc:: drivers/input/ff-memless.c
    :export:

Multitouch Library
==================


.. kernel-doc:: include/linux/input/mt.h
    :internal:

.. kernel-doc:: drivers/input/input-mt.c
    :export:

Polled input devices
====================


.. kernel-doc:: include/linux/input-polldev.h
    :internal:

.. kernel-doc:: drivers/input/input-polldev.c
    :export:

Matrix keyboards/keypads
========================


.. kernel-doc:: include/linux/input/matrix_keypad.h
    :internal:

Sparse keymap support
=====================


.. kernel-doc:: include/linux/input/sparse-keymap.h
    :internal:

.. kernel-doc:: drivers/input/sparse-keymap.c
    :export:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
