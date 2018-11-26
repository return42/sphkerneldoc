.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/cros_ec_commands.h

.. _`ec_lpc_host_args`:

struct ec_lpc_host_args
=======================

.. c:type:: struct ec_lpc_host_args

    Arguments at EC_LPC_ADDR_HOST_ARGS

.. _`ec_lpc_host_args.definition`:

Definition
----------

.. code-block:: c

    struct ec_lpc_host_args {
        uint8_t flags;
        uint8_t command_version;
        uint8_t data_size;
        uint8_t checksum;
    }

.. _`ec_lpc_host_args.members`:

Members
-------

flags
    The host argument flags.

command_version
    Command version.

data_size
    The length of data.

checksum
    Checksum; sum of command + flags + command_version + data_size +
    all params/response data bytes.

.. _`ec_host_request`:

struct ec_host_request
======================

.. c:type:: struct ec_host_request

    Version 3 request from host.

.. _`ec_host_request.definition`:

Definition
----------

.. code-block:: c

    struct ec_host_request {
        uint8_t struct_version;
        uint8_t checksum;
        uint16_t command;
        uint8_t command_version;
        uint8_t reserved;
        uint16_t data_len;
    }

.. _`ec_host_request.members`:

Members
-------

struct_version
    Should be 3. The EC will return EC_RES_INVALID_HEADER if it
    receives a header with a version it doesn't know how to
    parse.

checksum
    Checksum of request and data; sum of all bytes including checksum
    should total to 0.

command
    Command to send (EC_CMD_...)

command_version
    Command version.

reserved
    Unused byte in current protocol version; set to 0.

data_len
    Length of data which follows this header.

.. _`ec_host_response`:

struct ec_host_response
=======================

.. c:type:: struct ec_host_response

    Version 3 response from EC.

.. _`ec_host_response.definition`:

Definition
----------

.. code-block:: c

    struct ec_host_response {
        uint8_t struct_version;
        uint8_t checksum;
        uint16_t result;
        uint16_t data_len;
        uint16_t reserved;
    }

.. _`ec_host_response.members`:

Members
-------

struct_version
    Struct version (=3).

checksum
    Checksum of response and data; sum of all bytes including
    checksum should total to 0.

result
    EC's response to the command (separate from communication failure)

data_len
    Length of data which follows this header.

reserved
    Unused bytes in current protocol version; set to 0.

.. _`ec_response_proto_version`:

struct ec_response_proto_version
================================

.. c:type:: struct ec_response_proto_version

    Response to the proto version command.

.. _`ec_response_proto_version.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_proto_version {
        uint32_t version;
    }

.. _`ec_response_proto_version.members`:

Members
-------

version
    The protocol version.

.. _`ec_params_hello`:

struct ec_params_hello
======================

.. c:type:: struct ec_params_hello

    Parameters to the hello command.

.. _`ec_params_hello.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_hello {
        uint32_t in_data;
    }

.. _`ec_params_hello.members`:

Members
-------

in_data
    Pass anything here.

.. _`ec_response_hello`:

struct ec_response_hello
========================

.. c:type:: struct ec_response_hello

    Response to the hello command.

.. _`ec_response_hello.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_hello {
        uint32_t out_data;
    }

.. _`ec_response_hello.members`:

Members
-------

out_data
    Output will be in_data + 0x01020304.

.. _`ec_response_get_version`:

struct ec_response_get_version
==============================

.. c:type:: struct ec_response_get_version

    Response to the get version command.

.. _`ec_response_get_version.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_get_version {
        char version_string_ro[32];
        char version_string_rw[32];
        char reserved[32];
        uint32_t current_image;
    }

.. _`ec_response_get_version.members`:

Members
-------

version_string_ro
    Null-terminated RO firmware version string.

version_string_rw
    Null-terminated RW firmware version string.

reserved
    Unused bytes; was previously RW-B firmware version string.

