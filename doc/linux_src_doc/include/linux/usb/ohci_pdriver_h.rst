.. -*- coding: utf-8; mode: rst -*-

==============
ohci_pdriver.h
==============


.. _`usb_ohci_pdata`:

struct usb_ohci_pdata
=====================

.. c:type:: usb_ohci_pdata

    platform_data for generic ohci driver


.. _`usb_ohci_pdata.definition`:

Definition
----------

.. code-block:: c

  struct usb_ohci_pdata {
    unsigned big_endian_desc:1;
    unsigned big_endian_mmio:1;
    unsigned no_big_frame_no:1;
    unsigned int num_ports;
  };


.. _`usb_ohci_pdata.members`:

Members
-------

:``big_endian_desc``:
    BE descriptors

:``big_endian_mmio``:
    BE registers

:``no_big_frame_no``:
    no big endian frame_no shift

:``num_ports``:
    number of ports




.. _`usb_ohci_pdata.description`:

Description
-----------

These are general configuration options for the OHCI controller. All of
these options are activating more or less workarounds for some hardware.

