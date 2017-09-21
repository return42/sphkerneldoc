.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_hw_eqs.c

.. _`hinic_aeq_register_hw_cb`:

hinic_aeq_register_hw_cb
========================

.. c:function:: void hinic_aeq_register_hw_cb(struct hinic_aeqs *aeqs, enum hinic_aeq_type event, void *handle, void (*hwe_handler)(void *handle, void *data, u8 size))

    register AEQ callback for specific event

    :param struct hinic_aeqs \*aeqs:
        pointer to Async eqs of the chip

    :param enum hinic_aeq_type event:
        aeq event to register callback for it

    :param void \*handle:
        private data will be used by the callback

    :param void (\*hwe_handler)(void \*handle, void \*data, u8 size):
        *undescribed*

.. _`hinic_aeq_unregister_hw_cb`:

hinic_aeq_unregister_hw_cb
==========================

.. c:function:: void hinic_aeq_unregister_hw_cb(struct hinic_aeqs *aeqs, enum hinic_aeq_type event)

    unregister the AEQ callback for specific event

    :param struct hinic_aeqs \*aeqs:
        pointer to Async eqs of the chip

    :param enum hinic_aeq_type event:
        aeq event to unregister callback for it

.. _`hinic_ceq_register_cb`:

hinic_ceq_register_cb
=====================

.. c:function:: void hinic_ceq_register_cb(struct hinic_ceqs *ceqs, enum hinic_ceq_type event, void *handle, void (*handler)(void *handle, u32 ceqe_data))

    register CEQ callback for specific event

    :param struct hinic_ceqs \*ceqs:
        pointer to Completion eqs part of the chip

    :param enum hinic_ceq_type event:
        ceq event to register callback for it

    :param void \*handle:
        private data will be used by the callback

    :param void (\*handler)(void \*handle, u32 ceqe_data):
        callback function

.. _`hinic_ceq_unregister_cb`:

hinic_ceq_unregister_cb
=======================

.. c:function:: void hinic_ceq_unregister_cb(struct hinic_ceqs *ceqs, enum hinic_ceq_type event)

    unregister the CEQ callback for specific event

    :param struct hinic_ceqs \*ceqs:
        pointer to Completion eqs part of the chip

    :param enum hinic_ceq_type event:
        ceq event to unregister callback for it

.. _`eq_update_ci`:

eq_update_ci
============

.. c:function:: void eq_update_ci(struct hinic_eq *eq)

    update the HW cons idx of event queue

    :param struct hinic_eq \*eq:
        the event queue to update the cons idx for

.. _`aeq_irq_handler`:

aeq_irq_handler
===============

.. c:function:: void aeq_irq_handler(struct hinic_eq *eq)

    handler for the AEQ event

    :param struct hinic_eq \*eq:
        the Async Event Queue that received the event

.. _`ceq_event_handler`:

ceq_event_handler
=================

.. c:function:: void ceq_event_handler(struct hinic_ceqs *ceqs, u32 ceqe)

    handler for the ceq events

    :param struct hinic_ceqs \*ceqs:
        ceqs part of the chip

    :param u32 ceqe:
        ceq element that describes the event

.. _`ceq_irq_handler`:

ceq_irq_handler
===============

.. c:function:: void ceq_irq_handler(struct hinic_eq *eq)

    handler for the CEQ event

    :param struct hinic_eq \*eq:
        the Completion Event Queue that received the event

.. _`eq_irq_handler`:

eq_irq_handler
==============

.. c:function:: void eq_irq_handler(void *data)

    handler for the EQ event

    :param void \*data:
        the Event Queue that received the event

.. _`eq_irq_work`:

eq_irq_work
===========

.. c:function:: void eq_irq_work(struct work_struct *work)

    the work of the EQ that received the event

    :param struct work_struct \*work:
        the work struct that is associated with the EQ

.. _`ceq_tasklet`:

ceq_tasklet
===========

.. c:function:: void ceq_tasklet(unsigned long ceq_data)

    the tasklet of the EQ that received the event

    :param unsigned long ceq_data:
        the eq

.. _`aeq_interrupt`:

aeq_interrupt
=============

.. c:function:: irqreturn_t aeq_interrupt(int irq, void *data)

    aeq interrupt handler

    :param int irq:
        irq number

    :param void \*data:
        the Async Event Queue that collected the event

.. _`ceq_interrupt`:

ceq_interrupt
=============

.. c:function:: irqreturn_t ceq_interrupt(int irq, void *data)

    ceq interrupt handler

    :param int irq:
        irq number

    :param void \*data:
        the Completion Event Queue that collected the event

.. _`set_eq_ctrls`:

