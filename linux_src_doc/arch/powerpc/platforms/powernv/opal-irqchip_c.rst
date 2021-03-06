.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/powernv/opal-irqchip.c

.. _`opal_event_request`:

opal_event_request
==================

.. c:function:: int opal_event_request(unsigned int opal_event_nr)

    Request an event

    :param opal_event_nr:
        the opal event number to request
    :type opal_event_nr: unsigned int

.. _`opal_event_request.description`:

Description
-----------

This routine can be used to find the linux virq number which can
then be passed to request_irq to assign a handler for a particular
opal event. This should only be used by legacy devices which don't
have proper device tree bindings. Most devices should use
\ :c:func:`irq_of_parse_and_map`\  instead.

.. This file was automatic generated / don't edit.

