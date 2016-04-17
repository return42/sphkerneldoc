.. -*- coding: utf-8; mode: rst -*-

===========
8250_port.c
===========


.. _`serial8250_em485_init`:

serial8250_em485_init
=====================

.. c:function:: int serial8250_em485_init (struct uart_8250_port *p)

    put uart_8250_port into rs485 emulating

    :param struct uart_8250_port \*p:
        uart_8250_port port instance



.. _`serial8250_em485_init.description`:

Description
-----------

The function is used to start rs485 software emulating on the
:c:type:`struct uart_8250_port <uart_8250_port>`\* ``p``\ . Namely, RTS is switched before/after
transmission. The function is idempotent, so it is safe to call it
multiple times.

The caller MUST enable interrupt on empty shift register before
calling :c:func:`serial8250_em485_init`. This interrupt is not a part of
8250 standard, but implementation defined.

The function is supposed to be called from .rs485_config callback
or from any other callback protected with p->port.lock spinlock.

See also :c:func:`serial8250_em485_destroy`

Return 0 - success, -errno - otherwise



.. _`serial8250_em485_destroy`:

serial8250_em485_destroy
========================

.. c:function:: void serial8250_em485_destroy (struct uart_8250_port *p)

    put uart_8250_port into normal state

    :param struct uart_8250_port \*p:
        uart_8250_port port instance



.. _`serial8250_em485_destroy.description`:

Description
-----------

The function is used to stop rs485 software emulating on the
:c:type:`struct uart_8250_port <uart_8250_port>`\* ``p``\ . The function is idempotent, so it is safe to
call it multiple times.

The function is supposed to be called from .rs485_config callback
or from any other callback protected with p->port.lock spinlock.

See also :c:func:`serial8250_em485_init`

