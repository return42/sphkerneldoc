.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_tlv.c

.. _`fm10k_tlv_msg_init`:

fm10k_tlv_msg_init
==================

.. c:function:: s32 fm10k_tlv_msg_init(u32 *msg, u16 msg_id)

    Initialize message block for TLV data storage

    :param u32 \*msg:
        Pointer to message block

    :param u16 msg_id:
        Message ID indicating message type

.. _`fm10k_tlv_msg_init.description`:

Description
-----------

This function return success if provided with a valid message pointer

.. _`fm10k_tlv_attr_put_null_string`:

fm10k_tlv_attr_put_null_string
==============================

.. c:function:: s32 fm10k_tlv_attr_put_null_string(u32 *msg, u16 attr_id, const unsigned char *string)

    Place null terminated string on message

    :param u32 \*msg:
        Pointer to message block

    :param u16 attr_id:
        Attribute ID

    :param const unsigned char \*string:
        Pointer to string to be stored in attribute

.. _`fm10k_tlv_attr_put_null_string.description`:

Description
-----------

This function will reorder a string to be CPU endian and store it in
the attribute buffer.  It will return success if provided with a valid
pointers.

.. _`fm10k_tlv_attr_get_null_string`:

fm10k_tlv_attr_get_null_string
==============================

.. c:function:: s32 fm10k_tlv_attr_get_null_string(u32 *attr, unsigned char *string)

    Get null terminated string from attribute

    :param u32 \*attr:
        Pointer to attribute

    :param unsigned char \*string:
        Pointer to location of destination string

.. _`fm10k_tlv_attr_get_null_string.description`:

Description
-----------

This function pulls the string back out of the attribute and will place
it in the array pointed by by string.  It will return success if provided
with a valid pointers.

.. _`fm10k_tlv_attr_put_mac_vlan`:

fm10k_tlv_attr_put_mac_vlan
===========================

.. c:function:: s32 fm10k_tlv_attr_put_mac_vlan(u32 *msg, u16 attr_id, const u8 *mac_addr, u16 vlan)

    Store MAC/VLAN attribute in message

    :param u32 \*msg:
        Pointer to message block

    :param u16 attr_id:
        Attribute ID

    :param const u8 \*mac_addr:
        MAC address to be stored

    :param u16 vlan:
        VLAN to be stored

.. _`fm10k_tlv_attr_put_mac_vlan.description`:

Description
-----------

This function will reorder a MAC address to be CPU endian and store it
in the attribute buffer.  It will return success if provided with a
valid pointers.

.. _`fm10k_tlv_attr_get_mac_vlan`:

fm10k_tlv_attr_get_mac_vlan
===========================

.. c:function:: s32 fm10k_tlv_attr_get_mac_vlan(u32 *attr, u8 *mac_addr, u16 *vlan)

    Get MAC/VLAN stored in attribute

    :param u32 \*attr:
        Pointer to attribute

    :param u8 \*mac_addr:
        location of buffer to store MAC address

    :param u16 \*vlan:
        location of buffer to store VLAN

.. _`fm10k_tlv_attr_get_mac_vlan.description`:

Description
-----------

This function pulls the MAC address back out of the attribute and will
place it in the array pointed by by mac_addr.  It will return success
if provided with a valid pointers.

.. _`fm10k_tlv_attr_put_bool`:

fm10k_tlv_attr_put_bool
=======================

.. c:function:: s32 fm10k_tlv_attr_put_bool(u32 *msg, u16 attr_id)

    Add header indicating value "true"

    :param u32 \*msg:
        Pointer to message block

    :param u16 attr_id:
        Attribute ID

.. _`fm10k_tlv_attr_put_bool.description`:

Description
-----------

This function will simply add an attribute header, the fact
that the header is here means the attribute value is true, else
it is false.  The function will return success if provided with a
valid pointers.

.. _`fm10k_tlv_attr_put_value`:

fm10k_tlv_attr_put_value
========================

.. c:function:: s32 fm10k_tlv_attr_put_value(u32 *msg, u16 attr_id, s64 value, u32 len)

    Store integer value attribute in message

    :param u32 \*msg:
        Pointer to message block

    :param u16 attr_id:
        Attribute ID

    :param s64 value:
        Value to be written

    :param u32 len:
        Size of value

