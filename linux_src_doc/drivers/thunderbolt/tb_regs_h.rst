.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/tb_regs.h

.. _`tb_cap_extended_short`:

struct tb_cap_extended_short
============================

.. c:type:: struct tb_cap_extended_short

    Switch extended short capability

.. _`tb_cap_extended_short.definition`:

Definition
----------

.. code-block:: c

    struct tb_cap_extended_short {
        u8 next;
        u8 cap;
        u8 vsec_id;
        u8 length;
    }

.. _`tb_cap_extended_short.members`:

Members
-------

next
    Pointer to the next capability. If \ ``next``\  and \ ``length``\  are zero
    then we have a long cap.

cap
    Base capability ID (see \ :c:type:`enum tb_switch_cap <tb_switch_cap>`\ )

vsec_id
    Vendor specific capability ID (see \ :c:type:`enum switch_vse_cap <switch_vse_cap>`\ )

length
    Length of this capability

.. _`tb_cap_extended_long`:

struct tb_cap_extended_long
===========================

.. c:type:: struct tb_cap_extended_long

    Switch extended long capability

.. _`tb_cap_extended_long.definition`:

Definition
----------

.. code-block:: c

    struct tb_cap_extended_long {
        u8 zero1;
        u8 cap;
        u8 vsec_id;
        u8 zero2;
        u16 next;
        u16 length;
    }

.. _`tb_cap_extended_long.members`:

Members
-------

zero1
    This field should be zero

cap
    Base capability ID (see \ :c:type:`enum tb_switch_cap <tb_switch_cap>`\ )

vsec_id
    Vendor specific capability ID (see \ :c:type:`enum switch_vse_cap <switch_vse_cap>`\ )

zero2
    This field should be zero

next
    Pointer to the next capability

length
    Length of this capability

.. This file was automatic generated / don't edit.

