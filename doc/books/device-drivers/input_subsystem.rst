.. -*- coding: utf-8; mode: rst -*-

.. _input_subsystem:

***************
Input Subsystem
***************


Input core
==========


.. kernel-doc:: include/linux/input.h
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/input/input.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/input/ff-core.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/input/ff-memless.c
    :man-sect: 9
    :export:


Multitouch Library
==================


.. kernel-doc:: include/linux/input/mt.h
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/input/input-mt.c
    :man-sect: 9
    :export:


Polled input devices
====================


.. kernel-doc:: include/linux/input-polldev.h
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/input/input-polldev.c
    :man-sect: 9
    :export:


Matrix keyboards/keypads
========================


.. kernel-doc:: include/linux/input/matrix_keypad.h
    :man-sect: 9
    :internal:


Sparse keymap support
=====================


.. kernel-doc:: include/linux/input/sparse-keymap.h
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/input/sparse-keymap.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