.. _`fm10k_tlv_attr_put_value.description`:

Description
-----------

This function will place an integer value of up to 8 bytes in size
in a message attribute.  The function will return success provided
that msg is a valid pointer, and len is 1, 2, 4, or 8.

.. _`fm10k_tlv_attr_get_value`:

fm10k_tlv_attr_get_value
========================

.. c:function:: s32 fm10k_tlv_attr_get_value(u32 *attr, void *value, u32 len)

    Get integer value stored in attribute

    :param u32 \*attr:
        Pointer to attribute

    :param void \*value:
        Pointer to destination buffer

    :param u32 len:
        Size of value

.. _`fm10k_tlv_attr_get_value.description`:

Description
-----------

This function will place an integer value of up to 8 bytes in size
in the offset pointed to by value.  The function will return success
provided that pointers are valid and the len value matches the
attribute length.

.. _`fm10k_tlv_attr_put_le_struct`:

fm10k_tlv_attr_put_le_struct
============================

.. c:function:: s32 fm10k_tlv_attr_put_le_struct(u32 *msg, u16 attr_id, const void *le_struct, u32 len)

    Store little endian structure in message

    :param u32 \*msg:
        Pointer to message block

    :param u16 attr_id:
        Attribute ID

    :param const void \*le_struct:
        Pointer to structure to be written

    :param u32 len:
        Size of le_struct

.. _`fm10k_tlv_attr_put_le_struct.description`:

Description
-----------

This function will place a little endian structure value in a message
attribute.  The function will return success provided that all pointers
are valid and length is a non-zero multiple of 4.

.. _`fm10k_tlv_attr_get_le_struct`:

fm10k_tlv_attr_get_le_struct
============================

.. c:function:: s32 fm10k_tlv_attr_get_le_struct(u32 *attr, void *le_struct, u32 len)

    Get little endian struct form attribute

    :param u32 \*attr:
        Pointer to attribute

    :param void \*le_struct:
        Pointer to structure to be written

    :param u32 len:
        Size of structure

.. _`fm10k_tlv_attr_get_le_struct.description`:

Description
-----------

This function will place a little endian structure in the buffer
pointed to by le_struct.  The function will return success
provided that pointers are valid and the len value matches the
attribute length.

.. _`fm10k_tlv_attr_nest_start`:

fm10k_tlv_attr_nest_start
=========================

.. c:function:: u32 *fm10k_tlv_attr_nest_start(u32 *msg, u16 attr_id)

    Start a set of nested attributes

    :param u32 \*msg:
        Pointer to message block

    :param u16 attr_id:
        Attribute ID

.. _`fm10k_tlv_attr_nest_start.description`:

Description
-----------

This function will mark off a new nested region for encapsulating
a given set of attributes.  The idea is if you wish to place a secondary
structure within the message this mechanism allows for that.  The
function will return NULL on failure, and a pointer to the start
of the nested attributes on success.

.. _`fm10k_tlv_attr_nest_stop`:

fm10k_tlv_attr_nest_stop
========================

.. c:function:: s32 fm10k_tlv_attr_nest_stop(u32 *msg)

    Stop a set of nested attributes

    :param u32 \*msg:
        Pointer to message block

.. _`fm10k_tlv_attr_nest_stop.description`:

Description
-----------

This function closes off an existing set of nested attributes.  The
message pointer should be pointing to the parent of the nest.  So in
the case of a nest within the nest this would be the outer nest pointer.
This function will return success provided all pointers are valid.

.. _`fm10k_tlv_attr_validate`:

fm10k_tlv_attr_validate
=======================

.. c:function:: s32 fm10k_tlv_attr_validate(u32 *attr, const struct fm10k_tlv_attr *tlv_attr)

    Validate attribute metadata

    :param u32 \*attr:
        Pointer to attribute

    :param const struct fm10k_tlv_attr \*tlv_attr:
        Type and length info for attribute

.. _`fm10k_tlv_attr_validate.description`:

Description
-----------

This function does some basic validation of the input TLV.  It
verifies the length, and in the case of null terminated strings
it verifies that the last byte is null.  The function will
return FM10K_ERR_PARAM if any attribute is malformed, otherwise
it returns 0.

.. _`fm10k_tlv_attr_parse`:

