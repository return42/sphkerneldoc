.. -*- coding: utf-8; mode: rst -*-

=========
kprobes.c
=========


.. _`__get_insn_slot`:

__get_insn_slot
===============

.. c:function:: kprobe_opcode_t *__get_insn_slot (struct kprobe_insn_cache *c)

    Find a slot on an executable page for an instruction. We allocate an executable page if there's no room on existing ones.

    :param struct kprobe_insn_cache \*c:

        *undescribed*

