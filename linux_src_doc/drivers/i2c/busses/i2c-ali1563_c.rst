.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-ali1563.c

.. _`ali1563_max_timeout`:

ALI1563_MAX_TIMEOUT
===================

.. c:function::  ALI1563_MAX_TIMEOUT()

    ali1563.c - i2c driver for the ALi 1563 Southbridge

.. _`ali1563_max_timeout.description`:

Description
-----------

Copyright (C) 2004 Patrick Mochel
2005 Rudolf Marek <r.marek\ ``assembler``\ .cz>

The 1563 southbridge is deceptively similar to the 1533, with a
few notable exceptions. One of those happens to be the fact they
upgraded the i2c core to be 2.0 compliant, and happens to be almost
identical to the i2c controller found in the Intel 801 south
bridges.

This driver is based on a mix of the 15x3, 1535, and i801 drivers,
with a little help from the ALi 1563 spec.

This file is released under the GPLv2

.. This file was automatic generated / don't edit.

