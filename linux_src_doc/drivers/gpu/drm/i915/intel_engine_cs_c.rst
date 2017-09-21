.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_engine_cs.c

.. _`__intel_engine_context_size`:

__intel_engine_context_size
===========================

.. c:function:: u32 __intel_engine_context_size(struct drm_i915_private *dev_priv, u8 class)

    return the size of the context for an engine

    :param struct drm_i915_private \*dev_priv:
        i915 device private

    :param u8 class:
        engine class

.. _`__intel_engine_context_size.description`:

Description
-----------

Each engine class may require a different amount of space for a context
image.

.. _`__intel_engine_context_size.return`:

Return
------

size (in bytes) of an engine class specific context image

.. _`__intel_engine_context_size.note`:

Note
----

this size includes the HWSP, which is part of the context image
in LRC mode, but does not include the "shared data page" used with
GuC submission. The caller should account for this if using the GuC.

.. _`intel_engines_init_mmio`:

intel_engines_init_mmio
=======================

.. c:function:: int intel_engines_init_mmio(struct drm_i915_private *dev_priv)

    allocate and prepare the Engine Command Streamers

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. _`intel_engines_init_mmio.return`:

Return
------

non-zero if the initialization failed.

.. _`intel_engines_init`:

intel_engines_init
==================

.. c:function:: int intel_engines_init(struct drm_i915_private *dev_priv)

    init the Engine Command Streamers

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. _`intel_engines_init.return`:

Return
------

non-zero if the initialization failed.

.. _`intel_engine_setup_common`:

intel_engine_setup_common
=========================

.. c:function:: void intel_engine_setup_common(struct intel_engine_cs *engine)

    setup engine state not requiring hw access

    :param struct intel_engine_cs \*engine:
        Engine to setup.

.. _`intel_engine_setup_common.description`:

Description
-----------

Initializes \ ``engine``\ @ structure members shared between legacy and execlists
submission modes which do not require hardware access.

Typically done early in the submission mode specific engine setup stage.

.. _`intel_engine_init_common`:

intel_engine_init_common
========================

.. c:function:: int intel_engine_init_common(struct intel_engine_cs *engine)

    initialize cengine state which might require hw access

    :param struct intel_engine_cs \*engine:
        Engine to initialize.

.. _`intel_engine_init_common.description`:

Description
-----------

Initializes \ ``engine``\ @ structure members shared between legacy and execlists
submission modes which do require hardware access.

Typcally done at later stages of submission mode specific engine setup.

Returns zero on success or an error code on failure.

.. _`intel_engine_cleanup_common`:

intel_engine_cleanup_common
===========================

.. c:function:: void intel_engine_cleanup_common(struct intel_engine_cs *engine)

    cleans up the engine state created by the common initiailizers.

    :param struct intel_engine_cs \*engine:
        Engine to cleanup.

.. _`intel_engine_cleanup_common.description`:

Description
-----------

This cleans up everything created by the common helpers.

.. _`intel_engine_is_idle`:

intel_engine_is_idle
====================

.. c:function:: bool intel_engine_is_idle(struct intel_engine_cs *engine)

    Report if the engine has finished process all work

    :param struct intel_engine_cs \*engine:
        the intel_engine_cs

.. _`intel_engine_is_idle.description`:

Description
-----------

Return true if there are no requests pending, nothing left to be submitted
to hardware, and that the engine is idle.

.. This file was automatic generated / don't edit.

