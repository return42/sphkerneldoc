.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/scu_task_context.h

.. _`scu_sata_task_type`:

typedef scu_sata_task_type
==========================

.. c:type:: typedef scu_sata_task_type

    This enumeration defines the various SATA task types the SCU hardware will accept. The definition for the various task types the SCU hardware will accept can be found in the DS specification.

.. _`scu_sata_task_type.description`:

Description
-----------

???

.. _`scu_context_command_request_type_post_tc`:

SCU_CONTEXT_COMMAND_REQUEST_TYPE_POST_TC
========================================

.. c:function::  SCU_CONTEXT_COMMAND_REQUEST_TYPE_POST_TC()

.. _`scu_context_command_request_type_post_tc.description`:

Description
-----------

SCU_COMMAND_TYPES These constants provide the grouping of the different SCU
command types.

.. _`ssp_task_context`:

struct ssp_task_context
=======================

.. c:type:: struct ssp_task_context

    This is the SCU hardware definition for an SSP request.

.. _`ssp_task_context.definition`:

Definition
----------

.. code-block:: c

    struct ssp_task_context {
        u32 reserved00:24;
        u32 frame_type:8;
        u32 reserved01;
        u32 fill_bytes:2;
        u32 reserved02:6;
        u32 changing_data_pointer:1;
        u32 retransmit:1;
        u32 retry_data_frame:1;
        u32 tlr_control:2;
        u32 reserved03:19;
        u32 uiRsvd4;
        u32 target_port_transfer_tag:16;
        u32 tag:16;
        u32 data_offset;
    }

.. _`ssp_task_context.members`:

Members
-------

reserved00
    *undescribed*

frame_type
    *undescribed*

reserved01
    *undescribed*

fill_bytes
    *undescribed*

reserved02
    *undescribed*

changing_data_pointer
    *undescribed*

retransmit
    *undescribed*

retry_data_frame
    *undescribed*

tlr_control
    *undescribed*

reserved03
    *undescribed*

uiRsvd4
    *undescribed*

target_port_transfer_tag
    *undescribed*

tag
    *undescribed*

data_offset
    *undescribed*

.. _`ssp_task_context.description`:

Description
-----------



.. _`stp_task_context`:

struct stp_task_context
=======================

.. c:type:: struct stp_task_context

    This is the SCU hardware definition for an STP request.

.. _`stp_task_context.definition`:

Definition
----------

.. code-block:: c

    struct stp_task_context {
        u32 fis_type:8;
        u32 pm_port:4;
        u32 reserved0:3;
        u32 control:1;
        u32 command:8;
        u32 features:8;
        u32 reserved1;
        u32 reserved2;
        u32 reserved3;
        u32 ncq_tag:5;
        u32 reserved4:27;
        u32 data_offset;
    }

.. _`stp_task_context.members`:

Members
-------

fis_type
    *undescribed*

pm_port
    *undescribed*

reserved0
    *undescribed*

control
    *undescribed*

command
    *undescribed*

features
    *undescribed*

reserved1
    *undescribed*

reserved2
    *undescribed*

reserved3
    *undescribed*

ncq_tag
    *undescribed*

reserved4
    *undescribed*

data_offset
    *undescribed*

.. _`stp_task_context.description`:

Description
-----------



.. _`smp_task_context`:

struct smp_task_context
=======================

.. c:type:: struct smp_task_context

    This is the SCU hardware definition for an SMP request.

.. _`smp_task_context.definition`:

Definition
----------

.. code-block:: c

    struct smp_task_context {
        u32 response_length:8;
        u32 function_result:8;
        u32 function:8;
        u32 frame_type:8;
        u32 smp_response_ufi:12;
        u32 reserved1:20;
        u32 reserved2;
        u32 reserved3;
        u32 reserved4;
        u32 reserved5;
    }

.. _`smp_task_context.members`:

Members
-------

response_length
    *undescribed*

