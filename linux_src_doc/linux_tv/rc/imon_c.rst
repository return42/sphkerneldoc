.. -*- coding: utf-8; mode: rst -*-

======
imon.c
======



.. _xref_display_open:

display_open
============

.. c:function:: int display_open (struct inode * inode, struct file * file)

    

    :param struct inode * inode:

        _undescribed_

    :param struct file * file:

        _undescribed_



Description
-----------

is opened by the application.




.. _xref_display_close:

display_close
=============

.. c:function:: int display_close (struct inode * inode, struct file * file)

    

    :param struct inode * inode:

        _undescribed_

    :param struct file * file:

        _undescribed_



Description
-----------

is closed by the application.




.. _xref_send_packet:

send_packet
===========

.. c:function:: int send_packet (struct imon_context * ictx)

    - this function must be called with ictx-\\\gt;lock held, or its unlock/lock sequence while waiting for tx to complete can/will lead to a deadlock.

    :param struct imon_context * ictx:

        _undescribed_




.. _xref_send_associate_24g:

send_associate_24g
==================

.. c:function:: int send_associate_24g (struct imon_context * ictx)

    

    :param struct imon_context * ictx:

        _undescribed_



Description
-----------



This might not be such a good idea, since it has an id collision with
some versions of the "IR & VFD" combo. The only way to determine if it
is an RF version is to look at the product description string. (Which
we currently do not fetch).




.. _xref_send_set_imon_clock:

send_set_imon_clock
===================

.. c:function:: int send_set_imon_clock (struct imon_context * ictx, unsigned int year, unsigned int month, unsigned int day, unsigned int dow, unsigned int hour, unsigned int minute, unsigned int second)

    

    :param struct imon_context * ictx:

        _undescribed_

    :param unsigned int year:

        _undescribed_

    :param unsigned int month:

        _undescribed_

    :param unsigned int day:

        _undescribed_

    :param unsigned int dow:

        _undescribed_

    :param unsigned int hour:

        _undescribed_

    :param unsigned int minute:

        _undescribed_

    :param unsigned int second:

        _undescribed_



Arguments
---------

year - last 2 digits of year, month - 1..12,
day - 1..31, dow - day of the week (0-Sun...6-Sat),
hour - 0..23, minute - 0..59, second - 0..59




.. _xref_show_associate_remote:

show_associate_remote
=====================

.. c:function:: ssize_t show_associate_remote (struct device * d, struct device_attribute * attr, char * buf)

    

    :param struct device * d:

        _undescribed_

    :param struct device_attribute * attr:

        _undescribed_

    :param char * buf:

        _undescribed_




.. _xref_show_imon_clock:

show_imon_clock
===============

.. c:function:: ssize_t show_imon_clock (struct device * d, struct device_attribute * attr, char * buf)

    

    :param struct device * d:

        _undescribed_

    :param struct device_attribute * attr:

        _undescribed_

    :param char * buf:

        _undescribed_




.. _xref_vfd_write:

vfd_write
=========

.. c:function:: ssize_t vfd_write (struct file * file, const char __user * buf, size_t n_bytes, loff_t * pos)

    

    :param struct file * file:

        _undescribed_

    :param const char __user * buf:

        _undescribed_

    :param size_t n_bytes:

        _undescribed_

    :param loff_t * pos:

        _undescribed_



Description
-----------

and requires data in 5 consecutive USB interrupt packets,
each packet but the last carrying 7 bytes.


I don't know if the VFD board supports features such as
scrolling, clearing rows, blanking, etc. so at
the caller must provide a full screen of data.  If fewer
than 32 bytes are provided spaces will be appended to
generate a full screen.




.. _xref_lcd_write:

lcd_write
=========

