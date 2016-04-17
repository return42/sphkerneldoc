.. -*- coding: utf-8; mode: rst -*-

=============
wm831x-core.c
=============


.. _`wm831x_reg_lock`:

wm831x_reg_lock
===============

.. c:function:: void wm831x_reg_lock (struct wm831x *wm831x)

    :param struct wm831x \*wm831x:

        *undescribed*



.. _`wm831x_reg_lock.description`:

Description
-----------


The WM831x has a user key preventing writes to particularly
critical registers.  This function locks those registers,
allowing writes to them.



.. _`wm831x_reg_unlock`:

wm831x_reg_unlock
=================

.. c:function:: int wm831x_reg_unlock (struct wm831x *wm831x)

    :param struct wm831x \*wm831x:

        *undescribed*



.. _`wm831x_reg_unlock.description`:

Description
-----------


The WM831x has a user key preventing writes to particularly
critical registers.  This function locks those registers,
preventing spurious writes.



.. _`wm831x_reg_read`:

wm831x_reg_read
===============

.. c:function:: int wm831x_reg_read (struct wm831x *wm831x, unsigned short reg)

    :param struct wm831x \*wm831x:
        Device to read from.

    :param unsigned short reg:
        Register to read.



.. _`wm831x_bulk_read`:

wm831x_bulk_read
================

.. c:function:: int wm831x_bulk_read (struct wm831x *wm831x, unsigned short reg, int count, u16 *buf)

    :param struct wm831x \*wm831x:
        Device to read from

    :param unsigned short reg:
        First register

    :param int count:
        Number of registers

    :param u16 \*buf:
        Buffer to fill.



.. _`wm831x_reg_write`:

wm831x_reg_write
================

.. c:function:: int wm831x_reg_write (struct wm831x *wm831x, unsigned short reg, unsigned short val)

    :param struct wm831x \*wm831x:
        Device to write to.

    :param unsigned short reg:
        Register to write to.

    :param unsigned short val:
        Value to write.



.. _`wm831x_set_bits`:

wm831x_set_bits
===============

.. c:function:: int wm831x_set_bits (struct wm831x *wm831x, unsigned short reg, unsigned short mask, unsigned short val)

    :param struct wm831x \*wm831x:
        Device to write to.

    :param unsigned short reg:
        Register to write to.

    :param unsigned short mask:
        Mask of bits to set.

    :param unsigned short val:
        Value to set (unshifted)

