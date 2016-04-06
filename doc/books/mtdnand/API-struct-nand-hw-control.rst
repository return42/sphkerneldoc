
.. _API-struct-nand-hw-control:

======================
struct nand_hw_control
======================

*man struct nand_hw_control(9)*

*4.6.0-rc1*

Control structure for hardware controller (e.g ECC generator) shared among independent devices


Synopsis
========

.. code-block:: c

    struct nand_hw_control {
      spinlock_t lock;
      struct nand_chip * active;
      wait_queue_head_t wq;
    };


Members
=======

lock
    protection lock

active
    the mtd device which holds the controller currently

wq
    wait queue to sleep on if a NAND operation is in progress used instead of the per chip wait queue when a hw controller is available.