function_result
    *undescribed*

function
    *undescribed*

frame_type
    *undescribed*

smp_response_ufi
    *undescribed*

reserved1
    *undescribed*

reserved2
    *undescribed*

reserved3
    *undescribed*

reserved4
    *undescribed*

reserved5
    *undescribed*

.. _`smp_task_context.description`:

Description
-----------



.. _`primitive_task_context`:

struct primitive_task_context
=============================

.. c:type:: struct primitive_task_context

    This is the SCU hardware definition used when the driver wants to send a primitive on the link.

.. _`primitive_task_context.definition`:

Definition
----------

.. code-block:: c

    struct primitive_task_context {
        u32 control;
        u32 sequence;
        u32 reserved0;
        u32 reserved1;
        u32 reserved2;
        u32 reserved3;
    }

.. _`primitive_task_context.members`:

Members
-------

control
    *undescribed*

sequence
    *undescribed*

reserved0
    *undescribed*

reserved1
    *undescribed*

reserved2
    *undescribed*

reserved3
    *undescribed*

.. _`primitive_task_context.description`:

Description
-----------



.. _`scu_sgl_element`:

struct scu_sgl_element
======================

.. c:type:: struct scu_sgl_element

    This structure represents a single SCU defined SGL element. SCU SGLs contain a 64 bit address with the maximum data transfer being 24 bits in size.  The SGL can not cross a 4GB boundary.

.. _`scu_sgl_element.definition`:

Definition
----------

.. code-block:: c

    struct scu_sgl_element {
        u32 address_upper;
        u32 address_lower;
        u32 length:24;
        u32 address_modifier:8;
    }

.. _`scu_sgl_element.members`:

Members
-------

address_upper
    *undescribed*

address_lower
    *undescribed*

length
    *undescribed*

address_modifier
    *undescribed*

.. _`scu_sgl_element.description`:

Description
-----------

struct scu_sgl_element

.. _`scu_sgl_element_pair`:

struct scu_sgl_element_pair
===========================

.. c:type:: struct scu_sgl_element_pair

    This structure is the SCU hardware definition of a pair of SGL elements. The SCU hardware always works on SGL pairs. They are refered to in the DS specification as SGL A and SGL B.  Each SGL pair is followed by the address of the next pair.

.. _`scu_sgl_element_pair.definition`:

Definition
----------

.. code-block:: c

    struct scu_sgl_element_pair {
        struct scu_sgl_element A;
        struct scu_sgl_element B;
        u32 next_pair_upper;
        u32 next_pair_lower;
    }

.. _`scu_sgl_element_pair.members`:

Members
-------

A
    *undescribed*

B
    *undescribed*

next_pair_upper
    *undescribed*

next_pair_lower
    *undescribed*

.. _`scu_sgl_element_pair.description`:

Description
-----------



.. _`transport_snapshot`:

struct transport_snapshot
=========================

.. c:type:: struct transport_snapshot

    This structure is the SCU hardware scratch area for the task context. This is set to 0 by the driver but can be read by issuing a dump TC request to the SCU.

.. _`transport_snapshot.definition`:

Definition
----------

.. code-block:: c

    struct transport_snapshot {
        u32 xfer_rdy_write_data_length;
        u32 data_offset;
        u32 data_transfer_size:24;
        u32 reserved_50_0:8;
        u32 next_initiator_write_data_offset;
        u32 next_initiator_write_data_xfer_size:24;
        u32 reserved_58_0:8;
    }

.. _`transport_snapshot.members`:

Members
-------

xfer_rdy_write_data_length
    *undescribed*

data_offset
    *undescribed*

data_transfer_size
    *undescribed*

reserved_50_0
    *undescribed*

next_initiator_write_data_offset
    *undescribed*

next_initiator_write_data_xfer_size
    *undescribed*

reserved_58_0
    *undescribed*

.. _`transport_snapshot.description`:

