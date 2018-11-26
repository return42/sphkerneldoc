.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/vt/keyboard.c

.. _`vt_get_leds`:

vt_get_leds
===========

.. c:function:: int vt_get_leds(int console, int flag)

    helper for braille console

    :param console:
        console to read
    :type console: int

    :param flag:
        flag we want to check
    :type flag: int

.. _`vt_get_leds.description`:

Description
-----------

Check the status of a keyboard led flag and report it back

.. _`vt_set_led_state`:

vt_set_led_state
================

.. c:function:: void vt_set_led_state(int console, int leds)

    set LED state of a console

    :param console:
        console to set
    :type console: int

    :param leds:
        LED bits
    :type leds: int

.. _`vt_set_led_state.description`:

Description
-----------

Set the LEDs on a console. This is a wrapper for the VT layer
so that we can keep kbd knowledge internal

.. _`vt_kbd_con_start`:

vt_kbd_con_start
================

.. c:function:: void vt_kbd_con_start(int console)

    Keyboard side of console start

    :param console:
        console
    :type console: int

.. _`vt_kbd_con_start.description`:

Description
-----------

Handle console start. This is a wrapper for the VT layer
so that we can keep kbd knowledge internal

.. _`vt_kbd_con_start.fixme`:

FIXME
-----

We eventually need to hold the kbd lock here to protect
the LED updating. We can't do it yet because fn_hold calls stop_tty
and start_tty under the kbd_event_lock, while normal tty paths
don't hold the lock. We probably need to split out an LED lock
but not during an -rc release!

.. _`vt_kbd_con_stop`:

vt_kbd_con_stop
===============

.. c:function:: void vt_kbd_con_stop(int console)

    Keyboard side of console stop

    :param console:
        console
    :type console: int

.. _`vt_kbd_con_stop.description`:

Description
-----------

Handle console stop. This is a wrapper for the VT layer
so that we can keep kbd knowledge internal

.. _`vt_do_diacrit`:

vt_do_diacrit
=============

.. c:function:: int vt_do_diacrit(unsigned int cmd, void __user *udp, int perm)

    diacritical table updates

    :param cmd:
        ioctl request
    :type cmd: unsigned int

    :param udp:
        pointer to user data for ioctl
    :type udp: void __user \*

    :param perm:
        permissions check computed by caller
    :type perm: int

.. _`vt_do_diacrit.description`:

Description
-----------

Update the diacritical tables atomically and safely. Lock them
against simultaneous keypresses

.. _`vt_do_kdskbmode`:

vt_do_kdskbmode
===============

.. c:function:: int vt_do_kdskbmode(int console, unsigned int arg)

    set keyboard mode ioctl

    :param console:
        the console to use
    :type console: int

    :param arg:
        the requested mode
    :type arg: unsigned int

.. _`vt_do_kdskbmode.description`:

Description
-----------

Update the keyboard mode bits while holding the correct locks.
Return 0 for success or an error code.

.. _`vt_do_kdskbmeta`:

vt_do_kdskbmeta
===============

.. c:function:: int vt_do_kdskbmeta(int console, unsigned int arg)

    set keyboard meta state

    :param console:
        the console to use
    :type console: int

    :param arg:
        the requested meta state
    :type arg: unsigned int

.. _`vt_do_kdskbmeta.description`:

Description
-----------

Update the keyboard meta bits while holding the correct locks.
Return 0 for success or an error code.

.. _`vt_do_kdgkbmeta`:

vt_do_kdgkbmeta
===============

.. c:function:: int vt_do_kdgkbmeta(int console)

    report meta status

    :param console:
        console to report
    :type console: int

.. _`vt_do_kdgkbmeta.description`:

Description
-----------

Report the meta flag status of this console

.. _`vt_reset_unicode`:

vt_reset_unicode
================

.. c:function:: void vt_reset_unicode(int console)

    reset the unicode status

    :param console:
        console being reset
    :type console: int

.. _`vt_reset_unicode.description`:

Description
-----------

Restore the unicode console state to its default

.. _`vt_get_shift_state`:

vt_get_shift_state
==================

.. c:function:: int vt_get_shift_state( void)

    shift bit state

    :param void:
        no arguments
    :type void: 

.. _`vt_get_shift_state.description`:

Description
-----------

Report the shift bits from the keyboard state. We have to export
this to support some oddities in the vt layer.

.. _`vt_reset_keyboard`:

vt_reset_keyboard
=================

.. c:function:: void vt_reset_keyboard(int console)

    reset keyboard state

    :param console:
        console to reset
    :type console: int

.. _`vt_reset_keyboard.description`:

Description
-----------

Reset the keyboard bits for a console as part of a general console
reset event

.. _`vt_get_kbd_mode_bit`:

vt_get_kbd_mode_bit
===================

.. c:function:: int vt_get_kbd_mode_bit(int console, int bit)

    read keyboard status bits

    :param console:
        console to read from
    :type console: int

    :param bit:
        mode bit to read
    :type bit: int

.. _`vt_get_kbd_mode_bit.description`:

Description
-----------

Report back a vt mode bit. We do this without locking so the
caller must be sure that there are no synchronization needs

.. _`vt_set_kbd_mode_bit`:

vt_set_kbd_mode_bit
===================

.. c:function:: void vt_set_kbd_mode_bit(int console, int bit)

    read keyboard status bits

    :param console:
        console to read from
    :type console: int

    :param bit:
        mode bit to read
    :type bit: int

.. _`vt_set_kbd_mode_bit.description`:

Description
-----------

Set a vt mode bit. We do this without locking so the
caller must be sure that there are no synchronization needs

.. _`vt_clr_kbd_mode_bit`:

vt_clr_kbd_mode_bit
===================

.. c:function:: void vt_clr_kbd_mode_bit(int console, int bit)

    read keyboard status bits

    :param console:
        console to read from
    :type console: int

    :param bit:
        mode bit to read
    :type bit: int

.. _`vt_clr_kbd_mode_bit.description`:

Description
-----------

Report back a vt mode bit. We do this without locking so the
caller must be sure that there are no synchronization needs

.. This file was automatic generated / don't edit.

