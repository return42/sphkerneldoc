.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-sa1100/jornada720_ssp.c

.. _`define_spinlock`:

DEFINE_SPINLOCK
===============

.. c:function::  DEFINE_SPINLOCK( jornada_ssp_lock)

    sa1100/jornada720_ssp.c

    :param  jornada_ssp_lock:
        *undescribed*

.. _`define_spinlock.description`:

Description
-----------

Copyright (C) 2006/2007 Kristoffer Ericson <Kristoffer.Ericson@gmail.com>
Copyright (C) 2006 Filip Zyzniewski <filip.zyzniewski@tefnet.pl>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation.

SSP driver for the HP Jornada 710/720/728

.. _`jornada_ssp_reverse`:

jornada_ssp_reverse
===================

.. c:function:: u8 jornada_ssp_reverse(u8 byte)

    reverses input byte

    :param u8 byte:
        *undescribed*

.. _`jornada_ssp_reverse.description`:

Description
-----------

we need to reverse all data we receive from the mcu due to its physical location
returns : 01110111 -> 11101110

.. _`jornada_ssp_byte`:

jornada_ssp_byte
================

.. c:function:: int jornada_ssp_byte(u8 byte)

    waits for ready ssp bus and sends byte

    :param u8 byte:
        *undescribed*

.. _`jornada_ssp_byte.description`:

Description
-----------

waits for fifo buffer to clear and then transmits, if it doesn't then we will
timeout after <timeout> rounds. Needs mcu running before its called.

returns : \ ``mcu``\  output on success
: \ ``-ETIMEDOUT``\  on timeout

.. _`jornada_ssp_inout`:

jornada_ssp_inout
=================

.. c:function:: int jornada_ssp_inout(u8 byte)

    decide if input is command or trading byte

    :param u8 byte:
        *undescribed*

.. _`jornada_ssp_inout.description`:

Description
-----------

returns : (jornada_ssp_byte(byte)) on success
: \ ``-ETIMEDOUT``\  on timeout failure

.. _`jornada_ssp_start`:

jornada_ssp_start
=================

.. c:function:: void jornada_ssp_start( void)

    enable mcu

    :param  void:
        no arguments

.. _`jornada_ssp_end`:

jornada_ssp_end
===============

.. c:function:: void jornada_ssp_end( void)

    disable mcu and turn off lock

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

