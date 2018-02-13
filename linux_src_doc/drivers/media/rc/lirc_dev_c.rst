.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/lirc_dev.c

.. _`ir_lirc_raw_event`:

ir_lirc_raw_event
=================

.. c:function:: void ir_lirc_raw_event(struct rc_dev *dev, struct ir_raw_event ev)

    Send raw IR data to lirc to be relayed to userspace

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param struct ir_raw_event ev:
        the struct ir_raw_event descriptor of the pulse/space

.. _`ir_lirc_scancode_event`:

ir_lirc_scancode_event
======================

.. c:function:: void ir_lirc_scancode_event(struct rc_dev *dev, struct lirc_scancode *lsc)

    Send scancode data to lirc to be relayed to userspace. This can be called in atomic context.

    :param struct rc_dev \*dev:
        the struct rc_dev descriptor of the device

    :param struct lirc_scancode \*lsc:
        the struct lirc_scancode describing the decoded scancode

.. This file was automatic generated / don't edit.

