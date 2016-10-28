.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/omap-usb-tll.c

.. _`usbtll_driver_name`:

USBTLL_DRIVER_NAME
==================

.. c:function::  USBTLL_DRIVER_NAME()

    usb-tll.c - The USB TLL driver for OMAP EHCI & OHCI

.. _`usbtll_driver_name.description`:

Description
-----------

Copyright (C) 2012-2013 Texas Instruments Incorporated - http://www.ti.com

.. _`usbtll_driver_name.author`:

Author
------

Keshava Munegowda <keshava_mgowda\ ``ti``\ .com>

Roger Quadros <rogerq\ ``ti``\ .com>

.. _`usbtll_driver_name.this-program-is-free-software`:

This program is free software
-----------------------------

you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2  of
the License as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

.. _`usbtll_omap_probe`:

usbtll_omap_probe
=================

.. c:function:: int usbtll_omap_probe(struct platform_device *pdev)

    initialize TI-based HCDs

    :param struct platform_device \*pdev:
        *undescribed*

.. _`usbtll_omap_probe.description`:

Description
-----------

Allocates basic resources for this USB host controller.

.. _`usbtll_omap_remove`:

usbtll_omap_remove
==================

.. c:function:: int usbtll_omap_remove(struct platform_device *pdev)

    shutdown processing for UHH & TLL HCDs

    :param struct platform_device \*pdev:
        USB Host Controller being removed

.. _`usbtll_omap_remove.description`:

Description
-----------

Reverses the effect of \ :c:func:`usbtll_omap_probe`\ .

.. This file was automatic generated / don't edit.

