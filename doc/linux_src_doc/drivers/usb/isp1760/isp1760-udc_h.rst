.. -*- coding: utf-8; mode: rst -*-

=============
isp1760-udc.h
=============


.. _`isp1760_udc`:

struct isp1760_udc
==================

.. c:type:: isp1760_udc

    UDC state information


.. _`isp1760_udc.definition`:

Definition
----------

.. code-block:: c

  struct isp1760_udc {
    #ifdef CONFIG_USB_ISP1761_UDC
    #endif
  };


.. _`isp1760_udc.members`:

Members
-------




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



.. _`isp1760_udc.ep`:

ep
--

Array of endpoints



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

