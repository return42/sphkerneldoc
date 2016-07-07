.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/layout.c

.. _`req_layout_init`:

req_layout_init
===============

.. c:function:: int req_layout_init( void)

    field of RQFs and the \a rmf_offset field of RMFs.

    :param  void:
        no arguments

.. _`req_capsule_init_area`:

req_capsule_init_area
=====================

.. c:function:: void req_capsule_init_area(struct req_capsule *pill)

    1.

    :param struct req_capsule \*pill:
        *undescribed*

.. _`req_capsule_init_area.description`:

Description
-----------

Actual/expected field sizes are set elsewhere in functions in this file:
\ :c:func:`req_capsule_init`\ , \ :c:func:`req_capsule_server_pack`\ , \ :c:func:`req_capsule_set_size`\  and
\ :c:func:`req_capsule_msg_size`\ .  The \a rc_area information is used by.
\ :c:func:`ptlrpc_request_set_replen`\ .

.. _`req_capsule_init`:

req_capsule_init
================

.. c:function:: void req_capsule_init(struct req_capsule *pill, struct ptlrpc_request *req, enum req_location location)

    :param struct req_capsule \*pill:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param enum req_location location:
        *undescribed*

.. _`req_capsule_init.description`:

Description
-----------

The \a location indicates whether the caller is executing on the client side
(RCL_CLIENT) or server side (RCL_SERVER)..

.. _`req_capsule_set`:

req_capsule_set
===============

.. c:function:: void req_capsule_set(struct req_capsule *pill, const struct req_format *fmt)

    (see \ :c:func:`req_capsule_extend`\ ).

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_format \*fmt:
        *undescribed*

.. _`req_capsule_filled_sizes`:

req_capsule_filled_sizes
========================

.. c:function:: int req_capsule_filled_sizes(struct req_capsule *pill, enum req_location loc)

    yet. \a rc_area is an array of REQ_MAX_FIELD_NR elements, used to store sizes of variable-sized fields.  The field sizes come from the declared \a rmf_size field of a \a pill's \a rc_fmt's RMF's.

    :param struct req_capsule \*pill:
        *undescribed*

    :param enum req_location loc:
        *undescribed*

.. _`req_capsule_server_pack`:

req_capsule_server_pack
=======================

.. c:function:: int req_capsule_server_pack(struct req_capsule *pill)

    :param struct req_capsule \*pill:
        *undescribed*

.. _`req_capsule_server_pack.description`:

Description
-----------

This function uses the \a pill's \a rc_area as filled in by
\ :c:func:`req_capsule_set_size`\  or \ :c:func:`req_capsule_filled_sizes`\  (the latter is called by
this function).

.. _`__req_capsule_offset`:

__req_capsule_offset
====================

.. c:function:: int __req_capsule_offset(const struct req_capsule *pill, const struct req_msg_field *field, enum req_location loc)

    corresponding to the given RMF (\a field).

    :param const struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param enum req_location loc:
        *undescribed*

.. _`swabber_dumper_helper`:

swabber_dumper_helper
=====================

