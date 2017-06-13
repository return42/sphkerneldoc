.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/registers.h

.. _`scu_viit_entry_id_mask`:

SCU_VIIT_ENTRY_ID_MASK
======================

.. c:function::  SCU_VIIT_ENTRY_ID_MASK()

    registers.

.. _`scu_viit_entry_id_mask.description`:

Description
-----------



.. _`scu_viit_entry`:

struct scu_viit_entry
=====================

.. c:type:: struct scu_viit_entry

    This is the SCU Virtual Initiator Table Entry

.. _`scu_viit_entry.definition`:

Definition
----------

.. code-block:: c

    struct scu_viit_entry {
        u32 status;
        u32 initiator_sas_address_hi;
        u32 initiator_sas_address_lo;
        u32 reserved;
    }

.. _`scu_viit_entry.members`:

Members
-------

status
    *undescribed*

initiator_sas_address_hi
    *undescribed*

initiator_sas_address_lo
    *undescribed*

reserved
    *undescribed*

.. _`scu_viit_entry.description`:

Description
-----------



.. _`scu_iit_entry`:

struct scu_iit_entry
====================

.. c:type:: struct scu_iit_entry

    This will be implemented later when we support virtual functions

.. _`scu_iit_entry.definition`:

Definition
----------

.. code-block:: c

    struct scu_iit_entry {
        u32 status;
        u32 remote_initiator_sas_address_hi;
        u32 remote_initiator_sas_address_lo;
        u32 remote_initiator;
    }

.. _`scu_iit_entry.members`:

Members
-------

status
    *undescribed*

remote_initiator_sas_address_hi
    *undescribed*

remote_initiator_sas_address_lo
    *undescribed*

remote_initiator
    *undescribed*

.. _`scu_iit_entry.description`:

Description
-----------



.. _`smu_registers`:

struct smu_registers
====================

.. c:type:: struct smu_registers

    These are the SMU registers

.. _`smu_registers.definition`:

Definition
----------

.. code-block:: c

    struct smu_registers {
        u32 post_context_port;
        u32 address_modifier;
        u32 reserved_08;
        u32 reserved_0C;
        u32 interrupt_status;
        u32 interrupt_mask;
        u32 interrupt_coalesce_control;
        u32 reserved_1C;
        u32 host_task_table_lower;
        u32 host_task_table_upper;
        u32 task_context_range;
        u32 reserved_2C;
        u32 completion_queue_lower;
        u32 completion_queue_upper;
        u32 reserved_38;
        u32 reserved_3C;
        u32 completion_queue_put;
        u32 completion_queue_get;
        u32 completion_queue_control;
        u32 reserved_4C;
        u32 reserved_5x[4];
        u32 reserved_6x[4];
        u32 reserved_7x[4];
        u32 remote_node_context_lower;
        u32 remote_node_context_upper;
        u32 reserved_88;
        u32 reserved_8C;
        u32 device_context_capacity;
        u32 device_function_capacity;
        u32 control_status;
        u32 soft_reset_control;
        u32 mmr_address_window;
        u32 mmr_data_window;
        u32 clock_gating_control;
        u32 clock_gating_performance;
        u32 reserved_Bx[4];
        u32 reserved_Cx[4];
        u32 reserved_Dx[4];
        u32 reserved_Ex[4];
        u32 reserved_Fx[4];
        u32 reserved_1xx[64];
        u32 reserved_2xx[64];
        u32 reserved_3xx[64];
        u32 task_context_assignment[256];
    }

.. _`smu_registers.members`:

Members
-------

post_context_port
    *undescribed*

address_modifier
    *undescribed*

reserved_08
    *undescribed*

reserved_0C
    *undescribed*

interrupt_status
    *undescribed*

interrupt_mask
    *undescribed*

interrupt_coalesce_control
    *undescribed*

reserved_1C
    *undescribed*

host_task_table_lower
    *undescribed*

host_task_table_upper
    *undescribed*

