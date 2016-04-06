.. -*- coding: utf-8; mode: rst -*-

============
ff-memless.c
============



.. _xref_input_ff_create_memless:

input_ff_create_memless
=======================

.. c:function:: int input_ff_create_memless (struct input_dev * dev, void * data, int (*play_effect) (struct input_dev *, void *, struct ff_effect *)

    create memoryless force-feedback device

    :param struct input_dev * dev:
        input device supporting force-feedback

    :param void * data:
        driver-specific data to be passed into **play_effect**

    :param int (*)(struct input_dev *, void *, struct ff_effect *) play_effect:
        driver-specific method for playing FF effect


