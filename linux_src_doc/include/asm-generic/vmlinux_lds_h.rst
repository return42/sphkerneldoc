.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/vmlinux.lds.h

.. _`percpu_input`:

PERCPU_INPUT
============

.. c:function::  PERCPU_INPUT( cacheline)

    the percpu input sections

    :param  cacheline:
        cacheline size

.. _`percpu_input.description`:

Description
-----------

The core percpu section names and core symbols which do not rely
directly upon load addresses.

\ ``cacheline``\  is used to align subsections to avoid false cacheline
sharing between subsections for different purposes.

.. _`percpu_vaddr`:

PERCPU_VADDR
============

.. c:function::  PERCPU_VADDR( cacheline,  vaddr,  phdr)

    define output section for percpu area

    :param  cacheline:
        cacheline size

    :param  vaddr:
        explicit base address (optional)

    :param  phdr:
        destination PHDR (optional)

.. _`percpu_vaddr.description`:

Description
-----------

Macro which expands to output section for percpu area.

\ ``cacheline``\  is used to align subsections to avoid false cacheline
sharing between subsections for different purposes.

If \ ``vaddr``\  is not blank, it specifies explicit base address and all
percpu symbols will be offset from the given address.  If blank,
\ ``vaddr``\  always equals \ ``laddr``\  + LOAD_OFFSET.

\ ``phdr``\  defines the output PHDR to use if not blank.  Be warned that
output PHDR is sticky.  If \ ``phdr``\  is specified, the next output
section in the linker script will go there too.  \ ``phdr``\  should have
a leading colon.

Note that this macros defines \__per_cpu_load as an absolute symbol.
If there is no need to put the percpu section at a predetermined
address, use PERCPU_SECTION.

.. _`percpu_section`:

PERCPU_SECTION
==============

.. c:function::  PERCPU_SECTION( cacheline)

    define output section for percpu area, simple version

    :param  cacheline:
        cacheline size

.. _`percpu_section.description`:

Description
-----------

Align to PAGE_SIZE and outputs output section for percpu area.  This
macro doesn't manipulate \ ``vaddr``\  or \ ``phdr``\  and \__per_cpu_load and
\__per_cpu_start will be identical.

This macro is equivalent to ALIGN(PAGE_SIZE); PERCPU_VADDR(@cacheline,,)
except that \__per_cpu_load is defined as a relative symbol against
.data..percpu which is required for relocatable x86_32 configuration.

.. This file was automatic generated / don't edit.