task_context_range
    *undescribed*

reserved_2C
    *undescribed*

completion_queue_lower
    *undescribed*

completion_queue_upper
    *undescribed*

reserved_38
    *undescribed*

reserved_3C
    *undescribed*

completion_queue_put
    *undescribed*

completion_queue_get
    *undescribed*

completion_queue_control
    *undescribed*

reserved_4C
    *undescribed*

remote_node_context_lower
    *undescribed*

remote_node_context_upper
    *undescribed*

reserved_88
    *undescribed*

reserved_8C
    *undescribed*

device_context_capacity
    *undescribed*

device_function_capacity
    *undescribed*

control_status
    *undescribed*

soft_reset_control
    *undescribed*

mmr_address_window
    *undescribed*

mmr_data_window
    *undescribed*

clock_gating_control
    *undescribed*

clock_gating_performance
    *undescribed*

.. _`smu_registers.description`:

Description
-----------



.. _`scu_sdma_registers`:

struct scu_sdma_registers
=========================

.. c:type:: struct scu_sdma_registers

    These are the SCU SDMA Registers

.. _`scu_sdma_registers.definition`:

Definition
----------

.. code-block:: c

    struct scu_sdma_registers {
        u32 uf_address_table_lower;
        u32 uf_address_table_upper;
        u32 uf_header_base_address_lower;
        u32 uf_header_base_address_upper;
        u32 unsolicited_frame_queue_control;
        u32 unsolicited_frame_put_pointer;
        u32 unsolicited_frame_get_pointer;
        u32 pdma_configuration;
        u32 reserved_0020_007C[0x18];
        u32 cdma_configuration;
        u32 reserved_0084_0400[0xDF];
    }

.. _`scu_sdma_registers.members`:

Members
-------

uf_address_table_lower
    *undescribed*

uf_address_table_upper
    *undescribed*

uf_header_base_address_lower
    *undescribed*

uf_header_base_address_upper
    *undescribed*

unsolicited_frame_queue_control
    *undescribed*

unsolicited_frame_put_pointer
    *undescribed*

unsolicited_frame_get_pointer
    *undescribed*

pdma_configuration
    *undescribed*

cdma_configuration
    *undescribed*

.. _`scu_sdma_registers.description`:

Description
-----------



.. _`scu_transport_layer_registers`:

struct scu_transport_layer_registers
====================================

.. c:type:: struct scu_transport_layer_registers

    These are the SCU Transport Layer registers

.. _`scu_transport_layer_registers.definition`:

Definition
----------

.. code-block:: c

    struct scu_transport_layer_registers {
        u32 control;
        u32 arbitration_delay_timer;
        u32 timer_test_mode;
        u32 reserved_0C;
        u32 stp_rni;
        u32 tlfe_wpo_read_control;
        u32 tlfe_wpo_read_data;
        u32 rxtl_single_step_control_status_1;
        u32 rxtl_single_step_control_status_2;
        u32 tlfe_awt_retry_delay_debug_control;
        u32 reserved_0028_007F[0x16];
    }

.. _`scu_transport_layer_registers.members`:

Members
-------

control
    *undescribed*

arbitration_delay_timer
    *undescribed*

timer_test_mode
    *undescribed*

reserved_0C
    *undescribed*

stp_rni
    *undescribed*

tlfe_wpo_read_control
    *undescribed*

tlfe_wpo_read_data
    *undescribed*

rxtl_single_step_control_status_1
    *undescribed*

rxtl_single_step_control_status_2
    *undescribed*

tlfe_awt_retry_delay_debug_control
    *undescribed*

.. _`scu_transport_layer_registers.description`:

Description
-----------



.. _`scu_link_layer_registers`:

struct scu_link_layer_registers
===============================

.. c:type:: struct scu_link_layer_registers

    SCU Link Layer Registers

.. _`scu_link_layer_registers.definition`:

Definition
----------