set_eq_ctrls
============

.. c:function:: void set_eq_ctrls(struct hinic_eq *eq)

    setting eq's ctrl registers

    :param struct hinic_eq \*eq:
        the Event Queue for setting

.. _`aeq_elements_init`:

aeq_elements_init
=================

.. c:function:: void aeq_elements_init(struct hinic_eq *eq, u32 init_val)

    initialize all the elements in the aeq

    :param struct hinic_eq \*eq:
        the Async Event Queue

    :param u32 init_val:
        value to initialize the elements with it

.. _`ceq_elements_init`:

ceq_elements_init
=================

.. c:function:: void ceq_elements_init(struct hinic_eq *eq, u32 init_val)

    Initialize all the elements in the ceq

    :param struct hinic_eq \*eq:
        the event queue

    :param u32 init_val:
        value to init with it the elements

.. _`alloc_eq_pages`:

alloc_eq_pages
==============

.. c:function:: int alloc_eq_pages(struct hinic_eq *eq)

    allocate the pages for the queue

    :param struct hinic_eq \*eq:
        the event queue

.. _`alloc_eq_pages.description`:

Description
-----------

Return 0 - Success, Negative - Failure

.. _`free_eq_pages`:

free_eq_pages
=============

.. c:function:: void free_eq_pages(struct hinic_eq *eq)

    free the pages of the queue

    :param struct hinic_eq \*eq:
        the Event Queue

.. _`init_eq`:

init_eq
=======

.. c:function:: int init_eq(struct hinic_eq *eq, struct hinic_hwif *hwif, enum hinic_eq_type type, int q_id, u32 q_len, u32 page_size, struct msix_entry entry)

    initialize Event Queue

    :param struct hinic_eq \*eq:
        the event queue

    :param struct hinic_hwif \*hwif:
        the HW interface of a PCI function device

    :param enum hinic_eq_type type:
        the type of the event queue, aeq or ceq

    :param int q_id:
        Queue id number

    :param u32 q_len:
        the number of EQ elements

    :param u32 page_size:
        the page size of the pages in the event queue

    :param struct msix_entry entry:
        msix entry associated with the event queue

.. _`init_eq.description`:

Description
-----------

Return 0 - Success, Negative - Failure

.. _`remove_eq`:

remove_eq
=========

.. c:function:: void remove_eq(struct hinic_eq *eq)

    remove Event Queue

    :param struct hinic_eq \*eq:
        the event queue

.. _`hinic_aeqs_init`:

hinic_aeqs_init
===============

.. c:function:: int hinic_aeqs_init(struct hinic_aeqs *aeqs, struct hinic_hwif *hwif, int num_aeqs, u32 q_len, u32 page_size, struct msix_entry *msix_entries)

    initialize all the aeqs

    :param struct hinic_aeqs \*aeqs:
        pointer to Async eqs of the chip

    :param struct hinic_hwif \*hwif:
        the HW interface of a PCI function device

    :param int num_aeqs:
        number of AEQs

    :param u32 q_len:
        number of EQ elements

    :param u32 page_size:
        the page size of the pages in the event queue

    :param struct msix_entry \*msix_entries:
        msix entries associated with the event queues

.. _`hinic_aeqs_init.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_aeqs_free`:

hinic_aeqs_free
===============

.. c:function:: void hinic_aeqs_free(struct hinic_aeqs *aeqs)

    free all the aeqs

    :param struct hinic_aeqs \*aeqs:
        pointer to Async eqs of the chip

.. _`hinic_ceqs_init`:

hinic_ceqs_init
===============

.. c:function:: int hinic_ceqs_init(struct hinic_ceqs *ceqs, struct hinic_hwif *hwif, int num_ceqs, u32 q_len, u32 page_size, struct msix_entry *msix_entries)

    init all the ceqs

    :param struct hinic_ceqs \*ceqs:
        ceqs part of the chip

    :param struct hinic_hwif \*hwif:
        the hardware interface of a pci function device

    :param int num_ceqs:
        number of CEQs

    :param u32 q_len:
        number of EQ elements

    :param u32 page_size:
        the page size of the event queue

    :param struct msix_entry \*msix_entries:
        msix entries associated with the event queues

.. _`hinic_ceqs_init.description`:

Description
-----------

Return 0 - Success, Negative - Failure

.. _`hinic_ceqs_free`:

hinic_ceqs_free
===============

.. c:function:: void hinic_ceqs_free(struct hinic_ceqs *ceqs)

    free all the ceqs

    :param struct hinic_ceqs \*ceqs:
        ceqs part of the chip

.. This file was automatic generated / don't edit.

