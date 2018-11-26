.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_asic.c

.. _`radeon_invalid_rreg`:

radeon_invalid_rreg
===================

.. c:function:: uint32_t radeon_invalid_rreg(struct radeon_device *rdev, uint32_t reg)

    dummy reg read function

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param reg:
        offset of register
    :type reg: uint32_t

.. _`radeon_invalid_rreg.description`:

Description
-----------

Dummy register read function.  Used for register blocks
that certain asics don't have (all asics).
Returns the value in the register.

.. _`radeon_invalid_wreg`:

radeon_invalid_wreg
===================

.. c:function:: void radeon_invalid_wreg(struct radeon_device *rdev, uint32_t reg, uint32_t v)

    dummy reg write function

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param reg:
        offset of register
    :type reg: uint32_t

    :param v:
        value to write to the register
    :type v: uint32_t

.. _`radeon_invalid_wreg.description`:

Description
-----------

Dummy register read function.  Used for register blocks
that certain asics don't have (all asics).

.. _`radeon_register_accessor_init`:

radeon_register_accessor_init
=============================

.. c:function:: void radeon_register_accessor_init(struct radeon_device *rdev)

    sets up the register accessor callbacks

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_register_accessor_init.description`:

Description
-----------

Sets up the register accessor callbacks for various register
apertures.  Not all asics have all apertures (all asics).

.. _`radeon_agp_disable`:

radeon_agp_disable
==================

.. c:function:: void radeon_agp_disable(struct radeon_device *rdev)

    AGP disable helper function

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_agp_disable.description`:

Description
-----------

Removes AGP flags and changes the gart callbacks on AGP
cards when using the internal gart rather than AGP (all asics).

.. _`radeon_asic_init`:

radeon_asic_init
================

.. c:function:: int radeon_asic_init(struct radeon_device *rdev)

    register asic specific callbacks

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_asic_init.description`:

Description
-----------

Registers the appropriate asic specific callbacks for each
chip family.  Also sets other asics specific info like the number
of crtcs and the register aperture accessors (all asics).
Returns 0 for success.

.. This file was automatic generated / don't edit.