.. code-block:: c

    struct scu_link_layer_registers {
        u32 speed_negotiation_timers;
        u32 link_layer_status;
        u32 port_selector_timeout;
        u32 reserved0C;
        u32 timeout_unit_value;
        u32 rcd_timeout;
        u32 link_timer_timeouts;
        u32 sas_phy_timeouts;
        u32 received_address_frame_error_counter;
        u32 invalid_dword_counter;
        u32 transmit_identification;
        u32 sas_device_name_high;
        u32 sas_device_name_low;
        u32 source_sas_address_high;
        u32 source_sas_address_low;
        u32 identify_frame_phy_id;
        u32 identify_frame_reserved;
        u32 received_address_frame;
        u32 maximum_arbitration_wait_timer_timeout;
        u32 transmit_primitive;
        u32 error_counter_event_notification_control;
        u32 frxq_payload_fill_threshold;
        u32 link_layer_hang_detection_timeout;
        u32 reserved_5C;
        u32 received_frame_count;
        u32 transmit_frame_count;
        u32 received_dword_count;
        u32 transmit_dword_count;
        u32 loss_of_sync_error_count;
        u32 running_disparity_error_count;
        u32 received_frame_crc_error_count;
        u32 stp_control;
        u32 phy_configuration;
        u32 clock_skew_management;
        u32 transmit_comwake_signal;
        u32 transmit_cominit_signal;
        u32 transmit_comsas_signal;
        u32 cominit_control;
        u32 comwake_control;
        u32 comsas_control;
        u32 received_short_frame_count;
        u32 received_frame_without_credit_count;
        u32 received_frame_after_done_count;
        u32 phy_reset_problem_count;
        u32 counter_control;
        u32 ssp_timer_timeout_values;
        u32 ftx_control;
        u32 frx_control;
        u32 ftx_watermark;
        u32 notify_enable_spinup_control;
        u32 sas_training_sequence_timer_values;
        u32 phy_capabilities;
        u32 phy_control;
        u32 reserved_d4;
        u32 link_layer_control;
        u32 afe_xcvr_control;
        u32 afe_lookup_table_control;
        u32 phy_source_zone_group_control;
        u32 receive_phycap;
        u32 reserved_ec;
        u32 speed_negotiation_afe_rx_reset_control;
        u32 power_management_control;
        u32 sas_pm_partial_request_primitive;
        u32 sas_pm_slumber_request_primitive;
        u32 sas_pm_ack_primitive_register;
        u32 sas_pm_nak_primitive_register;
        u32 sas_primitive_timeout;
        u32 reserved_10c;
        u32 pla_product_control[4];
        u32 pla_product_sum;
        u32 pla_control;
        u32 reserved_0128_037f[0x96];
    }

.. _`scu_link_layer_registers.members`:

Members
-------

speed_negotiation_timers
    *undescribed*

link_layer_status
    *undescribed*

port_selector_timeout
    *undescribed*

reserved0C
    *undescribed*

timeout_unit_value
    *undescribed*

rcd_timeout
    *undescribed*

link_timer_timeouts
    *undescribed*

sas_phy_timeouts
    *undescribed*

received_address_frame_error_counter
    *undescribed*

invalid_dword_counter
    *undescribed*

transmit_identification
    *undescribed*

sas_device_name_high
    *undescribed*

sas_device_name_low
    *undescribed*

source_sas_address_high
    *undescribed*

source_sas_address_low
    *undescribed*

identify_frame_phy_id
    *undescribed*

identify_frame_reserved
    *undescribed*

received_address_frame
    *undescribed*

maximum_arbitration_wait_timer_timeout
    *undescribed*

transmit_primitive
    *undescribed*

error_counter_event_notification_control
    *undescribed*

frxq_payload_fill_threshold
    *undescribed*

link_layer_hang_detection_timeout
    *undescribed*

reserved_5C
    *undescribed*

received_frame_count
    *undescribed*

transmit_frame_count
    *undescribed*

received_dword_count
    *undescribed*

transmit_dword_count
    *undescribed*

