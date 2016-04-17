.. -*- coding: utf-8; mode: rst -*-

=======
types.h
=======


.. _`callback_head`:

struct callback_head
====================

.. c:type:: callback_head

    callback structure for use with RCU and task_work


.. _`callback_head.definition`:

Definition
----------

.. code-block:: c

  struct callback_head {
    struct callback_head * next;
    void (* func) (struct callback_head *head);
  };


.. _`callback_head.members`:

Members
-------

:``next``:
    next update requests in a list

:``func``:
    actual update function to call after the grace period.




.. _`callback_head.description`:

Description
-----------

The struct is aligned to size of pointer. On most architectures it happens
naturally due ABI requirements, but some architectures (like CRIS) have
weird ABI and we need to ask it explicitly.

The alignment is required to guarantee that bits 0 and 1 of ``next`` will be
clear under normal conditions -- as long as we use :c:func:`call_rcu`,
:c:func:`call_rcu_bh`, :c:func:`call_rcu_sched`, or :c:func:`call_srcu` to queue callback.



.. _`callback_head.this-guarantee-is-important-for-few-reasons`:

This guarantee is important for few reasons
-------------------------------------------

- future :c:func:`call_rcu_lazy` will make use of lower bits in the pointer;
- the structure shares storage spacer in struct page with ``compound_head``\ ,

  which encode :c:func:`PageTail` in bit 0. The guarantee is needed to avoid
  false-positive :c:func:`PageTail`.

