.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/include/asm/bug.h

.. _`_emit_bug_entry`:

_EMIT_BUG_ENTRY
===============

.. c:function::  _EMIT_BUG_ENTRY()

    \ ``1``\  - \__FILE_\_ \ ``2``\  - \__LINE_\_ \ ``3``\  - trap type \ ``4``\  - sizeof(struct bug_entry)

.. _`_emit_bug_entry.description`:

Description
-----------

The trapa opcode itself sits in \ ``0``\ .
The \ ``O``\  notation is used to avoid # generation.

The offending file and line are encoded in the \__bug_table section.

.. This file was automatic generated / don't edit.

