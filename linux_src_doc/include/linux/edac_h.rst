.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/edac.h

.. _`dev_type`:

enum dev_type
=============

.. c:type:: enum dev_type

    describe the type of memory DRAM chips used at the stick

.. _`dev_type.definition`:

Definition
----------

.. code-block:: c

    enum dev_type {
        DEV_UNKNOWN,
        DEV_X1,
        DEV_X2,
        DEV_X4,
        DEV_X8,
        DEV_X16,
        DEV_X32,
        DEV_X64
    };

.. _`dev_type.constants`:

Constants
---------

DEV_UNKNOWN
    Can't be determined, or MC doesn't support detect it

DEV_X1
    1 bit for data

DEV_X2
    2 bits for data

DEV_X4
    4 bits for data

DEV_X8
    8 bits for data

DEV_X16
    16 bits for data

DEV_X32
    32 bits for data

DEV_X64
    64 bits for data

.. _`dev_type.description`:

Description
-----------

Typical values are x4 and x8.

.. _`hw_event_mc_err_type`:

enum hw_event_mc_err_type
=========================

.. c:type:: enum hw_event_mc_err_type

    type of the detected error

.. _`hw_event_mc_err_type.definition`:

Definition
----------

.. code-block:: c

    enum hw_event_mc_err_type {
        HW_EVENT_ERR_CORRECTED,
        HW_EVENT_ERR_UNCORRECTED,
        HW_EVENT_ERR_DEFERRED,
        HW_EVENT_ERR_FATAL,
        HW_EVENT_ERR_INFO
    };

.. _`hw_event_mc_err_type.constants`:

Constants
---------

HW_EVENT_ERR_CORRECTED
    Corrected Error - Indicates that an ECC
    corrected error was detected

HW_EVENT_ERR_UNCORRECTED
    Uncorrected Error - Indicates an error that
    can't be corrected by ECC, but it is not
    fatal (maybe it is on an unused memory area,
    or the memory controller could recover from
    it for example, by re-trying the operation).

HW_EVENT_ERR_DEFERRED
    Deferred Error - Indicates an uncorrectable
    error whose handling is not urgent. This could
    be due to hardware data poisoning where the
    system can continue operation until the poisoned
    data is consumed. Preemptive measures may also
    be taken, e.g. offlining pages, etc.

HW_EVENT_ERR_FATAL
    Fatal Error - Uncorrected error that could not
    be recovered.

HW_EVENT_ERR_INFO
    Informational - The CPER spec defines a forth
    type of error: informational logs.

.. _`mem_type`:

enum mem_type
=============

.. c:type:: enum mem_type

    memory types. For a more detailed reference, please see http://en.wikipedia.org/wiki/DRAM

.. _`mem_type.definition`:

Definition
----------

.. code-block:: c

    enum mem_type {
        MEM_EMPTY,
        MEM_RESERVED,
        MEM_UNKNOWN,
        MEM_FPM,
        MEM_EDO,
        MEM_BEDO,
        MEM_SDR,
        MEM_RDR,
        MEM_DDR,
        MEM_RDDR,
        MEM_RMBS,
        MEM_DDR2,
        MEM_FB_DDR2,
        MEM_RDDR2,
        MEM_XDR,
        MEM_DDR3,
        MEM_RDDR3,
        MEM_LRDDR3,
        MEM_DDR4,
        MEM_RDDR4,
        MEM_LRDDR4,
        MEM_NVDIMM
    };

.. _`mem_type.constants`:

Constants
---------

MEM_EMPTY
    Empty csrow

MEM_RESERVED
    Reserved csrow type

MEM_UNKNOWN
    Unknown csrow type

MEM_FPM
    FPM - Fast Page Mode, used on systems up to 1995.

MEM_EDO
    EDO - Extended data out, used on systems up to 1998.

MEM_BEDO
    BEDO - Burst Extended data out, an EDO variant.

MEM_SDR
    SDR - Single data rate SDRAM
    http://en.wikipedia.org/wiki/Synchronous_dynamic_random-access_memory
    They use 3 pins for chip select: Pins 0 and 2 are
    for rank 0; pins 1 and 3 are for rank 1, if the memory
    is dual-rank.

MEM_RDR
    Registered SDR SDRAM

MEM_DDR
    Double data rate SDRAM
    http://en.wikipedia.org/wiki/DDR_SDRAM

MEM_RDDR
    Registered Double data rate SDRAM
    This is a variant of the DDR memories.
    A registered memory has a buffer inside it, hiding
    part of the memory details to the memory controller.

MEM_RMBS
    Rambus DRAM, used on a few Pentium III/IV controllers.

MEM_DDR2
    DDR2 RAM, as described at JEDEC JESD79-2F.
    Those memories are labeled as "PC2-" instead of "PC" to
    differentiate from DDR.

MEM_FB_DDR2
    Fully-Buffered DDR2, as described at JEDEC Std No. 205
    and JESD206.
    Those memories are accessed per DIMM slot, and not by
    a chip select signal.

MEM_RDDR2
    Registered DDR2 RAM
    This is a variant of the DDR2 memories.