Description
-----------



.. _`scu_task_context`:

struct scu_task_context
=======================

.. c:type:: struct scu_task_context

    This structure defines the contents of the SCU silicon task context. It lays out all of the fields according to the expected order and location for the Storage Controller unit.

.. _`scu_task_context.definition`:

Definition
----------

.. code-block:: c

    struct scu_task_context {
        u32 priority:2;
        u32 initiator_request:1;
        u32 connection_rate:4;
        u32 protocol_engine_index:3;
        u32 logical_port_index:3;
        u32 protocol_type:3;
        u32 task_index:12;
        u32 reserved_00_0:1;
        u32 abort:1;
        u32 valid:1;
        u32 context_type:1;
        u32 remote_node_index:12;
        u32 mirrored_node_index:12;
        u32 sata_direction:1;
        u32 command_code:2;
        u32 suspend_node:1;
        u32 task_type:4;
        u32 link_layer_control:8;
        u32 ssp_tlr_enable:1;
        u32 dma_ssp_target_good_response:1;
        u32 do_not_dma_ssp_good_response:1;
        u32 strict_ordering:1;
        u32 control_frame:1;
        u32 tl_control_reserved:3;
        u32 timeout_enable:1;
        u32 pts_control_reserved:7;
        u32 block_guard_enable:1;
        u32 sdma_control_reserved:7;
        u32 address_modifier:16;
        u32 mirrored_protocol_engine:3;
        u32 mirrored_logical_port:4;
        u32 reserved_0C_0:8;
        u32 mirror_request_enable:1;
        u32 ssp_command_iu_length:8;
        u32 xfer_ready_tlr_enable:1;
        u32 reserved_10_0:7;
        u32 ssp_max_burst_size:16;
        u32 transfer_length_bytes:24;
        u32 reserved_14_0:8;
        union protocol_context type;
        u32 command_iu_upper;
        u32 command_iu_lower;
        u32 response_iu_upper;
        u32 response_iu_lower;
        u32 task_phase:8;
        u32 task_status:8;
        u32 previous_extended_tag:4;
        u32 stp_retry_count:2;
        u32 reserved_40_1:2;
        u32 ssp_tlr_threshold:4;
        u32 reserved_40_2:4;
        u32 write_data_length;
        struct transport_snapshot snapshot;
        u32 blk_prot_en:1;
        u32 blk_sz:2;
        u32 blk_prot_func:2;
        u32 reserved_5C_0:9;
        u32 active_sgl_element:2;
        u32 sgl_exhausted:1;
        u32 payload_data_transfer_error:4;
        u32 frame_buffer_offset:11;
        struct scu_sgl_element_pair sgl_pair_ab;
        struct scu_sgl_element_pair sgl_pair_cd;
        struct scu_sgl_element_pair sgl_snapshot_ac;
        u32 active_sgl_element_pair;
        u32 reserved_C4_CC;
        u32 interm_crc_val:16;
        u32 init_crc_seed:16;
        u32 app_tag_verify:16;
        u32 app_tag_gen:16;
        u32 ref_tag_seed_verify;
        u32 UD_bytes_immed_val:13;
        u32 reserved_DC_0:3;
        u32 DIF_bytes_immed_val:4;
        u32 reserved_DC_1:12;
        u32 bgc_blk_sz:13;
        u32 reserved_E0_0:3;
        u32 app_tag_gen_mask:16;
        union {unnamed_union};
        u16 app_tag_verify_mask;
        u32 blk_guard_err:8;
        u32 reserved_E8_0:24;
        u32 ref_tag_seed_gen;
        u32 intermediate_crc_valid_snapshot:16;
        u32 reserved_F0_0:16;
        u32 reference_tag_seed_for_verify_function_snapshot;
        u32 snapshot_of_reserved_dword_DC_of_tc;
        u32 reference_tag_seed_for_generate_function_snapshot;
    }

