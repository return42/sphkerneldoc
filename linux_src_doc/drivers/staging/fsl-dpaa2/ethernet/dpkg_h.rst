.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-dpaa2/ethernet/dpkg.h

.. _`dpkg_num_of_masks`:

DPKG_NUM_OF_MASKS
=================

.. c:function::  DPKG_NUM_OF_MASKS()

.. _`dpkg_max_num_of_extracts`:

DPKG_MAX_NUM_OF_EXTRACTS
========================

.. c:function::  DPKG_MAX_NUM_OF_EXTRACTS()

.. _`dpkg_extract_from_hdr_type`:

enum dpkg_extract_from_hdr_type
===============================

.. c:type:: enum dpkg_extract_from_hdr_type

    Selecting extraction by header types

.. _`dpkg_extract_from_hdr_type.definition`:

Definition
----------

.. code-block:: c

    enum dpkg_extract_from_hdr_type {
        DPKG_FROM_HDR,
        DPKG_FROM_FIELD,
        DPKG_FULL_FIELD
    };

.. _`dpkg_extract_from_hdr_type.constants`:

Constants
---------

DPKG_FROM_HDR
    Extract selected bytes from header, by offset

DPKG_FROM_FIELD
    Extract selected bytes from header, by offset from field

DPKG_FULL_FIELD
    Extract a full field

.. _`dpkg_extract_type`:

enum dpkg_extract_type
======================

.. c:type:: enum dpkg_extract_type

    Enumeration for selecting extraction type

.. _`dpkg_extract_type.definition`:

Definition
----------

.. code-block:: c

    enum dpkg_extract_type {
        DPKG_EXTRACT_FROM_HDR,
        DPKG_EXTRACT_FROM_DATA,
        DPKG_EXTRACT_FROM_PARSE
    };

.. _`dpkg_extract_type.constants`:

Constants
---------

DPKG_EXTRACT_FROM_HDR
    Extract from the header

DPKG_EXTRACT_FROM_DATA
    Extract from data not in specific header

DPKG_EXTRACT_FROM_PARSE
    Extract from parser-result;
    e.g. can be used to extract header existence;
    please refer to 'Parse Result definition' section in the parser BG

.. _`dpkg_mask`:

struct dpkg_mask
================

.. c:type:: struct dpkg_mask

    A structure for defining a single extraction mask

.. _`dpkg_mask.definition`:

Definition
----------

.. code-block:: c

    struct dpkg_mask {
        u8 mask;
        u8 offset;
    }

.. _`dpkg_mask.members`:

Members
-------

mask
    Byte mask for the extracted content

offset
    Offset within the extracted content

.. _`dpkg_extract`:

struct dpkg_extract
===================

.. c:type:: struct dpkg_extract

    A structure for defining a single extraction

.. _`dpkg_extract.definition`:

Definition
----------

.. code-block:: c

    struct dpkg_extract {
        enum dpkg_extract_type type;
        union {
            struct {
                enum net_prot prot;
                enum dpkg_extract_from_hdr_type type;
                u32 field;
                u8 size;
                u8 offset;
                u8 hdr_index;
            } from_hdr;
            struct {
                u8 size;
                u8 offset;
            } from_data;
            struct {
                u8 size;
                u8 offset;
            } from_parse;
        } extract;
        u8 num_of_byte_masks;
        struct dpkg_mask masks[DPKG_NUM_OF_MASKS];
    }

.. _`dpkg_extract.members`:

Members
-------

type
    Determines how the union below is interpreted:
    DPKG_EXTRACT_FROM_HDR: selects 'from_hdr';
    DPKG_EXTRACT_FROM_DATA: selects 'from_data';
    DPKG_EXTRACT_FROM_PARSE: selects 'from_parse'

extract
    Selects extraction method

num_of_byte_masks
    Defines the number of valid entries in the array below;
    This is also the number of bytes to be used as masks

masks
    Masks parameters

.. _`dpkg_profile_cfg`:

struct dpkg_profile_cfg
=======================

.. c:type:: struct dpkg_profile_cfg

    A structure for defining a full Key Generation profile (rule)

.. _`dpkg_profile_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpkg_profile_cfg {
        u8 num_extracts;
        struct dpkg_extract extracts[DPKG_MAX_NUM_OF_EXTRACTS];
    }

.. _`dpkg_profile_cfg.members`:

Members
-------

num_extracts
    Defines the number of valid entries in the array below

extracts
    Array of required extractions

.. This file was automatic generated / don't edit.