current_image
    One of ec_current_image.

.. _`ec_params_read_test`:

struct ec_params_read_test
==========================

.. c:type:: struct ec_params_read_test

    Parameters for the read test command.

.. _`ec_params_read_test.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_read_test {
        uint32_t offset;
        uint32_t size;
    }

.. _`ec_params_read_test.members`:

Members
-------

offset
    Starting value for read buffer.

size
    Size to read in bytes.

.. _`ec_response_read_test`:

struct ec_response_read_test
============================

.. c:type:: struct ec_response_read_test

    Response to the read test command.

.. _`ec_response_read_test.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_read_test {
        uint32_t data[32];
    }

.. _`ec_response_read_test.members`:

Members
-------

data
    Data returned by the read test command.

.. _`ec_response_get_chip_info`:

struct ec_response_get_chip_info
================================

.. c:type:: struct ec_response_get_chip_info

    Response to the get chip info command.

.. _`ec_response_get_chip_info.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_get_chip_info {
        char vendor[32];
        char name[32];
        char revision[32];
    }

.. _`ec_response_get_chip_info.members`:

Members
-------

vendor
    Null-terminated string for chip vendor.

name
    Null-terminated string for chip name.

revision
    Null-terminated string for chip mask version.

.. _`ec_response_board_version`:

struct ec_response_board_version
================================

.. c:type:: struct ec_response_board_version

    Response to the board version command.

.. _`ec_response_board_version.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_board_version {
        uint16_t board_version;
    }

.. _`ec_response_board_version.members`:

Members
-------

board_version
    A monotonously incrementing number.

.. _`ec_params_read_memmap`:

struct ec_params_read_memmap
============================

.. c:type:: struct ec_params_read_memmap

    Parameters for the read memory map command.

.. _`ec_params_read_memmap.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_read_memmap {
        uint8_t offset;
        uint8_t size;
    }

.. _`ec_params_read_memmap.members`:

Members
-------

offset
    Offset in memmap (EC_MEMMAP\_\*).

size
    Size to read in bytes.

.. _`ec_params_get_cmd_versions`:

struct ec_params_get_cmd_versions
=================================

.. c:type:: struct ec_params_get_cmd_versions

    Parameters for the get command versions.

.. _`ec_params_get_cmd_versions.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_get_cmd_versions {
        uint8_t cmd;
    }

.. _`ec_params_get_cmd_versions.members`:

Members
-------

cmd
    Command to check.

.. _`ec_params_get_cmd_versions_v1`:

struct ec_params_get_cmd_versions_v1
====================================

.. c:type:: struct ec_params_get_cmd_versions_v1

    Parameters for the get command versions (v1)

.. _`ec_params_get_cmd_versions_v1.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_get_cmd_versions_v1 {
        uint16_t cmd;
    }

.. _`ec_params_get_cmd_versions_v1.members`:

Members
-------

cmd
    Command to check.

.. _`ec_response_get_cmd_versions`:

struct ec_response_get_cmd_versions
===================================

.. c:type:: struct ec_response_get_cmd_versions

    Response to the get command versions.

.. _`ec_response_get_cmd_versions.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_get_cmd_versions {
        uint32_t version_mask;
    }

.. _`ec_response_get_cmd_versions.members`:

Members
-------

version_mask
    Mask of supported versions; use \ :c:func:`EC_VER_MASK`\  to compare with
    a desired version.

.. _`ec_response_get_comms_status`:

struct ec_response_get_comms_status
===================================

.. c:type:: struct ec_response_get_comms_status

    Response to the get comms status command.

.. _`ec_response_get_comms_status.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_get_comms_status {
        uint32_t flags;
    }

.. _`ec_response_get_comms_status.members`:

Members
-------

flags
    Mask of enum ec_comms_status.

.. _`ec_response_get_protocol_info`:

struct ec_response_get_protocol_info
====================================

.. c:type:: struct ec_response_get_protocol_info

    Response to the get protocol info.

.. _`ec_response_get_protocol_info.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_get_protocol_info {
        uint32_t protocol_versions;
        uint16_t max_request_packet_size;
        uint16_t max_response_packet_size;
        uint32_t flags;
    }

