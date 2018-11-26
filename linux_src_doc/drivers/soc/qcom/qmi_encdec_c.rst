.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/qmi_encdec.c

.. _`skip_to_next_elem`:

skip_to_next_elem
=================

.. c:function:: struct qmi_elem_info *skip_to_next_elem(struct qmi_elem_info *ei_array, int level)

    Skip to next element in the structure to be encoded

    :param ei_array:
        Struct info describing the element to be skipped.
    :type ei_array: struct qmi_elem_info \*

    :param level:
        Depth level of encoding/decoding to identify nested structures.
    :type level: int

.. _`skip_to_next_elem.description`:

Description
-----------

This function is used while encoding optional elements. If the flag
corresponding to an optional element is not set, then encoding the
optional element can be skipped. This function can be used to perform
that operation.

.. _`skip_to_next_elem.return`:

Return
------

struct info of the next element that can be encoded.

.. _`qmi_calc_min_msg_len`:

qmi_calc_min_msg_len
====================

.. c:function:: int qmi_calc_min_msg_len(struct qmi_elem_info *ei_array, int level)

    Calculate the minimum length of a QMI message

    :param ei_array:
        Struct info array describing the structure.
    :type ei_array: struct qmi_elem_info \*

    :param level:
        Level to identify the depth of the nested structures.
    :type level: int

.. _`qmi_calc_min_msg_len.return`:

Return
------

Expected minimum length of the QMI message or 0 on error.

.. _`qmi_encode_basic_elem`:

qmi_encode_basic_elem
=====================

.. c:function:: int qmi_encode_basic_elem(void *buf_dst, const void *buf_src, u32 elem_len, u32 elem_size)

    Encodes elements of basic/primary data type

    :param buf_dst:
        Buffer to store the encoded information.
    :type buf_dst: void \*

    :param buf_src:
        Buffer containing the elements to be encoded.
    :type buf_src: const void \*

    :param elem_len:
        Number of elements, in the buf_src, to be encoded.
    :type elem_len: u32

    :param elem_size:
        Size of a single instance of the element to be encoded.
    :type elem_size: u32

.. _`qmi_encode_basic_elem.description`:

Description
-----------

This function encodes the "elem_len" number of data elements, each of
size "elem_size" bytes from the source buffer "buf_src" and stores the
encoded information in the destination buffer "buf_dst". The elements are
of primary data type which include u8 - u64 or similar. This
function returns the number of bytes of encoded information.

.. _`qmi_encode_basic_elem.return`:

Return
------

The number of bytes of encoded information.

.. _`qmi_encode_struct_elem`:

qmi_encode_struct_elem
======================

.. c:function:: int qmi_encode_struct_elem(struct qmi_elem_info *ei_array, void *buf_dst, const void *buf_src, u32 elem_len, u32 out_buf_len, int enc_level)

    Encodes elements of struct data type

    :param ei_array:
        Struct info array descibing the struct element.
    :type ei_array: struct qmi_elem_info \*

    :param buf_dst:
        Buffer to store the encoded information.
    :type buf_dst: void \*

    :param buf_src:
        Buffer containing the elements to be encoded.
    :type buf_src: const void \*

    :param elem_len:
        Number of elements, in the buf_src, to be encoded.
    :type elem_len: u32

    :param out_buf_len:
        Available space in the encode buffer.
    :type out_buf_len: u32

    :param enc_level:
        Depth of the nested structure from the main structure.
    :type enc_level: int

.. _`qmi_encode_struct_elem.description`:

Description
-----------

This function encodes the "elem_len" number of struct elements, each of
size "ei_array->elem_size" bytes from the source buffer "buf_src" and
stores the encoded information in the destination buffer "buf_dst". The
elements are of struct data type which includes any C structure. This
function returns the number of bytes of encoded information.

.. _`qmi_encode_struct_elem.return`:

Return
------

The number of bytes of encoded information on success or negative
errno on error.

.. _`qmi_encode_string_elem`:

qmi_encode_string_elem
======================

