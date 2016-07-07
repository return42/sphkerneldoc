.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/serial_core.h

.. _`uart_pm_state`:

enum uart_pm_state
==================

.. c:type:: enum uart_pm_state

    power states for UARTs

.. _`uart_pm_state.definition`:

Definition
----------

.. code-block:: c

    enum uart_pm_state {
        UART_PM_STATE_ON,
        UART_PM_STATE_OFF,
        UART_PM_STATE_UNDEFINED
    };

.. _`uart_pm_state.constants`:

Constants
---------

UART_PM_STATE_ON
    UART is powered, up and operational

UART_PM_STATE_OFF
    UART is powered off

UART_PM_STATE_UNDEFINED
    sentinel

.. This file was automatic generated / don't edit.