.. _`ec_response_get_protocol_info.members`:

Members
-------

protocol_versions
    Bitmask of protocol versions supported (1 << n means
    version n).

max_request_packet_size
    Maximum request packet size in bytes.

max_response_packet_size
    Maximum response packet size in bytes.

flags
    see EC_PROTOCOL_INFO\_\*

.. _`ec_response_flash_info`:

struct ec_response_flash_info
=============================

.. c:type:: struct ec_response_flash_info

    Response to the flash info command.

.. _`ec_response_flash_info.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_flash_info {
        uint32_t flash_size;
        uint32_t write_block_size;
        uint32_t erase_block_size;
        uint32_t protect_block_size;
    }

.. _`ec_response_flash_info.members`:

Members
-------

flash_size
    Usable flash size in bytes.

write_block_size
    Write block size. Write offset and size must be a
    multiple of this.

erase_block_size
    Erase block size. Erase offset and size must be a
    multiple of this.

protect_block_size
    Protection block size. Protection offset and size
    must be a multiple of this.

.. _`ec_response_flash_info.description`:

Description
-----------

Version 0 returns these fields.

.. _`ec_response_flash_info_1`:

struct ec_response_flash_info_1
===============================

.. c:type:: struct ec_response_flash_info_1

    Response to the flash info v1 command.

.. _`ec_response_flash_info_1.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_flash_info_1 {
        uint32_t flash_size;
        uint32_t write_block_size;
        uint32_t erase_block_size;
        uint32_t protect_block_size;
        uint32_t write_ideal_size;
        uint32_t flags;
    }

.. _`ec_response_flash_info_1.members`:

Members
-------

flash_size
    Usable flash size in bytes.

write_block_size
    Write block size. Write offset and size must be a
    multiple of this.

erase_block_size
    Erase block size. Erase offset and size must be a
    multiple of this.

protect_block_size
    Protection block size. Protection offset and size
    must be a multiple of this.

write_ideal_size
    Ideal write size in bytes.  Writes will be fastest if
    size is exactly this and offset is a multiple of this.
    For example, an EC may have a write buffer which can do
    half-page operations if data is aligned, and a slower
    word-at-a-time write mode.

flags
    Flags; see EC_FLASH_INFO\_\*

.. _`ec_response_flash_info_1.description`:

Description
-----------

Version 1 returns the same initial fields as version 0, with additional
fields following.

gcc anonymous structs don't seem to get along with the \__packed directive;
if they did we'd define the version 0 struct as a sub-struct of this one.

.. _`ec_params_flash_read`:

struct ec_params_flash_read
===========================

.. c:type:: struct ec_params_flash_read

    Parameters for the flash read command.

.. _`ec_params_flash_read.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_flash_read {
        uint32_t offset;
        uint32_t size;
    }

.. _`ec_params_flash_read.members`:

Members
-------

offset
    Byte offset to read.

size
    Size to read in bytes.

.. _`ec_params_flash_write`:

struct ec_params_flash_write
============================

.. c:type:: struct ec_params_flash_write

    Parameters for the flash write command.

.. _`ec_params_flash_write.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_flash_write {
        uint32_t offset;
        uint32_t size;
    }

.. _`ec_params_flash_write.members`:

Members
-------

offset
    Byte offset to write.

size
    Size to write in bytes.

.. _`ec_params_flash_erase`:

struct ec_params_flash_erase
============================

.. c:type:: struct ec_params_flash_erase

    Parameters for the flash erase command.

