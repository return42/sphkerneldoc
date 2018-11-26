.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_cmd_parser.c

.. _`batch-buffer-command-parser`:

batch buffer command parser
===========================

Motivation:
Certain OpenGL features (e.g. transform feedback, performance monitoring)
require userspace code to submit batches containing commands such as
MI_LOAD_REGISTER_IMM to access various registers. Unfortunately, some
generations of the hardware will noop these commands in "unsecure" batches
(which includes all userspace batches submitted via i915) even though the
commands may be safe and represent the intended programming model of the
device.

The software command parser is similar in operation to the command parsing
done in hardware for unsecure batches. However, the software parser allows
some operations that would be noop'd by hardware, if the parser determines
the operation is safe, and submits the batch as "secure" to prevent hardware
parsing.

Threats:
At a high level, the hardware (and software) checks attempt to prevent
granting userspace undue privileges. There are three categories of privilege.

First, commands which are explicitly defined as privileged or which should
only be used by the kernel driver. The parser generally rejects such
commands, though it may allow some from the drm master process.

Second, commands which access registers. To support correct/enhanced
userspace functionality, particularly certain OpenGL extensions, the parser
provides a whitelist of registers which userspace may safely access (for both
normal and drm master processes).

Third, commands which access privileged memory (i.e. GGTT, HWS page, etc).
The parser always rejects such commands.

The majority of the problematic commands fall in the MI_* range, with only a
few specific commands on each engine (e.g. PIPE_CONTROL and MI_FLUSH_DW).

Implementation:
Each engine maintains tables of commands and registers which the parser
uses in scanning batch buffers submitted to that engine.

Since the set of commands that the parser must check for is significantly
smaller than the number of commands supported, the parser tables contain only
those commands required by the parser. This generally works because command
opcode ranges have standard command length encodings. So for commands that
the parser does not need to check, it can easily skip them. This is
implemented via a per-engine length decoding vfunc.

Unfortunately, there are a number of commands that do not follow the standard
length encoding for their opcode range, primarily amongst the MI_* commands.
To handle this, the parser provides a way to define explicit "skip" entries
in the per-engine command tables.

Other command table entries map fairly directly to high level categories
mentioned above: rejected, master-only, register whitelist. The parser
implements a number of checks, including the privileged memory checks, via a
general bitmasking mechanism.

.. _`intel_engine_init_cmd_parser`:

intel_engine_init_cmd_parser
============================

.. c:function:: void intel_engine_init_cmd_parser(struct intel_engine_cs *engine)

    set cmd parser related fields for an engine

    :param engine:
        the engine to initialize
    :type engine: struct intel_engine_cs \*

.. _`intel_engine_init_cmd_parser.description`:

Description
-----------

Optionally initializes fields related to batch buffer command parsing in the
struct intel_engine_cs based on whether the platform requires software
command parsing.

.. _`intel_engine_cleanup_cmd_parser`:

intel_engine_cleanup_cmd_parser
===============================

.. c:function:: void intel_engine_cleanup_cmd_parser(struct intel_engine_cs *engine)

    clean up cmd parser related fields

    :param engine:
        the engine to clean up
    :type engine: struct intel_engine_cs \*

.. _`intel_engine_cleanup_cmd_parser.description`:

Description
-----------

Releases any resources related to command parsing that may have been
initialized for the specified engine.

.. _`intel_engine_cmd_parser`:

intel_engine_cmd_parser
=======================

.. c:function:: int intel_engine_cmd_parser(struct intel_engine_cs *engine, struct drm_i915_gem_object *batch_obj, struct drm_i915_gem_object *shadow_batch_obj, u32 batch_start_offset, u32 batch_len, bool is_master)

    parse a submitted batch buffer for privilege violations

    :param engine:
        the engine on which the batch is to execute
    :type engine: struct intel_engine_cs \*

    :param batch_obj:
        the batch buffer in question
    :type batch_obj: struct drm_i915_gem_object \*

    :param shadow_batch_obj:
        copy of the batch buffer in question
    :type shadow_batch_obj: struct drm_i915_gem_object \*

    :param batch_start_offset:
        byte offset in the batch at which execution starts
    :type batch_start_offset: u32

    :param batch_len:
        length of the commands in batch_obj
    :type batch_len: u32

    :param is_master:
        is the submitting process the drm master?
    :type is_master: bool

.. _`intel_engine_cmd_parser.description`:

Description
-----------

Parses the specified batch buffer looking for privilege violations as
described in the overview.

.. _`intel_engine_cmd_parser.return`:

Return
------

non-zero if the parser finds violations or otherwise fails; -EACCES
if the batch appears legal but should use hardware parsing

.. _`i915_cmd_parser_get_version`:

i915_cmd_parser_get_version
===========================

.. c:function:: int i915_cmd_parser_get_version(struct drm_i915_private *dev_priv)

    get the cmd parser version number

    :param dev_priv:
        i915 device private
    :type dev_priv: struct drm_i915_private \*

.. _`i915_cmd_parser_get_version.description`:

Description
-----------

The cmd parser maintains a simple increasing integer version number suitable
for passing to userspace clients to determine what operations are permitted.

.. _`i915_cmd_parser_get_version.return`:

Return
------

the current version number of the cmd parser

.. This file was automatic generated / don't edit.