.. c:function:: void swabber_dumper_helper(struct req_capsule *pill, const struct req_msg_field *field, enum req_location loc, int offset, void *value, int len, int dump, void (*) swabber (void *)

    them if desired.

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param enum req_location loc:
        *undescribed*

    :param int offset:
        *undescribed*

    :param void \*value:
        *undescribed*

    :param int len:
        *undescribed*

    :param int dump:
        *undescribed*

    :param (void (\*) swabber (void \*):
        *undescribed*

.. _`__req_capsule_get`:

__req_capsule_get
=================

.. c:function:: void *__req_capsule_get(struct req_capsule *pill, const struct req_msg_field *field, enum req_location loc, void (*) swabber (void *, int dump)

    corresponding to the given RMF (\a field).

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param enum req_location loc:
        *undescribed*

    :param (void (\*) swabber (void \*):
        *undescribed*

    :param int dump:
        *undescribed*

.. _`__req_capsule_get.description`:

Description
-----------

The buffer will be swabbed using the given \a swabber.  If \a swabber == NULL
then the \a rmf_swabber from the RMF will be used.  Soon there will be no
calls to \\ :c:func:`__req_capsule_get`\  with a non-NULL \a swabber; \a swabber will then
be removed.  Fields with the \a RMF_F_STRUCT_ARRAY flag set will have each
element of the array swabbed.

.. _`req_capsule_client_get`:

req_capsule_client_get
======================

.. c:function:: void *req_capsule_client_get(struct req_capsule *pill, const struct req_msg_field *field)

    buffer corresponding to the given RMF (\a field) of a \a pill.

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

.. _`req_capsule_client_swab_get`:

req_capsule_client_swab_get
===========================

.. c:function:: void *req_capsule_client_swab_get(struct req_capsule *pill, const struct req_msg_field *field, void *swabber)

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param void \*swabber:
        *undescribed*

.. _`req_capsule_client_swab_get.description`:

Description
-----------

Currently unused; will be removed when \ :c:func:`req_capsule_server_swab_get`\  is
unused too.

.. _`req_capsule_client_sized_get`:

req_capsule_client_sized_get
============================

.. c:function:: void *req_capsule_client_sized_get(struct req_capsule *pill, const struct req_msg_field *field, int len)

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param int len:
        *undescribed*

.. _`req_capsule_client_sized_get.description`:

Description
-----------

First the \a pill's request \a field's size is set (\a rc_area) using
\ :c:func:`req_capsule_set_size`\  with the given \a len.  Then the actual buffer is
returned.

.. _`req_capsule_server_get`:

req_capsule_server_get
======================

.. c:function:: void *req_capsule_server_get(struct req_capsule *pill, const struct req_msg_field *field)

    buffer corresponding to the given RMF (\a field) of a \a pill.

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

.. _`req_capsule_server_swab_get`:

req_capsule_server_swab_get
===========================

.. c:function:: void *req_capsule_server_swab_get(struct req_capsule *pill, const struct req_msg_field *field, void *swabber)

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param void \*swabber:
        *undescribed*

.. _`req_capsule_server_swab_get.description`:

Description
-----------

Ideally all swabbing should be done pursuant to RMF definitions, with no
swabbing done outside this capsule abstraction.

.. _`req_capsule_server_sized_get`:

req_capsule_server_sized_get
============================

.. c:function:: void *req_capsule_server_sized_get(struct req_capsule *pill, const struct req_msg_field *field, int len)

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param int len:
        *undescribed*

.. _`req_capsule_server_sized_get.description`:

Description
-----------

First the \a pill's request \a field's size is set (\a rc_area) using
\ :c:func:`req_capsule_set_size`\  with the given \a len.  Then the actual buffer is
returned.

.. _`req_capsule_set_size`:

req_capsule_set_size
====================

.. c:function:: void req_capsule_set_size(struct req_capsule *pill, const struct req_msg_field *field, enum req_location loc, int size)

    field of the given \a pill.

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param enum req_location loc:
        *undescribed*

    :param int size:
        *undescribed*

.. _`req_capsule_set_size.description`:

Description
-----------

This function must be used when constructing variable sized fields of a
request or reply.

.. _`req_capsule_get_size`:

req_capsule_get_size
====================

.. c:function:: int req_capsule_get_size(const struct req_capsule *pill, const struct req_msg_field *field, enum req_location loc)

    for the given \a pill's given \a field.

    :param const struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param enum req_location loc:
        *undescribed*

.. _`req_capsule_get_size.description`:

Description
-----------

NB: this function doesn't correspond with \ :c:func:`req_capsule_set_size`\ , which
actually sets the size in pill.rc_area[loc][offset], but this function
returns the message buflen[offset], maybe we should use another name.

.. _`req_capsule_msg_size`:

req_capsule_msg_size
====================

.. c:function:: int req_capsule_msg_size(struct req_capsule *pill, enum req_location loc)

    given \a pill's request or reply (\a loc) given the field size recorded in the \a pill's rc_area.

    :param struct req_capsule \*pill:
        *undescribed*

    :param enum req_location loc:
        *undescribed*

.. _`req_capsule_msg_size.description`:

Description
-----------

See also \ :c:func:`req_capsule_set_size`\ .

.. _`req_capsule_fmt_size`:

req_capsule_fmt_size
====================

.. c:function:: int req_capsule_fmt_size(__u32 magic, const struct req_format *fmt, enum req_location loc)

    (\a loc) given a \a pill's \a rc_area, this function computes the size of a PTLRPC request or reply given only an RQF (\a fmt).

    :param __u32 magic:
        *undescribed*

    :param const struct req_format \*fmt:
        *undescribed*

    :param enum req_location loc:
        *undescribed*

.. _`req_capsule_fmt_size.description`:

Description
-----------

This function should not be used for formats which contain variable size
fields.

.. _`req_capsule_extend`:

req_capsule_extend
==================

.. c:function:: void req_capsule_extend(struct req_capsule *pill, const struct req_format *fmt)

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_format \*fmt:
        *undescribed*

.. _`req_capsule_extend.description`:

Description
-----------

The pill must already have been initialized, which means that it already has
a request format.  The new format \a fmt must be an extension of the pill's
old format.  Specifically: the new format must have as many request and reply
fields as the old one, and all fields shared by the old and new format must
be at least as large in the new format.

The new format's fields may be of different "type" than the old format, but
only for fields that are "opaque" blobs: fields which have a) have no
\a rmf_swabber, b) \a rmf_flags == 0 or RMF_F_NO_SIZE_CHECK, and c) \a
rmf_size == -1 or \a rmf_flags == RMF_F_NO_SIZE_CHECK.  For example,
OBD_SET_INFO has a key field and an opaque value field that gets interpreted
according to the key field.  When the value, according to the key, contains a
structure (or array thereof) to be swabbed, the format should be changed to
one where the value field has \a rmf_size/rmf_flags/rmf_swabber set
accordingly.

.. _`req_capsule_has_field`:

req_capsule_has_field
=====================

.. c:function:: int req_capsule_has_field(const struct req_capsule *pill, const struct req_msg_field *field, enum req_location loc)

    zero value if the given \a field is present in the format (\a rc_fmt) of \a pill's PTLRPC request or reply (\a loc), else it returns 0.

    :param const struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param enum req_location loc:
        *undescribed*

.. _`req_capsule_field_present`:

req_capsule_field_present
=========================

.. c:function:: int req_capsule_field_present(const struct req_capsule *pill, const struct req_msg_field *field, enum req_location loc)

    zero value if the given \a field is present in the given \a pill's PTLRPC request or reply (\a loc), else it returns 0.

    :param const struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param enum req_location loc:
        *undescribed*

.. _`req_capsule_shrink`:

req_capsule_shrink
==================

.. c:function:: void req_capsule_shrink(struct req_capsule *pill, const struct req_msg_field *field, unsigned int newlen, enum req_location loc)

    request or reply (\a loc).

    :param struct req_capsule \*pill:
        *undescribed*

    :param const struct req_msg_field \*field:
        *undescribed*

    :param unsigned int newlen:
        *undescribed*

    :param enum req_location loc:
        *undescribed*

.. _`req_capsule_shrink.description`:

Description
-----------

This is not the opposite of \ :c:func:`req_capsule_extend`\ .

.. This file was automatic generated / don't edit.

