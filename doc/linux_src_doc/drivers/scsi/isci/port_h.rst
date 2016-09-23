.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/port.h

.. _`isci_port`:

struct isci_port
================

.. c:type:: struct isci_port

    isci direct attached sas port object

.. _`isci_port.definition`:

Definition
----------

.. code-block:: c

    struct isci_port {
        struct isci_host *isci_host;
        struct list_head remote_dev_list;
    #define IPORT_RESET_PENDING 0
        unsigned long state;
        enum sci_status hard_reset_status;
        struct sci_base_state_machine sm;
        bool ready_exit;
        u8 logical_port_index;
        u8 physical_port_index;
        u8 active_phy_mask;
        u8 enabled_phy_mask;
        u8 last_active_phy;
        u16 reserved_rni;
        u16 reserved_tag;
        u32 started_request_count;
        u32 assigned_device_count;
        u32 hang_detect_users;
        u32 not_ready_reason;
        struct isci_phy  *phy_table[SCI_MAX_PHYS];
        struct isci_host *owning_controller;
        struct sci_timer timer;
        struct scu_port_task_scheduler_registers __iomem *port_task_scheduler_registers;
        u32 __iomem *port_pe_configuration_register;
        struct scu_viit_entry __iomem *viit_registers;
    }

.. _`isci_port.members`:

Members
-------

isci_host
    *undescribed*

remote_dev_list
    *undescribed*

state
    *undescribed*

hard_reset_status
    *undescribed*

sm
    *undescribed*

ready_exit
    several states constitute 'ready'. When exiting ready we
    need to take extra port-teardown actions that are
    skipped when exiting to another 'ready' state.

logical_port_index
    software port index

physical_port_index
    hardware port index

active_phy_mask
    identifies phy members

enabled_phy_mask
    phy mask for the port
    that are already part of the port

last_active_phy
    *undescribed*

reserved_rni
    reserver for port task scheduler workaround

reserved_tag
    *undescribed*

started_request_count
    reference count for outstanding commands

assigned_device_count
    *undescribed*

hang_detect_users
    *undescribed*

not_ready_reason
    set during state transitions and notified

owning_controller
    *undescribed*

timer
    timeout start/stop operations

port_task_scheduler_registers
    *undescribed*

port_pe_configuration_register
    *undescribed*

viit_registers
    *undescribed*

.. This file was automatic generated / don't edit.

