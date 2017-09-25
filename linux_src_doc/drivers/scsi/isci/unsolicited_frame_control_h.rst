.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/unsolicited_frame_control.h

.. _`scu_unsolicited_frame_header`:

struct scu_unsolicited_frame_header
===================================

.. c:type:: struct scu_unsolicited_frame_header


.. _`scu_unsolicited_frame_header.definition`:

Definition
----------

.. code-block:: c

    struct scu_unsolicited_frame_header {
        u32 iit_exists:1;
        u32 protocol_type:3;
        u32 is_address_frame:1;
        u32 connection_rate:4;
        u32 reserved:23;
        u32 data[SCU_UNSOLICITED_FRAME_HEADER_DATA_DWORDS];
    }

.. _`scu_unsolicited_frame_header.members`:

Members
-------

iit_exists
    *undescribed*

protocol_type
    *undescribed*

is_address_frame
    *undescribed*

connection_rate
    *undescribed*

reserved
    *undescribed*

data
    *undescribed*

.. _`scu_unsolicited_frame_header.description`:

Description
-----------

This structure delineates the format of an unsolicited frame header. The
first DWORD are UF attributes defined by the silicon architecture. The data
depicts actual header information received on the link.

.. _`unsolicited_frame_state`:

enum unsolicited_frame_state
============================

.. c:type:: enum unsolicited_frame_state


.. _`unsolicited_frame_state.definition`:

Definition
----------

.. code-block:: c

    enum unsolicited_frame_state {
        UNSOLICITED_FRAME_EMPTY,
        UNSOLICITED_FRAME_IN_USE,
        UNSOLICITED_FRAME_RELEASED,
        UNSOLICITED_FRAME_MAX_STATES
    };

.. _`unsolicited_frame_state.constants`:

Constants
---------

UNSOLICITED_FRAME_EMPTY
    *undescribed*

UNSOLICITED_FRAME_IN_USE
    *undescribed*

UNSOLICITED_FRAME_RELEASED
    *undescribed*

UNSOLICITED_FRAME_MAX_STATES
    *undescribed*

.. _`unsolicited_frame_state.description`:

Description
-----------

This enumeration represents the current unsolicited frame state.  The
controller object can not updtate the hardware unsolicited frame put pointer
unless it has already processed the priror unsolicited frames.

.. _`sci_unsolicited_frame`:

struct sci_unsolicited_frame
============================

.. c:type:: struct sci_unsolicited_frame


.. _`sci_unsolicited_frame.definition`:

Definition
----------

.. code-block:: c

    struct sci_unsolicited_frame {
        enum unsolicited_frame_state state;
        struct scu_unsolicited_frame_header *header;
        void *buffer;
    }

.. _`sci_unsolicited_frame.members`:

Members
-------

state
    *undescribed*

header
    *undescribed*

buffer
    *undescribed*

.. _`sci_unsolicited_frame.description`:

Description
-----------

This is the unsolicited frame data structure it acts as the container for
the current frame state, frame header and frame buffer.

.. _`sci_uf_header_array`:

struct sci_uf_header_array
==========================

.. c:type:: struct sci_uf_header_array


.. _`sci_uf_header_array.definition`:

Definition
----------

.. code-block:: c

    struct sci_uf_header_array {
        struct scu_unsolicited_frame_header *array;
        dma_addr_t physical_address;
    }

.. _`sci_uf_header_array.members`:

Members
-------

array
    *undescribed*

physical_address
    *undescribed*

.. _`sci_uf_header_array.description`:

Description
-----------

This structure contains all of the unsolicited frame header information.

.. _`sci_uf_buffer_array`:

struct sci_uf_buffer_array
==========================

.. c:type:: struct sci_uf_buffer_array


.. _`sci_uf_buffer_array.definition`:

Definition
----------

.. code-block:: c

    struct sci_uf_buffer_array {
        struct sci_unsolicited_frame array[SCU_MAX_UNSOLICITED_FRAMES];
        dma_addr_t physical_address;
    }

.. _`sci_uf_buffer_array.members`:

Members
-------

array
    *undescribed*

physical_address
    *undescribed*

.. _`sci_uf_buffer_array.description`:

Description
-----------

This structure contains all of the unsolicited frame buffer (actual payload)
information.

.. _`sci_uf_address_table_array`:

struct sci_uf_address_table_array
=================================

.. c:type:: struct sci_uf_address_table_array


.. _`sci_uf_address_table_array.definition`:

Definition
----------

.. code-block:: c

    struct sci_uf_address_table_array {
        u64 *array;
        dma_addr_t physical_address;
    }

.. _`sci_uf_address_table_array.members`:

Members
-------

array
    *undescribed*

physical_address
    *undescribed*

.. _`sci_uf_address_table_array.description`:

Description
-----------

This object maintains all of the unsolicited frame address table specific
data.  The address table is a collection of 64-bit pointers that point to
1KB buffers into which the silicon will DMA unsolicited frames.

.. _`sci_unsolicited_frame_control`:

struct sci_unsolicited_frame_control
====================================

.. c:type:: struct sci_unsolicited_frame_control


.. _`sci_unsolicited_frame_control.definition`:

Definition
----------

.. code-block:: c

    struct sci_unsolicited_frame_control {
        u32 get;
        struct sci_uf_header_array headers;
        struct sci_uf_buffer_array buffers;
        struct sci_uf_address_table_array address_table;
    }

.. _`sci_unsolicited_frame_control.members`:

Members
-------

get
    *undescribed*

headers
    *undescribed*

buffers
    *undescribed*

address_table
    *undescribed*

.. _`sci_unsolicited_frame_control.description`:

Description
-----------

This object contains all of the data necessary to handle unsolicited frames.

.. This file was automatic generated / don't edit.

