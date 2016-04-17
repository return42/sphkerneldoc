.. -*- coding: utf-8; mode: rst -*-

===========
irqreturn.h
===========


.. _`irqreturn`:

enum irqreturn
==============

.. c:type:: irqreturn

    


.. _`irqreturn.definition`:

Definition
----------

.. code-block:: c

    enum irqreturn {
      IRQ_NONE,
      IRQ_HANDLED,
      IRQ_WAKE_THREAD
    };


.. _`irqreturn.constants`:

Constants
---------

:``IRQ_NONE``:
-- undescribed --

:``IRQ_HANDLED``:
-- undescribed --

:``IRQ_WAKE_THREAD``:
-- undescribed --


.. _`irqreturn.description`:

Description
-----------

``IRQ_NONE``                interrupt was not from this device or was not handled
``IRQ_HANDLED``                interrupt was handled by this device
``IRQ_WAKE_THREAD``        handler requests to wake the handler thread