.. c:function:: int qmi_encode_string_elem(struct qmi_elem_info *ei_array, void *buf_dst, const void *buf_src, u32 out_buf_len, int enc_level)

    Encodes elements of string data type

    :param ei_array:
        Struct info array descibing the string element.
    :type ei_array: struct qmi_elem_info \*

    :param buf_dst:
        Buffer to store the encoded information.
    :type buf_dst: void \*

    :param buf_src:
        Buffer containing the elements to be encoded.
    :type buf_src: const void \*

    :param out_buf_len:
        Available space in the encode buffer.
    :type out_buf_len: u32

    :param enc_level:
        Depth of the string element from the main structure.
    :type enc_level: int

.. _`qmi_encode_string_elem.description`:

Description
-----------

This function encodes a string element of maximum length "ei_array->elem_len"
bytes from the source buffer "buf_src" and stores the encoded information in
the destination buffer "buf_dst". This function returns the number of bytes
of encoded information.

.. _`qmi_encode_string_elem.return`:

Return
------

The number of bytes of encoded information on success or negative
errno on error.

.. _`qmi_encode`:

qmi_encode
==========

.. c:function:: int qmi_encode(struct qmi_elem_info *ei_array, void *out_buf, const void *in_c_struct, u32 out_buf_len, int enc_level)

    Core Encode Function

    :param ei_array:
        Struct info array describing the structure to be encoded.
    :type ei_array: struct qmi_elem_info \*

    :param out_buf:
        Buffer to hold the encoded QMI message.
    :type out_buf: void \*

    :param in_c_struct:
        Pointer to the C structure to be encoded.
    :type in_c_struct: const void \*

    :param out_buf_len:
        Available space in the encode buffer.
    :type out_buf_len: u32

    :param enc_level:
        Encode level to indicate the depth of the nested structure,
        within the main structure, being encoded.
    :type enc_level: int

.. _`qmi_encode.return`:

Return
------

The number of bytes of encoded information on success or negative
errno on error.

.. _`qmi_decode_basic_elem`:

qmi_decode_basic_elem
=====================

.. c:function:: int qmi_decode_basic_elem(void *buf_dst, const void *buf_src, u32 elem_len, u32 elem_size)

    Decodes elements of basic/primary data type

    :param buf_dst:
        Buffer to store the decoded element.
    :type buf_dst: void \*

    :param buf_src:
        Buffer containing the elements in QMI wire format.
    :type buf_src: const void \*

    :param elem_len:
        Number of elements to be decoded.
    :type elem_len: u32

    :param elem_size:
        Size of a single instance of the element to be decoded.
    :type elem_size: u32

.. _`qmi_decode_basic_elem.description`:

Description
-----------

This function decodes the "elem_len" number of elements in QMI wire format,
each of size "elem_size" bytes from the source buffer "buf_src" and stores
the decoded elements in the destination buffer "buf_dst". The elements are
of primary data type which include u8 - u64 or similar. This
function returns the number of bytes of decoded information.

.. _`qmi_decode_basic_elem.return`:

Return
------

The total size of the decoded data elements, in bytes.

.. _`qmi_decode_struct_elem`:

qmi_decode_struct_elem
======================

.. c:function:: int qmi_decode_struct_elem(struct qmi_elem_info *ei_array, void *buf_dst, const void *buf_src, u32 elem_len, u32 tlv_len, int dec_level)

    Decodes elements of struct data type

    :param ei_array:
        Struct info array descibing the struct element.
    :type ei_array: struct qmi_elem_info \*

    :param buf_dst:
        Buffer to store the decoded element.
    :type buf_dst: void \*

    :param buf_src:
        Buffer containing the elements in QMI wire format.
    :type buf_src: const void \*

    :param elem_len:
        Number of elements to be decoded.
    :type elem_len: u32

    :param tlv_len:
        Total size of the encoded inforation corresponding to
        this struct element.
    :type tlv_len: u32

    :param dec_level:
        Depth of the nested structure from the main structure.
    :type dec_level: int

.. _`qmi_decode_struct_elem.description`:

Description
-----------

This function decodes the "elem_len" number of elements in QMI wire format,
each of size "(tlv_len/elem_len)" bytes from the source buffer "buf_src"
and stores the decoded elements in the destination buffer "buf_dst". The
elements are of struct data type which includes any C structure. This
function returns the number of bytes of decoded information.

.. _`qmi_decode_struct_elem.return`:

Return
------

The total size of the decoded data elements on success, negative
errno on error.

.. _`qmi_decode_string_elem`:

qmi_decode_string_elem
======================

