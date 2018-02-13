.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/include/uapi/linux/netlink.h

.. _`nlmsgerr_attrs`:

enum nlmsgerr_attrs
===================

.. c:type:: enum nlmsgerr_attrs

    nlmsgerr attributes

.. _`nlmsgerr_attrs.definition`:

Definition
----------

.. code-block:: c

    enum nlmsgerr_attrs {
        NLMSGERR_ATTR_UNUSED,
        NLMSGERR_ATTR_MSG,
        NLMSGERR_ATTR_OFFS,
        NLMSGERR_ATTR_COOKIE,
        __NLMSGERR_ATTR_MAX,
        NLMSGERR_ATTR_MAX
    };

.. _`nlmsgerr_attrs.constants`:

Constants
---------

NLMSGERR_ATTR_UNUSED
    unused

NLMSGERR_ATTR_MSG
    error message string (string)

NLMSGERR_ATTR_OFFS
    offset of the invalid attribute in the original
    message, counting from the beginning of the header (u32)

NLMSGERR_ATTR_COOKIE
    arbitrary subsystem specific cookie to
    be used - in the success case - to identify a created
    object or operation or similar (binary)

__NLMSGERR_ATTR_MAX
    number of attributes

NLMSGERR_ATTR_MAX
    highest attribute number

.. This file was automatic generated / don't edit.

