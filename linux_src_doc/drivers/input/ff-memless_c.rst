.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/ff-memless.c

.. _`input_ff_create_memless`:

input_ff_create_memless
=======================

.. c:function:: int input_ff_create_memless(struct input_dev *dev, void *data, int (*play_effect)(struct input_dev *, void *, struct ff_effect *))

    create memoryless force-feedback device

    :param dev:
        input device supporting force-feedback
    :type dev: struct input_dev \*

    :param data:
        driver-specific data to be passed into \ ``play_effect``\ 
    :type data: void \*

    :param int (\*play_effect)(struct input_dev \*, void \*, struct ff_effect \*):
        driver-specific method for playing FF effect

.. This file was automatic generated / don't edit.