.. c:function:: ssize_t lcd_write (struct file * file, const char __user * buf, size_t n_bytes, loff_t * pos)

    byte packets. We accept data as 16 hexadecimal digits, followed by a newline (to make it easy to drive the device from a command-line -- even though the actual binary data is a bit complicated).

    :param struct file * file:

        _undescribed_

    :param const char __user * buf:

        _undescribed_

    :param size_t n_bytes:

        _undescribed_

    :param loff_t * pos:

        _undescribed_



Description
-----------



The device itself is not a "traditional" text-mode display. It's
actually a 16x96 pixel bitmap display. That means if you want to
display text, you've got to have your own "font" and translate the
text into bitmaps for display. This is really flexible (you can
display whatever diacritics you need, and so on), but it's also
a lot more complicated than most LCDs...




.. _xref_usb_tx_callback:

usb_tx_callback
===============

.. c:function:: void usb_tx_callback (struct urb * urb)

    

    :param struct urb * urb:

        _undescribed_




.. _xref_imon_touch_display_timeout:

imon_touch_display_timeout
==========================

.. c:function:: void imon_touch_display_timeout (unsigned long data)

    

    :param unsigned long data:

        _undescribed_




.. _xref_imon_ir_change_protocol:

imon_ir_change_protocol
=======================

.. c:function:: int imon_ir_change_protocol (struct rc_dev * rc, u64 * rc_type)

    - those used by the iMON remotes, and those used by the Windows MCE remotes (which is really just RC-6), but only one or the other at a time, as the signals are decoded onboard the receiver.

    :param struct rc_dev * rc:

        _undescribed_

    :param u64 * rc_type:

        _undescribed_



Description
-----------



This function gets called two different ways, one way is from
rc_register_device, for initial protocol selection/setup, and the other is
via a userspace-initiated protocol change request, either by direct sysfs
prodding or by something like ir-keytable. In the rc_register_device case,
the imon context lock is already held, but when initiated from userspace,
it is not, so we must acquire it prior to calling send_packet, which
requires that the lock is held.




.. _xref_stabilize:

stabilize
=========

.. c:function:: int stabilize (int a, int b, u16 timeout, u16 threshold)

    

    :param int a:

        _undescribed_

    :param int b:

        _undescribed_

    :param u16 timeout:

        _undescribed_

    :param u16 threshold:

        _undescribed_



Description
-----------

one of the older ffdc devices or a newer device. Newer devices appear to
have a higher resolution matrix for more precise mouse movement, but it
makes things overly sensitive in keyboard mode, so we do some interesting
contortions to make it less touchy. Older devices run through the same
routine with shorter timeout and a smaller threshold.




.. _xref_imon_parse_press_type:

imon_parse_press_type
=====================

.. c:function:: int imon_parse_press_type (struct imon_context * ictx, unsigned char * buf, u8 ktype)

    

    :param struct imon_context * ictx:

        _undescribed_

    :param unsigned char * buf:

        _undescribed_

    :param u8 ktype:

        _undescribed_



Description
-----------

care about repeats, as those will be auto-generated within the IR
subsystem for repeating scancodes.




.. _xref_imon_incoming_packet:

imon_incoming_packet
====================

.. c:function:: void imon_incoming_packet (struct imon_context * ictx, struct urb * urb, int intf)

    

    :param struct imon_context * ictx:

        _undescribed_

    :param struct urb * urb:

        _undescribed_

    :param int intf:

        _undescribed_




.. _xref_usb_rx_callback_intf0:

usb_rx_callback_intf0
=====================

.. c:function:: void usb_rx_callback_intf0 (struct urb * urb)

    

    :param struct urb * urb:

        _undescribed_




.. _xref_imon_probe:

imon_probe
==========

.. c:function:: int imon_probe (struct usb_interface * interface, const struct usb_device_id * id)

    

    :param struct usb_interface * interface:

        _undescribed_

    :param const struct usb_device_id * id:

        _undescribed_




.. _xref_imon_disconnect:

imon_disconnect
===============

.. c:function:: void imon_disconnect (struct usb_interface * interface)

    

    :param struct usb_interface * interface:

        _undescribed_


