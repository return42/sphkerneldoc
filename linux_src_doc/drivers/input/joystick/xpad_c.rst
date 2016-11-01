.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/joystick/xpad.c

.. _`xpad_send_led_command`:

xpad_send_led_command
=====================

.. c:function:: void xpad_send_led_command(struct usb_xpad *xpad, int command)

    @param command 0: off 1: all blink, then previous setting 2: 1/top-left blink, then on 3: 2/top-right blink, then on 4: 3/bottom-left blink, then on 5: 4/bottom-right blink, then on 6: 1/top-left on 7: 2/top-right on 8: 3/bottom-left on 9: 4/bottom-right on 10: rotate 11: blink, based on previous setting 12: slow blink, based on previous setting 13: rotate with two lights 14: persistent slow all blink 15: blink once, then previous setting

    :param struct usb_xpad \*xpad:
        *undescribed*

    :param int command:
        *undescribed*

.. This file was automatic generated / don't edit.

