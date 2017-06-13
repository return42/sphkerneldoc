.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/include/cgs_linux.h

.. _`cgs_irq_source_set_func_t`:

cgs_irq_source_set_func_t
=========================

.. c:function:: int cgs_irq_source_set_func_t(void *private_data, unsigned src_id, unsigned type, int enabled)

    Callback for enabling/disabling interrupt sources

    :param void \*private_data:
        private data provided to cgs_add_irq_source

    :param unsigned src_id:
        interrupt source ID

    :param unsigned type:
        interrupt type

    :param int enabled:
        0 = disable source, non-0 = enable source

.. _`cgs_irq_source_set_func_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_irq_handler_func_t`:

cgs_irq_handler_func_t
======================

.. c:function:: int cgs_irq_handler_func_t(void *private_data, unsigned src_id, const uint32_t *iv_entry)

    Interrupt handler callback

    :param void \*private_data:
        private data provided to cgs_add_irq_source

    :param unsigned src_id:
        interrupt source ID

    :param const uint32_t \*iv_entry:
        pointer to raw ih ring entry

.. _`cgs_irq_handler_func_t.description`:

Description
-----------

This callback runs in interrupt context.

.. _`cgs_irq_handler_func_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_add_irq_source_t`:

cgs_add_irq_source_t
====================

.. c:function:: int cgs_add_irq_source_t(void *cgs_device, unsigned client_id, unsigned src_id, unsigned num_types, cgs_irq_source_set_func_t set, cgs_irq_handler_func_t handler, void *private_data)

    Add an IRQ source

    :param void \*cgs_device:
        opaque device handle

    :param unsigned client_id:
        *undescribed*

    :param unsigned src_id:
        interrupt source ID

    :param unsigned num_types:
        number of interrupt types that can be independently enabled

    :param cgs_irq_source_set_func_t set:
        callback function to enable/disable an interrupt type

    :param cgs_irq_handler_func_t handler:
        interrupt handler callback

    :param void \*private_data:
        private data to pass to callback functions

.. _`cgs_add_irq_source_t.description`:

Description
-----------

The same IRQ source can be added only once. Adding an IRQ source
indicates ownership of that IRQ source and all its IRQ types.

.. _`cgs_add_irq_source_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_irq_get_t`:

cgs_irq_get_t
=============

.. c:function:: int cgs_irq_get_t(void *cgs_device, unsigned client_id, unsigned src_id, unsigned type)

    Request enabling an IRQ source and type

    :param void \*cgs_device:
        opaque device handle

    :param unsigned client_id:
        *undescribed*

    :param unsigned src_id:
        interrupt source ID

    :param unsigned type:
        interrupt type

.. _`cgs_irq_get_t.description`:

Description
-----------

cgs_irq_get and cgs_irq_put calls must be balanced. They count
"references" to IRQ sources.

.. _`cgs_irq_get_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_irq_put_t`:

cgs_irq_put_t
=============

.. c:function:: int cgs_irq_put_t(void *cgs_device, unsigned client_id, unsigned src_id, unsigned type)

    Indicate IRQ source is no longer needed

    :param void \*cgs_device:
        opaque device handle

    :param unsigned client_id:
        *undescribed*

    :param unsigned src_id:
        interrupt source ID

    :param unsigned type:
        interrupt type

.. _`cgs_irq_put_t.description`:

Description
-----------

cgs_irq_get and cgs_irq_put calls must be balanced. They count
"references" to IRQ sources. Even after cgs_irq_put is called, the
IRQ handler may still be called if there are more refecences to
the IRQ source.

.. _`cgs_irq_put_t.return`:

Return
------

0 on success, -errno otherwise

.. This file was automatic generated / don't edit.

