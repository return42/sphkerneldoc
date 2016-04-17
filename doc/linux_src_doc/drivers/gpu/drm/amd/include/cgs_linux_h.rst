.. -*- coding: utf-8; mode: rst -*-

===========
cgs_linux.h
===========


.. _`int`:

int
===

.. c:function:: typedef int ( *cgs_irq_source_set_func_t)

    Callback for enabling/disabling interrupt sources

    :param  \*cgs_irq_source_set_func_t:

        *undescribed*



.. _`int.return`:

Return
------

0 on success, -errno otherwise



.. _`int`:

int
===

.. c:function:: typedef int ( *cgs_irq_handler_func_t)

    Interrupt handler callback

    :param  \*cgs_irq_handler_func_t:

        *undescribed*



.. _`int.description`:

Description
-----------

This callback runs in interrupt context.



.. _`int.return`:

Return
------

0 on success, -errno otherwise



.. _`int`:

int
===

.. c:function:: typedef int ( *cgs_add_irq_source_t)

    Add an IRQ source

    :param  \*cgs_add_irq_source_t:

        *undescribed*



.. _`int.description`:

Description
-----------

The same IRQ source can be added only once. Adding an IRQ source
indicates ownership of that IRQ source and all its IRQ types.



.. _`int.return`:

Return
------

0 on success, -errno otherwise



.. _`int`:

int
===

.. c:function:: typedef int ( *cgs_irq_get_t)

    Request enabling an IRQ source and type

    :param  \*cgs_irq_get_t:

        *undescribed*



.. _`int.description`:

Description
-----------

cgs_irq_get and cgs_irq_put calls must be balanced. They count
"references" to IRQ sources.



.. _`int.return`:

Return
------

0 on success, -errno otherwise



.. _`int`:

int
===

.. c:function:: typedef int ( *cgs_irq_put_t)

    Indicate IRQ source is no longer needed

    :param  \*cgs_irq_put_t:

        *undescribed*



.. _`int.description`:

Description
-----------

cgs_irq_get and cgs_irq_put calls must be balanced. They count
"references" to IRQ sources. Even after cgs_irq_put is called, the
IRQ handler may still be called if there are more refecences to
the IRQ source.



.. _`int.return`:

Return
------

0 on success, -errno otherwise

