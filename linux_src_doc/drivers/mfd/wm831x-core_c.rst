.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/wm831x-core.c

.. _`wm831x_reg_lock`:

wm831x_reg_lock
===============

.. c:function:: void wm831x_reg_lock(struct wm831x *wm831x)

    Unlock user keyed registers

    :param wm831x:
        *undescribed*
    :type wm831x: struct wm831x \*

.. _`wm831x_reg_lock.description`:

Description
-----------

The WM831x has a user key preventing writes to particularly
critical registers.  This function locks those registers,
allowing writes to them.

.. _`wm831x_reg_unlock`:

wm831x_reg_unlock
=================

.. c:function:: int wm831x_reg_unlock(struct wm831x *wm831x)

    Unlock user keyed registers

    :param wm831x:
        *undescribed*
    :type wm831x: struct wm831x \*

.. _`wm831x_reg_unlock.description`:

Description
-----------

The WM831x has a user key preventing writes to particularly
critical registers.  This function locks those registers,
preventing spurious writes.

.. _`wm831x_reg_read`:

wm831x_reg_read
===============

.. c:function:: int wm831x_reg_read(struct wm831x *wm831x, unsigned short reg)

    Read a single WM831x register.

    :param wm831x:
        Device to read from.
    :type wm831x: struct wm831x \*

    :param reg:
        Register to read.
    :type reg: unsigned short

.. _`wm831x_bulk_read`:

wm831x_bulk_read
================

.. c:function:: int wm831x_bulk_read(struct wm831x *wm831x, unsigned short reg, int count, u16 *buf)

    Read multiple WM831x registers

    :param wm831x:
        Device to read from
    :type wm831x: struct wm831x \*

    :param reg:
        First register
    :type reg: unsigned short

    :param count:
        Number of registers
    :type count: int

    :param buf:
        Buffer to fill.
    :type buf: u16 \*

.. _`wm831x_reg_write`:

wm831x_reg_write
================

.. c:function:: int wm831x_reg_write(struct wm831x *wm831x, unsigned short reg, unsigned short val)

    Write a single WM831x register.

    :param wm831x:
        Device to write to.
    :type wm831x: struct wm831x \*

    :param reg:
        Register to write to.
    :type reg: unsigned short

    :param val:
        Value to write.
    :type val: unsigned short

.. _`wm831x_set_bits`:

wm831x_set_bits
===============

.. c:function:: int wm831x_set_bits(struct wm831x *wm831x, unsigned short reg, unsigned short mask, unsigned short val)

    Set the value of a bitfield in a WM831x register

    :param wm831x:
        Device to write to.
    :type wm831x: struct wm831x \*

    :param reg:
        Register to write to.
    :type reg: unsigned short

    :param mask:
        Mask of bits to set.
    :type mask: unsigned short

    :param val:
        Value to set (unshifted)
    :type val: unsigned short

.. This file was automatic generated / don't edit.

