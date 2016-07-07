.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/si476x-platform.h

.. _`si476x_phase_diversity_mode`:

enum si476x_phase_diversity_mode
================================

.. c:type:: enum si476x_phase_diversity_mode

    possbile phase diversity modes for SI4764/5/6/7 chips.

.. _`si476x_phase_diversity_mode.definition`:

Definition
----------

.. code-block:: c

    enum si476x_phase_diversity_mode {
        SI476X_PHDIV_DISABLED,
        SI476X_PHDIV_PRIMARY_COMBINING,
        SI476X_PHDIV_PRIMARY_ANTENNA,
        SI476X_PHDIV_SECONDARY_ANTENNA,
        SI476X_PHDIV_SECONDARY_COMBINING
    };

.. _`si476x_phase_diversity_mode.constants`:

Constants
---------

SI476X_PHDIV_DISABLED
    Phase diversity feature is
    disabled.

SI476X_PHDIV_PRIMARY_COMBINING
    Tuner works as a primary tuner
    in combination with a
    secondary one.

SI476X_PHDIV_PRIMARY_ANTENNA
    Tuner works as a primary tuner
    using only its own antenna.

SI476X_PHDIV_SECONDARY_ANTENNA
    Tuner works as a primary tuner
    usning seconary tuner's antenna.

SI476X_PHDIV_SECONDARY_COMBINING
    Tuner works as a secondary
    tuner in combination with the
    primary one.

.. This file was automatic generated / don't edit.

