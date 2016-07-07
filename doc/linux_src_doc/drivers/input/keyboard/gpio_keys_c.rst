.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/keyboard/gpio_keys.c

.. _`get_n_events_by_type`:

get_n_events_by_type
====================

.. c:function:: int get_n_events_by_type(int type)

    returns maximum number of events per \ ``type``\ 

    :param int type:
        type of button (\ ``EV_KEY``\ , \ ``EV_SW``\ )

.. _`get_n_events_by_type.description`:

Description
-----------

Return value of this function can be used to allocate bitmap
large enough to hold all bits for given type.

.. _`get_bm_events_by_type`:

get_bm_events_by_type
=====================

.. c:function:: const unsigned long *get_bm_events_by_type(struct input_dev *dev, int type)

    returns bitmap of supported events per \ ``type``\ 

    :param struct input_dev \*dev:
        *undescribed*

    :param int type:
        type of button (\ ``EV_KEY``\ , \ ``EV_SW``\ )

.. _`get_bm_events_by_type.description`:

Description
-----------

Return value of this function can be used to allocate bitmap
large enough to hold all bits for given type.

.. _`gpio_keys_disable_button`:

gpio_keys_disable_button
========================

.. c:function:: void gpio_keys_disable_button(struct gpio_button_data *bdata)

    disables given GPIO button

    :param struct gpio_button_data \*bdata:
        button data for button to be disabled

.. _`gpio_keys_disable_button.description`:

Description
-----------

Disables button pointed by \ ``bdata``\ . This is done by masking
IRQ line. After this function is called, button won't generate
input events anymore. Note that one can only disable buttons
that don't share IRQs.

Make sure that \ ``bdata``\ ->disable_lock is locked when entering
this function to avoid races when concurrent threads are
disabling buttons at the same time.

.. _`gpio_keys_enable_button`:

gpio_keys_enable_button
=======================

.. c:function:: void gpio_keys_enable_button(struct gpio_button_data *bdata)

    enables given GPIO button

    :param struct gpio_button_data \*bdata:
        button data for button to be disabled

.. _`gpio_keys_enable_button.description`:

Description
-----------

Enables given button pointed by \ ``bdata``\ .

Make sure that \ ``bdata``\ ->disable_lock is locked when entering
this function to avoid races with concurrent threads trying
to enable the same button at the same time.

.. _`gpio_keys_attr_show_helper`:

gpio_keys_attr_show_helper
==========================

.. c:function:: ssize_t gpio_keys_attr_show_helper(struct gpio_keys_drvdata *ddata, char *buf, unsigned int type, bool only_disabled)

    fill in stringified bitmap of buttons

    :param struct gpio_keys_drvdata \*ddata:
        pointer to drvdata

    :param char \*buf:
        buffer where stringified bitmap is written

    :param unsigned int type:
        button type (\ ``EV_KEY``\ , \ ``EV_SW``\ )

    :param bool only_disabled:
        does caller want only those buttons that are
        currently disabled or all buttons that can be
        disabled

.. _`gpio_keys_attr_show_helper.description`:

Description
-----------

This function writes buttons that can be disabled to \ ``buf``\ . If
\ ``only_disabled``\  is true, then \ ``buf``\  contains only those buttons
that are currently disabled. Returns 0 on success or negative
errno on failure.

.. _`gpio_keys_attr_store_helper`:

gpio_keys_attr_store_helper
===========================

.. c:function:: ssize_t gpio_keys_attr_store_helper(struct gpio_keys_drvdata *ddata, const char *buf, unsigned int type)

    enable/disable buttons based on given bitmap

    :param struct gpio_keys_drvdata \*ddata:
        pointer to drvdata

    :param const char \*buf:
        buffer from userspace that contains stringified bitmap

    :param unsigned int type:
        button type (\ ``EV_KEY``\ , \ ``EV_SW``\ )

.. _`gpio_keys_attr_store_helper.description`:

Description
-----------

This function parses stringified bitmap from \ ``buf``\  and disables/enables
GPIO buttons accordingly. Returns 0 on success and negative error
on failure.

.. This file was automatic generated / don't edit.

