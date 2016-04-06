
.. _API-media-gobj-gen-id:

=================
media_gobj_gen_id
=================

*man media_gobj_gen_id(9)*

*4.6.0-rc1*

encapsulates type and ID on at the object ID


Synopsis
========

.. c:function:: u32 media_gobj_gen_id( enum media_gobj_type type, u64 local_id )

Arguments
=========

``type``
    object type as define at enum ``media_gobj_type``.

``local_id``
    next ID, from struct ``media_device``.\ ``id``.
