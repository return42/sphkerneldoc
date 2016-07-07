.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/octeon-feature.h

.. _`octeon_has_crypto`:

octeon_has_crypto
=================

.. c:function:: int octeon_has_crypto( void)

    Check if this OCTEON has crypto acceleration support.

    :param  void:
        no arguments

.. _`octeon_has_crypto.return`:

Return
------

Non-zero if the feature exists. Zero if the feature does not exist.

.. _`octeon_has_feature`:

octeon_has_feature
==================

.. c:function:: bool octeon_has_feature(enum octeon_feature feature)

    checks have been optimized to be fairly quick, but they should still be kept out of fast path code.

    :param enum octeon_feature feature:
        Feature to check for. This should always be a constant so the
        compiler can remove the switch statement through optimization.

.. _`octeon_has_feature.description`:

Description
-----------

Returns Non zero if the feature exists. Zero if the feature does not
exist.

.. This file was automatic generated / don't edit.

