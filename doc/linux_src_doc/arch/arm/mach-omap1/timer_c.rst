.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap1/timer.c

.. _`omap1610_gptimer1_base`:

OMAP1610_GPTIMER1_BASE
======================

.. c:function::  OMAP1610_GPTIMER1_BASE()

    Mode Timers - platform device registration

.. _`omap1610_gptimer1_base.description`:

Description
-----------

Contains first level initialization routines which internally
generates timer device information and registers with linux
device model. It also has low level function to chnage the timer
input clock source.

Copyright (C) 2011 Texas Instruments Incorporated - http://www.ti.com/
Tarun Kanti DebBarma <tarun.kanti\ ``ti``\ .com>
Thara Gopinath <thara\ ``ti``\ .com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation.

This program is distributed "as is" WITHOUT ANY WARRANTY of any
kind, whether express or implied; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

.. This file was automatic generated / don't edit.

