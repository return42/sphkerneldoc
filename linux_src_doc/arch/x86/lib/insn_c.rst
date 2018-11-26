.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/lib/insn.c

.. _`insn_init`:

insn_init
=========

.. c:function:: void insn_init(struct insn *insn, const void *kaddr, int buf_len, int x86_64)

    initialize struct insn

    :param insn:
        \ :c:type:`struct insn <insn>`\  to be initialized
    :type insn: struct insn \*

    :param kaddr:
        address (in kernel memory) of instruction (or copy thereof)
    :type kaddr: const void \*

    :param buf_len:
        *undescribed*
    :type buf_len: int

    :param x86_64:
        !0 for 64-bit kernel or 64-bit app
    :type x86_64: int

.. _`insn_get_prefixes`:

insn_get_prefixes
=================

.. c:function:: void insn_get_prefixes(struct insn *insn)

    scan x86 instruction prefix bytes

    :param insn:
        \ :c:type:`struct insn <insn>`\  containing instruction
    :type insn: struct insn \*

.. _`insn_get_prefixes.description`:

Description
-----------

Populates the \ ``insn->prefixes``\  bitmap, and updates \ ``insn->next_byte``\ 
to point to the (first) opcode.  No effect if \ ``insn->prefixes.got``\ 
is already set.

.. _`insn_get_opcode`:

insn_get_opcode
===============

.. c:function:: void insn_get_opcode(struct insn *insn)

    collect opcode(s)

    :param insn:
        \ :c:type:`struct insn <insn>`\  containing instruction
    :type insn: struct insn \*

.. _`insn_get_opcode.description`:

Description
-----------

Populates \ ``insn->opcode``\ , updates \ ``insn->next_byte``\  to point past the
opcode byte(s), and set \ ``insn->attr``\  (except for groups).
If necessary, first collects any preceding (prefix) bytes.
Sets \ ``insn->opcode.value``\  = opcode1.  No effect if \ ``insn->opcode.got``\ 
is already 1.

.. _`insn_get_modrm`:

insn_get_modrm
==============

.. c:function:: void insn_get_modrm(struct insn *insn)

    collect ModRM byte, if any

    :param insn:
        \ :c:type:`struct insn <insn>`\  containing instruction
    :type insn: struct insn \*

.. _`insn_get_modrm.description`:

Description
-----------

Populates \ ``insn->modrm``\  and updates \ ``insn->next_byte``\  to point past the
ModRM byte, if any.  If necessary, first collects the preceding bytes
(prefixes and opcode(s)).  No effect if \ ``insn->modrm.got``\  is already 1.

.. _`insn_rip_relative`:

insn_rip_relative
=================

.. c:function:: int insn_rip_relative(struct insn *insn)

    Does instruction use RIP-relative addressing mode?

    :param insn:
        \ :c:type:`struct insn <insn>`\  containing instruction
    :type insn: struct insn \*

.. _`insn_rip_relative.description`:

Description
-----------

If necessary, first collects the instruction up to and including the
ModRM byte.  No effect if \ ``insn->x86_64``\  is 0.

.. _`insn_get_sib`:

insn_get_sib
============

.. c:function:: void insn_get_sib(struct insn *insn)

    Get the SIB byte of instruction

    :param insn:
        \ :c:type:`struct insn <insn>`\  containing instruction
    :type insn: struct insn \*

.. _`insn_get_sib.description`:

Description
-----------

If necessary, first collects the instruction up to and including the
ModRM byte.

.. _`insn_get_displacement`:

insn_get_displacement
=====================

.. c:function:: void insn_get_displacement(struct insn *insn)

    Get the displacement of instruction

    :param insn:
        \ :c:type:`struct insn <insn>`\  containing instruction
    :type insn: struct insn \*

.. _`insn_get_displacement.description`:

Description
-----------

If necessary, first collects the instruction up to and including the
SIB byte.
Displacement value is sign-expanded.

.. _`insn_get_immediate`:

insn_get_immediate
==================

.. c:function:: void insn_get_immediate(struct insn *insn)

    Get the immediates of instruction

    :param insn:
        \ :c:type:`struct insn <insn>`\  containing instruction
    :type insn: struct insn \*

.. _`insn_get_immediate.description`:

Description
-----------

If necessary, first collects the instruction up to and including the
displacement bytes.
Basically, most of immediates are sign-expanded. Unsigned-value can be
get by bit masking with ((1 << (nbytes \* 8)) - 1)

.. _`insn_get_length`:

insn_get_length
===============

.. c:function:: void insn_get_length(struct insn *insn)

    Get the length of instruction

    :param insn:
        \ :c:type:`struct insn <insn>`\  containing instruction
    :type insn: struct insn \*

.. _`insn_get_length.description`:

Description
-----------

If necessary, first collects the instruction up to and including the
immediates bytes.

.. This file was automatic generated / don't edit.