loss_of_sync_error_count
    *undescribed*

running_disparity_error_count
    *undescribed*

received_frame_crc_error_count
    *undescribed*

stp_control
    *undescribed*

phy_configuration
    *undescribed*

clock_skew_management
    *undescribed*

transmit_comwake_signal
    *undescribed*

transmit_cominit_signal
    *undescribed*

transmit_comsas_signal
    *undescribed*

cominit_control
    *undescribed*

comwake_control
    *undescribed*

comsas_control
    *undescribed*

received_short_frame_count
    *undescribed*

received_frame_without_credit_count
    *undescribed*

received_frame_after_done_count
    *undescribed*

phy_reset_problem_count
    *undescribed*

counter_control
    *undescribed*

ssp_timer_timeout_values
    *undescribed*

ftx_control
    *undescribed*

frx_control
    *undescribed*

ftx_watermark
    *undescribed*

notify_enable_spinup_control
    *undescribed*

sas_training_sequence_timer_values
    *undescribed*

phy_capabilities
    *undescribed*

phy_control
    *undescribed*

reserved_d4
    *undescribed*

link_layer_control
    *undescribed*

afe_xcvr_control
    *undescribed*

afe_lookup_table_control
    *undescribed*

phy_source_zone_group_control
    *undescribed*

receive_phycap
    *undescribed*

reserved_ec
    *undescribed*

speed_negotiation_afe_rx_reset_control
    *undescribed*

power_management_control
    *undescribed*

sas_pm_partial_request_primitive
    *undescribed*

sas_pm_slumber_request_primitive
    *undescribed*

sas_pm_ack_primitive_register
    *undescribed*

sas_pm_nak_primitive_register
    *undescribed*

sas_primitive_timeout
    *undescribed*

reserved_10c
    *undescribed*

pla_product_sum
    *undescribed*

pla_control
    *undescribed*

.. _`scu_link_layer_registers.description`:

Description
-----------



.. _`scu_sgpio_registers`:

struct scu_sgpio_registers
==========================

.. c:type:: struct scu_sgpio_registers

    SCU SGPIO Registers

.. _`scu_sgpio_registers.definition`:

Definition
----------

.. code-block:: c

    struct scu_sgpio_registers {
        u32 interface_control;
        u32 blink_rate;
        u32 start_drive_lower;
        u32 start_drive_upper;
        u32 serial_input_lower;
        u32 serial_input_upper;
        u32 vendor_specific_code;
        u32 reserved_001c;
        u32 output_data_select[8];
        u32 reserved_1444_14ff[0x30];
    }

.. _`scu_sgpio_registers.members`:

Members
-------

interface_control
    *undescribed*

blink_rate
    *undescribed*

start_drive_lower
    *undescribed*

start_drive_upper
    *undescribed*

serial_input_lower
    *undescribed*

serial_input_upper
    *undescribed*

vendor_specific_code
    *undescribed*

reserved_001c
    *undescribed*

.. _`scu_sgpio_registers.description`:

Description
-----------



.. _`scu_port_task_scheduler_registers`:

struct scu_port_task_scheduler_registers
========================================

.. c:type:: struct scu_port_task_scheduler_registers

    These are the control/stats pairs for each Port Task Scheduler.

.. _`scu_port_task_scheduler_registers.definition`:

Definition
----------

.. code-block:: c

    struct scu_port_task_scheduler_registers {
        u32 control;
        u32 status;
    }

.. _`scu_port_task_scheduler_registers.members`:

Members
-------

control
    *undescribed*

status
    *undescribed*

.. _`scu_port_task_scheduler_registers.description`:

Description
-----------



.. _`scu_port_task_scheduler_group_registers`:

struct scu_port_task_scheduler_group_registers
==============================================

.. c:type:: struct scu_port_task_scheduler_group_registers

    These are the PORT Task Scheduler registers

.. _`scu_port_task_scheduler_group_registers.definition`:

Definition
----------

