.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/pciehp.h

.. _`controller`:

struct controller
=================

.. c:type:: struct controller

    PCIe hotplug controller

.. _`controller.definition`:

Definition
----------

.. code-block:: c

    struct controller {
        struct pcie_device *pcie;
        u32 slot_cap;
        u16 slot_ctrl;
        struct mutex ctrl_lock;
        unsigned long cmd_started;
        unsigned int cmd_busy:1;
        wait_queue_head_t queue;
        atomic_t pending_events;
        unsigned int notification_enabled:1;
        unsigned int power_fault_detected;
        struct task_struct *poll_thread;
        u8 state;
        struct mutex state_lock;
        struct delayed_work button_work;
        struct hotplug_slot hotplug_slot;
        struct rw_semaphore reset_lock;
        int request_result;
        wait_queue_head_t requester;
    }

.. _`controller.members`:

Members
-------

pcie
    pointer to the controller's PCIe port service device

slot_cap
    cached copy of the Slot Capabilities register

slot_ctrl
    cached copy of the Slot Control register

ctrl_lock
    serializes writes to the Slot Control register

cmd_started
    jiffies when the Slot Control register was last written;
    the next write is allowed 1 second later, absent a Command Completed
    interrupt (PCIe r4.0, sec 6.7.3.2)

cmd_busy
    flag set on Slot Control register write, cleared by IRQ handler
    on reception of a Command Completed event

queue
    wait queue to wake up on reception of a Command Completed event,
    used for synchronous writes to the Slot Control register

pending_events
    used by the IRQ handler to save events retrieved from the
    Slot Status register for later consumption by the IRQ thread

notification_enabled
    whether the IRQ was requested successfully

power_fault_detected
    whether a power fault was detected by the hardware
    that has not yet been cleared by the user

poll_thread
    thread to poll for slot events if no IRQ is available,
    enabled with pciehp_poll_mode module parameter

state
    current state machine position

state_lock
    protects reads and writes of \ ``state``\ ;
    protects scheduling, execution and cancellation of \ ``button_work``\ 

button_work
    work item to turn the slot on or off after 5 seconds
    in response to an Attention Button press

hotplug_slot
    structure registered with the PCI hotplug core

reset_lock
    prevents access to the Data Link Layer Link Active bit in the
    Link Status register and to the Presence Detect State bit in the Slot
    Status register during a slot reset which may cause them to flap

request_result
    result of last user request submitted to the IRQ thread

requester
    wait queue to wake up on completion of user request,
    used for synchronous slot enable/disable request via sysfs

.. _`controller.description`:

Description
-----------

PCIe hotplug has a 1:1 relationship between controller and slot, hence
unlike other drivers, the two aren't represented by separate structures.

.. _`slot-state`:

Slot state
==========

\ ``OFF_STATE``\ : slot is powered off, no subordinate devices are enumerated
\ ``BLINKINGON_STATE``\ : slot will be powered on after the 5 second delay,
green led is blinking
\ ``BLINKINGOFF_STATE``\ : slot will be powered off after the 5 second delay,
green led is blinking
\ ``POWERON_STATE``\ : slot is currently powering on
\ ``POWEROFF_STATE``\ : slot is currently powering off
\ ``ON_STATE``\ : slot is powered on, subordinate devices have been enumerated

.. _`flags-to-request-an-action-from-the-irq-thread`:

Flags to request an action from the IRQ thread
==============================================

These are stored together with events read from the Slot Status register,
hence must be greater than its 16-bit width.

\ ``DISABLE_SLOT``\ : Disable the slot in response to a user request via sysfs or
an Attention Button press after the 5 second delay
\ ``RERUN_ISR``\ : Used by the IRQ handler to inform the IRQ thread that the
hotplug port was inaccessible when the interrupt occurred, requiring
that the IRQ handler is rerun by the IRQ thread after it has made the
hotplug port accessible by runtime resuming its parents to D0

.. This file was automatic generated / don't edit.

