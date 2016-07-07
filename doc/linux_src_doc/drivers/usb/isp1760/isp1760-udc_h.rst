.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/isp1760/isp1760-udc.h

.. _`isp1760_udc`:

struct isp1760_udc
==================

.. c:type:: struct isp1760_udc

    UDC state information

.. _`isp1760_udc.definition`:

Definition
----------

.. code-block:: c

    struct isp1760_udc {
        #ifdef CONFIG_USB_ISP1761_UDC
        struct isp1760_device *isp;
        int irq;
        char *irqname;
        void __iomem *regs;
        struct usb_gadget_driver *driver;
        struct usb_gadget gadget;
        spinlock_t lock;
        struct timer_list vbus_timer;
        struct isp1760_ep ep[15];
        enum isp1760_ctrl_state ep0_state;
        u8 ep0_dir;
        u16 ep0_length;
        bool connected;
        unsigned int devstatus;
        #endif
    }

.. _`isp1760_udc.members`:

Members
-------

isp
    *undescribed*

irq
    *undescribed*

irqname
    *undescribed*

regs
    *undescribed*

driver
    *undescribed*

gadget
    *undescribed*

lock
    *undescribed*

vbus_timer
    *undescribed*

ep0_state
    *undescribed*

ep0_dir
    *undescribed*

ep0_length
    *undescribed*

connected
    *undescribed*

devstatus
    *undescribed*

.. _`isp1760_udc.irq`:

irq
---

IRQ number

.. _`isp1760_udc.irqname`:

irqname
-------

IRQ name (as passed to request_irq)

.. _`isp1760_udc.regs`:

regs
----

Base address of the UDC registers

.. _`isp1760_udc.driver`:

driver
------

Gadget driver

.. _`isp1760_udc.gadget`:

gadget
------

Gadget device

.. _`isp1760_udc.lock`:

lock
----

Protects driver, vbus_timer, ep, ep0\_\*, DC_EPINDEX register
ep: Array of endpoints

.. _`isp1760_udc.ep0_state`:

ep0_state
---------

Control request state for endpoint 0

.. _`isp1760_udc.ep0_dir`:

ep0_dir
-------

Direction of the current control request

.. _`isp1760_udc.ep0_length`:

ep0_length
----------

Length of the current control request

.. _`isp1760_udc.connected`:

connected
---------

Tracks gadget driver bus connection state

.. This file was automatic generated / don't edit.