.. c:function:: int qmi_decode_string_elem(struct qmi_elem_info *ei_array, void *buf_dst, const void *buf_src, u32 tlv_len, int dec_level)

    Decodes elements of string data type

    :param ei_array:
        Struct info array descibing the string element.
    :type ei_array: struct qmi_elem_info \*

    :param buf_dst:
        Buffer to store the decoded element.
    :type buf_dst: void \*

    :param buf_src:
        Buffer containing the elements in QMI wire format.
    :type buf_src: const void \*

    :param tlv_len:
        Total size of the encoded inforation corresponding to
        this string element.
    :type tlv_len: u32

    :param dec_level:
        Depth of the string element from the main structure.
    :type dec_level: int

.. _`qmi_decode_string_elem.description`:

Description
-----------

This function decodes the string element of maximum length
"ei_array->elem_len" from the source buffer "buf_src" and puts it into
the destination buffer "buf_dst". This function returns number of bytes
decoded from the input buffer.

.. _`qmi_decode_string_elem.return`:

Return
------

The total size of the decoded data elements on success, negative
errno on error.

.. _`find_ei`:

find_ei
=======

.. c:function:: struct qmi_elem_info *find_ei(struct qmi_elem_info *ei_array, u32 type)

    Find element info corresponding to TLV Type

    :param ei_array:
        Struct info array of the message being decoded.
    :type ei_array: struct qmi_elem_info \*

    :param type:
        TLV Type of the element being searched.
    :type type: u32

.. _`find_ei.description`:

Description
-----------

Every element that got encoded in the QMI message will have a type
information associated with it. While decoding the QMI message,
this function is used to find the struct info regarding the element
that corresponds to the type being decoded.

.. _`find_ei.return`:

Return
------

Pointer to struct info, if found

.. _`qmi_decode`:

qmi_decode
==========

.. c:function:: int qmi_decode(struct qmi_elem_info *ei_array, void *out_c_struct, const void *in_buf, u32 in_buf_len, int dec_level)

    Core Decode Function

    :param ei_array:
        Struct info array describing the structure to be decoded.
    :type ei_array: struct qmi_elem_info \*

    :param out_c_struct:
        Buffer to hold the decoded C struct
    :type out_c_struct: void \*

    :param in_buf:
        Buffer containing the QMI message to be decoded
    :type in_buf: const void \*

    :param in_buf_len:
        Length of the QMI message to be decoded
    :type in_buf_len: u32

    :param dec_level:
        Decode level to indicate the depth of the nested structure,
        within the main structure, being decoded
    :type dec_level: int

.. _`qmi_decode.return`:

Return
------

The number of bytes of decoded information on success, negative
errno on error.

.. _`qmi_encode_message`:

qmi_encode_message
==================

.. c:function:: void *qmi_encode_message(int type, unsigned int msg_id, size_t *len, unsigned int txn_id, struct qmi_elem_info *ei, const void *c_struct)

    Encode C structure as QMI encoded message

    :param type:
        Type of QMI message
    :type type: int

    :param msg_id:
        Message ID of the message
    :type msg_id: unsigned int

    :param len:
        Passed as max length of the message, updated to actual size
    :type len: size_t \*

    :param txn_id:
        Transaction ID
    :type txn_id: unsigned int

    :param ei:
        QMI message descriptor
    :type ei: struct qmi_elem_info \*

    :param c_struct:
        Reference to structure to encode
    :type c_struct: const void \*

.. _`qmi_encode_message.return`:

Return
------

Buffer with encoded message, or negative \ :c:func:`ERR_PTR`\  on error

.. _`qmi_decode_message`:

qmi_decode_message
==================

.. c:function:: int qmi_decode_message(const void *buf, size_t len, struct qmi_elem_info *ei, void *c_struct)

    Decode QMI encoded message to C structure

    :param buf:
        Buffer with encoded message
    :type buf: const void \*

    :param len:
        Amount of data in \ ``buf``\ 
    :type len: size_t

    :param ei:
        QMI message descriptor
    :type ei: struct qmi_elem_info \*

    :param c_struct:
        Reference to structure to decode into
    :type c_struct: void \*

.. _`qmi_decode_message.return`:

Return
------

The number of bytes of decoded information on success, negative
errno on error.

.. This file was automatic generated / don't edit.