.. _`scu_task_context.members`:

Members
-------

priority
    *undescribed*

initiator_request
    *undescribed*

connection_rate
    *undescribed*

protocol_engine_index
    *undescribed*

logical_port_index
    *undescribed*

protocol_type
    *undescribed*

task_index
    *undescribed*

reserved_00_0
    *undescribed*

abort
    *undescribed*

valid
    *undescribed*

context_type
    *undescribed*

remote_node_index
    *undescribed*

mirrored_node_index
    *undescribed*

sata_direction
    *undescribed*

command_code
    *undescribed*

suspend_node
    *undescribed*

task_type
    *undescribed*

link_layer_control
    *undescribed*

ssp_tlr_enable
    *undescribed*

dma_ssp_target_good_response
    *undescribed*

do_not_dma_ssp_good_response
    *undescribed*

strict_ordering
    *undescribed*

control_frame
    *undescribed*

tl_control_reserved
    *undescribed*

timeout_enable
    *undescribed*

pts_control_reserved
    *undescribed*

block_guard_enable
    *undescribed*

sdma_control_reserved
    *undescribed*

address_modifier
    *undescribed*

mirrored_protocol_engine
    *undescribed*

mirrored_logical_port
    *undescribed*

reserved_0C_0
    *undescribed*

mirror_request_enable
    *undescribed*

ssp_command_iu_length
    *undescribed*

xfer_ready_tlr_enable
    *undescribed*

reserved_10_0
    *undescribed*

ssp_max_burst_size
    *undescribed*

transfer_length_bytes
    *undescribed*

reserved_14_0
    *undescribed*

type
    *undescribed*

command_iu_upper
    *undescribed*

command_iu_lower
    *undescribed*

response_iu_upper
    *undescribed*

response_iu_lower
    *undescribed*

task_phase
    *undescribed*

task_status
    *undescribed*

previous_extended_tag
    *undescribed*

stp_retry_count
    *undescribed*

reserved_40_1
    *undescribed*

ssp_tlr_threshold
    *undescribed*

reserved_40_2
    *undescribed*

write_data_length
    *undescribed*

snapshot
    *undescribed*

blk_prot_en
    *undescribed*

blk_sz
    *undescribed*

blk_prot_func
    *undescribed*

reserved_5C_0
    *undescribed*

active_sgl_element
    *undescribed*

sgl_exhausted
    *undescribed*

payload_data_transfer_error
    *undescribed*

frame_buffer_offset
    *undescribed*

sgl_pair_ab
    *undescribed*

sgl_pair_cd
    *undescribed*

sgl_snapshot_ac
    *undescribed*

active_sgl_element_pair
    *undescribed*

reserved_C4_CC
    *undescribed*

interm_crc_val
    *undescribed*

init_crc_seed
    *undescribed*

app_tag_verify
    *undescribed*

app_tag_gen
    *undescribed*

ref_tag_seed_verify
    *undescribed*

UD_bytes_immed_val
    *undescribed*

reserved_DC_0
    *undescribed*

DIF_bytes_immed_val
    *undescribed*

reserved_DC_1
    *undescribed*

bgc_blk_sz
    *undescribed*

reserved_E0_0
    *undescribed*

app_tag_gen_mask
    *undescribed*

{unnamed_union}
    anonymous


app_tag_verify_mask
    *undescribed*

blk_guard_err
    *undescribed*

reserved_E8_0
    *undescribed*

ref_tag_seed_gen
    *undescribed*

intermediate_crc_valid_snapshot
    *undescribed*

reserved_F0_0
    *undescribed*

reference_tag_seed_for_verify_function_snapshot
    *undescribed*

snapshot_of_reserved_dword_DC_of_tc
    *undescribed*

reference_tag_seed_for_generate_function_snapshot
    *undescribed*

.. _`scu_task_context.description`:

Description
-----------



.. This file was automatic generated / don't edit.

