.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

.. _`nvram_parser`:

struct nvram_parser
===================

.. c:type:: struct nvram_parser

    internal info for parser.

.. _`nvram_parser.definition`:

Definition
----------

.. code-block:: c

    struct nvram_parser {
        enum nvram_parser_state state;
        const u8 *data;
        u8 *nvram;
        u32 nvram_len;
        u32 line;
        u32 column;
        u32 pos;
        u32 entry;
        bool multi_dev_v1;
        bool multi_dev_v2;
        bool boardrev_found;
    }

.. _`nvram_parser.members`:

Members
-------

state
    current parser state.

data
    input buffer being parsed.

nvram
    output buffer with parse result.

nvram_len
    lenght of parse result.

line
    current line.

column
    current column in line.

pos
    byte offset in input buffer.

entry
    start position of key,value entry.

multi_dev_v1
    detect pcie multi device v1 (compressed).

multi_dev_v2
    detect pcie multi device v2.

boardrev_found
    nvram contains boardrev information.

.. _`is_nvram_char`:

is_nvram_char
=============

.. c:function:: bool is_nvram_char(char c)

    check if char is a valid one for NVRAM entry

    :param char c:
        *undescribed*

.. _`is_nvram_char.description`:

Description
-----------

It accepts all printable ASCII chars except for '#' which opens a comment.
Please note that ' ' (space) while accepted is not a valid key name char.

.. This file was automatic generated / don't edit.