.. code-block:: c

    struct scu_port_task_scheduler_group_registers {
        u32 control;
        u32 real_time_clock;
        u32 real_time_clock_control;
        u32 reserved_0C;
        struct scu_port_task_scheduler_registers port[4];
        u32 protocol_engine[4];
        u32 tc_scanning_interval_control;
        u32 rnc_scanning_interval_control;
        u32 reserved_1048_107f[0x0E];
    }

.. _`scu_port_task_scheduler_group_registers.members`:

Members
-------

control
    *undescribed*

real_time_clock
    *undescribed*

real_time_clock_control
    *undescribed*

reserved_0C
    *undescribed*

tc_scanning_interval_control
    *undescribed*

rnc_scanning_interval_control
    *undescribed*

.. _`scu_port_task_scheduler_group_registers.description`:

Description
-----------



.. _`transport_link_layer_pair`:

struct transport_link_layer_pair
================================

.. c:type:: struct transport_link_layer_pair

    The SCU Hardware pairs up the TL registers with the LL registers so we must place them adjcent to make the array of registers in the PEG.

.. _`transport_link_layer_pair.definition`:

Definition
----------

.. code-block:: c

    struct transport_link_layer_pair {
        struct scu_transport_layer_registers tl;
        struct scu_link_layer_registers ll;
    }

.. _`transport_link_layer_pair.members`:

Members
-------

tl
    *undescribed*

ll
    *undescribed*

.. _`transport_link_layer_pair.description`:

Description
-----------



.. _`scu_peg_registers`:

struct scu_peg_registers
========================

.. c:type:: struct scu_peg_registers

    SCU Protocol Engine Memory mapped register space. These registers are unique to each protocol engine group.  There can be at most two PEG for a single SCU part.

.. _`scu_peg_registers.definition`:

Definition
----------

.. code-block:: c

    struct scu_peg_registers {
        struct transport_link_layer_pair pe[4];
        struct scu_port_task_scheduler_group_registers ptsg;
        struct scu_protocol_engine_group_registers peg;
        struct scu_sgpio_registers sgpio;
        u32 reserved_01500_1BFF[0x1C0];
        struct scu_viit_entry viit[64];
        struct scu_zone_partition_table zpt0;
        struct scu_zone_partition_table zpt1;
    }

.. _`scu_peg_registers.members`:

Members
-------

ptsg
    *undescribed*

peg
    *undescribed*

sgpio
    *undescribed*

zpt0
    *undescribed*

zpt1
    *undescribed*

.. _`scu_peg_registers.description`:

Description
-----------



.. _`scu_registers`:

struct scu_registers
====================

.. c:type:: struct scu_registers

    SCU registers including both PEG registers if we turn on that compile option. All of these registers are in the memory mapped space returned from BAR1.

.. _`scu_registers.definition`:

Definition
----------

.. code-block:: c

    struct scu_registers {
        struct scu_peg_registers peg0;
        struct scu_sdma_registers sdma;
        struct scu_completion_ram cram;
        struct scu_frame_buffer_ram fbram;
        u32 reserved_6800_69FF[0x80];
        struct noa_protocol_engine_partition noa_pe;
        struct noa_hub_partition noa_hub;
        struct noa_host_interface_partition noa_if;
        u32 reserved_6d00_7fff[0x4c0];
        struct scu_peg_registers peg1;
        struct scu_afe_registers afe;
        u32 reserved_f000_211fff[0x80c00];
        struct scu_scratch_ram scratch_ram;
    }

.. _`scu_registers.members`:

Members
-------

peg0
    *undescribed*

sdma
    *undescribed*

cram
    *undescribed*

fbram
    *undescribed*

noa_pe
    *undescribed*

noa_hub
    *undescribed*

noa_if
    *undescribed*

peg1
    *undescribed*

afe
    *undescribed*

scratch_ram
    *undescribed*

.. _`scu_registers.description`:

Description
-----------



.. This file was automatic generated / don't edit.

