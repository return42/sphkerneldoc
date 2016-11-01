.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_engine_cs.c

.. _`intel_engines_init`:

intel_engines_init
==================

.. c:function:: int intel_engines_init(struct drm_device *dev)

    allocate, populate and init the Engine Command Streamers

    :param struct drm_device \*dev:
        DRM device.

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

.. This file was automatic generated / don't edit.

