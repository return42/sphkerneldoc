.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pcmcia/cardbus.c

.. _`cb_alloc`:

cb_alloc
========

.. c:function:: int __ref cb_alloc(struct pcmcia_socket *s)

    add CardBus device

    :param struct pcmcia_socket \*s:
        the pcmcia_socket where the CardBus device is located

.. _`cb_alloc.description`:

Description
-----------

\ :c:func:`cb_alloc`\  allocates the kernel data structures for a Cardbus device
and handles the lowest level PCI device setup issues.

.. _`cb_free`:

cb_free
=======

.. c:function:: void cb_free(struct pcmcia_socket *s)

    remove CardBus device

    :param struct pcmcia_socket \*s:
        the pcmcia_socket where the CardBus device was located

.. _`cb_free.description`:

Description
-----------

\ :c:func:`cb_free`\  handles the lowest level PCI device cleanup.

.. This file was automatic generated / don't edit.