.. _`ec_params_flash_erase.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_flash_erase {
        uint32_t offset;
        uint32_t size;
    }

.. _`ec_params_flash_erase.members`:

Members
-------

offset
    Byte offset to erase.

size
    Size to erase in bytes.

.. _`ec_params_flash_protect`:

struct ec_params_flash_protect
==============================

.. c:type:: struct ec_params_flash_protect

    Parameters for the flash protect command.

.. _`ec_params_flash_protect.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_flash_protect {
        uint32_t mask;
        uint32_t flags;
    }

.. _`ec_params_flash_protect.members`:

Members
-------

mask
    Bits in flags to apply.

flags
    New flags to apply.

.. _`ec_response_flash_protect`:

struct ec_response_flash_protect
================================

.. c:type:: struct ec_response_flash_protect

    Response to the flash protect command.

.. _`ec_response_flash_protect.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_flash_protect {
        uint32_t flags;
        uint32_t valid_flags;
        uint32_t writable_flags;
    }

.. _`ec_response_flash_protect.members`:

Members
-------

flags
    Current value of flash protect flags.

valid_flags
    Flags which are valid on this platform. This allows the
    caller to distinguish between flags which aren't set vs. flags
    which can't be set on this platform.

writable_flags
    Flags which can be changed given the current protection
    state.

.. _`ec_params_flash_region_info`:

struct ec_params_flash_region_info
==================================

.. c:type:: struct ec_params_flash_region_info

    Parameters for the flash region info command.

.. _`ec_params_flash_region_info.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_flash_region_info {
        uint32_t region;
    }

.. _`ec_params_flash_region_info.members`:

Members
-------

region
    Flash region; see EC_FLASH_REGION\_\*

.. _`ec_params_cec_write`:

struct ec_params_cec_write
==========================

.. c:type:: struct ec_params_cec_write

    Message to write to the CEC bus

.. _`ec_params_cec_write.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_cec_write {
        uint8_t msg[EC_MAX_CEC_MSG_LEN];
    }

.. _`ec_params_cec_write.members`:

Members
-------

msg
    message content to write to the CEC bus

.. _`ec_params_cec_set`:

struct ec_params_cec_set
========================

.. c:type:: struct ec_params_cec_set

    CEC parameters set

.. _`ec_params_cec_set.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_cec_set {
        uint8_t cmd;
        uint8_t val;
    }

.. _`ec_params_cec_set.members`:

Members
-------

cmd
    parameter type, can be CEC_CMD_ENABLE or CEC_CMD_LOGICAL_ADDRESS

val
    in case cmd is CEC_CMD_ENABLE, this field can be 0 to disable CEC
    or 1 to enable CEC functionality, in case cmd is CEC_CMD_LOGICAL_ADDRESS,
    this field encodes the requested logical address between 0 and 15
    or 0xff to unregister

.. _`ec_params_cec_get`:

struct ec_params_cec_get
========================

.. c:type:: struct ec_params_cec_get

    CEC parameters get

.. _`ec_params_cec_get.definition`:

Definition
----------

.. code-block:: c

    struct ec_params_cec_get {
        uint8_t cmd;
    }

.. _`ec_params_cec_get.members`:

Members
-------

cmd
    parameter type, can be CEC_CMD_ENABLE or CEC_CMD_LOGICAL_ADDRESS

.. _`ec_response_cec_get`:

struct ec_response_cec_get
==========================

.. c:type:: struct ec_response_cec_get

    CEC parameters get response

.. _`ec_response_cec_get.definition`:

Definition
----------

.. code-block:: c

    struct ec_response_cec_get {
        uint8_t val;
    }

.. _`ec_response_cec_get.members`:

Members
-------

val
    in case cmd was CEC_CMD_ENABLE, this field will 0 if CEC is
    disabled or 1 if CEC functionality is enabled,
    in case cmd was CEC_CMD_LOGICAL_ADDRESS, this will encode the
    configured logical address between 0 and 15 or 0xff if unregistered

.. This file was automatic generated / don't edit.