MEM_XDR
    Rambus XDR
    It is an evolution of the original RAMBUS memories,
    created to compete with DDR2. Weren't used on any
    x86 arch, but cell_edac PPC memory controller uses it.

MEM_DDR3
    DDR3 RAM

MEM_RDDR3
    Registered DDR3 RAM
    This is a variant of the DDR3 memories.

MEM_LRDDR3
    Load-Reduced DDR3 memory.

MEM_DDR4
    Unbuffered DDR4 RAM

MEM_RDDR4
    Registered DDR4 RAM
    This is a variant of the DDR4 memories.

MEM_LRDDR4
    Load-Reduced DDR4 memory.

MEM_NVDIMM
    Non-volatile RAM

.. _`edac_type`:

enum edac_type
==============

.. c:type:: enum edac_type

    type - Error Detection and Correction capabilities and mode

.. _`edac_type.definition`:

Definition
----------

.. code-block:: c

    enum edac_type {
        EDAC_UNKNOWN,
        EDAC_NONE,
        EDAC_RESERVED,
        EDAC_PARITY,
        EDAC_EC,
        EDAC_SECDED,
        EDAC_S2ECD2ED,
        EDAC_S4ECD4ED,
        EDAC_S8ECD8ED,
        EDAC_S16ECD16ED
    };

.. _`edac_type.constants`:

Constants
---------

EDAC_UNKNOWN
    Unknown if ECC is available

EDAC_NONE
    Doesn't support ECC

EDAC_RESERVED
    Reserved ECC type

EDAC_PARITY
    Detects parity errors

EDAC_EC
    Error Checking - no correction

EDAC_SECDED
    Single bit error correction, Double detection

EDAC_S2ECD2ED
    Chipkill x2 devices - do these exist?

EDAC_S4ECD4ED
    Chipkill x4 devices

EDAC_S8ECD8ED
    Chipkill x8 devices

EDAC_S16ECD16ED
    Chipkill x16 devices

.. _`scrub_type`:

enum scrub_type
===============

.. c:type:: enum scrub_type

    scrubbing capabilities

.. _`scrub_type.definition`:

Definition
----------

.. code-block:: c

    enum scrub_type {
        SCRUB_UNKNOWN,
        SCRUB_NONE,
        SCRUB_SW_PROG,
        SCRUB_SW_SRC,
        SCRUB_SW_PROG_SRC,
        SCRUB_SW_TUNABLE,
        SCRUB_HW_PROG,
        SCRUB_HW_SRC,
        SCRUB_HW_PROG_SRC,
        SCRUB_HW_TUNABLE
    };

.. _`scrub_type.constants`:

Constants
---------

SCRUB_UNKNOWN
    Unknown if scrubber is available

SCRUB_NONE
    No scrubber

SCRUB_SW_PROG
    SW progressive (sequential) scrubbing

SCRUB_SW_SRC
    Software scrub only errors

SCRUB_SW_PROG_SRC
    Progressive software scrub from an error

SCRUB_SW_TUNABLE
    Software scrub frequency is tunable

SCRUB_HW_PROG
    HW progressive (sequential) scrubbing

SCRUB_HW_SRC
    Hardware scrub only errors

SCRUB_HW_PROG_SRC
    Progressive hardware scrub from an error

SCRUB_HW_TUNABLE
    Hardware scrub frequency is tunable

.. _`edac_mc_layer_type`:

enum edac_mc_layer_type
=======================

.. c:type:: enum edac_mc_layer_type

    memory controller hierarchy layer

.. _`edac_mc_layer_type.definition`:

Definition
----------

.. code-block:: c

    enum edac_mc_layer_type {
        EDAC_MC_LAYER_BRANCH,
        EDAC_MC_LAYER_CHANNEL,
        EDAC_MC_LAYER_SLOT,
        EDAC_MC_LAYER_CHIP_SELECT,
        EDAC_MC_LAYER_ALL_MEM
    };

.. _`edac_mc_layer_type.constants`:

Constants
---------

EDAC_MC_LAYER_BRANCH
    memory layer is named "branch"

EDAC_MC_LAYER_CHANNEL
    memory layer is named "channel"

EDAC_MC_LAYER_SLOT
    memory layer is named "slot"

EDAC_MC_LAYER_CHIP_SELECT
    memory layer is named "chip select"

EDAC_MC_LAYER_ALL_MEM
    memory layout is unknown. All memory is mapped
    as a single memory area. This is used when
    retrieving errors from a firmware driven driver.

.. _`edac_mc_layer_type.description`:

Description
-----------

This enum is used by the drivers to tell edac_mc_sysfs what name should
be used when describing a memory stick location.

.. _`edac_mc_layer`:

struct edac_mc_layer
====================

.. c:type:: struct edac_mc_layer

    describes the memory controller hierarchy

.. _`edac_mc_layer.definition`:

Definition
----------

.. code-block:: c

    struct edac_mc_layer {
        enum edac_mc_layer_type type;
        unsigned size;
        bool is_virt_csrow;
    }

