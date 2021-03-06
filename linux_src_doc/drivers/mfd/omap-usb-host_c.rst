.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/omap-usb-host.c

.. _`usbhs_driver_name`:

USBHS_DRIVER_NAME
=================

.. c:function::  USBHS_DRIVER_NAME()

    usb-host.c - The USBHS core driver for OMAP EHCI & OHCI

.. _`usbhs_driver_name.description`:

Description
-----------

Copyright (C) 2011-2013 Texas Instruments Incorporated - http://www.ti.com

.. _`usbhs_driver_name.author`:

Author
------

Keshava Munegowda <keshava_mgowda@ti.com>

Roger Quadros <rogerq@ti.com>

.. _`usbhs_driver_name.this-program-is-free-software`:

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

.. _`usbhs_omap_probe`:

usbhs_omap_probe
================

.. c:function:: int usbhs_omap_probe(struct platform_device *pdev)

    initialize TI-based HCDs

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

.. _`usbhs_omap_probe.description`:

Description
-----------

Allocates basic resources for this USB host controller.

.. _`usbhs_omap_remove`:

usbhs_omap_remove
=================

.. c:function:: int usbhs_omap_remove(struct platform_device *pdev)

    shutdown processing for UHH & TLL HCDs

    :param pdev:
        USB Host Controller being removed
    :type pdev: struct platform_device \*

.. _`usbhs_omap_remove.description`:

Description
-----------

Reverses the effect of \ :c:func:`usbhs_omap_probe`\ .

.. This file was automatic generated / don't edit.

