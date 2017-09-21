.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/imon.c

.. _`display_open`:

display_open
============

.. c:function:: int display_open(struct inode *inode, struct file *file)

    is opened by the application.

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

.. _`display_close`:

display_close
=============

.. c:function:: int display_close(struct inode *inode, struct file *file)

    is closed by the application.

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*file:
        *undescribed*

.. _`send_packet`:

send_packet
===========

.. c:function:: int send_packet(struct imon_context *ictx)

    - this function must be called with ictx->lock held, or its unlock/lock sequence while waiting for tx to complete can/will lead to a deadlock.

    :param struct imon_context \*ictx:
        *undescribed*

.. _`send_associate_24g`:

send_associate_24g
==================

.. c:function:: int send_associate_24g(struct imon_context *ictx)

    :param struct imon_context \*ictx:
        *undescribed*

.. _`send_associate_24g.description`:

Description
-----------

This might not be such a good idea, since it has an id collision with
some versions of the "IR & VFD" combo. The only way to determine if it
is an RF version is to look at the product description string. (Which
we currently do not fetch).

.. _`send_set_imon_clock`:

send_set_imon_clock
===================

.. c:function:: int send_set_imon_clock(struct imon_context *ictx, unsigned int year, unsigned int month, unsigned int day, unsigned int dow, unsigned int hour, unsigned int minute, unsigned int second)

    :param struct imon_context \*ictx:
        *undescribed*

    :param unsigned int year:
        *undescribed*

    :param unsigned int month:
        *undescribed*

    :param unsigned int day:
        *undescribed*

    :param unsigned int dow:
        *undescribed*

    :param unsigned int hour:
        *undescribed*

    :param unsigned int minute:
        *undescribed*

    :param unsigned int second:
        *undescribed*

.. _`send_set_imon_clock.arguments`:

Arguments
---------

year - last 2 digits of year, month - 1..12,
day - 1..31, dow - day of the week (0-Sun...6-Sat),
hour - 0..23, minute - 0..59, second - 0..59

.. _`show_associate_remote`:

show_associate_remote
=====================

.. c:function:: ssize_t show_associate_remote(struct device *d, struct device_attribute *attr, char *buf)

    :param struct device \*d:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`show_imon_clock`:

show_imon_clock
===============

.. c:function:: ssize_t show_imon_clock(struct device *d, struct device_attribute *attr, char *buf)

    :param struct device \*d:
        *undescribed*

    :param struct device_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`vfd_write`:

vfd_write
=========

.. c:function:: ssize_t vfd_write(struct file *file, const char __user *buf, size_t n_bytes, loff_t *pos)

    and requires data in 5 consecutive USB interrupt packets, each packet but the last carrying 7 bytes.

    :param struct file \*file:
        *undescribed*

    :param const char __user \*buf:
        *undescribed*

    :param size_t n_bytes:
        *undescribed*

    :param loff_t \*pos:
        *undescribed*

.. _`vfd_write.description`:

Description
-----------

I don't know if the VFD board supports features such as
scrolling, clearing rows, blanking, etc. so at
the caller must provide a full screen of data.  If fewer
than 32 bytes are provided spaces will be appended to
generate a full screen.

.. _`lcd_write`:

lcd_write
=========

.. c:function:: ssize_t lcd_write(struct file *file, const char __user *buf, size_t n_bytes, loff_t *pos)

    byte packets. We accept data as 16 hexadecimal digits, followed by a newline (to make it easy to drive the device from a command-line -- even though the actual binary data is a bit complicated).

    :param struct file \*file:
        *undescribed*

    :param const char __user \*buf:
        *undescribed*

    :param size_t n_bytes:
        *undescribed*

    :param loff_t \*pos:
        *undescribed*

.. _`lcd_write.description`:

Description
-----------

The device itself is not a "traditional" text-mode display. It's
actually a 16x96 pixel bitmap display. That means if you want to
display text, you've got to have your own "font" and translate the
text into bitmaps for display. This is really flexible (you can
display whatever diacritics you need, and so on), but it's also
a lot more complicated than most LCDs...

.. _`usb_tx_callback`:

usb_tx_callback
===============

.. c:function:: void usb_tx_callback(struct urb *urb)

    transmit data

    :param struct urb \*urb:
        *undescribed*

.. _`imon_touch_display_timeout`:

imon_touch_display_timeout
==========================

.. c:function:: void imon_touch_display_timeout(unsigned long data)

    :param unsigned long data:
        *undescribed*

.. _`imon_ir_change_protocol`:

imon_ir_change_protocol
=======================

.. c:function:: int imon_ir_change_protocol(struct rc_dev *rc, u64 *rc_proto)

    - those used by the iMON remotes, and those used by the Windows MCE remotes (which is really just RC-6), but only one or the other at a time, as the signals are decoded onboard the receiver.

    :param struct rc_dev \*rc:
        *undescribed*

    :param u64 \*rc_proto:
        *undescribed*

.. _`imon_ir_change_protocol.description`:

Description
-----------

This function gets called two different ways, one way is from
rc_register_device, for initial protocol selection/setup, and the other is
via a userspace-initiated protocol change request, either by direct sysfs
prodding or by something like ir-keytable. In the rc_register_device case,
the imon context lock is already held, but when initiated from userspace,
it is not, so we must acquire it prior to calling send_packet, which
requires that the lock is held.

.. _`stabilize`:

stabilize
=========

.. c:function:: int stabilize(int a, int b, u16 timeout, u16 threshold)

    one of the older ffdc devices or a newer device. Newer devices appear to have a higher resolution matrix for more precise mouse movement, but it makes things overly sensitive in keyboard mode, so we do some interesting contortions to make it less touchy. Older devices run through the same routine with shorter timeout and a smaller threshold.

    :param int a:
        *undescribed*

    :param int b:
        *undescribed*

    :param u16 timeout:
        *undescribed*

    :param u16 threshold:
        *undescribed*

.. _`imon_parse_press_type`:

imon_parse_press_type
=====================

.. c:function:: int imon_parse_press_type(struct imon_context *ictx, unsigned char *buf, u8 ktype)

    care about repeats, as those will be auto-generated within the IR subsystem for repeating scancodes.

    :param struct imon_context \*ictx:
        *undescribed*

    :param unsigned char \*buf:
        *undescribed*

    :param u8 ktype:
        *undescribed*

.. _`submit_data`:

submit_data
===========

.. c:function:: void submit_data(struct imon_context *context)

    :param struct imon_context \*context:
        *undescribed*

.. _`imon_incoming_ir_raw`:

imon_incoming_ir_raw
====================

.. c:function:: void imon_incoming_ir_raw(struct imon_context *context, struct urb *urb, int intf)

    :param struct imon_context \*context:
        *undescribed*

    :param struct urb \*urb:
        *undescribed*

    :param int intf:
        *undescribed*

.. _`usb_rx_callback_intf0`:

usb_rx_callback_intf0
=====================

.. c:function:: void usb_rx_callback_intf0(struct urb *urb)

    receive data

    :param struct urb \*urb:
        *undescribed*

.. _`imon_probe`:

imon_probe
==========

.. c:function:: int imon_probe(struct usb_interface *interface, const struct usb_device_id *id)

    Probe

    :param struct usb_interface \*interface:
        *undescribed*

    :param const struct usb_device_id \*id:
        *undescribed*

.. _`imon_disconnect`:

imon_disconnect
===============

.. c:function:: void imon_disconnect(struct usb_interface *interface)

    disconnect

    :param struct usb_interface \*interface:
        *undescribed*

.. This file was automatic generated / don't edit.