.. _`edac_mc_layer.members`:

Members
-------

type
    layer type

size
    number of components per layer. For example,
    if the channel layer has two channels, size = 2

is_virt_csrow
    This layer is part of the "csrow" when old API
    compatibility mode is enabled. Otherwise, it is
    a channel

.. _`edac_dimm_off`:

EDAC_DIMM_OFF
=============

.. c:function::  EDAC_DIMM_OFF( layers,  nlayers,  layer0,  layer1,  layer2)

    Macro responsible to get a pointer offset inside a pointer array for the element given by [layer0,layer1,layer2] position

    :param  layers:
        a struct edac_mc_layer array, describing how many elements
        were allocated for each layer

    :param  nlayers:
        Number of layers at the \ ``layers``\  array

    :param  layer0:
        layer0 position

    :param  layer1:
        layer1 position. Unused if n_layers < 2

    :param  layer2:
        layer2 position. Unused if n_layers < 3

.. _`edac_dimm_off.description`:

Description
-----------

For 1 layer, this macro returns "var[layer0] - var";

For 2 layers, this macro is similar to allocate a bi-dimensional array
and to return "var[layer0][layer1] - var";

For 3 layers, this macro is similar to allocate a tri-dimensional array
and to return "var[layer0][layer1][layer2] - var".

A loop could be used here to make it more generic, but, as we only have
3 layers, this is a little faster.

By design, layers can never be 0 or more than 3. If that ever happens,
a NULL is returned, causing an OOPS during the memory allocation routine,
with would point to the developer that he's doing something wrong.

.. _`edac_dimm_ptr`:

EDAC_DIMM_PTR
=============

.. c:function::  EDAC_DIMM_PTR( layers,  var,  nlayers,  layer0,  layer1,  layer2)

    Macro responsible to get a pointer inside a pointer array for the element given by [layer0,layer1,layer2] position

    :param  layers:
        a struct edac_mc_layer array, describing how many elements
        were allocated for each layer

    :param  var:
        name of the var where we want to get the pointer
        (like mci->dimms)

    :param  nlayers:
        Number of layers at the \ ``layers``\  array

    :param  layer0:
        layer0 position

    :param  layer1:
        layer1 position. Unused if n_layers < 2

    :param  layer2:
        layer2 position. Unused if n_layers < 3

.. _`edac_dimm_ptr.description`:

Description
-----------

For 1 layer, this macro returns "var[layer0]";

For 2 layers, this macro is similar to allocate a bi-dimensional array
and to return "var[layer0][layer1]";

For 3 layers, this macro is similar to allocate a tri-dimensional array
and to return "var[layer0][layer1][layer2]";

.. _`rank_info`:

struct rank_info
================

.. c:type:: struct rank_info

    contains the information for one DIMM rank

.. _`rank_info.definition`:

Definition
----------

.. code-block:: c

    struct rank_info {
        int chan_idx;
        struct csrow_info *csrow;
        struct dimm_info *dimm;
        u32 ce_count;
    }

.. _`rank_info.members`:

Members
-------

chan_idx
    channel number where the rank is (typically, 0 or 1)

csrow
    A pointer to the chip select row structure (the parent
    structure). The location of the rank is given by
    the (csrow->csrow_idx, chan_idx) vector.

dimm
    A pointer to the DIMM structure, where the DIMM label
    information is stored.

ce_count
    number of correctable errors for this rank

.. _`rank_info.description`:

Description
-----------

FIXME: Currently, the EDAC core model will assume one DIMM per rank.
       This is a bad assumption, but it makes this patch easier. Later
       patches in this series will fix this issue.

.. _`edac_raw_error_desc`:

struct edac_raw_error_desc
==========================

.. c:type:: struct edac_raw_error_desc

    Raw error report structure

.. _`edac_raw_error_desc.definition`:

Definition
----------

.. code-block:: c

    struct edac_raw_error_desc {
        char location[LOCATION_SIZE];
        char label[(EDAC_MC_LABEL_LEN + 1 + sizeof(OTHER_LABEL)) * EDAC_MAX_LABELS];
        long grain;
        u16 error_count;
        int top_layer;
        int mid_layer;
        int low_layer;
        unsigned long page_frame_number;
        unsigned long offset_in_page;
        unsigned long syndrome;
        const char *msg;
        const char *other_detail;
        bool enable_per_layer_report;
    }

.. _`edac_raw_error_desc.members`:

Members
-------

location
    location of the error

label
    label of the affected DIMM(s)

grain
    minimum granularity for an error report, in bytes

error_count
    number of errors of the same type

top_layer
    top layer of the error (layer[0])

mid_layer
    middle layer of the error (layer[1])

low_layer
    low layer of the error (layer[2])

page_frame_number
    page where the error happened

offset_in_page
    page offset

syndrome
    syndrome of the error (or 0 if unknown or if
    the syndrome is not applicable)

msg
    error message

other_detail
    other driver-specific detail about the error

enable_per_layer_report
    if false, the error affects all layers
    (typically, a memory controller error)

.. This file was automatic generated / don't edit.

