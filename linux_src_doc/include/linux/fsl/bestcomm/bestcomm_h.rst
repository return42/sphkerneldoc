.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fsl/bestcomm/bestcomm.h

.. _`bcom_bd`:

struct bcom_bd
==============

.. c:type:: struct bcom_bd

    Structure describing a generic BestComm buffer descriptor

.. _`bcom_bd.definition`:

Definition
----------

.. code-block:: c

    struct bcom_bd {
        u32 status;
        u32 data[0];
    }

.. _`bcom_bd.members`:

Members
-------

status
    The current status of this buffer. Exact meaning depends on the
    task type

data
    An array of u32 extra data.  Size of array is task dependent.

.. _`bcom_bd.note`:

Note
----

Don't dereference a bcom_bd pointer as an array.  The size of the
bcom_bd is variable.  Use \ :c:func:`bcom_get_bd`\  instead.

.. _`bcom_task`:

struct bcom_task
================

.. c:type:: struct bcom_task

    Structure describing a loaded BestComm task

.. _`bcom_task.definition`:

Definition
----------

.. code-block:: c

    struct bcom_task {
        unsigned int tasknum;
        unsigned int flags;
        int irq;
        struct bcom_bd *bd;
        phys_addr_t bd_pa;
        void **cookie;
        unsigned short index;
        unsigned short outdex;
        unsigned int num_bd;
        unsigned int bd_size;
        void* priv;
    }

.. _`bcom_task.members`:

Members
-------

tasknum
    *undescribed*

flags
    *undescribed*

irq
    *undescribed*

bd
    *undescribed*

bd_pa
    *undescribed*

cookie
    *undescribed*

index
    *undescribed*

outdex
    *undescribed*

num_bd
    *undescribed*

bd_size
    *undescribed*

priv
    *undescribed*

.. _`bcom_task.description`:

Description
-----------

This structure is never built by the driver it self. It's built and
filled the intermediate layer of the BestComm API, the task dependent
support code.

Most likely you don't need to poke around inside this structure. The
fields are exposed in the header just for the sake of inline functions

.. _`bcom_enable`:

bcom_enable
===========

.. c:function:: void bcom_enable(struct bcom_task *tsk)

    Enable a BestComm task

    :param struct bcom_task \*tsk:
        The BestComm task structure

.. _`bcom_enable.description`:

Description
-----------

This function makes sure the given task is enabled and can be run
by the BestComm engine as needed

.. _`bcom_disable`:

bcom_disable
============

.. c:function:: void bcom_disable(struct bcom_task *tsk)

    Disable a BestComm task

    :param struct bcom_task \*tsk:
        The BestComm task structure

.. _`bcom_disable.description`:

Description
-----------

This function disable a given task, making sure it's not executed
by the BestComm engine.

.. _`bcom_get_task_irq`:

bcom_get_task_irq
=================

.. c:function:: int bcom_get_task_irq(struct bcom_task *tsk)

    Returns the irq number of a BestComm task

    :param struct bcom_task \*tsk:
        The BestComm task structure

.. _`bcom_queue_empty`:

bcom_queue_empty
================

.. c:function:: int bcom_queue_empty(struct bcom_task *tsk)

    Checks if a BestComm task BD queue is empty

    :param struct bcom_task \*tsk:
        The BestComm task structure

.. _`bcom_queue_full`:

bcom_queue_full
===============

.. c:function:: int bcom_queue_full(struct bcom_task *tsk)

    Checks if a BestComm task BD queue is full

    :param struct bcom_task \*tsk:
        The BestComm task structure

.. _`bcom_get_bd`:

bcom_get_bd
===========

.. c:function:: struct bcom_bd *bcom_get_bd(struct bcom_task *tsk, unsigned int index)

    Get a BD from the queue

    :param struct bcom_task \*tsk:
        The BestComm task structure

    :param unsigned int index:
        *undescribed*

.. _`bcom_get_bd.index`:

index
-----

Index of the BD to fetch

.. _`bcom_buffer_done`:

bcom_buffer_done
================

.. c:function:: int bcom_buffer_done(struct bcom_task *tsk)

    Checks if a BestComm

    :param struct bcom_task \*tsk:
        The BestComm task structure

.. _`bcom_prepare_next_buffer`:

bcom_prepare_next_buffer
========================

.. c:function:: struct bcom_bd *bcom_prepare_next_buffer(struct bcom_task *tsk)

    clear status of next available buffer.

    :param struct bcom_task \*tsk:
        The BestComm task structure

.. _`bcom_prepare_next_buffer.description`:

Description
-----------

Returns pointer to next buffer descriptor

.. This file was automatic generated / don't edit.

