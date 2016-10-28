.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/ir-lirc-codec.c

.. _`ir_lirc_decode`:

ir_lirc_decode
==============

.. c:function:: int ir_lirc_decode(struct rc_dev *dev, struct ir_raw_event ev)

    Send raw IR data to lirc_dev to be relayed to the lircd userspace daemon for decoding.

    :param struct rc_dev \*dev:
        *undescribed*

    :param struct ir_raw_event ev:
        *undescribed*

.. _`ir_lirc_decode.description`:

Description
-----------

This function returns -EINVAL if the lirc interfaces aren't wired up.

.. This file was automatic generated / don't edit.