fm10k_tlv_attr_parse
====================

.. c:function:: s32 fm10k_tlv_attr_parse(u32 *attr, u32 **results, const struct fm10k_tlv_attr *tlv_attr)

    Parses stream of attribute data

    :param u32 \*attr:
        Pointer to attribute list

    :param u32 \*\*results:
        Pointer array to store pointers to attributes

    :param const struct fm10k_tlv_attr \*tlv_attr:
        Type and length info for attributes

.. _`fm10k_tlv_attr_parse.description`:

Description
-----------

This function validates a stream of attributes and parses them
up into an array of pointers stored in results.  The function will
return FM10K_ERR_PARAM on any input or message error,
FM10K_NOT_IMPLEMENTED for any attribute that is outside of the array
and 0 on success. Any attributes not found in tlv_attr will be silently
ignored.

.. _`fm10k_tlv_msg_parse`:

fm10k_tlv_msg_parse
===================

.. c:function:: s32 fm10k_tlv_msg_parse(struct fm10k_hw *hw, u32 *msg, struct fm10k_mbx_info *mbx, const struct fm10k_msg_data *data)

    Parses message header and calls function handler

    :param struct fm10k_hw \*hw:
        Pointer to hardware structure

    :param u32 \*msg:
        Pointer to message

    :param struct fm10k_mbx_info \*mbx:
        Pointer to mailbox information structure

    :param const struct fm10k_msg_data \*data:
        Pointer to message handler data structure

.. _`fm10k_tlv_msg_parse.description`:

Description
-----------

This function should be the first function called upon receiving a
message.  The handler will identify the message type and call the correct
handler for the given message.  It will return the value from the function
call on a recognized message type, otherwise it will return
FM10K_NOT_IMPLEMENTED on an unrecognized type.

.. _`fm10k_tlv_msg_error`:

fm10k_tlv_msg_error
===================

.. c:function:: s32 fm10k_tlv_msg_error(struct fm10k_hw *hw, u32 **results, struct fm10k_mbx_info *mbx)

    Default handler for unrecognized TLV message IDs

    :param struct fm10k_hw \*hw:
        Pointer to hardware structure

    :param u32 \*\*results:
        Pointer array to message, results[0] is pointer to message

    :param struct fm10k_mbx_info \*mbx:
        Unused mailbox pointer

.. _`fm10k_tlv_msg_error.description`:

Description
-----------

This function is a default handler for unrecognized messages.  At a
a minimum it just indicates that the message requested was
unimplemented.

.. _`fm10k_tlv_msg_test_generate_data`:

fm10k_tlv_msg_test_generate_data
================================

.. c:function:: void fm10k_tlv_msg_test_generate_data(u32 *msg, u32 attr_flags)

    Stuff message with data

    :param u32 \*msg:
        Pointer to message

    :param u32 attr_flags:
        List of flags indicating what attributes to add

.. _`fm10k_tlv_msg_test_generate_data.description`:

Description
-----------

This function is meant to load a message buffer with attribute data

.. _`fm10k_tlv_msg_test_create`:

fm10k_tlv_msg_test_create
=========================

.. c:function:: void fm10k_tlv_msg_test_create(u32 *msg, u32 attr_flags)

    Create a test message testing all attributes

    :param u32 \*msg:
        Pointer to message

    :param u32 attr_flags:
        List of flags indicating what attributes to add

.. _`fm10k_tlv_msg_test_create.description`:

Description
-----------

This function is meant to load a message buffer with all attribute types
including a nested attribute.

.. _`fm10k_tlv_msg_test`:

fm10k_tlv_msg_test
==================

.. c:function:: s32 fm10k_tlv_msg_test(struct fm10k_hw *hw, u32 **results, struct fm10k_mbx_info *mbx)

    Validate all results on test message receive

    :param struct fm10k_hw \*hw:
        Pointer to hardware structure

    :param u32 \*\*results:
        Pointer array to attributes in the message

    :param struct fm10k_mbx_info \*mbx:
        Pointer to mailbox information structure

.. _`fm10k_tlv_msg_test.description`:

Description
-----------

This function does a check to verify all attributes match what the test
message placed in the message buffer.  It is the default handler
for TLV test messages.

.. This file was automatic generated / don't edit.

