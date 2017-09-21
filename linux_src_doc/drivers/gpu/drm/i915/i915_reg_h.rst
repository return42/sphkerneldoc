.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_reg.h

.. _`the-i915-register-macro-definition-style-guide`:

The i915 register macro definition style guide
==============================================

Follow the style described here for new macros, and while changing existing
macros. Do **not** mass change existing definitions just to update the style.

Layout
''''''

Keep helper macros near the top. For example, \ :c:func:`_PIPE`\  and friends.

Prefix macros that generally should not be used outside of this file with
underscore '_'. For example, \ :c:func:`_PIPE`\  and friends, single instances of
registers that are defined solely for the use by function-like macros.

Avoid using the underscore prefixed macros outside of this file. There are
exceptions, but keep them to a minimum.

There are two basic types of register definitions: Single registers and
register groups. Register groups are registers which have two or more
instances, for example one per pipe, port, transcoder, etc. Register groups
should be defined using function-like macros.

For single registers, define the register offset first, followed by register
contents.

For register groups, define the register instance offsets first, prefixed
with underscore, followed by a function-like macro choosing the right
instance based on the parameter, followed by register contents.

Define the register contents (i.e. bit and bit field macros) from most
significant to least significant bit. Indent the register content macros
using two extra spaces between ``#define`` and the macro name.

For bit fields, define a ``_MASK`` and a ``_SHIFT`` macro. Define bit field
contents so that they are already shifted in place, and can be directly
OR'd. For convenience, function-like macros may be used to define bit fields,
but do note that the macros may be needed to read as well as write the
register contents.

Define bits using ``(1 << N)`` instead of ``BIT(N)``. We may change this in
the future, but this is the prevailing style. Do **not** add ``_BIT`` suffix
to the name.

Group the register and its contents together without blank lines, separate
from other registers and their contents with one blank line.

Indent macro values from macro names using TABs. Align values vertically. Use
braces in macro values as needed to avoid unintended precedence after macro
substitution. Use spaces in macro values according to kernel coding
style. Use lower case in hexadecimal values.

Naming
''''''

Try to name registers according to the specs. If the register name changes in
the specs from platform to another, stick to the original name.

Try to re-use existing register macro definitions. Only add new macros for
new register offsets, or when the register contents have changed enough to
warrant a full redefinition.

When a register macro changes for a new platform, prefix the new macro using
the platform acronym or generation. For example, ``SKL_`` or ``GEN8_``. The
prefix signifies the start platform/generation using the register.

When a bit (field) macro changes or gets added for a new platform, while
retaining the existing register macro, add a platform acronym or generation
suffix to the name. For example, ``_SKL`` or ``_GEN8``.

Examples
''''''''

(Note that the values in the example are indented using spaces instead of
TABs to avoid misalignment in generated documentation. Use TABs in the
definitions.)::

 #define _FOO_A                      0xf000
 #define _FOO_B                      0xf001
 #define FOO(pipe)                   _MMIO_PIPE(pipe, _FOO_A, _FOO_B)
 #define   FOO_ENABLE                (1 << 31)
 #define   FOO_MODE_MASK             (0xf << 16)
 #define   FOO_MODE_SHIFT            16
 #define   FOO_MODE_BAR              (0 << 16)
 #define   FOO_MODE_BAZ              (1 << 16)
 #define   FOO_MODE_QUX_SNB          (2 << 16)

 #define BAR                         _MMIO(0xb000)
 #define GEN8_BAR                    _MMIO(0xb888)

.. This file was automatic generated / don't edit.

