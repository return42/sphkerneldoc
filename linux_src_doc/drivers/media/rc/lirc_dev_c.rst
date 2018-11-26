.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/lirc_dev.c

.. _`ir_lirc_raw_event`:

ir_lirc_raw_event
=================

.. c:function:: void ir_lirc_raw_event(struct rc_dev *dev, struct ir_raw_event ev)

    Send raw IR data to lirc to be relayed to userspace

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

    :param ev:
        the struct ir_raw_event descriptor of the pulse/space
    :type ev: struct ir_raw_event

.. _`ir_lirc_scancode_event`:

ir_lirc_scancode_event
======================

.. c:function:: void ir_lirc_scancode_event(struct rc_dev *dev, struct lirc_scancode *lsc)

    Send scancode data to lirc to be relayed to userspace. This can be called in atomic context.

    :param dev:
        the struct rc_dev descriptor of the device
    :type dev: struct rc_dev \*

    :param lsc:
        the struct lirc_scancode describing the decoded scancode
    :type lsc: struct lirc_scancode \*

.. This file was automatic generated / don't edit.

